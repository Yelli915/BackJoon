import sys
N = int(sys.stdin.readline().strip())

array = list(map(int, sys.stdin.readline().strip().split()))
   
M = max(array)
new_scores = [(score / M) * 100 for score in array]
print(sum(new_scores) / N)
