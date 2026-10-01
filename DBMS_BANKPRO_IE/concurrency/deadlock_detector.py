# class DeadlockDetector:

#     # Create Wait-For Graph
#     def build_wait_for_graph(
#         self,
#         lock_manager
#     ):

#         graph = {}

#         for (
#             waiting_transaction,
#             account
#         ) in lock_manager.waiting.items():

#             graph.setdefault(
#                 waiting_transaction,
#                 set()
#             )

#             holders = lock_manager.get_holders(
#                 account
#             )

#             for holder in holders:

#                 if holder != waiting_transaction:

#                     graph[
#                         waiting_transaction
#                     ].add(holder)

#         return graph

#     # Detect cycle
#     def detect_cycle(self, graph):

#         visited = set()

#         recursion_stack = set()

#         def dfs(node):

#             visited.add(node)

#             recursion_stack.add(node)

#             for neighbour in graph.get(
#                 node,
#                 set()
#             ):

#                 if neighbour not in visited:

#                     cycle = dfs(neighbour)

#                     if cycle:
#                         return cycle

#                 elif neighbour in recursion_stack:

#                     return [
#                         neighbour,
#                         node,
#                         neighbour
#                     ]

#             recursion_stack.remove(node)

#             return None

#         for node in graph:

#             if node not in visited:

#                 cycle = dfs(node)

#                 if cycle:

#                     return cycle

#         return None

class DeadlockDetector:

    # Create Wait-For Graph
    def build_wait_for_graph(self, lock_manager):

        graph = {}

        # waiting is expected to be:
        # {waiting_transaction: account}
        for waiting_transaction, account in lock_manager.waiting.items():

            # Make sure the waiting transaction exists
            graph.setdefault(waiting_transaction, set())

            # Find transactions currently holding the requested account
            holders = lock_manager.get_holders(account)

            for holder in holders:

                # A transaction should not wait for itself
                if holder != waiting_transaction:

                    graph[waiting_transaction].add(holder)

                    # Also make sure holder appears in graph
                    graph.setdefault(holder, set())

        return graph

    # Detect cycle in Wait-For Graph
    def detect_cycle(self, graph):

        visited = set()
        recursion_stack = set()

        def dfs(node, path):

            visited.add(node)
            recursion_stack.add(node)
            path.append(node)

            for neighbour in graph.get(node, set()):

                # Found a cycle
                if neighbour in recursion_stack:

                    cycle_start = path.index(neighbour)

                    return path[cycle_start:] + [neighbour]

                # Visit new node
                if neighbour not in visited:

                    cycle = dfs(
                        neighbour,
                        path.copy()
                    )

                    if cycle:
                        return cycle

            recursion_stack.remove(node)

            return None

        # Check every transaction
        for node in graph:

            if node not in visited:

                cycle = dfs(node, [])

                if cycle:
                    return cycle

        return None

    # Complete deadlock check
    def check_deadlock(self, lock_manager):

        graph = self.build_wait_for_graph(lock_manager)

        cycle = self.detect_cycle(graph)

        return graph, cycle