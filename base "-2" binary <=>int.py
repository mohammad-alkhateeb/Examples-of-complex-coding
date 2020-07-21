def int2binary(X):
  c=[]
  while (x!=0):
    r = X % -2
    X //= -2
    if r < 0 :
      r+= 2
      X += 1
    c = c+[r] 
  return c

def binary2int(A):
  val=0
  for i in  range(0,len(A)):
    val+=A[i]*pow(-2,i)
  return val
