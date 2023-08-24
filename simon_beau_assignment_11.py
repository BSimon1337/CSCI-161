'''
Beau Simon
CSCI L02
Assignment #11
Online Student - 0869416
'''

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = [node2]
        else:
            self.graph[node1].append(node2)
        if node2 not in self.graph:
            self.graph[node2] = [node1]
        else:
            self.graph[node2].append(node1)

    def generate_edges(self):
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                edges.append((node, neighbor))
        return edges

    def find_shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return "No such path exists"

        visited = {node: False for node in self.graph}
        queue = [[start]]

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == end:
                return path

            if not visited[node]:
                for neighbor in self.graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                visited[node] = True

        return "No such path exists"

def menu():
    g = Graph()
    graph_created = False

    while True:
        print("\n1. Create the graph")
        print("2. Display the edges of the graph")
        print("3. Find the shortest path")
        print("4. Exit")

        option = int(input("Enter the option number: "))

        if option == 1:
            confirm = input("This will overwrite the current graph. Do you want to continue? (y/n): ")
            if confirm.lower() == 'y':
                g = Graph()  # Reset the graph variable
                graph_created = False  # Set the graph_created flag to False

                n = int(input("Enter the number of edges: "))
                for _ in range(n):
                    node1 = input("Enter the first node: ")
                    node2 = input("Enter the end node: ")
                    g.add_edge(node1, node2)
                graph_created = True
            else:
                print("Graph creation cancelled.")
        elif option == 2:
            if graph_created:
                print("Edges:", g.generate_edges())
            else:
                print("Create the graph first.")
        elif option == 3:
            if graph_created:
                start, end = input("Enter start and end nodes (format: start_node end_node): ").split()
                print("Shortest path:", g.find_shortest_path(start, end))
            else:
                print("Create the graph first.")
        elif option == 4:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()




