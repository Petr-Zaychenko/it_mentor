def first_decoratory(func):
    def wrapper(*args, **kwargs):
        print("--------что то делаем в декораторе перед фвызовом функции   ")
        res = func(*args, **kwargs)
        print("--------что то делаем в декораторе после вызова функции   ")
        return res
    return wrapper
@first_decoratory
def my_func(a,b,c):
    print(f"Самая простая функция ")
    return f"переданы : {a} , {b} , {c}"
# my_func(1, 5, 6)
res1 = my_func("первое", "второе", "третье")
print(res1)