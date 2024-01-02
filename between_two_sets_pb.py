
import os


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    lcm_value = a[0]
    gcd_value = b[0]

    for i in range(1, len(a)):
        lcm_value = lcm(lcm_value, a[i])

    for i in range(1, len(b)):
        gcd_value = gcd(gcd_value, b[i])

    count = 0
    multiple = lcm_value
    while multiple <= gcd_value:
        if gcd_value % multiple == 0:
            count += 1
        multiple += lcm_value

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
