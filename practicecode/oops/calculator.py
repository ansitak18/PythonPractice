def main():
    name= input("whats ur name:")
    hello(name)

def hello(to="world"):
    print("hello", to)
    hello()

main()