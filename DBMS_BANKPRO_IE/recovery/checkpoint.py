from copy import deepcopy
from datetime import datetime


class CheckpointManager:

    def __init__(self):

        self.snapshot = None

        self.active_transactions = []

        self.time = ""

    # Create checkpoint
    def create_checkpoint(
        self,
        database,
        transaction_manager
    ):

        self.snapshot = deepcopy(
            database.create_snapshot()
        )

        self.active_transactions = [
            transaction.transaction_id
            for transaction
            in transaction_manager.get_active_transactions()
        ]

        self.time = datetime.now().strftime(
            "%H:%M:%S"
        )

        return (
            self.time,
            self.active_transactions
        )

    # Check checkpoint
    def exists(self):

        return self.snapshot is not None

    # Get information
    def get_info(self):

        if not self.exists():

            return "No checkpoint created."

        active = (
            ", ".join(
                self.active_transactions
            )
            if self.active_transactions
            else "None"
        )

        return (
            f"Checkpoint: {self.time} | "
            f"Active: {active}"
        )