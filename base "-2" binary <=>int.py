# In base -2 integers are represented by sequences of bits in the following way.
# Bits are ordered from the least to the most significant. Sequence B of N bits
# represents the number: sum(B[i] * (-2)^i for i = 0..N-1). The empty sequence represents 0.
# Note that such representation is suitable for both positive and negative numbers.

# In regular english:
# You are given a binary number in the form of an array in base -2
# Base -2 works in the following way:
# Given an array A = [1,1,0,1,1,0,1]
# The number is: 1 + (-2) + 0 + (-8) + 16+0+64 = 71. The numbers come from the following operations.
# A[0] * -2 ^ 0 = 1 * 1 = 1
# A[1] * -2 ^ 1 = 1 *-2 = -2
# A[2] * -2 ^ 2 = 0
# A[3] * -2 ^ 3 = 1 *-8 = -8
# A[4] * -2 ^ 4 = 1 *16 = 16
# A[5] * -2 ^ 5 = 0 *-32 = -8
# A[6] * -2 ^ 6 = 1 *64= 64


# We have to express now -71 in base -2
# Which would be [1, 0, 0, 1, 0, 0, 1, 1]
# A[0] * -2 ^ 0 = 1 * 1 = 1
# A[1] * -2 ^ 1 = 0
# A[2] * -2 ^ 2 = 0
# A[3] * -2 ^ 3 = 1 *-8 = -8
# A[4] * -2 ^ 4 = 0 *16 = 0
# A[5] * -2 ^ 5 = 0 *-32 = 0
# A[6] * -2 ^ 6 = 1 *64= 64
# A[7] * -2 ^ 7 = 1 *-128 = -128



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
