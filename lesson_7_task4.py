# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]

# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# 1. Преобразует список запрошенных ролей во множество для мгновенного удаления дубликатов.
unique_requested_roles = set(requested_roles)
print(f"Уникальные запрошенные роли: {unique_requested_roles}")

# 2. Определяет роли, которые одновременно присутствуют как в списке уникальных
# запрошенных, так и в списке обязательных административных ролей (пересечение множеств).
common_admin_roles = unique_requested_roles.intersection(required_admin_roles)
# Или с помощью оператора: common_admin_roles = unique_requested_roles & required_admin_roles
print(f"Общие административные роли: {common_admin_roles}")

# 3. Вычисляет недостающие административные роли, которые не были запрошены пользователем (разность множеств).
missing_admin_roles = required_admin_roles.difference(unique_requested_roles)
# Или с помощью оператора: missing_admin_roles = required_admin_roles - unique_requested_roles
print(f"Недостающие административные роли: {missing_admin_roles}")

# 4. Проверяет наличие роли security_officer в дедуплицированном множестве запрошенных ролей
# с помощью высокопроизводительного оператора членства, выполняющегося за время O(1).
has_security_officer = "security_officer" in unique_requested_roles
print(f"Наличие роли security_officer в запросе: {has_security_officer}")