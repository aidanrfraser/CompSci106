def get_first_odd():
    """
    Will bother you until you give it an odd number
    """
    num = int(input("Please enter an odd number: "))
    while num % 2 == 0:
        num = int(input("That was even. Enter an odd number. "))
    print(num)