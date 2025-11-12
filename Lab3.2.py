

word = input("Введіть слово кирилицею: ")

latin_letters = ['i', 'a', 'o']
contains_latin = any(letter in word for letter in latin_letters)

if contains_latin:
    print("Слово містить підміну літер латиницею (i, a, o).")
else:
    print("Слово не містить латинських підмін.")
