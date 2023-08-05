#Problem Statement: Write a function that takes the binary representation of an unsigned integer and returns the
#number of '1' bits it has (also known as the Hamming weight).

def hammingWeight(n):
    count = 0
    while n:
        count += n & 1
        n = n >> 1
    return count

print(hammingWeight(23))