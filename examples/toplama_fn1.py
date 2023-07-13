def toplama(*args):
    args = list(args)
    while True:
        input_value = input("Enter to some number or press to 'q' for quit ")
        if input_value.isdigit():
            args.append(int(input_value))
        elif input_value == "q":
            break
    summ = sum(args)
    return summ

print(toplama())
