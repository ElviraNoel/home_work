# создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3, 7)
rectangle3 = Rectangle(6, 4)


for i, rect in enumerate([rectangle1, rectangle2, rectangle3], start=1):
    print(f"Rectangle {i}: Area = {rect.area()}, Perimeter = {rect.perimeter()}")


# Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"Addition: {self.a} + {self.b} = {result}")

    def multiplication(self):
        result = self.a * self.b
        print(f"Multiplication: {self.a} * {self.b} = {result}")

    def division(self):
            result = self.a / self.b
            print(f"Division: {self.a} / {self.b} = {result}")

    def subtraction(self):
        result = self.a - self.b
        print(f"Subtraction: {self.a} - {self.b} = {result}")


math_instance = Math(15, 25)
math_instance.addition()
math_instance.multiplication()
math_instance.division()
math_instance.subtraction()


# откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Button:
    def __init__(self, text, button_type="Button", locator=""):
        self.text = text
        self.button_type = button_type
        self.locator = locator

    def click(self):
        return f"Clicked on button {self.text}"

text_box_button = Button("Text Box")
check_box_button = Button("Check Box")
radio_button = Button("Radio Button")

buttons = [text_box_button, check_box_button, radio_button]
for button in buttons:
    print(button.text)

for button in buttons:
    print(button.click())
