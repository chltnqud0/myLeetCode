from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        m = [[0 for _ in range(len(wordList))] for __ in range(len(wordList))]
        for i in range(len(wordList)):
            for j in range(i, len(wordList)):
                if i == j:
                    continue
                temp = 0
                for k in range(len(beginWord)):
                    if wordList[i][k] != wordList[j][k]:
                        temp += 1
                    if temp == 2:
                        break
                else:
                    m[i][j] = m[j][i] = 1

        answer = self.shortest_path(m, len(wordList) - 1, wordList.index(endWord))
        return answer + 1

    def shortest_path(self, matrix, start, end):
        if start == end:
            return 0  # 시작과 끝이 같으면 거리 0
        n = len(matrix)  # 정점 개수
        visited = [False] * n  # 방문 여부
        queue = deque([(start, 0)])  # (현재 정점, 현재까지 거리)
        while queue:
            node, distance = queue.popleft()
            if node == end:
                return distance  # 최단 거리 반환

            visited[node] = True  # 방문 처리

            for neighbor in range(n):
                if matrix[node][neighbor] == 1 and not visited[neighbor]:  # 연결된 노드
                    queue.append((neighbor, distance + 1))
                    visited[neighbor] = True  # 중복 방문 방지

        return -1  # 도달할 수 없는 경우
