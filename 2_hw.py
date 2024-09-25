#Задача 1.
def task_1() -> None:
    name: str = 'Elvira'
    print(name, "относится к типу", type(name))

    age: int = 26
    print(age, "относится к типу", type(age))

    time: float = 13.54
    print(time, "относится к типу", type(time))

    visit: list = [1.09, 2.09, 3.09, 4.09, 5.09, 6.09, 10.09, 11.09, 12.09, 13.09, 14.09, 15.09, 16.09, 17.09, 18.09, 19.09, 20.09, 21.09, 22.09, 23.09, 24.09, 25.09, 26.09, 27.09, 28.09, 29.09, 30.09, 31.09]
    print(visit, "относится к типу", type(visit))
    print("visit = ", visit[5])

    presence: bool = True
    if presence:
        print('presence = True')
    else:
        print('presence != True')

    print(presence, "относится к типу", type(presence))


task_1()



#Задача 2.
def task_2() -> list[int]:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[:3])

task_2()


#Задача 3.
def task_3(x: float) -> float:
    return x ** 2
result = task_3(6)
print(result)

