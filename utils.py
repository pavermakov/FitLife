import constants


def format_age_postfix(age):
    """Возвращает правильное окончание слова «год» по возрасту"""
    if 11 <= age % 100 <= 14:
        return "лет"

    last_digit = age % 10

    if last_digit == 1:
        return "год"

    if 2 <= last_digit <= 4:
        return "года"

    return "лет"


def calculate_bmi(weight, height):
    """Вычисляет индекс массы тела по весу и росту пользователя."""
    return weight / (height ** 2)


def get_bmi_result(bmi):
    """Возвращает категорию индекса массы тела по значению BMI."""
    if bmi < 16:
        return "Выраженный дефицит массы тела"

    if 16 <= bmi < 18.5:
        return "Недостаточная (дефицит) масса тела"

    if 18.5 <= bmi < 25:
        return "Норма"

    if 25 <= bmi < 30:
        return "Избыточная масса тела (предожирение)"

    if 30 <= bmi < 35:
        return "Ожирение 1 степени"

    if 35 <= bmi < 40:
        return "Ожирение 2 степени"

    return "Ожирение 3 степени"


def calculate_water_needed(weight):
    """Рассчитывает рекомендуемое количество воды в литрах"""
    return (weight * constants.WATER_ML_PER_KG) / constants.ML_PER_L
