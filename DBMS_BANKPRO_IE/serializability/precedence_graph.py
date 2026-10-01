class PrecedenceGraph:

    def build_graph(self, schedule):

        graph = {}

        # Add all transactions
        for transaction_id, operation, item in schedule:

            graph.setdefault(
                transaction_id,
                set()
            )

        # Find conflicts
        for i in range(
            len(schedule)
        ):

            t1, op1, item1 = schedule[i]

            for j in range(
                i + 1,
                len(schedule)
            ):

                t2, op2, item2 = schedule[j]

                # Same transaction
                if t1 == t2:
                    continue

                # Different data item
                if item1 != item2:
                    continue

                # Conflict occurs if at least
                # one operation is WRITE
                if (
                    op1 == "W"
                    or op2 == "W"
                ):

                    graph[t1].add(t2)

        return graph

    # Cycle detection
    def has_cycle(self, graph):

        visited = set()

        recursion_stack = set()

        def dfs(node):

            visited.add(node)

            recursion_stack.add(node)

            for neighbour in graph.get(
                node,
                set()
            ):

                if neighbour not in visited:

                    if dfs(neighbour):

                        return True

                elif neighbour in recursion_stack:

                    return True

            recursion_stack.remove(node)

            return False

        for node in graph:

            if node not in visited:

                if dfs(node):

                    return True

        return False

    # Analyze schedule
    def analyze(self, schedule):

        graph = self.build_graph(
            schedule
        )

        cycle = self.has_cycle(
            graph
        )

        return (
            graph,
            not cycle
        )