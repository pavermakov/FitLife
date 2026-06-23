# Проект FitLife - MVP версия 1.0

# Константы
WATER_ML_PER_KG = 30
ML_PER_L = 1000

# Ввод данных
user_name = input("Добрый день! Как вас зовут? ").strip().title()
user_age = int(input("Сколько вам лет? "))
user_weight = float(input("Какой у вас вес (кг)? "))
user_height = float(input("Какой у вас рост (м)? "))

# Вычисления
bmi = user_weight / (user_height ** 2)
water_needed_l = (user_weight * WATER_ML_PER_KG) / ML_PER_L

# Вывод данных
print(f"Отчёт для пользователя: {user_name} ({user_age} г.)")
print(f"Твой индекс массы тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_needed_l:.1f} л. в день")
print("Расчет окончен. Будьте здоровы!")
