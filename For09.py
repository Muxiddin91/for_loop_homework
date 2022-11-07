def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    r = range(10)
    list1 = []
    for a in r:
        list1+=[int(price*a)]
    return list1
print(main(12))
'''r = range(5)
for i in r:
    print(i)'''