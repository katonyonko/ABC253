import io
import sys

_INPUT = """\
6
2 3
--o
o--
5 4
-o--
----
----
----
-o--
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W=map(int,input().split())
  S=[input() for _ in range(H)]
  t=0
  for i in range(H):
    for j in range(W):
      if S[i][j]=='o':
        if t==0:
          si,sj=i,j
          t=1
        else:
          gi,gj=i,j
  print(abs(si-gi)+abs(sj-gj))