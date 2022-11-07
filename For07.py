def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    a = 0
    b = 0
    while a<=N:
        if a%2==1:
            b+=a
        a+=1
    return b
print (main(12))