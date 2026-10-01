import sqlite3
from pathlib import Path
from copy import deepcopy


BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "dbms.sqlite3"

# These are the same initial accounts that were previously stored in data.json.
DEFAULT_ACCOUNTS = (
    ("A", "Account A", 18000.0),
    ("B", "Account B", 5000.0),
    ("C", "Account C", 14000.0),
)


class Database:
    """SQLite-backed database used by the DBMS simulator."""

    def __init__(self):
        self.database_file = DATABASE_FILE
        self._initialize()

    def _connect(self):
        connection = sqlite3.connect(self.database_file)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self):
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS accounts (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    balance REAL NOT NULL CHECK(balance >= 0)
                )
                """
            )

            count = connection.execute(
                "SELECT COUNT(*) FROM accounts"
            ).fetchone()[0]

            if count == 0:
                connection.executemany(
                    """
                    INSERT INTO accounts (id, name, balance)
                    VALUES (?, ?, ?)
                    """,
                    DEFAULT_ACCOUNTS,
                )

            connection.commit()

    # Get balance
    def get_balance(self, account_id):
        with self._connect() as connection:
            row = connection.execute(
                "SELECT balance FROM accounts WHERE id = ?",
                (account_id,),
            ).fetchone()

        if row is None:
            raise ValueError("Account does not exist.")

        return float(row["balance"])

    # Update balance
    def set_balance(self, account_id, balance):
        balance = round(float(balance), 2)

        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        with self._connect() as connection:
            cursor = connection.execute(
                """
                UPDATE accounts
                SET balance = ?
                WHERE id = ?
                """,
                (balance, account_id),
            )

            if cursor.rowcount == 0:
                raise ValueError("Account does not exist.")

            connection.commit()

    # Atomic transfer between two accounts
    def transfer(self, from_account, to_account, amount):
        amount = round(float(amount), 2)

        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")

        if from_account == to_account:
            raise ValueError("Source and destination accounts must be different.")

        with self._connect() as connection:
            connection.execute("BEGIN IMMEDIATE")

            source = connection.execute(
                "SELECT balance FROM accounts WHERE id = ?",
                (from_account,),
            ).fetchone()
            destination = connection.execute(
                "SELECT balance FROM accounts WHERE id = ?",
                (to_account,),
            ).fetchone()

            if source is None:
                raise ValueError(f"Account {from_account} does not exist.")
            if destination is None:
                raise ValueError(f"Account {to_account} does not exist.")

            source_old = round(float(source["balance"]), 2)
            destination_old = round(float(destination["balance"]), 2)

            if source_old < amount:
                raise ValueError(
                    f"Insufficient balance in {from_account}. "
                    f"Available: ₹{source_old:,.2f}"
                )

            source_new = round(source_old - amount, 2)
            destination_new = round(destination_old + amount, 2)

            connection.execute(
                "UPDATE accounts SET balance = ? WHERE id = ?",
                (source_new, from_account),
            )
            connection.execute(
                "UPDATE accounts SET balance = ? WHERE id = ?",
                (destination_new, to_account),
            )

            connection.commit()

        return {
            "from_account": from_account,
            "to_account": to_account,
            "amount": amount,
            "from_old": source_old,
            "from_new": source_new,
            "to_old": destination_old,
            "to_new": destination_new,
        }

    # Return all accounts
    def get_accounts(self):
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT id, name, balance
                FROM accounts
                ORDER BY id
                """
            ).fetchall()

        return [
            {
                "id": row["id"],
                "name": row["name"],
                "balance": float(row["balance"]),
            }
            for row in rows
        ]

    # Create snapshot
    def create_snapshot(self):
        accounts = self.get_accounts()
        return {
            account["id"]: deepcopy(account)
            for account in accounts
        }

    # Restore snapshot
    def restore_snapshot(self, snapshot):
        with self._connect() as connection:
            connection.execute("DELETE FROM accounts")

            connection.executemany(
                """
                INSERT INTO accounts (id, name, balance)
                VALUES (?, ?, ?)
                """,
                [
                    (
                        account["id"],
                        account["name"],
                        round(float(account["balance"]), 2),
                    )
                    for account in snapshot.values()
                ],
            )

            connection.commit()
