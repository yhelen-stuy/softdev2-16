def union(a, b):
    c = [x for x in a if x not in b]
    return c + b

print "UNION"
print union([1, 2, 3], [2, 3, 4])
print union([1, 2, 3, 5], [2, 3, 4, 6])

def intersection(a, b):
    c = [x for x in a if x in b]
    return c

print "INTERSECTION"
print intersection([1, 2, 3], [2, 3, 4])
print intersection([1, 2, 3, 5, 6], [2, 3, 4, 5])

def difference(a, b):
    c = [x for x in a if x not in b]
    return c

print "SET DIFFERENCE"
print difference([1, 2, 3], [2, 3, 4])
print difference([2, 3, 4], [1, 2, 3])

def symmetric(a, b):
    c = difference(union(a, b), intersection(a, b))
    return c

print "SYMMETRIC DIFFERENCE"
print symmetric([1, 2, 3], [2, 3, 4])
print symmetric([2, 3, 4], [1, 2, 3])

def cartesian(a, b):
    c = [[x, y] for x in a for y in b]
    return c

print "CARTESIAN PRODUCT"
print cartesian([1, 2], ["red", "white"])
print cartesian([2, 3, 4], [1, 2, 3])
