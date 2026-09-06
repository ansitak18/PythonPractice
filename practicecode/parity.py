def main():
    n = int(input("what's x:"))
    if is_even(n):
        print("Even")
    else: 
        print("Odd")


def is_even(x) :
    #return True if x % 2 == 0 else False
    return (x % 2 == 0)
#here the bool value is returned as true or false for even or odd respectively
main()