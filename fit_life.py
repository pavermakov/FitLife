# Проект FitLife - MVP версия 1.0
import constants
import utils


def parse_int(user_input):
    """Преобразует пользовательский ввод в целое число"""
    return int(user_input)


def parse_float(user_input):
    """Преобразует пользовательский ввод в дробное число"""
    return float(user_input)


def get_name():
    """Запрашивает у пользователя имя и возвращает непустую строку"""
    input_message = "Добрый день! Как вас зовут? "

    while True:
        if name := input(input_message).strip():
            return name

        input_message = "(!) Пожалуйста, введите хотя бы 1 символ: "


def get_age():
    """Запрашивает возраст и возвращает корректное целое число"""
    return utils.get_user_input(
        parser=parse_int,
        min_val=constants.MIN_AGE_REQUIRED,
        max_val=constants.MAX_HUMAN_AGE_RECORDED,
        initial_input_fn=lambda: input("Сколько вам лет? "),
        range_err_msg=(
            "(!) Возраст должен быть в диапазоне от "
            "{0} до {1} лет. Попробуйте ещё раз: "
        ),
        val_err_msg=(
            "(!) Введите возраст целым числом без дробной части: "
        )
    )


def get_weight():
    """Запрашивает вес и возвращает корректное значение в килограммах"""
    return utils.get_user_input(
        parser=parse_float,
        min_val=constants.MIN_HUMAN_WEIGHT_RECORDED_KG,
        max_val=constants.MAX_HUMAN_WEIGHT_RECORDED_KG,
        initial_input_fn=lambda: input("Какой у вас вес (кг)? "),
        range_err_msg=(
            "(!) Вес должен быть в диапазоне от "
            "{0} до {1} кг. Попробуйте ещё раз: "
        ),
        val_err_msg=(
            "(!) Введите вес целым или дробным числом в килограммах: "
        )
    )


def get_height():
    """Запрашивает рост и возвращает корректное значение в метрах"""
    return utils.get_user_input(
        parser=parse_float,
        min_val=constants.MIN_HUMAN_HEIGHT_RECORDED_M,
        max_val=constants.MAX_HUMAN_HEIGHT_RECORDED_M,
        initial_input_fn=lambda: input("Какой у вас рост (м.)? "),
        range_err_msg=(
            "(!) Рост должен быть в диапазоне от "
            "{0} до {1} м. Попробуйте ещё раз: "
        ),
        val_err_msg=(
            "(!) Введите рост целым или дробным числом в метрах: "
        )
    )


# Ввод данных
user_name = get_name()
user_age = get_age()
user_weight = get_weight()
user_height = get_height()


# Вычисления
bmi = utils.calculate_bmi(user_weight, user_height)
water_needed_l = utils.calculate_water_needed(user_weight)


# Вывод данных
age_postfix = utils.format_age_postfix(user_age)
bmi_result = utils.get_bmi_result(bmi)
print("-" * 50)
print(f"Отчёт для пользователя: {user_name} ({user_age} {age_postfix})")
print(f"Твой индекс массы тела: {bmi:.1f} ({bmi_result})")
print(f"Рекомендуемая норма воды: {water_needed_l:.1f} л. в день")
print("Расчёт окончен. Будьте здоровы!")
