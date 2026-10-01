# import tkinter as tk
# from tkinter import ttk, messagebox

# from database.database import Database

# from transactions.transaction_manager import (
#     TransactionManager
# )

# from concurrency.lock_manager import (
#     LockManager
# )

# from concurrency.two_phase_locking import (
#     TwoPhaseLocking
# )

# from concurrency.deadlock_detector import (
#     DeadlockDetector
# )

# from recovery.log_manager import (
#     LogManager
# )

# from recovery.checkpoint import (
#     CheckpointManager
# )

# from recovery.recovery_manager import (
#     RecoveryManager
# )

# from serializability.precedence_graph import (
#     PrecedenceGraph
# )

# from gui.transaction_panel import (
#     TransactionPanel
# )

# from gui.database_panel import (
#     DatabasePanel
# )

# from gui.log_panel import (
#     LogPanel
# )


# class TransactionRecoveryApp(tk.Tk):

#     # Colors
#     BG = "#0F172A"

#     CARD = "#172033"

#     CARD2 = "#1E293B"

#     TEXT = "#F8FAFC"

#     MUTED = "#94A3B8"

#     BLUE = "#4F8CFF"

#     GREEN = "#22C55E"

#     RED = "#EF4444"

#     ORANGE = "#F59E0B"

#     def __init__(self):

#         super().__init__()

#         self.title(
#             "DBMS Transaction Recovery & Concurrency Control Simulator"
#         )

#         self.geometry(
#             "1250x780"
#         )

#         self.minsize(
#             1100,
#             700
#         )

#         self.configure(
#             bg=self.BG
#         )

#         # Core components
#         self.database = Database()

#         self.lock_manager = LockManager()

#         self.two_pl = TwoPhaseLocking()

#         self.deadlock_detector = (
#             DeadlockDetector()
#         )

#         self.log_manager = LogManager()

#         self.checkpoint = (
#             CheckpointManager()
#         )

#         self.recovery_manager = (
#             RecoveryManager(
#                 self.database,
#                 self.log_manager,
#                 self.checkpoint
#             )
#         )

#         self.transaction_manager = (
#             TransactionManager(
#                 self.database,
#                 self.lock_manager,
#                 self.log_manager
#             )
#         )

#         self.precedence_graph = (
#             PrecedenceGraph()
#         )

#         self.configure_styles()

#         self.create_interface()

#         self.refresh_all()

#     # Configure ttk
#     def configure_styles(self):

#         style = ttk.Style(self)

#         style.theme_use(
#             "clam"
#         )

#         style.configure(
#             "TNotebook",
#             background=self.BG,
#             borderwidth=0
#         )

#         style.configure(
#             "TNotebook.Tab",
#             background=self.CARD2,
#             foreground=self.TEXT,
#             padding=(18, 10),
#             font=(
#                 "Segoe UI",
#                 10,
#                 "bold"
#             )
#         )

#         style.map(
#             "TNotebook.Tab",
#             background=[
#                 (
#                     "selected",
#                     self.BLUE
#                 )
#             ]
#         )

#         style.configure(
#             "Treeview",
#             background="#111827",
#             foreground=self.TEXT,
#             fieldbackground="#111827",
#             rowheight=30,
#             borderwidth=0,
#             font=(
#                 "Segoe UI",
#                 10
#             )
#         )

#         style.configure(
#             "Treeview.Heading",
#             background=self.CARD2,
#             foreground=self.TEXT,
#             font=(
#                 "Segoe UI",
#                 10,
#                 "bold"
#             )
#         )

#         style.map(
#             "Treeview",
#             background=[
#                 (
#                     "selected",
#                     "#294A86"
#                 )
#             ]
#         )

#     # Button creator
#     def create_button(
#         self,
#         parent,
#         text,
#         command,
#         color=None
#     ):

#         return tk.Button(

#             parent,

#             text=text,

#             command=command,

#             bg=color or self.BLUE,

#             fg="white",

#             activebackground=color or self.BLUE,

#             activeforeground="white",

#             relief="flat",

#             bd=0,

#             padx=12,

#             pady=9,

#             font=(
#                 "Segoe UI",
#                 10,
#                 "bold"
#             ),

#             cursor="hand2"
#         )

#     # Main interface
#     def create_interface(self):

#         # Header
#         header = tk.Frame(
#             self,
#             bg=self.BG
#         )

#         header.pack(
#             fill="x",
#             padx=25,
#             pady=(20, 10)
#         )

#         tk.Label(
#             header,
#             text="DBMS TRANSACTION LAB",
#             bg=self.BG,
#             fg=self.BLUE,
#             font=(
#                 "Segoe UI",
#                 11,
#                 "bold"
#             )
#         ).pack(
#             anchor="w"
#         )

#         tk.Label(
#             header,
#             text=(
#                 "Transaction Recovery & "
#                 "Concurrency Control Simulator"
#             ),
#             bg=self.BG,
#             fg=self.TEXT,
#             font=(
#                 "Segoe UI",
#                 24,
#                 "bold"
#             )
#         ).pack(
#             anchor="w"
#         )

#         tk.Label(
#             header,
#             text=(
#                 "Transactions • Locks • 2PL • "
#                 "Deadlocks • Serializability • "
#                 "Recovery"
#             ),
#             bg=self.BG,
#             fg=self.MUTED,
#             font=(
#                 "Segoe UI",
#                 10
#             )
#         ).pack(
#             anchor="w"
#         )

#         # Body
#         body = tk.Frame(
#             self,
#             bg=self.BG
#         )

#         body.pack(
#             fill="both",
#             expand=True,
#             padx=25,
#             pady=10
#         )

#         # Sidebar
#         sidebar = tk.Frame(
#             body,
#             bg=self.CARD,
#             width=230
#         )

#         sidebar.pack(
#             side="left",
#             fill="y",
#             padx=(0, 15)
#         )

#         sidebar.pack_propagate(
#             False
#         )

