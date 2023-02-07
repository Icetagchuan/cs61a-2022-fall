# Q1: Map, Filter, Reduce
def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"
    alist = []
    for i in seq:
        alist.append(fn(i))
    return alist


def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    "*** YOUR CODE HERE ***"
    alist = []
    for i in seq:
        if pred(i):
            alist.append(i)
    return alist


def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"

    # Solutions 1
    length = len(seq)
    if length == 1:
        return seq[0]
    else:
        result = combiner(seq[0], seq[1])
        for i in range(2, length):
            result = combiner(result, seq[i])
    return result

    # Solutions2
    result = seq[0]
    for i in seq[1:]:
        result = combiner(result, i)
    return result


# Q2: Count Palindromes
def count_palindromes(L):
    """The number of palindromic strings in the sequence of strings
    L (ignoring case).
    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    >>> count_palindromes(["101", "rAcECaR", "much", "wow"])
    3
    """
    return len(my_filter(lambda s: s.lower()==s[::-1].lower(), L))


# Q4: Height
def height(t):
    # Solution 1
    if is_leaf(t): return 0
    max_height=0
    for i in branches(t):
        max_height=max(height(i),max_height)
    return max_height+1
    
    # Solution 2
    if is_leaf(t): return 0
    return 1+max([height(branch) for branch in branches(t)])


# Q5: Maximum Path Sum
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t): return label(t)
    return label(t)+max([label(branch) for branch in branches(t)])


# Q6: Find Path
def find_path(t,x):
    if label(t)==x: return [label(t)]

    for branch in branches(t):
        path=find_path(branch,x)
        if path:
            return [label(t)]+path


# Q7: Perfectly Balanced
def sum_tree(t):
    total = 0
    for b in branches(t):
        total += sum_tree(b)
    return label(t) + total

def balanced(t):
    for branch in branches(t):
        if sum_tree(branches(t)[0]) != sum_tree(branch) or not balanced(branch):
            return False
    return True


# Q8: Hailstone Tree
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H.
    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
        2
            4
                8
                    16
    >>> print_tree(hailstone_tree(8, 3))
    8
        16
            32
                64
            5
                10
    """
    if h == 0:
        return tree(n)
    branches = [hailstone_tree(n * 2, h - 1)]
    if (n - 1) % 3 == 0 and ((n - 1) // 3) % 2 == 1 and (n - 1) // 3 > 1:
        branches += [hailstone_tree((n - 1) // 3, h - 1)]
    return tree(n, branches)

def print_tree(t):
    def helper(i, t):
        print("    " * i + str(label(t)))
        for b in branches(t):
            helper(i + 1, b)
    helper(0, t)
