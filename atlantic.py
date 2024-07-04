from Queue import Queue
class Solution(object):
    def bfs(self, q, matrix, visited):
        N, M  = len(matrix), len(matrix[0])
        while q.empty() == False:
            (x,y) = q.get()
            candidates = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
            for (x1,y1) in candidates:
                if 0<=x1<N and 0<=y1<M and not visited[x1][y1] and matrix[x1][y1] >= matrix[x][y]:
                    q.put((x1,y1))
                    visited[x1][y1]=True
        return
    
    def initialize_q(self, N, M, pac_q, atl_q, pac_visited, atl_visited):
        for i in range(N):
            pac_q.put((i,0))
            atl_q.put((i, M-1))
            pac_visited[i][0], atl_visited[i][M-1] = True, True
                        
        for j in range(M):
            pac_q.put((0,j))
            atl_q.put((N-1,j))
            pac_visited[0][j], atl_visited[N-1][j] = True, True
        return
    
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix == []:
            return []
        N, M  = len(matrix), len(matrix[0])
        pac_q, atl_q = Queue(), Queue()
        pac_visited = [[False]*M for _ in range(N)]
        atl_visited = [[False]*M for _ in range(N)]        
        
        self.initialize_q(N, M, pac_q, atl_q, pac_visited, atl_visited)
        self.bfs(pac_q, matrix, pac_visited)            
        self.bfs(atl_q, matrix, atl_visited)            
        
        result = []
        for i in range(N):
            for j in range(M):
                if pac_visited[i][j] and atl_visited[i][j]:
                    result.append([i,j])
                    
        return result