def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    list1 = []
    a = 0
    while a<n:
        list1=list1+[a]
        a+=1
    return str(list1)
print (main(5))