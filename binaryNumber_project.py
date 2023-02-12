# 1. THIS IS THE add(a, b, c) FUNCTION
def add(a, b, c):
    # This is full adder. It adds given binary values. Return values using or, and, not operator.
    # A tuple of three booleans (d0,d1,d2) will represent the binary numeral 𝑑2𝑑1𝑑0
    # It represents the number 𝑑2 × 2^2 + 𝑑1 × 2^1 + 𝑑0 × 2^0
    # XOR is used to get the unit's place bit of the required answer.
    # XOR will be used twice, first to add a and b, and then to add the result to c to get the final unit's bit
    # d variable is basically a xor b.
    d = (a or b) and not (a and b)
    # s1 is basically d xor c
    s1 = (a and b) or (a and c) or (b and c)
    s0 = (d or c) and not (d and c)
    return s0, s1
    # The value returned is addition of a, b and c


# 2. THIS IS THE add4(a0, a1, a2, a3, b0, b1, b2, b3, c0) FUNCTION

# This is a 4-bit adder which adds two 4-bit numerals and one 1-bit numeral termed as carrier.
# While adding, we get two terms, sum and carry.
# To calculate carry, I have defined carry function.
# To calculate sum, I have used sum1 function.


def carry(a, b, c):
    return (a and b) or (a and c) or (b and c)


# carry gives the carry bit.


def xor(a, b):
    return (a or b) and not (a and b)


# xor is defined to calculate sum1.

def sum1(a, b, c):
    d = xor(a, b)
    return (d or c) and not (d and c)


# sum1 gives the sum.


def add4(a0, a1, a2, a3, b0, b1, b2, b3, c0):
    d0 = sum1(a0, b0, c0)  # Sum calculated by sum1 function
    # The argument inside the sum1 function will be used again inside the carry function to get the carrier value for the next sum.
    d1 = sum1(a1, b1, carry(a0, b0, c0))
    d2 = sum1(a2, b2, carry(a1, b1, carry(a0, b0, c0)))
    d3 = sum1(a3, b3, carry(a2, b2, carry(a1, b1, carry(a0, b0, c0))))
    d4 = carry(a3, b3, carry(a2, b2, carry(a1, b1, carry(a0, b0, c0))))

    return d0, d1, d2, d3, d4


# 3. THIS IS THE COMPARATOR FUNCTION cmp(a0,a1,a2,a3, b0,b1,b2,b3)

# Last two digits of my entry number are 83. Hence, remainder is 3.
# Comparator sign is >=
# I have used the following functions for making the cmp function:-


def union(a, b):  # Synonymous to the OR gate
    return a or b


# Here I have used union to find out the value of the bit.
# XOR gate can be used to check whether two given values are equal or not.
# If two unequal values are given to xor, then it gives true, else it gives false.


def cmp(a0, a1, a2, a3, b0, b1, b2, b3):
    # I have compared the 4-bit numeral by comparing each bit.
    # This part compares a3 and b3 using xor function
    if xor(a3, b3) is True:
        if union(a3, not b3) is True:
            return True  # i.e. a3 = True and b3 = 0
        elif union(a3, not b3) is False:
            return False  # i.e. a3 = False and b3 = True
    # This part compares a2 and b2
    elif xor(a3, b3) is False:  # i.e. a3 = b3
        if xor(a2, b2) is True:
            if union(a2, not b2) is True:
                return True  # i.e. a2 = True and b2 = False
            elif union(a2, not b2) is False:
                return False  # i.e. a2 = False and b2 = True
        # This part compares a1 and b1
        elif xor(a2, b2) is False:  # i.e. a2 = b2
            if xor(a1, b1) is True:
                if union(a1, not b1) is True:
                    return True  # i.e. a1 = True and b1 = False
                elif union(a1, not b1) is False:
                    return False  # i.e. a1 = False and b1 = True
            # This part compares a0 and b0
            elif xor(a1, b1) is False:  # i.e. a1 = b1
                if xor(a0, b0) is True:
                    if union(a0, not b0) is True:
                        return True  # i.e a0 = True and b0 = False
                    elif union(a0, not b0) is False:
                        return False  # i.e. a0 = False and b0 = True
                elif xor(a0, b0) is False:
                    return True  # i.e. a0 = b0


# 4. THIS IS THE sub4(a0, a1, a2, a3, b0, b1, b2, b3) FUNCTION

# This is a 4 bit subtractor that subtracts two given 4 bit binary using a 4 bit adder.
# It also gives the final value with its sign either + or -
# To give the sign, I have used comparator i.e. the cmp() function
# add4(a0, a1, a2, a3, b0, b1, b2, b3, c0) is used by neglecting the carry bit of the add4 function.


