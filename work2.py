user_input = str(input("Введите слово:"))
word1 = user_input[:len(user_input)//2]
word2 = user_input[len(user_input)//2:]
print("Результат:", word1, word2)