import sqlite3
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR.parent / "database" / "dbms.sqlite3"


class LogManager:
    """SQLite-backed transaction log manager."""

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
                CREATE TABLE IF NOT EXISTS transaction_logs (
                    lsn INTEGER PRIMARY KEY AUTOINCREMENT,
                    time TEXT NOT NULL,
                    transaction_id TEXT NOT NULL,
                    operation TEXT NOT NULL,
                    account TEXT DEFAULT '',
                    old_value REAL,
                    new_value REAL,
                    details TEXT DEFAULT ''
                )
                """
            )
            connection.commit()

    # Write log
    def write(
        self,
        transaction_id,
        operation,
        account="",
        old_value=None,
        new_value=None,
        details=""
    ):
        timestamp = datetime.now().strftime("%H:%M:%S")

        with self._connect() as connection:
            cursor = connection.execute(
                """
                INSERT INTO transaction_logs
                    (time, transaction_id, operation, account,
                     old_value, new_value, details)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    timestamp,
                    transaction_id,
                    operation,
                    account,
                    old_value,
                    new_value,
                    details,
                ),
            )
            connection.commit()

            row = connection.execute(
                """
                SELECT lsn, time, transaction_id, operation,
                       account, old_value, new_value, details
                FROM transaction_logs
                WHERE lsn = ?
                """,
                (cursor.lastrowid,),
            ).fetchone()

        return self._row_to_dict(row)

    # Get logs
    def get_logs(self):
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT lsn, time, transaction_id, operation,
                       account, old_value, new_value, details
                FROM transaction_logs
                ORDER BY lsn
                """
            ).fetchall()

        return [self._row_to_dict(row) for row in rows]

    # Clear logs
    def clear(self):
        with self._connect() as connection:
            connection.execute("DELETE FROM transaction_logs")
            # Keep LSNs predictable after a reset.
            connection.execute(
                """
                DELETE FROM sqlite_sequence
                WHERE name = 'transaction_logs'
                """
            )
            connection.commit()

    @staticmethod
    def _row_to_dict(row):
        if row is None:
            return None

        return {
            "lsn": row["lsn"],
            "time": row["time"],
            "transaction": row["transaction_id"],
            "operation": row["operation"],
            "account": row["account"] or "",
            "old_value": row["old_value"],
            "new_value": row["new_value"],
            "details": row["details"] or "",
        }
