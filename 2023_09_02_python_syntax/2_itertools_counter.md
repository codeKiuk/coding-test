## itertools
- 순열 및 조합을 이용해 완전 탐색 문제를 풀 때 사용한다
- 완전탐색이란 : 모든 경우의 수를 고려한다

## 순열 및 조합
> (순서가 다르면 다른 것으로 취급한다)

```py
---
nPr = n * (n-1) * (n-2) ... * (n-r+1)
CBA 와 ABC는 다르다 (순서 고려 o)
---
from itertools import permutations
# 순열 data.length 가 n, 3이 r
result = list(permutations(data, 3))

# 중복순열 data.length 가 n, 2가 r, 2번 중복까지 허용
result = list(permutations(data, repeat=2))
```

```py
---
nCr = n * (n-1) ... (n-r+1) / r!
CBA 와 ABC 는 동일하다 (순서 고려 x)
---
# 조합
from itertools import combinations
result = combinations(data, 2)

# 중복조합
from itertools import combinations_with_replacement
result = combinations_with_replacement(data, 2)

```

## Counter : 등장횟수
```py
---
리스트와 같은 이터러블한 객체가 주여졌을 때 내부의 원소가 몇 번씩 등장했는지 알려준다
---
from collections import Counter
counter = Counter(['red', 'blue', 'red'])

counter['blue'] # 1
dict(counter) # {'red': 2, 'blue': 1}

for key, value in counter.items():
    # key: 'red', value: 1
```