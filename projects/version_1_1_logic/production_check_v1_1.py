print("="*40)

temperature = int(input("Температура (°С): "))
pressure = int(input("Давление (бар): "))
raw_material = int(input("Сырье (кг): "))

all_conditions_are_fulfilled = ((18 <= temperature <= 25) and (100 <= pressure <= 200) and (raw_material > 500))

if all_conditions_are_fulfilled:
    print("Все условия выполнены!")
    print("Смена может начаться")
else:
    print("Есть проблемы")
    print("Смену начинать нельзя")

problems = 0

if not (18 <= temperature <= 25):
    problems += 1
if not (100 <= pressure <= 200):
    problems += 1
if not (raw_material > 500):
    problems += 1
print(f"Найдено проблем: {problems}")

print("="*40)
