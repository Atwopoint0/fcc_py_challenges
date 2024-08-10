class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
    
    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    # Depth first search
    def dfs(self, start_vertex_data):
        visited = [False] * self.size
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)

    # Breadth first search
    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True
          
        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=' ')
      
            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
    # Detect cycles
    def is_cyclic(self):
        visited = [False] * self.size
        for i in range(self.size):
            if not visited[i]:
                if self.dfs_util(i, visited, -1):
                    return True
        return False