"""
You are an avid rock collector who lives in southern California. Some rare and desirable rocks just became available in New York, so you are planning a cross-country road trip. There are several other rare rocks that you could pick up along the way. You have been given a grid filled with numbers, representing the number of rare rocks available in various cities across the country. Your objective is to find the optimal path from So_Cal to New_York that would allow you to accumulate the most rocks along the way.

You can only travel either north (up) or east (right).
b) Consider adding some additional tests in doTestsPass().
c) Implement optimalPath() correctly.
d) Here is an example:
^
{{0, 0, 0, 0, 5}, New_York (finish) N
{0, 1, 1, 1, 0},
So_Cal (start) {2, 0, 0, 0, 0}} S
v
The total for this example would be 10 (2+0+1+1+1+0+5).
"""

def optimizeRock(route):
  origin = (len(route)-1, 0)
  origin_i, origin_j = origin
  directions = [(-1, 0), (0, 1)]
  value = 0
  stack = []
  stack.append(origin)

  while stack:
    row, col = stack.pop()
    value += route[row][col]
    temp = []
    for d in directions:
      r, c = row + d[0], col + d[1]

      if r < 0 or r > len(route)-1 or c < 0 or c> len(route[0])-1:
        continue
      else:
        temp.append((r,c))

    if temp:
      if len(temp) > 1:
        if route[temp[0][0]][temp[0][1]] >= route[temp[1][0]][temp[1][1]]:
          stack.append(temp[0])
        else:
          stack.append(temp[1])
      else:
        stack.append(temp[0])

  return value


route = [
  [0,0,0,0,5],
  [0,1,1,1,0],
  [2,0,0,0,0]
]

print (optimizeRock(route))
