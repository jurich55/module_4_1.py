
def fake_divide (first, second):
    if second != 0:
        return first / second
    if second == 0:
        return('Ошибка')


result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
print(result1)
print(result2)