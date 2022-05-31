import io
import sys

_INPUT = """\
6
5 3 2
2 5 3
100 100 100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  a,b,c=map(int,input().split())
  x=sorted([a,b,c])[1]
  if b==x: print('Yes')
  else: print('No')