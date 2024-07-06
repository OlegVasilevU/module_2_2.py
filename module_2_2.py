# "Условная конструкция. Операторы if, elif, else."
first = input("Напишите первое число: ")
second = input("Напишите второе число: ")
third = input("Напишите третье число: ")
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