def add4i(a0, a1, a2, a3, b0, b1, b2, b3, c0):
    (d0, d1, d2, d3, d4) = add4(a0, a1, a2, a3, b0, b1, b2, b3, c0)
    return d0, d1, d2, d3  # NOTE that d4 is not returned to the function


# Now I have defined the sub4 function
def sub4(a0, a1, a2, a3, b0, b1, b2, b3):
    e4 = not cmp(a0, a1, a2, a3, b0, b1, b2, b3)
    if cmp(a0, a1, a2, a3, b0, b1, b2, b3) is True:
        (d0, d1, d2, d3) = (not b0, not b1, not b2, not b3)
        c0 = True
        (e0, e1, e2, e3) = add4i(a0, a1, a2, a3, d0, d1, d2, d3, c0)
        return e0, e1, e2, e3, e4
    else:
        (d0, d1, d2, d3) = (not a0, not a1, not a2, not a3)
        c0 = True
        (e0, e1, e2, e3) = add4i(b0, b1, b2, b3, d0, d1, d2, d3, c0)
        return e0, e1, e2, e3, e4


# 5. THIS IS THE add8(a, b, c) FUNCTION.

# Similar to the add4 function, the carry function is used here.
# Further, the add4i(a0, a1, a2, a3, b0, b1, b2, b3, c) is used which returns add4(a0, a1, a2, a3, b0, b1, b2, b3, c) neglecting the carry bit


def add8(a, b, c):
    (a0, a1, a2, a3, a4, a5, a6, a7) = a
    (b0, b1, b2, b3, b4, b5, b6, b7) = b
    d4 = carry(a3, b3, carry(a2, b2, carry(a1, b1, carry(a0, b0, c))))
    cout = carry(a7, b7, carry(a6, b6, carry(a5, b5, carry(a4, b4, d4))))
    (x0, x1, x2, x3) = add4i(a0, a1, a2, a3, b0, b1, b2, b3, c)  # NOTE that add4i does not returns the carry bit.
    (x4, x5, x6, x7) = add4i(a4, a5, a6, a7, b4, b5, b6, b7, d4)
    s = (x0, x1, x2, x3, x4, x5, x6, x7)
    return s, cout


# 6. THIS IS THE mul4(a, b) FUNCTION

# Here I have defined the add8 function as add8i(a0, a1, a2, a3, a4, a5, a6, a7, b0, b1, b2, b3, b4, b5, b6, b7, c)
# It takes the value as two 8-bit numbers. It returns the sum except the carry bit of the add8 function.
def add8i(a0, a1, a2, a3, a4, a5, a6, a7, b0, b1, b2, b3, b4, b5, b6, b7, c):
    d4 = carry(a3, b3, carry(a2, b2, carry(a1, b1, carry(a0, b0, c))))
    (x0, x1, x2, x3) = add4i(a0, a1, a2, a3, b0, b1, b2, b3, c)
    (x4, x5, x6, x7) = add4i(a4, a5, a6, a7, b4, b5, b6, b7, d4)
    return x0, x1, x2, x3, x4, x5, x6, x7  # NOTE that the cout variable defined earlier in add8 is not returned.


# This is the modified sub4 function which neglects the boolean value corresponding to sign of subtraction.
def sub4i(a0, a1, a2, a3, b0, b1, b2, b3):
    (e0, e1, e2, e3, e4) = sub4(a0, a1, a2, a3, b0, b1, b2, b3)
    return e0, e1, e2, e3


# The mul4(a, b) acts recursively, by using repeated addition.
# For the base case, if both a and b have all 4 values as false, then the return value will be false.
# For the else case, I have defined another function as mul(a0, a1, a2, a3, b0, b1, b2, b3).
def mul4(a, b):
    (a0, a1, a2, a3) = a
    (b0, b1, b2, b3) = b
    if (a0, a1, a2, a3) == (False, False, False, False) or (b0, b1, b2, b3) == (False, False, False, False):
        return False, False, False, False, False, False, False, False
    else:
        return mul(a0, a1, a2, a3, b0, b1, b2, b3)


def mul(a0, a1, a2, a3, b0, b1, b2, b3):
    a = (a0, a1, a2, a3)
    b = sub4i(b0, b1, b2, b3, True, False, False, False)  # This step is basically subtracting one each time from b.
    (c0, c1, c2, c3, c4, c5, c6, c7) = mul4(a, b)
    # The False values are written here to satisfy the argument of the add8i function.
    # The last False value written signifies the initial carry bit in the add8i function.
    return add8i(c0, c1, c2, c3, c4, c5, c6, c7, a0, a1, a2, a3, False, False, False, False, False)
