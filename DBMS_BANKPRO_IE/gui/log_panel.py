import tkinter as tk
from tkinter import ttk


class LogPanel(tk.Frame):

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
            text="Transaction Log & Recovery",
            bg=app.BG,
            fg=app.TEXT,
            font=(
                "Segoe UI",
                19,
                "bold"
            )
        ).pack(
            side="left"
        )

        self.checkpoint_label = tk.Label(
            header,
            text="No checkpoint",
            bg=app.BG,
            fg=app.MUTED,
            font=(
                "Segoe UI",
                10
            )
        )

        self.checkpoint_label.pack(
            side="right"
        )

        columns = (
            "lsn",
            "time",
            "transaction",
            "operation",
            "account",
            "old",
            "new",
            "details"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings"
        )

        headings = {

            "lsn":
                "LSN",

            "time":
                "Time",

            "transaction":
                "Transaction",

            "operation":
                "Operation",

            "account":
                "Account",

            "old":
                "Old Value",

            "new":
                "New Value",

            "details":
                "Details"
        }

        for column in columns:

            self.tree.heading(
                column,
                text=headings[column]
            )

        widths = {

            "lsn": 60,

            "time": 80,

            "transaction": 100,

            "operation": 100,

            "account": 90,

            "old": 100,

            "new": 100,

            "details": 300
        }

        for column, width in widths.items():

            self.tree.column(
                column,
                width=width
            )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

    # Refresh logs
    def refresh(self):

        for item in (
            self.tree.get_children()
        ):

            self.tree.delete(
                item
            )

        for log in (
            self.app
            .log_manager
            .get_logs()
        ):

            old_value = ""

            new_value = ""

            if log["old_value"] is not None:

                old_value = (
                    f"{float(log['old_value']):.2f}"
                )

            if log["new_value"] is not None:

                new_value = (
                    f"{float(log['new_value']):.2f}"
                )

            self.tree.insert(
                "",
                "end",
                values=(
                    log["lsn"],
                    log["time"],
                    log["transaction"],
                    log["operation"],
                    log["account"],
                    old_value,
                    new_value,
                    log["details"]
                )
            )

        self.checkpoint_label.config(
            text=self.app.checkpoint.get_info()
        )