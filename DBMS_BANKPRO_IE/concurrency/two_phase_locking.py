class TwoPhaseLocking:

    def __init__(self):

        self.phases = {}

    # New transaction starts in growing phase
    def register(self, transaction_id):

        self.phases[
            transaction_id
        ] = "GROWING"

    # Check whether transaction can acquire lock
    def can_acquire(self, transaction_id):

        return (
            self.phases.get(
                transaction_id,
                "GROWING"
            )
            == "GROWING"
        )

    # Transaction enters shrinking phase
    def start_shrinking(
        self,
        transaction_id
    ):

        self.phases[
            transaction_id
        ] = "SHRINKING"

    # Get phase
    def get_phase(self, transaction_id):

        return self.phases.get(
            transaction_id,
            "-"
        )