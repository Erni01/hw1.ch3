# Попросить пользователя ввести текст.
# В результате вывести процент букв в верхнем регистре и в нижнем регистре.

text = input("Enter some text: ").replace(" ", "")

text_length = len(text)

lower = upper = 0

for i in text:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1

percent_lower = lower / text_length * 100
percent_upper = upper / text_length * 100

print("Lower: " + str(percent_lower) + "%." "\nUpper: " + str(percent_upper) + "%.")