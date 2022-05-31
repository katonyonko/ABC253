import io
import sys

_INPUT = """\
6
10 3 5
1000000000 314 159
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import math
  N,A,B=map(int,input().split())
  a,b=N//A,N//B
  c=N*math.gcd(A,B)//A//B
  print(N*(N+1)//2-a*(a+1)//2*A-b*(b+1)//2*B+c*(c+1)//2*A*B//math.gcd(A,B))