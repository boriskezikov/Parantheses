
import time

start_time = time.clock()
hash = {}
str = "(?)(?)????(???)???(?)???()??()??()??"


def rec(i, depth):
  if i < len(str):
    if (i, depth) in hash:
        return hash[i, depth]
    sol = 0  # solution
    if str[i] == '(' or str[i] == '?':
        sol += rec(i+1, depth+1)      # if thesis -> next recursion depth and solution counter +1
    if str[i] == ')' or str[i] == '?':
        if depth >= 1:
            sol += rec(i+1, depth-1)
    hash[i, depth] = sol
    return sol

  else:
    # if end of the line
    if depth != 0:
        return 0
    return 1


print(rec(0, 0))
print(time.clock() - start_time, "seconds")