def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    a = []
    for d in range(n):
        a.append(k)
    return a
print(main(9,8))