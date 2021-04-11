import math

pod = int(input())
L = int(input())

if L > 1:
    print(round(math.log(pod, L), 2))
else:
    print(round(math.log(pod), 2))
