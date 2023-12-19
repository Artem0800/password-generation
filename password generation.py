import random

digits = [chr(i) for i in range(48,58)]
uppercase_letters = [chr(i) for i in range(65,91)]
lowercase_letters = [chr(i) for i in range(97,123)]
punctuation = ["!","#","$","%","&","*","+","-","=","?","@","^","_"]

count_password = int(input("Сколько вам сгенирировать паролей ?"))
len_password = int(input("Сколько символов хотите ?"))
upper = input("Включать ли большие буквы ? д/н")
lower = input("Включать ли маленькие буквы д/н ?")
digit = input("Включать ли цифры ? д/н")
symbol = input("Включать ли символы ? д/н")

user_password = []

if upper == "д":
    user_password.extend(uppercase_letters)
if lower == "д":
    user_password.extend(lowercase_letters)
if digit == "д":
    user_password.extend(digits)
if symbol == "д":
    user_password.extend(punctuation)

def generate_password(chars,lenn):
    res = []
    for i in range(lenn):
        res.extend(chars)
    return "".join(random.sample(res,lenn))

for i in range(count_password):
    print(generate_password(user_password,len_password))