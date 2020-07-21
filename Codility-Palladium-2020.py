
def solution(H):
   s = max(H) * len(H)
   sa = s
   for i in range(1, len(H)):
       d = (max(H[0:i]) * len(H[0:i])) + (max(H[i:]) * len(H[i:]))
       if  d < sa:
           sa = d
   return sa
   pass