#         tk.Label(
#             sidebar,
#             text="TRANSACTION",
#             bg=self.CARD,
#             fg=self.MUTED,
#             font=(
#                 "Segoe UI",
#                 10,
#                 "bold"
#             )
#         ).pack(
#             anchor="w",
#             padx=18,
#             pady=(20, 8)
#         )

#         self.create_button(
#             sidebar,
#             "＋ Start Transaction",
#             self.start_transaction
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=4
#         )

#         self.create_button(
#             sidebar,
#             "✓ Commit",
#             self.commit_transaction,
#             self.GREEN
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=4
#         )

#         self.create_button(
#             sidebar,
#             "↩ Rollback",
#             self.rollback_transaction,
#             self.RED
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=4
#         )

#         tk.Label(
#             sidebar,
#             text="CONCURRENCY",
#             bg=self.CARD,
#             fg=self.MUTED,
#             font=(
#                 "Segoe UI",
#                 10,
#                 "bold"
#             )
#         ).pack(
#             anchor="w",
#             padx=18,
#             pady=(20, 8)
#         )

#         self.create_button(
#             sidebar,
#             "🔓 S-Lock / READ",
#             lambda: self.request_lock("S")
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=4
#         )

#         self.create_button(
#             sidebar,
#             "🔒 X-Lock / WRITE",
#             lambda: self.request_lock("X")
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=4
#         )

#         self.create_button(
#             sidebar,
#             "Release Lock",
#             self.release_lock,
#             self.ORANGE
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=4
#         )

#         self.create_button(
#             sidebar,
#             "⚠ Detect Deadlock",
#             self.detect_deadlock,
#             self.RED
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=4
#         )

#         tk.Label(
#             sidebar,
#             text="RECOVERY",
#             bg=self.CARD,
#             fg=self.MUTED,
#             font=(
#                 "Segoe UI",
#                 10,
#                 "bold"
#             )
#         ).pack(
#             anchor="w",
#             padx=18,
#             pady=(20, 8)
#         )

#         self.create_button(
#             sidebar,
#             "Create Checkpoint",
#             self.create_checkpoint
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=4
#         )

#         self.create_button(
#             sidebar,
#             "Simulate Failure",
#             self.simulate_failure,
#             self.RED
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=4
#         )

#         self.create_button(
#             sidebar,
#             "Recover Database",
#             self.recover_database,
#             self.GREEN
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=4
#         )

#         self.create_button(
#             sidebar,
#             "Reset System",
#             self.reset_system,
#             "#475569"
#         ).pack(
#             fill="x",
#             padx=15,
#             pady=(20, 4)
#         )

#         self.status_var = tk.StringVar(
#             value="System ready."
#         )

#         tk.Label(
#             sidebar,
#             textvariable=self.status_var,
#             bg=self.CARD,
#             fg=self.MUTED,
#             wraplength=190,
#             justify="left",
#             font=(
#                 "Segoe UI",
#                 9
#             )
#         ).pack(
#             anchor="w",
#             padx=18,
#             pady=20
#         )

#         # Right area
#         right = tk.Frame(
#             body,
#             bg=self.BG
#         )

#         right.pack(
#             side="left",
#             fill="both",
#             expand=True
#         )

#         self.notebook = ttk.Notebook(
#             right
#         )

#         self.notebook.pack(
#             fill="both",
#             expand=True
#         )

#         # Panels
#         self.transaction_panel = (
#             TransactionPanel(
#                 self.notebook,
#                 self
#             )
#         )

#         self.database_panel = (
#             DatabasePanel(
#                 self.notebook,
#                 self
#             )
#         )

#         self.log_panel = (
#             LogPanel(
#                 self.notebook,
#                 self
#             )
#         )

#         self.notebook.add(
#             self.transaction_panel,
#             text="  Transactions  "
#         )

#         self.notebook.add(
#             self.database_panel,
#             text="  Database & Locks  "
#         )

#         self.notebook.add(
#             self.log_panel,
#             text="  Transaction Log  "
#         )

#     # Refresh everything
#     def refresh_all(self):

#         self.transaction_panel.refresh()

#         self.database_panel.refresh()

#         self.log_panel.refresh()

#     # Start transaction
#     def start_transaction(self):

#         transaction = (
#             self.transaction_manager
#             .start_transaction()
#         )

#         self.two_pl.register(
#             transaction.transaction_id
#         )

#         self.status_var.set(
#             f"{transaction.transaction_id} started."
#         )

#         self.refresh_all()

#     # Get selected transaction
#     def selected_transaction(self):

#         return (
#             self.transaction_panel
#             .selected_transaction()
#         )

#     # Request lock
#     def request_lock(self, lock_type):

#         transaction_id = (
#             self.selected_transaction()
#         )

#         account = (
#             self.database_panel
#             .selected_account()
#         )

#         if not transaction_id or not account:

#             messagebox.showwarning(
#                 "Selection Required",
#                 "Select a transaction and account."
#             )

#             return

#         transaction = (
#             self.transaction_manager
#             .get_transaction(
#                 transaction_id
#             )
#         )

#         if transaction.status != "ACTIVE":

#             messagebox.showwarning(
#                 "Transaction",
#                 "Transaction is not active."
#             )

#             return

#         # 2PL
#         if not self.two_pl.can_acquire(
#             transaction_id
#         ):

#             messagebox.showwarning(
#                 "Two-Phase Locking",
#                 f"{transaction_id} is in "
#                 f"SHRINKING phase.\n\n"
#                 f"It cannot acquire new locks."
#             )

#             return

#         granted, message = (
#             self.lock_manager
#             .request_lock(
#                 transaction_id,
#                 account,
#                 lock_type
#             )
#         )

#         if granted:

#             transaction.locks.add(
#                 account
#             )

#         self.status_var.set(
#             message
#         )

#         self.refresh_all()

#     # Release lock
#     def release_lock(self):

#         transaction_id = (
#             self.selected_transaction()
#         )

#         account = (
#             self.database_panel
#             .selected_account()
#         )

#         if not transaction_id or not account:

#             messagebox.showwarning(
#                 "Selection Required",
#                 "Select a transaction and account."
#             )

#             return

#         self.lock_manager.release_lock(
#             transaction_id,
#             account
#         )

