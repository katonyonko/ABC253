import io
import sys

_INPUT = """\
6
3 3 9
1 1 2 1
3 2 2
2 3 2
3 3 3
3 3 1
1 2 3 3
3 3 2
3 2 3
3 1 2
1 1 10
1 1 1 1000000000
1 1 1 1000000000
1 1 1 1000000000
1 1 1 1000000000
1 1 1 1000000000
1 1 1 1000000000
1 1 1 1000000000
1 1 1 1000000000
1 1 1 1000000000
3 1 1
10 10 10
1 1 8 5
2 2 6
3 2 1
3 4 7
1 5 9 7
3 3 2
3 2 8
2 8 10
3 8 8
3 1 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    #合計にはrを含む
    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
  N,M,Q=map(int,input().split())
  query=[input().split() for _ in range(Q)]
  ans=[]
  tmp=[[0,0] for _ in range(N)]
  tmp2=[[] for _ in range(Q+1)]
  for i in range(Q):
      if query[i][0]=='2':
          tmp[int(query[i][1])-1]=[int(query[i][2]),i+1]
      elif query[i][0]=='3':
          ans.append([tmp[int(query[i][1])-1][0],tmp[int(query[i][1])-1][1],i+1,int(query[i][2])-1])
          tmp2[tmp[int(query[i][1])-1][1]].append(int(query[i][2])-1)
          tmp2[i+1].append(int(query[i][2])-1)
  dd={}
  bit=BIT(M+1)
  for i in range(Q):
      if query[i][0]=='1':
          d,l,r,x=map(int,query[i])
          bit.add(l-1,x)
          bit.add(r,-x)
      for j in tmp2[i+1]:
          dd[(i+1,j)]=bit.sum(0,j+1)
  for i in range(len(ans)):
      t=ans[i][0]
      if ans[i][2]>0:
          t+=dd[(ans[i][2],ans[i][3])]
      if ans[i][1]>0:
          t-=dd[(ans[i][1],ans[i][3])]
      print(t)