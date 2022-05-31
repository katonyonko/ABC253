import io
import sys

_INPUT = """\
6
2 3 1
3 3 2
100 1000 500
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,M,K=map(int,input().split())
  ans=[1]*M
  aans=list(range(M+1))
  for _ in range(N-1):
    tmp=ans.copy()
    for i in range(M):
      if K!=0:
        tmp[i]=(aans[-1]-aans[min(i+K,M)]+aans[max(i+1-K,0)])%mod
      else:
        tmp[i]=aans[-1]%mod
    ans=tmp
    aans=[0]
    for i in range(M):
      aans.append(aans[-1]+ans[i])
  print(sum(ans)%mod)