#         transaction = (
#             self.transaction_manager
#             .get_transaction(
#                 transaction_id
#             )
#         )

#         transaction.locks.discard(
#             account
#         )

#         # 2PL enters shrinking phase
#         self.two_pl.start_shrinking(
#             transaction_id
#         )

#         self.status_var.set(
#             f"{transaction_id} released "
#             f"{account}. 2PL → SHRINKING"
#         )

#         self.refresh_all()

#     # Commit
#     def commit_transaction(self):

#         transaction_id = (
#             self.selected_transaction()
#         )

#         if not transaction_id:

#             messagebox.showwarning(
#                 "Selection Required",
#                 "Select a transaction."
#             )

#             return

#         try:

#             self.transaction_manager.commit(
#                 transaction_id
#             )

#             self.status_var.set(
#                 f"{transaction_id} committed."
#             )

#             self.refresh_all()

#         except Exception as error:

#             messagebox.showerror(
#                 "Commit Error",
#                 str(error)
#             )

#     # Rollback
#     def rollback_transaction(self):

#         transaction_id = (
#             self.selected_transaction()
#         )

#         if not transaction_id:

#             messagebox.showwarning(
#                 "Selection Required",
#                 "Select a transaction."
#             )

#             return

#         try:

#             self.transaction_manager.rollback(
#                 transaction_id
#             )

#             self.status_var.set(
#                 f"{transaction_id} rolled back."
#             )

#             self.refresh_all()

#         except Exception as error:

#             messagebox.showerror(
#                 "Rollback Error",
#                 str(error)
#             )

#     # READ
#     def read_operation(
#         self,
#         transaction_id,
#         account
#     ):

#         transaction = (
#             self.transaction_manager
#             .get_transaction(
#                 transaction_id
#             )
#         )

#         if transaction.status != "ACTIVE":

#             raise ValueError(
#                 "Transaction is not active."
#             )

#         # S or X lock required
#         if transaction_id not in (
#             self.lock_manager
#             .get_holders(account)
#         ):

#             raise ValueError(
#                 f"{transaction_id} needs "
#                 f"S-Lock or X-Lock on "
#                 f"{account}."
#             )

#         balance = (
#             self.database
#             .get_balance(account)
#         )

#         self.log_manager.write(
#             transaction_id,
#             "READ",
#             account,
#             new_value=balance
#         )

#         self.status_var.set(
#             f"{transaction_id} read "
#             f"{account}: ₹{balance:,.2f}"
#         )

#         self.refresh_all()

#         return balance

#     # WRITE
#     def write_operation(
#         self,
#         transaction_id,
#         account,
#         amount
#     ):

#         transaction = (
#             self.transaction_manager
#             .get_transaction(
#                 transaction_id
#             )
#         )

#         if transaction.status != "ACTIVE":

#             raise ValueError(
#                 "Transaction is not active."
#             )

#         # X-lock required
#         lock_entry = (
#             self.lock_manager
#             .locks
#             .get(
#                 account,
#                 {
#                     "S": set(),
#                     "X": None
#                 }
#             )
#         )

#         if lock_entry["X"] != transaction_id:

#             raise ValueError(
#                 f"{transaction_id} needs "
#                 f"X-Lock on {account} "
#                 f"before WRITE."
#             )

#         old_value = (
#             self.database
#             .get_balance(account)
#         )

#         new_value = round(
#             old_value + amount,
#             2
#         )

#         if new_value < 0:

#             raise ValueError(
#                 "Balance cannot become negative."
#             )

#         # Update DB
#         self.database.set_balance(
#             account,
#             new_value
#         )

#         # Store operation
#         transaction.add_operation(
#             {
#                 "account":
#                     account,

#                 "old_value":
#                     old_value,

#                 "new_value":
#                     new_value,

#                 "amount":
#                     amount
#             }
#         )

#         # Write log
#         self.log_manager.write(
#             transaction_id,
#             "WRITE",
#             account,
#             old_value,
#             new_value
#         )

#         self.status_var.set(
#             f"{transaction_id}: "
#             f"{account} "
#             f"₹{old_value:,.2f} → "
#             f"₹{new_value:,.2f}"
#         )

#         self.refresh_all()

#     # Deadlock
#     def detect_deadlock(self):

#         graph = (
#             self.deadlock_detector
#             .build_wait_for_graph(
#                 self.lock_manager
#             )
#         )

#         cycle = (
#             self.deadlock_detector
#             .detect_cycle(
#                 graph
#             )
#         )

#         if cycle:

#             cycle_text = (
#                 " → ".join(cycle)
#             )

#             messagebox.showwarning(
#                 "DEADLOCK DETECTED",
#                 f"Wait-For Graph Cycle:\n\n"
#                 f"{cycle_text}\n\n"
#                 f"Rollback one transaction "
#                 f"to resolve the deadlock."
#             )

#             self.status_var.set(
#                 f"Deadlock detected: "
#                 f"{cycle_text}"
#             )

#         else:

#             messagebox.showinfo(
#                 "Deadlock Detection",
#                 "No deadlock detected."
#             )

#             self.status_var.set(
#                 "No deadlock detected."
#             )

#     # Checkpoint
#     def create_checkpoint(self):

#         time, active = (
#             self.checkpoint
#             .create_checkpoint(
#                 self.database,
#                 self.transaction_manager
#             )
#         )

#         self.log_manager.write(
#             "SYSTEM",
#             "CHECKPOINT",
#             details=(
#                 "Active transactions: "
#                 + (
#                     ", ".join(active)
#                     if active
#                     else "None"
#                 )
#             )
#         )

#         self.status_var.set(
#             f"Checkpoint created at {time}."
#         )

#         self.refresh_all()

#     # Failure
#     def simulate_failure(self):

#         active = [
#             t.transaction_id
#             for t
#             in self.transaction_manager
#             .get_active_transactions()
#         ]

#         if not active:

#             messagebox.showinfo(
#                 "Failure Simulation",
#                 "No active transaction.\n\n"
#                 "Start a transaction, "
#                 "obtain X-Lock and perform "
#                 "a WRITE first."
#             )

