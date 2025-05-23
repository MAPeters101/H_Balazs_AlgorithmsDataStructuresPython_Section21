
class Node:

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacency_list = []


def depth_first_search(start_node):

    # That we need a LIFO: List item we Insert is the First one we take Out
    stack = [start_node]

    # Let's iterate until the stack becomes empty
    while stack:
        # The pop() function returns with the last item we have inserted - O(1)
        actual_node = stack.pop()
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            # If the node has not been visited so far
            if not n.visited:
                n.visited = True
                # Insert the item into the stack
                stack.append(n)


if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    depth_first_search(node1)




