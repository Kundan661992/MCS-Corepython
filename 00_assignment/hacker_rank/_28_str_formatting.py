"""
Problem :

Given an integer , n, print the following values for each integer i from 1 to n :
Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should
be space-padded to match the width of the binary value of n.


Input Format :
A single integer denoting n.

Constraints :
1 <= n <= 99

Output Format :
Print n lines where each line i (in the range  1< i < n ) contains the respective decimal, octal, capitalized
hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.


Sample Input :
17

Sample Output :
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""

"""
def print_formatted(number):
    w = len(bin(number))-2
    for i in range(1, number+1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=w))


"""

"""
def print_formatted(number):
    l=len(bin(number)[2:])
    # this var 'l' has been used in rjust function and this will be shifting dec,octal,hex and bin to the right side in 
    each iteration
    #print(l)
    for i in range(1,number+1):
        dec=str(i)
        octal=oct(i)
        hexadec=hex(i)
        binary=bin(i)
        print(dec.rjust(l,' '),octal[2:].rjust(l,' '),hexadec[2:].upper().rjust(l,' '),binary[2:].rjust(l,' '))

"""


def print_formatted(number):
    width = len(f"{number:b}")
    # converts from decimal to binary format and takes length

    for i in range(1, number + 1):
        print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

# '>' means justify to the right
# '{width}' is the space padding
# 'd' = decimal
# 'o' = octal
# 'X' = hexadecimal
# 'b' = binary
