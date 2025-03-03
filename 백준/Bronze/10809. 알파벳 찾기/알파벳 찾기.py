import sys
import string
S = list(sys.stdin.readline().strip())
lower = list(string.ascii_lowercase)

positions = [-1]*26

for i in range(len(S)) :
    index = ord(S[i]) - ord('a')
    if positions[index] == -1 :
        positions[index] = i

print(" ".join(map(str,positions)))