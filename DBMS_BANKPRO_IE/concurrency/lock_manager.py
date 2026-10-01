class LockManager:

    def __init__(self):

        # account:
        # {
        #     "S": set(),
        #     "X": None
        # }

        self.locks = {}

        # Waiting transactions
        self.waiting = {}

    # Create lock entry
    def create_entry(self, account):

        if account not in self.locks:

            self.locks[account] = {
                "S": set(),
                "X": None
            }

        return self.locks[account]

    # Request lock
    def request_lock(
        self,
        transaction_id,
        account,
        lock_type
    ):

        entry = self.create_entry(account)

        lock_type = lock_type.upper()

        # Shared Lock
        if lock_type == "S":

            # Compatible if no other X lock
            if (
                entry["X"] is None
                or entry["X"] == transaction_id
            ):

                entry["S"].add(
                    transaction_id
                )

                self.waiting.pop(
                    transaction_id,
                    None
                )

                return (
                    True,
                    f"{transaction_id}: "
                    f"S-Lock granted on {account}"
                )

            # Otherwise wait
            self.waiting[
                transaction_id
            ] = account

            return (
                False,
                f"{transaction_id}: "
                f"Waiting for X-Lock on {account}"
            )

        # Exclusive Lock
        if lock_type == "X":

            other_shared = (
                entry["S"]
                - {transaction_id}
            )

            other_exclusive = (
                entry["X"] is not None
                and entry["X"] != transaction_id
            )

            if (
                not other_shared
                and not other_exclusive
            ):

                entry["X"] = transaction_id

                entry["S"].discard(
                    transaction_id
                )

                self.waiting.pop(
                    transaction_id,
                    None
                )

                return (
                    True,
                    f"{transaction_id}: "
                    f"X-Lock granted on {account}"
                )

            self.waiting[
                transaction_id
            ] = account

            holders = set(
                other_shared
            )

            if entry["X"]:

                holders.add(
                    entry["X"]
                )

            return (
                False,
                f"{transaction_id}: Waiting for "
                f"{', '.join(sorted(holders))}"
            )

        raise ValueError(
            "Lock must be S or X."
        )

    # Release specific lock
    def release_lock(
        self,
        transaction_id,
        account
    ):

        if account not in self.locks:
            return

        entry = self.locks[account]

        entry["S"].discard(
            transaction_id
        )

        if entry["X"] == transaction_id:

            entry["X"] = None

        if self.waiting.get(
            transaction_id
        ) == account:

            self.waiting.pop(
                transaction_id
            )

    # Release all locks
    def release_all(
        self,
        transaction_id
    ):

        for account in list(
            self.locks.keys()
        ):

            self.release_lock(
                transaction_id,
                account
            )

        self.waiting.pop(
            transaction_id,
            None
        )

    # Get lock holders
    def get_holders(self, account):

        entry = self.create_entry(account)

        holders = set(
            entry["S"]
        )

        if entry["X"]:

            holders.add(
                entry["X"]
            )

        return holders

    # Return lock table
    def get_lock_rows(self):

        rows = []

        for account, entry in self.locks.items():

            for transaction_id in sorted(
                entry["S"]
            ):

                rows.append(
                    (
                        transaction_id,
                        account,
                        "S"
                    )
                )

            if entry["X"]:

                rows.append(
                    (
                        entry["X"],
                        account,
                        "X"
                    )
                )

        return rows

    # Waiting requests
    def get_waiting_rows(self):

        return list(
            self.waiting.items()
        )