#             return

#         self.status_var.set(
#             "SYSTEM FAILURE simulated."
#         )

#         messagebox.showwarning(
#             "SYSTEM FAILURE",
#             "System failure simulated!\n\n"
#             f"Active transactions:\n"
#             f"{', '.join(active)}\n\n"
#             "Click Recover Database "
#             "to perform recovery."
#         )

#     # Recovery
#     def recover_database(self):

#         result = (
#             self.recovery_manager
#             .recover()
#         )

#         # Mark incomplete transactions aborted
#         for transaction_id in (
#             result["rolled_back"]
#         ):

#             if transaction_id in (
#                 self.transaction_manager
#                 .transactions
#             ):

#                 transaction = (
#                     self.transaction_manager
#                     .transactions[
#                         transaction_id
#                     ]
#                 )

#                 transaction.finish(
#                     "ABORTED"
#                 )

#                 self.lock_manager.release_all(
#                     transaction_id
#                 )

#         self.status_var.set(
#             f"Recovery completed: "
#             f"REDO={result['redo']} "
#             f"UNDO={result['undo']}"
#         )

#         messagebox.showinfo(
#             "Recovery Complete",
#             "Database Recovery Completed!\n\n"
#             f"REDO operations: "
#             f"{result['redo']}\n\n"
#             f"UNDO operations: "
#             f"{result['undo']}\n\n"
#             f"Committed transactions:\n"
#             f"{', '.join(result['committed']) or 'None'}\n\n"
#             f"Rolled back transactions:\n"
#             f"{', '.join(result['rolled_back']) or 'None'}"
#         )

#         self.refresh_all()

#     # Serializability
#     def show_serializability(self):

#         schedule = []

#         for transaction in (
#             self.transaction_manager
#             .transactions
#             .values()
#         ):

#             for operation in (
#                 transaction.operations
#             ):

#                 schedule.append(
#                     (
#                         transaction.transaction_id,
#                         "W",
#                         operation["account"]
#                     )
#                 )

#         if not schedule:

#             messagebox.showinfo(
#                 "Serializability",
#                 "Perform WRITE operations first."
#             )

#             return

#         graph, serializable = (
#             self.precedence_graph
#             .analyze(
#                 schedule
#             )
#         )

#         lines = []

#         for node, edges in graph.items():

#             if edges:

#                 lines.append(
#                     f"{node} → "
#                     f"{', '.join(sorted(edges))}"
#                 )

#             else:

#                 lines.append(
#                     f"{node} →"
#                 )

#         graph_text = "\n".join(
#             lines
#         )

#         result = (
#             "CONFLICT SERIALIZABLE"
#             if serializable
#             else
#             "NOT CONFLICT SERIALIZABLE"
#         )

#         messagebox.showinfo(
#             "Conflict Serializability",
#             f"PRECEDENCE GRAPH\n\n"
#             f"{graph_text}\n\n"
#             f"Result: {result}"
#         )

#     # Reset
#     def reset_system(self):

#         answer = messagebox.askyesno(
#             "Reset System",
#             "Reset database, transactions, "
#             "locks and logs?"
#         )

#         if not answer:

#             return

#         # Reset accounts
#         self.database.restore_snapshot(
#             {
#                 "A": {
#                     "id": "A",
#                     "name": "Account A",
#                     "balance": 10000
#                 },

#                 "B": {
#                     "id": "B",
#                     "name": "Account B",
#                     "balance": 5000
#                 },

#                 "C": {
#                     "id": "C",
#                     "name": "Account C",
#                     "balance": 7000
#                 }
#             }
#         )

#         self.lock_manager = (
#             LockManager()
#         )

#         self.two_pl = (
#             TwoPhaseLocking()
#         )

#         self.deadlock_detector = (
#             DeadlockDetector()
#         )

#         self.log_manager.clear()

#         self.checkpoint = (
#             CheckpointManager()
#         )

#         self.recovery_manager = (
#             RecoveryManager(
#                 self.database,
#                 self.log_manager,
#                 self.checkpoint
#             )
#         )

#         self.transaction_manager = (
#             TransactionManager(
#                 self.database,
#                 self.lock_manager,
#                 self.log_manager
#             )
#         )

#         self.status_var.set(
#             "System reset successfully."
#         )

#         self.refresh_all()

import tkinter as tk
from tkinter import ttk, messagebox

from database.database import Database

from transactions.transaction_manager import (
    TransactionManager
)

from concurrency.lock_manager import (
    LockManager
)

from concurrency.two_phase_locking import (
    TwoPhaseLocking
)

from concurrency.deadlock_detector import (
    DeadlockDetector
)

from recovery.log_manager import (
    LogManager
)

from recovery.checkpoint import (
    CheckpointManager
)

from recovery.recovery_manager import (
    RecoveryManager
)

from serializability.precedence_graph import (
    PrecedenceGraph
)

from gui.transaction_panel import (
    TransactionPanel
)

from gui.database_panel import (
    DatabasePanel
)

from gui.log_panel import (
    LogPanel
)


