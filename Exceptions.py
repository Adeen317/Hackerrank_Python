

def integer_division(a, b):
    try:
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

t = int(input())

for i in range(t):
    try:
        a, b = map(int, input().split())
        integer_division(a, b)
    except Exception as e:
        print("Error Code:", e)
