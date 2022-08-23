import io
import sys

_INPUT = """\
6
5 3 6
10 12 36
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
    from bisect import bisect_left, bisect_right
    from itertools import accumulate
    N,L,R=map(int,input().split())
    A=[i+1 for i in range(N)]
    tmp=[0]
    for i in range(N-1): tmp.append(N-1-i)
    tmp=list(accumulate(tmp))
    l,r=bisect_left(tmp,L),bisect_right(tmp,R)
    if l==r:
        for i in range(R-L+1): A[l-1],A[l-1+L-tmp[l-1]+i]=A[l-1+L-tmp[l-1]+i],A[l-1]
    else:
        for i in range(N-L+tmp[l-1]-l+1):
            A[l-1],A[l-1+L-tmp[l-1]+i]=A[l-1+L-tmp[l-1]+i],A[l-1]
        if r-l>1:
            A=A[:l]+A[-(r-l-1):][::-1]+A[l:l+N-r+1]
        for i in range(R-tmp[r-1]):A[r-1],A[r+i]=A[r+i],A[r-1]
    print(*A)