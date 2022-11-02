import py_compile
def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    list1 = []
    a = 0
    while a<n:
        list1=list1+[a]
        a+=1
    return list1
print (main(8))