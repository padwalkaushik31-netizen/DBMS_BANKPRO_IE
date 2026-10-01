from .transaction import Transaction


class TransactionManager:

    def __init__(
        self,
        database,
        lock_manager,
        log_manager
    ):

        self.database = database

        self.lock_manager = lock_manager

        self.log_manager = log_manager

        self.transactions = {}

        self.counter = 0

    # Start transaction
    def start_transaction(self):

        self.counter += 1

        transaction_id = f"T{self.counter}"

        transaction = Transaction(
            transaction_id
        )

        self.transactions[
            transaction_id
        ] = transaction

        self.log_manager.write(
            transaction_id,
            "START"
        )

        return transaction

    # Get transaction
    def get_transaction(self, transaction_id):

        if transaction_id not in self.transactions:

            raise ValueError(
                "Transaction does not exist."
            )

        return self.transactions[
            transaction_id
        ]

    # Get active transactions
    def get_active_transactions(self):

        return [
            transaction
            for transaction
            in self.transactions.values()
            if transaction.status == "ACTIVE"
        ]

    # Commit
    def commit(self, transaction_id):

        transaction = self.get_transaction(
            transaction_id
        )

        if transaction.status != "ACTIVE":

            raise ValueError(
                "Only ACTIVE transaction can commit."
            )

        self.log_manager.write(
            transaction_id,
            "COMMIT"
        )

        transaction.finish(
            "COMMITTED"
        )

        self.lock_manager.release_all(
            transaction_id
        )

    # Rollback
    def rollback(
        self,
        transaction_id,
        reason="Manual Rollback"
    ):

        transaction = self.get_transaction(
            transaction_id
        )

        if transaction.status != "ACTIVE":

            raise ValueError(
                "Only ACTIVE transaction can rollback."
            )

        # Undo operations in reverse order
        for operation in reversed(
            transaction.operations
        ):

            self.database.set_balance(
                operation["account"],
                operation["old_value"]
            )

            self.log_manager.write(
                transaction_id,
                "UNDO",
                operation["account"],
                operation["new_value"],
                operation["old_value"]
            )

        self.log_manager.write(
            transaction_id,
            "ABORT",
            details=reason
        )

        transaction.finish(
            "ABORTED"
        )

        self.lock_manager.release_all(
            transaction_id
        )