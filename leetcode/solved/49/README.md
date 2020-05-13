# [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

## 포인트
- `Hash Table`
- [처음](./time_error.py)에 타임 에러가 났는데 그 이유가 hash를 활용하지 않아서였다. 그룹에 넣으려면, 그룹을 돌면서 anagram인 그룹이 있는지 체크해야 한다고 생각했는데, 그럴 필요가 없었다. sort를 해서 만들든, 사이즈가 26인 리스트에 알파벳 숫자를 카운트해서 넣든, 어쨌든 아나그램이면 똑같은 값을 갖게 될거고 그냥 그걸로 key로 만들면 된다.👀 그러면 리스트를 순회할 필요가 없이 O(1)로 확인이 가능하다.
- 아나그램 체크할 때 소팅 안쓰고 O(N)으로 만드는 것만 생각하다보니 그 부분을 미스했다.
- `새롭게 알게 된 것`: 
  - tuple size가지고 Init할 때 `(0,) * n` 이런 식으로 trailing comma를 넣어줘야 한다. 
  - ord(x) - 97 이런 방식으로 알파벳 x를 숫자로 바꿀 수 있다. 97을 빼면 a가 0, b가 1 이런식으로 대응되는데, 97을 외우기가 귀찮으니 `ord(x) - ord("a")` 라고 하는 것이 좋겠다.   
 

## [풀이](./index.py)

## [Ref](https://leetcode.com/articles/group-anagrams/)