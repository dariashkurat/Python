
def shortest_word():
    A = input("Enter words: ").split()

    shortest = min(A, key=len)

    print("Shortest word:", shortest)
    return shortest

shortest_word()
