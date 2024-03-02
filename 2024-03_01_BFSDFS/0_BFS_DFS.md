# 그래프 탐색 유형

**DFS**

- 보통 재귀함수나 스택 자료구조를 활용해 DFS 문제를 풀 수 있다.
- 인접한 노드들을 모두 방문했다면 스택에서 제거하는 식으로 문제를 푼다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 해당 노드를 스택에 넣고 방문처리합니다.
3. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
4. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

**BFS**
- 보통 큐 자료구조를 이용한다.
- 간선의 가중치가 동일한 상황에서 최단 거리 문제를 푸는 데에도 사용된다.
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 **인접 노드 중에서 방문하니 않은 노드를 모두 큐에 삽입하고 방문 처리**합니다.
3. 더 이상 2번의 과정을 수행할 수 없을 때가지 반복합니다.

### 그래프 탐색 문제를 풀기 전 꼭 알아야 하는 자료구조
> **Stack**

```py
stack = []

stack.append(3)
stack.pop()

# 스택 최상단부터 출력
print(stack[::-1])

# 스택 최하단부터 출력
print(stack)
```


> **Queue**

```py
from collections import deque

# 성능상 이점때문에 list 대신 deque 라이브러리 사용
# deque는 popleft 가 O(1) 이지만, list의 pop은 O(k)
# list의 pop이 느린 이유는, pop 이후에 원소들의 위치를 옮겨주는 작업을 하기 때문
queue = deque()

queue.append(3)
queue.popleft()

# 먼저 들어온 순서대로 출력
print(queue)

# 나중에 들어온 순서대로 출력
print(queue.reverse())
```

### DFS 소스코드 예제

```py
def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [], # 보통 1번부터 시작하기에 0번 인덱스는 비워둔다.
    [2, 3, 8],
    [1, 7],
]

visited = [False] * 3

dfs(graph, 1, visited)
```

### BFS 소스코드 예제
```py
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start]) 

    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [], # 보통 1번부터 시작하기에 0번 인덱스는 비워둔다.
    [2, 3, 8],
    [1, 7],
]

visited = [False] * 3

bfs(graph, 1, visited)

```