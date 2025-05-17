def string_array():
    numOne = list(map(int, input("Enter numbers separated by commas: ").split()))
    print("list", numOne)

def array_sum():
    numOne = list(map(int, input("Enter numbers separated by commas: ").split()))
    ans = sum(numOne)
    print("sum", ans)

def find_max_and_min():
    numOne = list(map(int, input("Enter numbers separated by space: ").split()))

    minimum = min(numOne)
    maximum = max(numOne)

    print("minimum", minimum)
    print("maximum", maximum)

def even_odd():
    numOne = list(map(int, input("Enter numbers separated by commas: ").split()))

    even = 0
    odd = 0

    for num in numOne:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("even", even)
    print("odd", odd)



def reverse_without_reverse():
    numOne = list(map(int, input("Enter numbers separated by space: ").split()))

    a_reverse = numOne[::-1]

    print("reverse", a_reverse)

def no_dupes():
    numOne = list(map(int, input("Enter numbers separated by space: ").split()))
    numOne = list(dict.fromkeys(numOne))
    print("no dupes: ", numOne)

def second_largest():
    numOne = list(map(int, input("Enter numbers separated by space: ").split()))
    max1 = max2 = float("-inf")

    for num in numOne:
        if num > max1:
            max2 = max1

            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    print("second largest: ", max2)








def main():
    print("select your option")
    choice = int(input("Enter you option: "))
    if choice == 1:
        string_array()
    elif choice == 2:
        array_sum()
    elif choice == 3:
        find_max_and_min()
    elif choice == 4:
        even_odd()
    elif choice == 5:
        reverse_without_reverse()
    elif choice == 6:
        second_largest()
    elif choice == 7:
        no_dupes()
    elif choice == 0:
        print("goodbye")
        exit()

while 1:
    main()
