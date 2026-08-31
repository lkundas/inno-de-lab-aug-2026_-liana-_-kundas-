# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLeXAnDer_vLaDimiRov ; mInSk ; ACTIVE "

# Шаг 1 и 2: Разбиваем по ';' и сразу очищаем каждый элемент от лишних пробелов с помощью генератора списка
parts = [item.strip() for item in raw_user_record.split(';')]

# Шаг 3: Применяем к ID префикс "UID-"
user_id = f"UID-{parts[0]}"

# Шаг 4: Обрабатываем имя (заменяем '_' на пробел и делаем слова с заглавной буквы)
name = parts[1].replace('_', ' ').title()

# Шаг 5: Название города в верхний регистр
city = parts[2].upper()

# Шаг 6: Статус пользователя в нижний регистр
status = parts[3].lower()

# Шаг 7: Объединяем обработанные элементы в одну строку с разделителем " | " и выводим

result = ' | '.join([user_id, name, city, status])
# прошлая запись result = f"Нормализованная запись: {user_id} | {name} | {city} | {status}"
print(result)
