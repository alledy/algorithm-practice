def pick(n, picked, to_pick):
  if to_pick == 0:
    print(picked)
    return
  smallest = 0 if len(picked) == 0 else picked[-1]+1
  for i in range(smallest, n):
    picked.append(i)
    pick(n,picked,to_pick-1)
    picked.pop()
pick(6, [], 3)