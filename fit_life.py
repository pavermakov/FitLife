# Проект FitLife - MVP версия 1.0
import constants
import utils


def get_name():
    """Запрашивает у пользователя имя и возвращает непустую строку"""
    input_message = "Добрый день! Как вас зовут? "

    while True:
        name = input(input_message).strip()

        if len(name) > 0:
            return name
        else:
            input_message = "(!) Пожалуйста, введите хотя бы 1 символ: "


def get_age():
    """Запрашивает возраст и возвращает корректное целое число"""
    input_message = "Сколько вам лет? "

    while True:
        user_input = input(input_message).strip()

        if len(user_input) == 0:
            input_message = "(!) Пожалуйста, введите ваш возраст: "
            continue

        try:
            age = int(user_input)

            if age <= 0:
                input_message = (
                    "(!) Слишком маленькое значение. "
                    "Пожалуйста, введите ваш возраст: "
                )
                continue

            if age > constants.MAX_HUMAN_AGE_RECORDED:
                input_message = (
                    "(!) Слишком большое значение. "
                    "Пожалуйста, введите ваш возраст: "
                )
                continue

            return age

        except ValueError:
            input_message = (
                "(!) Неверное значение. "
                "Пожалуйста, введите ваш возраст: "
            )


def get_weight():
    """Запрашивает вес и возвращает корректное значение в килограммах"""
    input_message = "Какой у вас вес (кг)? "

    while True:
        user_input = input(input_message).strip()

        if len(user_input) == 0:
            input_message = (
                "(!) Пожалуйста, введите хотя бы приблизительное "
                "значение (кг.): "
            )
            continue

        try:
            weight = float(user_input)

            if weight < constants.MIN_HUMAN_WEIGHT_RECORDED_KG:
                input_message = (
                    "(!) Слишком маленькое значение. "
                    "Пожалуйста, введите ваш вес (кг.): "
                )
                continue

            if weight > constants.MAX_HUMAN_WEIGHT_RECORDED_KG:
                input_message = (
                    "(!) Слишком большое значение. "
                    "Пожалуйста, введите ваш вес (кг.): "
                )
                continue

            return weight

        except ValueError:
            input_message = (
                "(!) Неверное значение. "
                "Пожалуйста, введите ваш вес (кг.): "
            )


def get_height():
    """Запрашивает рост и возвращает корректное значение в метрах"""
    input_message = "Какой у вас рост (м.)? "

    while True:
        user_input = input(input_message).strip()

        if len(user_input) == 0:
            input_message = (
                "(!) Пожалуйста, введите хотя бы приблизительное "
                "значение (м.): "
            )
            continue

        try:
            height = float(user_input)

            if height < constants.MIN_HUMAN_HEIGHT_RECORDED_M:
                input_message = (
                    "(!) Слишком маленькое значение. "
                    "Пожалуйста, введите ваш рост (м.): "
                )
                continue

            if height > constants.MAX_HUMAN_HEIGHT_RECORDED_M:
                input_message = (
                    "(!) Слишком большое значение. "
                    "Пожалуйста, введите ваш рост (м.): "
                )
                continue

            return height
        except ValueError:
            input_message = (
                "(!) Неверное значение. "
                "Пожалуйста, введите ваш рост (м.): "
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
