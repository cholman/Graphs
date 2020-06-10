"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist") # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #queue = first in first out
        visited = set()
        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            node = queue.dequeue()
            
            if node not in visited and node is not None:
                print(node) 
                visited.add(node)
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    queue.enqueue(neighbor)      
                  

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #stack = first in last out
        visited = set()
        stack = Stack()

        stack.push(starting_vertex)

        while stack.size() > 0:
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.add(node)
                neighbors = self.vertices[node]
                for neighbors in neighbors:
                    stack.push(neighbors)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #initialize storage before recursion starts if one doesn't exist
        if visited is None:
            visited = set()
        
        cur = starting_vertex
        neighbors = self.vertices[cur]
        
        if cur:
            visited.add(cur)
            print(cur)

        if neighbors:
            for neighbor in neighbors:
                if neighbor not in visited:
                    self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #queue = first in first out
        
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()

        while queue.size() > 0:
            current_path = queue.dequeue()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            else:
                if current_node not in visited:
                    visited.add(current_node)
                    neighbors = self.get_neighbors(current_node)

                    for neighbor in neighbors:
                        path_copy = list(current_path)
                        path_copy.append(neighbor)
                        queue.enqueue(path_copy)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()

        while stack.size() > 0:
            current_path = stack.pop()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            else:
                if current_node not in visited:
                    visited.add(current_node)
                    neighbors = self.get_neighbors(current_node)

                    for neighbor in neighbors:
                        path_copy = list(current_path)
                        path_copy.append(neighbor)
                        stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        cur = starting_vertex
        visited.add(cur)
        path = path + [cur]
        
        if cur == destination_vertex:
            return path

        for neighbors in self.vertices[cur]:
            if neighbors not in visited:
                new_path = self.dfs_recursive(neighbors, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None
        # if neighbors:
        #     for neighbor in neighbors:
        #         if neighbor not in visited:
        #             self.dfs_recursive(neighbor, visited)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
