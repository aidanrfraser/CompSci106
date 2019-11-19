def check4():
    """
    Checks if a number is a multiple of 4
    """
    fourcheck = int(num)
    if (fourcheck % 4) is 0:
        print("It's also a multiple of four!")
def main():
    """
    Main logic sector of the function, will determine if a number is even or odd
    """
    intnum = int(num)
    if (intnum % 2) is 0:
        print("Even!")
        check4()
    else:
        print("Odd!")

num = input("Hi! give me a number, and I'll tell you if it's even or odd! ")
main()