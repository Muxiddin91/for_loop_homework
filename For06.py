def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    x = 0
    while A<=B:
        x+=A
        A+=1
    return x
print (main(4,7))