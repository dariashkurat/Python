
import nltk
import string
from collections import Counter
import matplotlib.pyplot as plt

# Завантажуємо потрібні пакети NLTK
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# 1. Зчитування тексту з файлу
with open("carroll-alice.txt", encoding="utf-8") as f:
    text = f.read()

# 2. Розбиття тексту на слова
words = word_tokenize(text)

# 3. Кількість слів у тексті
print("Кількість слів у тексті:", len(words))

# 4. 10 найчастіше вживаних слів (БЕЗ обробки)
freq = Counter(words)
top_10 = freq.most_common(10)

print("\n10 найчастіше вживаних слів:")
for word, count in top_10:
    print(word, "—", count)

# Побудова діаграми
words_list, counts_list = zip(*top_10)

plt.figure()
plt.bar(words_list, counts_list)
plt.title("ТОП-10 слів (без очищення)")
plt.xlabel("Слова")
plt.ylabel("Кількість")
plt.show()

# 5. Видалення стоп-слів та пунктуації
from nltk.corpus import stopwords
import string

stop_words = set(stopwords.words("english"))

clean_words = []

for word in words:
    word = word.lower()
    if word.isalpha() and word not in stop_words:
        clean_words.append(word)

# 6. Нові 10 найпопулярніших слів
clean_freq = Counter(clean_words)
clean_top_10 = clean_freq.most_common(10)

print("\n10 найчастіше вживаних слів після очищення:")
for word, count in clean_top_10:
    print(word, "—", count)

# Побудова очищеної діаграми
clean_words_list, clean_counts_list = zip(*clean_top_10)

plt.figure()
plt.bar(clean_words_list, clean_counts_list)
plt.title("ТОП-10 слів (після очищення)")
plt.xlabel("Слова")
plt.ylabel("Кількість")
plt.show()
