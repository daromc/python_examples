def main():
    x = float(input("What number is x? "))
    y = float(input("What number is y? "))
    compare(x, y)

def compare(n, m):
    if (n > m):
        print("x is greater than y")
    elif (n < m):
        print("x is less than y")
    else:
        print("both numbers are the same !")

main()
