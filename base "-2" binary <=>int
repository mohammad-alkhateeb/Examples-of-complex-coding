def int2binary(x):
  c=[]
  while (x!=0):
    r = x % -2
    x //= -2
    if r < 0 :
      r+= 2
      x += 1
    c = c+[r] 
  return c

def binary2int(A):
  val=0
  for i in  range(0,len(A)):
    val+=A[i]*pow(-2,i)
  return val
