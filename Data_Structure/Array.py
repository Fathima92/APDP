import array as arr
a = arr.array('i', [1,2,3,4,5,6])
while True:
    print("1. Print Array, 2. Add Element, 3. delete element, 4. Exit")
    choice = int(input("enter you choice"))
    if choice == 1:
        print("The array Element are: ")
        for numbers in a:
            print(numbers)

    elif choice == 2:
        val = int(input("Enter any integer"))
        if isinstance(val, int):
            a.append(val)
    elif choice == 3:
        print("the value deleted was: ", a.pop())
    elif choice == 4:
        break
    else:
        print("Enter valid Choice:")



