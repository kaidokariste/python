def number_counter(counter, step):

    i = 0
    numbers = []

    while i < counter:
        print("At the top i is {}".format(i))
        numbers.append(i)

        i = i + step
        print("Numbers now: ", numbers)
        print("At the bottom i is {}".format(i))

    print("The numbers: ")

    for num in numbers:
        print(num)


number_counter(8,2)
