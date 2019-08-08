def compressString(chars):
# Time Complexity - O(n), Space Complexity - O(n)

  i, count = 1, 1
  ch = chars[i]
  res = []

  while i < len(chars):
    if chars[i] != ch:
      res.append(ch)
      res.append(str(count))
      ch = chars[i]
      count = 0
    count += 1
    i += 1
  
  res.append(ch)
  res.append(str(count))

  return (res)

chars = "aaabbccdddee"
print (compressString(chars))
