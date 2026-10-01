class RecoveryManager:

    def __init__(
        self,
        database,
        log_manager,
        checkpoint_manager
    ):

        self.database = database

        self.log_manager = log_manager

        self.checkpoint_manager = (
            checkpoint_manager
        )

    # Recover database
    def recover(self):

        logs = self.log_manager.get_logs()

        transaction_status = {}

        write_operations = []

        # Analyze log
        for log in logs:

            transaction_id = (
                log["transaction"]
            )

            operation = log["operation"]

            if operation == "START":

                transaction_status[
                    transaction_id
                ] = "ACTIVE"

            elif operation == "COMMIT":

                transaction_status[
                    transaction_id
                ] = "COMMITTED"

            elif operation == "ABORT":

                transaction_status[
                    transaction_id
                ] = "ABORTED"

            elif operation == "WRITE":

                write_operations.append(
                    log
                )

        # Committed transactions
        committed = {
            tid
            for tid, status
            in transaction_status.items()
            if status == "COMMITTED"
        }

        # Transactions which did not commit
        incomplete = {
            tid
            for tid, status
            in transaction_status.items()
            if status == "ACTIVE"
        }

        redo_count = 0

        undo_count = 0

        # REDO committed operations
        for operation in write_operations:

            if (
                operation["transaction"]
                in committed
            ):

                self.database.set_balance(
                    operation["account"],
                    operation["new_value"]
                )

                redo_count += 1

        # UNDO incomplete transactions
        for operation in reversed(
            write_operations
        ):

            if (
                operation["transaction"]
                in incomplete
            ):

                self.database.set_balance(
                    operation["account"],
                    operation["old_value"]
                )

                undo_count += 1

        return {

            "redo":
                redo_count,

            "undo":
                undo_count,

            "committed":
                sorted(committed),

            "rolled_back":
                sorted(incomplete)
        }