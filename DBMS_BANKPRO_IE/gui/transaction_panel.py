import tkinter as tk
from tkinter import ttk, messagebox


class TransactionPanel(tk.Frame):

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

        # Header
        header = tk.Frame(
            self,
            bg=app.BG
        )

        header.pack(
            fill="x",
            padx=20,
            pady=20
        )

        tk.Label(
            header,
            text="Transaction Manager",
            bg=app.BG,
            fg=app.TEXT,
            font=(
                "Segoe UI",
                19,
                "bold"
            )
        ).pack(side="left")

        app.create_button(
            header,
            "Check Serializability",
            app.show_serializability
        ).pack(
            side="right",
            padx=(10, 0)
        )

        app.create_button(
            header,
            "Recover Database",
            app.recover_database,
            app.GREEN
        ).pack(
            side="right",
            padx=(10, 0)
        )

        # Transaction table
        columns = (
            "id",
            "status",
            "phase",
            "start",
            "end",
            "locks"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings"
        )

        headings = {

            "id":
                "Transaction",

            "status":
                "Status",

            "phase":
                "2PL Phase",

            "start":
                "Start",

            "end":
                "End",

            "locks":
                "Locks"
        }

        for column in columns:

            self.tree.heading(
                column,
                text=headings[column]
            )

        self.tree.column(
            "id",
            width=110
        )

        self.tree.column(
            "status",
            width=130
        )

        self.tree.column(
            "phase",
            width=130
        )

        self.tree.column(
            "start",
            width=100
        )

        self.tree.column(
            "end",
            width=100
        )

        self.tree.column(
            "locks",
            width=250
        )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=20
        )

        # Bottom actions
        bottom = tk.Frame(
            self,
            bg=app.CARD
        )

        bottom.pack(
            fill="x",
            padx=20,
            pady=20
        )

        self.selected_label = tk.Label(
            bottom,
            text="Selected: None",
            bg=app.CARD,
            fg=app.BLUE,
            font=(
                "Segoe UI",
                11,
                "bold"
            )
        )

        self.selected_label.pack(
            side="left",
            padx=15
        )

        app.create_button(
            bottom,
            "READ",
            self.read_selected
        ).pack(
            side="right",
            padx=5,
            pady=10
        )

        app.create_button(
            bottom,
            "WRITE",
            self.write_selected
        ).pack(
            side="right",
            padx=5,
            pady=10
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.selection_changed
        )

    # Selected transaction
    def selected_transaction(self):

        selection = self.tree.selection()

        if not selection:

            return None

        values = self.tree.item(
            selection[0],
            "values"
        )

        return values[0]

    # Selection changed
    def selection_changed(self, event=None):

        transaction = (
            self.selected_transaction()
        )

        self.selected_label.config(
            text=
            f"Selected: "
            f"{transaction or 'None'}"
        )

    # Refresh table
    def refresh(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

        for transaction in (
            self.app
            .transaction_manager
            .transactions
            .values()
        ):

            locks = ", ".join(
                sorted(
                    transaction.locks
                )
            )

            if not locks:

                locks = "-"

            self.tree.insert(
                "",
                "end",
                values=(
                    transaction.transaction_id,
                    transaction.status,
                    self.app.two_pl.get_phase(
                        transaction.transaction_id
                    ),
                    transaction.start_time,
                    transaction.end_time or "-",
                    locks
                )
            )

        self.selection_changed()

    # READ
    def read_selected(self):

        transaction_id = (
            self.selected_transaction()
        )

        account = (
            self.app
            .database_panel
            .selected_account()
        )

        if not transaction_id or not account:

            messagebox.showwarning(
                "Selection Required",
                "Select a transaction and account."
            )

            return

        try:

            balance = (
                self.app.read_operation(
                    transaction_id,
                    account
                )
            )

            messagebox.showinfo(
                "READ Operation",
                f"Transaction: {transaction_id}\n"
                f"Account: {account}\n\n"
                f"Balance: ₹{balance:,.2f}"
            )

        except Exception as error:

            messagebox.showerror(
                "READ Error",
                str(error)
            )

    # WRITE
    def write_selected(self):

        transaction_id = (
            self.selected_transaction()
        )

        account = (
            self.app
            .database_panel
            .selected_account()
        )

        if not transaction_id or not account:

            messagebox.showwarning(
                "Selection Required",
                "Select a transaction and account."
            )

            return

        dialog = tk.Toplevel(
            self
        )

        dialog.title(
            "Write Transaction"
        )

        dialog.geometry(
            "380x260"
        )

        dialog.configure(
            bg=self.app.CARD
        )

        tk.Label(
            dialog,
            text="WRITE Operation",
            bg=self.app.CARD,
            fg=self.app.TEXT,
            font=(
                "Segoe UI",
                17,
                "bold"
            )
        ).pack(
            pady=20
        )

        tk.Label(
            dialog,
            text=f"{transaction_id} → {account}",
            bg=self.app.CARD,
            fg=self.app.MUTED
        ).pack()

        tk.Label(
            dialog,
            text="Amount (+ deposit / - withdrawal)",
            bg=self.app.CARD,
            fg=self.app.MUTED
        ).pack(
            pady=(15, 5)
        )

        amount_entry = tk.Entry(
            dialog,
            bg="#0f172a",
            fg="white",
            insertbackground="white",
            relief="flat",
            font=(
                "Segoe UI",
                12
            )
        )

        amount_entry.pack(
            padx=40,
            fill="x",
            ipady=8
        )

        amount_entry.focus()

        def execute():

            try:

                amount = float(
                    amount_entry.get()
                )

                self.app.write_operation(
                    transaction_id,
                    account,
                    amount
                )

                dialog.destroy()

            except Exception as error:

                messagebox.showerror(
                    "WRITE Error",
                    str(error),
                    parent=dialog
                )

        self.app.create_button(
            dialog,
            "Execute WRITE",
            execute,
            self.app.GREEN
        ).pack(
            pady=20
        )