class TransactionRecoveryApp(tk.Tk):

    # Colors
    BG = "#0F172A"

    CARD = "#172033"

    CARD2 = "#1E293B"

    TEXT = "#F8FAFC"

    MUTED = "#94A3B8"

    BLUE = "#4F8CFF"

    GREEN = "#22C55E"

    RED = "#EF4444"

    ORANGE = "#F59E0B"

    def __init__(self):

        super().__init__()

        self.title(
            "DBMS Transaction Recovery & Concurrency Control Simulator"
        )

        # Larger default window so all sidebar options are visible
        self.geometry(
            "1250x850"
        )

        self.minsize(
            1100,
            750
        )

        self.configure(
            bg=self.BG
        )

        # Open maximized so Recovery and Reset buttons are not cut off
        try:
            self.state("zoomed")
        except Exception:
            pass

        # Core components
        self.database = Database()

        self.lock_manager = LockManager()

        self.two_pl = TwoPhaseLocking()

        self.deadlock_detector = (
            DeadlockDetector()
        )

        self.log_manager = LogManager()

        self.checkpoint = (
            CheckpointManager()
        )

        self.recovery_manager = (
            RecoveryManager(
                self.database,
                self.log_manager,
                self.checkpoint
            )
        )

        self.transaction_manager = (
            TransactionManager(
                self.database,
                self.lock_manager,
                self.log_manager
            )
        )

        self.precedence_graph = (
            PrecedenceGraph()
        )

        self.configure_styles()

        self.create_interface()

        self.refresh_all()

    # Configure ttk
    def configure_styles(self):

        style = ttk.Style(self)

        style.theme_use(
            "clam"
        )

        style.configure(
            "TNotebook",
            background=self.BG,
            borderwidth=0
        )

        style.configure(
            "TNotebook.Tab",
            background=self.CARD2,
            foreground=self.TEXT,
            padding=(18, 10),
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )

        style.map(
            "TNotebook.Tab",
            background=[
                (
                    "selected",
                    self.BLUE
                )
            ]
        )

        style.configure(
            "Treeview",
            background="#111827",
            foreground=self.TEXT,
            fieldbackground="#111827",
            rowheight=30,
            borderwidth=0,
            font=(
                "Segoe UI",
                10
            )
        )

        style.configure(
            "Treeview.Heading",
            background=self.CARD2,
            foreground=self.TEXT,
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )

        style.map(
            "Treeview",
            background=[
                (
                    "selected",
                    "#294A86"
                )
            ]
        )

    # Button creator
    def create_button(
        self,
        parent,
        text,
        command,
        color=None
    ):

        return tk.Button(

            parent,

            text=text,

            command=command,

            bg=color or self.BLUE,

            fg="white",

            activebackground=color or self.BLUE,

            activeforeground="white",

            relief="flat",

            bd=0,

            padx=12,

            pady=9,

            font=(
                "Segoe UI",
                10,
                "bold"
            ),

            cursor="hand2"
        )

    # Main interface
    def create_interface(self):

        # Header
        header = tk.Frame(
            self,
            bg=self.BG
        )

        header.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        tk.Label(
            header,
            text="DBMS TRANSACTION LAB",
            bg=self.BG,
            fg=self.BLUE,
            font=(
                "Segoe UI",
                11,
                "bold"
            )
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text=(
                "Transaction Recovery & "
                "Concurrency Control Simulator"
            ),
            bg=self.BG,
            fg=self.TEXT,
            font=(
                "Segoe UI",
                24,
                "bold"
            )
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text=(
                "Transactions • Locks • 2PL • "
                "Deadlocks • Serializability • "
                "Recovery"
            ),
            bg=self.BG,
            fg=self.MUTED,
            font=(
                "Segoe UI",
                10
            )
        ).pack(
            anchor="w"
        )

        # Body
        body = tk.Frame(
            self,
            bg=self.BG
        )

        body.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        # Sidebar
        sidebar = tk.Frame(
            body,
            bg=self.CARD,
            width=230
        )

        sidebar.pack(
            side="left",
            fill="y",
            padx=(0, 15)
        )

        sidebar.pack_propagate(
            False
        )

        tk.Label(
            sidebar,
            text="TRANSACTION",
            bg=self.CARD,
            fg=self.MUTED,
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        ).pack(
            anchor="w",
            padx=18,
            pady=(10, 4)
        )

        self.create_button(
            sidebar,
            "＋ Start Transaction",
            self.start_transaction
        ).pack(
            fill="x",
            padx=15,
            pady=2
        )

        self.create_button(
            sidebar,
            "✓ Commit",
            self.commit_transaction,
            self.GREEN
        ).pack(
            fill="x",
            padx=15,
            pady=2
        )

        self.create_button(
            sidebar,
            "↩ Rollback",
            self.rollback_transaction,
            self.RED
        ).pack(
            fill="x",
            padx=15,
            pady=2
        )

        self.create_button(
            sidebar,
            "⇄ Transfer",
            self.transfer_money,
            self.GREEN
        ).pack(
            fill="x",
            padx=15,
            pady=4
        )

        tk.Label(
            sidebar,
            text="CONCURRENCY",
            bg=self.CARD,
            fg=self.MUTED,
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        ).pack(
            anchor="w",
            padx=18,
            pady=(8, 4)
        )

        self.create_button(
            sidebar,
            "🔓 S-Lock / READ",
            lambda: self.request_lock("S")
        ).pack(
            fill="x",
            padx=15,
            pady=2
        )

        self.create_button(
            sidebar,
            "🔒 X-Lock / WRITE",
            lambda: self.request_lock("X")
        ).pack(
            fill="x",
            padx=15,
            pady=2
        )

        self.create_button(
            sidebar,
            "Release Lock",
            self.release_lock,
            self.ORANGE
        ).pack(
            fill="x",
            padx=15,
            pady=2
        )

        self.create_button(
            sidebar,
            "⚠ Detect Deadlock",
            self.detect_deadlock,
            self.RED
        ).pack(
            fill="x",
            padx=15,
            pady=4
        )

        tk.Label(
            sidebar,
            text="RECOVERY",
            bg=self.CARD,
            fg=self.MUTED,
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        ).pack(
            anchor="w",
            padx=18,
            pady=(8, 4)
        )

        self.create_button(
            sidebar,
            "Create Checkpoint",
            self.create_checkpoint
        ).pack(
            fill="x",
            padx=15,
            pady=2
        )

        self.create_button(
            sidebar,
            "Simulate Failure",
            self.simulate_failure,
            self.RED
        ).pack(
            fill="x",
            padx=15,
            pady=2
        )

        self.create_button(
            sidebar,
            "Reset System",
            self.reset_system,
            "#475569"
        ).pack(
            fill="x",
            padx=15,
            pady=(5, 2)
        )

        self.status_var = tk.StringVar(
            value="System ready."
        )

        tk.Label(
            sidebar,
            textvariable=self.status_var,
            bg=self.CARD,
            fg=self.MUTED,
            wraplength=190,
            justify="left",
            font=(
                "Segoe UI",
                9
            )
        ).pack(
            anchor="w",
            padx=18,
            pady=8
        )

        # Right area
        right = tk.Frame(
            body,
            bg=self.BG
        )

        right.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.notebook = ttk.Notebook(
            right
        )

        self.notebook.pack(
            fill="both",
            expand=True
        )

        # Panels
        self.transaction_panel = (
            TransactionPanel(
                self.notebook,
                self
            )
        )

        self.database_panel = (
            DatabasePanel(
                self.notebook,
                self
            )
        )

        self.log_panel = (
            LogPanel(
                self.notebook,
                self
            )
        )

        self.notebook.add(
            self.transaction_panel,
            text="  Transactions  "
        )

        self.notebook.add(
            self.database_panel,
            text="  Database & Locks  "
        )

        self.notebook.add(
            self.log_panel,
            text="  Transaction Log  "
        )

    # Refresh everything
    def refresh_all(self):

        self.transaction_panel.refresh()

        self.database_panel.refresh()

        self.log_panel.refresh()

    # Start transaction
    def start_transaction(self):

        transaction = (
            self.transaction_manager
            .start_transaction()
        )

        self.two_pl.register(
            transaction.transaction_id
        )

        self.status_var.set(
            f"{transaction.transaction_id} started."
        )

        self.refresh_all()

    # Get selected transaction
    def selected_transaction(self):

        return (
            self.transaction_panel
            .selected_transaction()
        )

    # Request lock
    def request_lock(self, lock_type):

        transaction_id = (
            self.selected_transaction()
        )

        account = (
            self.database_panel
            .selected_account()
        )

        if not transaction_id or not account:

            messagebox.showwarning(
                "Selection Required",
                "Select a transaction and account."
            )

            return

        transaction = (
            self.transaction_manager
            .get_transaction(
                transaction_id
            )
        )

        if transaction.status != "ACTIVE":

            messagebox.showwarning(
                "Transaction",
                "Transaction is not active."
            )

            return

        # 2PL
        if not self.two_pl.can_acquire(
            transaction_id
        ):

            messagebox.showwarning(
                "Two-Phase Locking",
                f"{transaction_id} is in "
                f"SHRINKING phase.\n\n"
                f"It cannot acquire new locks."
            )

            return

        granted, message = (
            self.lock_manager
            .request_lock(
                transaction_id,
                account,
                lock_type
            )
        )

        if granted:

            transaction.locks.add(
                account
            )

        self.status_var.set(
            message
        )

        self.refresh_all()

    # Release lock
    def release_lock(self):

        transaction_id = (
            self.selected_transaction()
        )

        account = (
            self.database_panel
            .selected_account()
        )

        if not transaction_id or not account:

            messagebox.showwarning(
                "Selection Required",
                "Select a transaction and account."
            )

            return

        self.lock_manager.release_lock(
            transaction_id,
            account
        )

        transaction = (
            self.transaction_manager
            .get_transaction(
                transaction_id
            )
        )

        transaction.locks.discard(
            account
        )

        # 2PL enters shrinking phase
        self.two_pl.start_shrinking(
            transaction_id
        )

        self.status_var.set(
            f"{transaction_id} released "
            f"{account}. 2PL → SHRINKING"
        )

        self.refresh_all()

    # Commit
    def commit_transaction(self):

        transaction_id = (
            self.selected_transaction()
        )

        if not transaction_id:

            messagebox.showwarning(
                "Selection Required",
                "Select a transaction."
            )

            return

        try:

            self.transaction_manager.commit(
                transaction_id
            )

            self.status_var.set(
                f"{transaction_id} committed."
            )

            self.refresh_all()

        except Exception as error:

            messagebox.showerror(
                "Commit Error",
                str(error)
            )

    # Rollback
    def rollback_transaction(self):

        transaction_id = (
            self.selected_transaction()
        )

        if not transaction_id:

            messagebox.showwarning(
                "Selection Required",
                "Select a transaction."
            )

            return

        try:

            self.transaction_manager.rollback(
                transaction_id
            )

            self.status_var.set(
                f"{transaction_id} rolled back."
            )

            self.refresh_all()

        except Exception as error:

            messagebox.showerror(
                "Rollback Error",
                str(error)
            )

    # READ
    def read_operation(
        self,
        transaction_id,
        account
    ):

        transaction = (
            self.transaction_manager
            .get_transaction(
                transaction_id
            )
        )

        if transaction.status != "ACTIVE":

            raise ValueError(
                "Transaction is not active."
            )

        # S or X lock required
        if transaction_id not in (
            self.lock_manager
            .get_holders(account)
        ):

            raise ValueError(
                f"{transaction_id} needs "
                f"S-Lock or X-Lock on "
                f"{account}."
            )

        balance = (
            self.database
            .get_balance(account)
        )

        self.log_manager.write(
            transaction_id,
            "READ",
            account,
            new_value=balance
        )

        self.status_var.set(
            f"{transaction_id} read "
            f"{account}: ₹{balance:,.2f}"
        )

        self.refresh_all()

        return balance

    # WRITE
    def write_operation(
        self,
        transaction_id,
        account,
        amount
    ):

        transaction = (
            self.transaction_manager
            .get_transaction(
                transaction_id
            )
        )

        if transaction.status != "ACTIVE":

            raise ValueError(
                "Transaction is not active."
            )

        # X-lock required
        lock_entry = (
            self.lock_manager
            .locks
            .get(
                account,
                {
                    "S": set(),
                    "X": None
                }
            )
        )

        if lock_entry["X"] != transaction_id:

            raise ValueError(
                f"{transaction_id} needs "
                f"X-Lock on {account} "
                f"before WRITE."
            )

        old_value = (
            self.database
            .get_balance(account)
        )

        new_value = round(
            old_value + amount,
            2
        )

        if new_value < 0:

            raise ValueError(
                "Balance cannot become negative."
            )

        # Update DB
        self.database.set_balance(
            account,
            new_value
        )

        # Store operation
        transaction.add_operation(
            {
                "account":
                    account,

                "old_value":
                    old_value,

                "new_value":
                    new_value,

                "amount":
                    amount
            }
        )

        # Write log
        self.log_manager.write(
            transaction_id,
            "WRITE",
            account,
            old_value,
            new_value
        )

        self.status_var.set(
            f"{transaction_id}: "
            f"{account} "
            f"₹{old_value:,.2f} → "
            f"₹{new_value:,.2f}"
        )

        self.refresh_all()

    # Transfer money between two accounts as one transaction
    def transfer_money(self):

        transaction_id = self.selected_transaction()

        if not transaction_id:
            messagebox.showwarning(
                "Selection Required",
                "Select an ACTIVE transaction first."
            )
            return

        try:
            transaction = self.transaction_manager.get_transaction(transaction_id)
        except Exception as error:
            messagebox.showerror("Transfer Error", str(error))
            return

        if transaction.status != "ACTIVE":
            messagebox.showwarning(
                "Transaction",
                "Only an ACTIVE transaction can transfer money."
            )
            return

        if not self.two_pl.can_acquire(transaction_id):
            messagebox.showwarning(
                "Two-Phase Locking",
                f"{transaction_id} is in SHRINKING phase and cannot acquire new locks."
            )
            return

        dialog = tk.Toplevel(self)
        dialog.title("Transfer Money")
        dialog.geometry("440x420")
        dialog.configure(bg=self.CARD)
        dialog.transient(self)
        dialog.grab_set()

        tk.Label(
            dialog,
            text="TRANSFER MONEY",
            bg=self.CARD,
            fg=self.TEXT,
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(20, 5))

        tk.Label(
            dialog,
            text=f"Transaction: {transaction_id}",
            bg=self.CARD,
            fg=self.MUTED,
            font=("Segoe UI", 10, "bold")
        ).pack(pady=(0, 15))

        accounts = self.database.get_accounts()
        account_ids = [account["id"] for account in accounts]

        form = tk.Frame(dialog, bg=self.CARD)
        form.pack(fill="x", padx=40)

        tk.Label(form, text="From Account", bg=self.CARD, fg=self.MUTED).pack(anchor="w")
        from_var = tk.StringVar(value=account_ids[0] if account_ids else "")
        from_combo = ttk.Combobox(form, textvariable=from_var, values=account_ids, state="readonly")
        from_combo.pack(fill="x", pady=(4, 12))

        tk.Label(form, text="To Account", bg=self.CARD, fg=self.MUTED).pack(anchor="w")
        to_var = tk.StringVar(value=account_ids[1] if len(account_ids) > 1 else "")
        to_combo = ttk.Combobox(form, textvariable=to_var, values=account_ids, state="readonly")
        to_combo.pack(fill="x", pady=(4, 12))

        tk.Label(form, text="Amount (₹)", bg=self.CARD, fg=self.MUTED).pack(anchor="w")
        amount_entry = tk.Entry(
            form,
            bg="#0f172a",
            fg="white",
            insertbackground="white",
            relief="flat",
            font=("Segoe UI", 12)
        )
        amount_entry.pack(fill="x", pady=(4, 18), ipady=8)
        amount_entry.focus()

        def execute_transfer():
            from_account = from_var.get().strip()
            to_account = to_var.get().strip()

            try:
                amount = round(float(amount_entry.get()), 2)
            except ValueError:
                messagebox.showerror("Transfer Error", "Enter a valid numeric amount.", parent=dialog)
                return

            if not from_account or not to_account:
                messagebox.showerror("Transfer Error", "Select both accounts.", parent=dialog)
                return

            if from_account == to_account:
                messagebox.showerror("Transfer Error", "Source and destination accounts must be different.", parent=dialog)
                return

            if amount <= 0:
                messagebox.showerror("Transfer Error", "Transfer amount must be greater than zero.", parent=dialog)
                return

            # Acquire both X-locks before changing either account.
            acquired = []
            for account in (from_account, to_account):
                if self.lock_manager.locks.get(account, {}).get("X") == transaction_id:
                    acquired.append(account)
                    continue

                granted, message = self.lock_manager.request_lock(transaction_id, account, "X")
                if not granted:
                    for locked_account in acquired:
                        self.lock_manager.release_lock(transaction_id, locked_account)
                        transaction.locks.discard(locked_account)
                    self.status_var.set(message)
                    self.refresh_all()
                    messagebox.showwarning(
                        "Transfer Waiting",
                        f"Could not obtain X-Lock on {account}.\n\n{message}\n\n"
                        "No balance was changed. Resolve the lock conflict and try again.",
                        parent=dialog
                    )
                    return

                acquired.append(account)
                transaction.locks.add(account)

            try:
                result = self.database.transfer(from_account, to_account, amount)

                # Record both balance changes so normal transaction rollback can undo them.
                transaction.add_operation({
                    "account": from_account,
                    "old_value": result["from_old"],
                    "new_value": result["from_new"],
                    "amount": -amount,
                })
                transaction.add_operation({
                    "account": to_account,
                    "old_value": result["to_old"],
                    "new_value": result["to_new"],
                    "amount": amount,
                })

                self.log_manager.write(
                    transaction_id,
                    "TRANSFER",
                    f"{from_account} → {to_account}",
                    result["from_old"],
                    result["from_new"],
                    details=(
                        f"Amount=₹{amount:,.2f}; "
                        f"{from_account} ₹{result['from_old']:,.2f} → ₹{result['from_new']:,.2f}; "
                        f"{to_account} ₹{result['to_old']:,.2f} → ₹{result['to_new']:,.2f}"
                    )
                )

                self.status_var.set(
                    f"{transaction_id}: ₹{amount:,.2f} transferred "
                    f"{from_account} → {to_account}."
                )

                dialog.destroy()
                self.refresh_all()

                messagebox.showinfo(
                    "Transfer Successful",
                    f"Transaction: {transaction_id}\n\n"
                    f"From: {from_account}\n"
                    f"To: {to_account}\n"
                    f"Amount: ₹{amount:,.2f}\n\n"
                    f"{from_account} balance: ₹{result['from_new']:,.2f}\n"
                    f"{to_account} balance: ₹{result['to_new']:,.2f}\n\n"
                    "Both account updates were committed atomically in SQLite."
                )

            except Exception as error:
                # The SQLite transfer is atomic, so no partial balance update remains.
                messagebox.showerror("Transfer Error", str(error), parent=dialog)
                self.refresh_all()

        self.create_button(
            dialog,
            "Transfer Money",
            execute_transfer,
            self.GREEN
        ).pack(pady=5)

        tk.Label(
            dialog,
            text="Both accounts require X-Locks. The transfer is one SQLite transaction.",
            bg=self.CARD,
            fg=self.MUTED,
            wraplength=360,
            justify="center"
        ).pack(pady=(8, 15))

    # Deadlock
    def detect_deadlock(self):

        graph = (
            self.deadlock_detector
            .build_wait_for_graph(
                self.lock_manager
            )
        )

        cycle = (
            self.deadlock_detector
            .detect_cycle(
                graph
            )
        )

        if cycle:

            cycle_text = (
                " → ".join(cycle)
            )

            messagebox.showwarning(
                "DEADLOCK DETECTED",
                f"Wait-For Graph Cycle:\n\n"
                f"{cycle_text}\n\n"
                f"Rollback one transaction "
                f"to resolve the deadlock."
            )

            self.status_var.set(
                f"Deadlock detected: "
                f"{cycle_text}"
            )

        else:

            messagebox.showinfo(
                "Deadlock Detection",
                "No deadlock detected."
            )

            self.status_var.set(
                "No deadlock detected."
            )

    # Checkpoint
    def create_checkpoint(self):

        time, active = (
            self.checkpoint
            .create_checkpoint(
                self.database,
                self.transaction_manager
            )
        )

        self.log_manager.write(
            "SYSTEM",
            "CHECKPOINT",
            details=(
                "Active transactions: "
                + (
                    ", ".join(active)
                    if active
                    else "None"
                )
            )
        )

        self.status_var.set(
            f"Checkpoint created at {time}."
        )

        self.refresh_all()

    # Failure
    def simulate_failure(self):

        active = [
            t.transaction_id
            for t
            in self.transaction_manager
            .get_active_transactions()
        ]

        if not active:

            messagebox.showinfo(
                "Failure Simulation",
                "No active transaction.\n\n"
                "Start a transaction, "
                "obtain X-Lock and perform "
                "a WRITE first."
            )

            return

        self.status_var.set(
            "SYSTEM FAILURE simulated."
        )

        messagebox.showwarning(
            "SYSTEM FAILURE",
            "System failure simulated!\n\n"
            f"Active transactions:\n"
            f"{', '.join(active)}\n\n"
            "Click Recover Database "
            "to perform recovery."
        )

    # Recovery
    def recover_database(self):

        result = (
            self.recovery_manager
            .recover()
        )

        # Mark incomplete transactions aborted
        for transaction_id in (
            result["rolled_back"]
        ):

            if transaction_id in (
                self.transaction_manager
                .transactions
            ):

                transaction = (
                    self.transaction_manager
                    .transactions[
                        transaction_id
                    ]
                )

                transaction.finish(
                    "ABORTED"
                )

                self.lock_manager.release_all(
                    transaction_id
                )

        self.status_var.set(
            f"Recovery completed: "
            f"REDO={result['redo']} "
            f"UNDO={result['undo']}"
        )

        messagebox.showinfo(
            "Recovery Complete",
            "Database Recovery Completed!\n\n"
            f"REDO operations: "
            f"{result['redo']}\n\n"
            f"UNDO operations: "
            f"{result['undo']}\n\n"
            f"Committed transactions:\n"
            f"{', '.join(result['committed']) or 'None'}\n\n"
            f"Rolled back transactions:\n"
            f"{', '.join(result['rolled_back']) or 'None'}"
        )

        self.refresh_all()

    # Serializability
    def show_serializability(self):

        schedule = []

        for transaction in (
            self.transaction_manager
            .transactions
            .values()
        ):

            for operation in (
                transaction.operations
            ):

                schedule.append(
                    (
                        transaction.transaction_id,
                        "W",
                        operation["account"]
                    )
                )

        if not schedule:

            messagebox.showinfo(
                "Serializability",
                "Perform WRITE operations first."
            )

            return

        graph, serializable = (
            self.precedence_graph
            .analyze(
                schedule
            )
        )

        lines = []

        for node, edges in graph.items():

            if edges:

                lines.append(
                    f"{node} → "
                    f"{', '.join(sorted(edges))}"
                )

            else:

                lines.append(
                    f"{node} →"
                )

        graph_text = "\n".join(
            lines
        )

        result = (
            "CONFLICT SERIALIZABLE"
            if serializable
            else
            "NOT CONFLICT SERIALIZABLE"
        )

        messagebox.showinfo(
            "Conflict Serializability",
            f"PRECEDENCE GRAPH\n\n"
            f"{graph_text}\n\n"
            f"Result: {result}"
        )

    # Reset
    def reset_system(self):

        answer = messagebox.askyesno(
            "Reset System",
            "Reset database, transactions, "
            "locks and logs?"
        )

        if not answer:

            return

        # Reset accounts
        self.database.restore_snapshot(
            {
                "A": {
                    "id": "A",
                    "name": "Account A",
                    "balance": 10000
                },

                "B": {
                    "id": "B",
                    "name": "Account B",
                    "balance": 5000
                },

                "C": {
                    "id": "C",
                    "name": "Account C",
                    "balance": 7000
                }
            }
        )

        self.lock_manager = (
            LockManager()
        )

        self.two_pl = (
            TwoPhaseLocking()
        )

        self.deadlock_detector = (
            DeadlockDetector()
        )

        self.log_manager.clear()

        self.checkpoint = (
            CheckpointManager()
        )

        self.recovery_manager = (
            RecoveryManager(
                self.database,
                self.log_manager,
                self.checkpoint
            )
        )

        self.transaction_manager = (
            TransactionManager(
                self.database,
                self.lock_manager,
                self.log_manager
            )
        )

        self.status_var.set(
            "System reset successfully."
        )

        self.refresh_all()