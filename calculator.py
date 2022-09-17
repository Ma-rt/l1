import math


def validate_input(input_field_text):
    while True:
        user_input = input(input_field_text)
        if user_input.isdigit():
            return float(user_input)
        else:
            print("Введенное значение не является числом!")


def get_two_args(first_arg_input_field_text="Введите первое число:", second_arg_input_field_text="Введите второе число:"):
    x = validate_input(first_arg_input_field_text)
    y = validate_input(second_arg_input_field_text)
    return x, y


def get_one_arg(arg_input_field_text="Введите число:"):
    x = validate_input(arg_input_field_text)
    return x


def addition():
    return sum(get_two_args())


def divide():
    a, b = get_two_args()
    return a / b


def substraction():
    a, b = get_two_args()
    return a - b


def multiply():
    a, b = get_two_args()
    return a * b


def upow():
    a, b = get_two_args(first_arg_input_field_text="Введите число:",
                        second_arg_input_field_text="Введите показатель степени:")
    return a ** b


def log():
    a, b = get_two_args(first_arg_input_field_text="Введите число:",
                        second_arg_input_field_text="Введите основание логарифма:")
    return math.log(a, b)


def round_to_up():
    a, b = get_two_args(first_arg_input_field_text="Введите число:",
                        second_arg_input_field_text="Введите количество чисел после запятой:")
    return math.ceil(a * (10 ** b)) / (10 ** b)


def round_to_bottom():
    a, b = get_two_args(first_arg_input_field_text="Введите число:",
                        second_arg_input_field_text="Введите количество чисел после запятой:")
    return math.floor(a * (10 ** b)) / (10 ** b)


operations = {
    "сложение": addition,
    "деление": divide,
    "вычитание": substraction,
    "умножение": multiply,
    "степень": upow,
    "логарифм": log,
    "округление вверх": round_to_up,
    "округление вниз": round_to_bottom
}
exit_operation = "выход"

string_with_operations_list = '\n'.join(operations.keys())

operation = ""

while True:
    print("=" * 10)
    operation = input(f"Введите {exit_operation}, чтобы выйти. \nВыберите операцию:\n{string_with_operations_list}")
    if operation in operations.keys():
        print(f"Результат:{operations[operation]()}")
    elif operation == exit_operation:
        exit()
    else:
        print("Такой операции не существует или введена некорректно")
