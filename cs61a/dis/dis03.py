# Q4: Is Prime
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def is_factor(i):
        if i>=n: return True
        if i<n and n%i==0: return False
        return is_factor(i+1)
    return is_factor(2)


# Q5: Recursive Hailstone
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    count=1
    def hailstone_r(n,count):
        print(n)
        if n==1: return count
        if n%2==0:return hailstone_r(n//2,count+1)
        else: return hailstone_r(n*3+1,count+1)
    return hailstone_r(n,count)

# Q6: Merge Numbers
def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"

    if n1==0:return n2
    if n2==0:return n1

    if n1%10<=n2%10: return merge(n1//10,n2)*10+n1%10
    else :return merge(n1,n2//10)*10+n2%10