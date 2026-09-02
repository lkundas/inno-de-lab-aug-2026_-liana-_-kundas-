# Поток данных телеметрии от серверов кластера
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online"),
]

# 1, 2, 3. Распаковываем элементы, отфильтровываем offline и формируем список имен активных серверов
active_nodes = [
    node_name
    for node_name, cpu_load, ram_usage, status in system_telemetry
    if status != "offline"
]

print("Активные узлы в сети:", active_nodes)

# Формируем отдельные списки показателей загрузки для активных серверов
cpu_loads = [
    cpu_load
    for node_name, cpu_load, ram_usage, status in system_telemetry
    if status != "offline"
]

ram_usages = [
    ram_usage
    for node_name, cpu_load, ram_usage, status in system_telemetry
    if status != "offline"
]

# 4. Рассчитываем суммарные показатели активной группы
active_nodes_count = len(active_nodes)

# Средняя нагрузка CPU с округлением до двух знаков после запятой
average_cpu = round(sum(cpu_loads) / active_nodes_count, 2)

# Пиковое (максимальное) значение использования оперативной памяти RAM
max_ram = max(ram_usages)

# 5. Помещаем рассчитанные метрики в итоговый вложенный словарь и выводим его структуру
telemetry_report = {
    "active_nodes_count": active_nodes_count,
    "metrics": {"average_cpu": average_cpu, "max_ram": max_ram},
}

print("Итоговый отчет телеметрии:")
print(telemetry_report)