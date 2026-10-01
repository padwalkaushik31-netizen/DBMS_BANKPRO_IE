import tkinter as tk
from tkinter import ttk


class DatabasePanel(tk.Frame):

    def __init__(
        self,
        parent,
        app
    ):

        super().__init__(
            parent,
            bg=app.BG
        )

        self.app = app

        tk.Label(
            self,
            text="Database & Concurrency Control",
            bg=app.BG,
            fg=app.TEXT,
            font=(
                "Segoe UI",
                19,
                "bold"
            )
        ).pack(
            anchor="w",
            padx=20,
            pady=20
        )

        container = tk.Frame(
            self,
            bg=app.BG
        )

        container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        # Accounts
        accounts_frame = tk.Frame(
            container,
            bg=app.CARD
        )

        accounts_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        tk.Label(
            accounts_frame,
            text="Bank Accounts",
            bg=app.CARD,
            fg=app.TEXT,
            font=(
                "Segoe UI",
                14,
                "bold"
            )
        ).pack(
            anchor="w",
            padx=15,
            pady=15
        )

        self.account_tree = ttk.Treeview(
            accounts_frame,
            columns=(
                "id",
                "name",
                "balance"
            ),
            show="headings"
        )

        self.account_tree.heading(
            "id",
            text="ID"
        )

        self.account_tree.heading(
            "name",
            text="Account"
        )

        self.account_tree.heading(
            "balance",
            text="Balance"
        )

        self.account_tree.column(
            "id",
            width=80
        )

        self.account_tree.column(
            "name",
            width=170
        )

        self.account_tree.column(
            "balance",
            width=150
        )

        self.account_tree.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # Locks
        locks_frame = tk.Frame(
            container,
            bg=app.CARD
        )

        locks_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(8, 0)
        )

        tk.Label(
            locks_frame,
            text="Current Locks",
            bg=app.CARD,
            fg=app.TEXT,
            font=(
                "Segoe UI",
                14,
                "bold"
            )
        ).pack(
            anchor="w",
            padx=15,
            pady=15
        )

        self.lock_tree = ttk.Treeview(
            locks_frame,
            columns=(
                "transaction",
                "account",
                "type"
            ),
            show="headings"
        )

        self.lock_tree.heading(
            "transaction",
            text="Transaction"
        )

        self.lock_tree.heading(
            "account",
            text="Account"
        )

        self.lock_tree.heading(
            "type",
            text="Lock"
        )

        self.lock_tree.column(
            "transaction",
            width=120
        )

        self.lock_tree.column(
            "account",
            width=120
        )

        self.lock_tree.column(
            "type",
            width=100
        )

        self.lock_tree.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        tk.Label(
            locks_frame,
            text="Waiting Requests",
            bg=app.CARD,
            fg=app.MUTED,
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        ).pack(
            anchor="w",
            padx=15
        )

        self.waiting_label = tk.Label(
            locks_frame,
            text="None",
            bg=app.CARD,
            fg=app.ORANGE,
            justify="left",
            wraplength=350
        )

        self.waiting_label.pack(
            anchor="w",
            padx=15,
            pady=10
        )

    # Selected account
    def selected_account(self):

        selection = (
            self.account_tree.selection()
        )

        if not selection:

            return None

        return self.account_tree.item(
            selection[0],
            "values"
        )[0]

    # Refresh
    def refresh(self):

        # Accounts
        for item in (
            self.account_tree
            .get_children()
        ):

            self.account_tree.delete(
                item
            )

        for account in (
            self.app.database.get_accounts()
        ):

            self.account_tree.insert(
                "",
                "end",
                values=(
                    account["id"],
                    account["name"],
                    f"₹{account['balance']:,.2f}"
                )
            )

        # Locks
        for item in (
            self.lock_tree.get_children()
        ):

            self.lock_tree.delete(
                item
            )

        for (
            transaction_id,
            account,
            lock_type
        ) in (
            self.app
            .lock_manager
            .get_lock_rows()
        ):

            self.lock_tree.insert(
                "",
                "end",
                values=(
                    transaction_id,
                    account,
                    lock_type
                )
            )

        # Waiting
        waiting = (
            self.app
            .lock_manager
            .get_waiting_rows()
        )

        if waiting:

            text = "\n".join(
                f"{tid} → waiting for {account}"
                for tid, account in waiting
            )

        else:

            text = "None"

        self.waiting_label.config(
            text=text
        )