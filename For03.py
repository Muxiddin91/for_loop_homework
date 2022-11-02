def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    list1 = []
    a=0
    while a<n:
        list1=list1+[k]
        a+=1
    return list1
print (main(3,5))