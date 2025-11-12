

sentence = input("Введіть речення: ")
ascii_sentence = ''.join(str(ord(char)) + ' ' for char in sentence)
print("Речення з ASCII кодами літер:", ascii_sentence)
