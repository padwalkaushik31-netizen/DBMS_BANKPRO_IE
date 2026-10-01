# DBMS Transaction Recovery & Concurrency Control Simulator — SQLite3

This version uses Python's built-in `sqlite3` module instead of JSON files.

## Run

```cmd
python main.py
```

The SQLite database is stored at `database/dbms.sqlite3` and is created automatically.

## Transfer Money Feature

The application now includes a **Transfer A → B** operation.

1. Start a transaction.
2. Select the transaction in the Transaction Manager.
3. Click the visible **⇄ Transfer Money (A → B)** button in the Transaction Manager header (the sidebar also contains the same action when there is enough vertical space).
4. Select the source account, destination account, and amount.
5. The application obtains X-Locks on both accounts.
6. It checks that the source has sufficient balance.
7. Both account updates are executed inside one SQLite transaction.
8. On success, a `TRANSFER` record is written to the transaction log.
9. The two balance changes are stored in the transaction's operation list, so normal transaction rollback can undo the transfer.

A failed transfer (for example, insufficient balance) leaves both accounts unchanged.

## Existing Features Preserved

- Start / commit / rollback transactions
- READ / WRITE operations
- S-Lock / X-Lock
- Two-Phase Locking
- Deadlock detection
- Checkpoints
- Failure simulation
- REDO / UNDO recovery
- Conflict serializability
- Reset system
- SQLite-backed accounts and transaction logs
