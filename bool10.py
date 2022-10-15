def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return float(pow (a,1/2))-int(pow (a,1/2))==0 and a>0
print (main(9))
