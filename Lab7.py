def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file


file1_name = "TF23_1.txt"
file2_name = "TF23_2.txt"

# a) створюємо TF23_1

file_1_w = Open(file1_name, "w")
if file_1_w is not None:
    file_1_w.write("Hello1111Word!\n")
    file_1_w.write("Python0000000Programing\n")
    file_1_w.write("hbfdc1111hjgg00\n")
    file_1_w.close()
    print("File TF23_1.txt was closed!")

# b) читаємо TF23_1 → замінюємо 1↔0 → пишемо по 15 символів

file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r is not None and file_2_w is not None:

    content = file_2_r.read()

    # Робимо заміну
    changed = ""
    for ch in content:
        if ch == "1":
            changed += "0"
        elif ch == "0":
            changed += "1"
        elif ch != "\n":   #рядкові переходи прибираємо
            changed += ch

    # Нарізаємо по 15 символів
    for i in range(0, len(changed), 15):
        file_2_w.write(changed[i:i+15] + "\n")

    file_2_r.close()
    file_2_w.close()
    print("Files were closed!")


# c) читаємо TF23_2 і друкуємо

file_3_r = Open(file2_name, "r")
if file_3_r is not None:
    print("\nNew content of TF23_2:")
    for line in file_3_r:
        print(line.strip())
    file_3_r.close()
