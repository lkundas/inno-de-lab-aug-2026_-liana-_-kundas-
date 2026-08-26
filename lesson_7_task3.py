# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres",
    }
}

# 1. Извлечь значения host и port из вложенного словаря connection.
connection_dict = db_config.get("connection", {})
host_val = connection_dict.get("host")
port_val = connection_dict.get("port")

# 2. Безопасно проверить наличие ключа ssl_settings.
# Если этот ключ или вложенный в него параметр ssl_mode отсутствуют, переменная должна принять дефолтное значение verify-full.
ssl_settings = db_config.get("ssl_settings", {})
ssl_mode = ssl_settings.get("ssl_mode", "verify-full")
print(f"SSL Mode: {ssl_mode}")

# 3. Изменить значение пользователя (user) во вложенном словаре connection на admin.
connection_dict["user"] = "admin"

# 4. Добавить новый параметр max_connections со значением 100 непосредственно во вложенный словарь connection.
connection_dict["max_connections"] = 100

# 5. Вывести обновленное содержимое конфигурации connection, используя итерацию по парам ключ-значение (.items()).
print("Параметры соединения:")
for key, value in connection_dict.items():
    print(f"* {key}: {value}")