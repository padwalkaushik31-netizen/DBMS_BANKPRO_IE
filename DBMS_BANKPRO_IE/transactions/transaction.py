from datetime import datetime


class Transaction:

    def __init__(self, transaction_id):

        self.transaction_id = transaction_id

        self.status = "ACTIVE"

        self.start_time = datetime.now().strftime(
            "%H:%M:%S"
        )

        self.end_time = ""

        self.locks = set()

        self.operations = []

    # Add operation
    def add_operation(self, operation):

        self.operations.append(operation)

    # Finish transaction
    def finish(self, status):

        self.status = status

        self.end_time = datetime.now().strftime(
            "%H:%M:%S"
        )

    def __str__(self):

        return (
            f"{self.transaction_id} - "
            f"{self.status}"
        )