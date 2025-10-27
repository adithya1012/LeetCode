def solution(A):
  """Your solution goes here."""
  if not A:
    return 0
  res = [[A[0]]]
  for h in A[1:]:
    inserted = False
    for lst in res:
      if lst[-1] > h:
        lst.append(h)
        inserted = True
        break
    if not inserted:
      res.append([h])
  return len(res)

print(solution([1,1,1,1,1]))