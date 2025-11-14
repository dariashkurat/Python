
def convert_list():
    A = list(map(float, input("Введіть дійсні числа: ").split()))

    result = [round(x) for x in A]

    print("Округлені числа:", result)
    return result
convert_list()
