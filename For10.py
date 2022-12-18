def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    list2 = []
    for i in list1:
        i=i.title()
        list2.append(i)
    return list2
print(main(['rustam', 'diyor', 'alisher', 'bektosh']))