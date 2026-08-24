-- Шаг 1: Бизнес-процесс
-- Обращение клиента в ветеринарную клинику с питомцем для получения медицинских услуг, консультаций или покупки сопутствующих товаров.
-- Шаг 2: Уровень детализации (Grain)
-- Одна строка в таблице фактов соответствует одной конкретной позиции (оказанной услуге или проданному товару) в чеке за визит питомца.
-- Шаг 3: Таблицы измерений (Dimension tables)
--   - dim_client (Владельцы животных: ID, ФИО, телефон, город)
--   - dim_patient (Питомцы: ID питомца, ID владельца, кличка, вид, порода)
--   - dim_doctor (Врачи: ID врача, ФИО, специализация)
--   - dim_service (Услуги и товары: ID услуги, название, категория, цена)
--   - dim_date (Календарное измерение: ID даты, день, месяц, год)
-- Шаг 4: Таблица фактов (Fact table)
--   - fact_visits (Факты визитов и продаж: visit_id, client_id, patient_id, doctor_id, service_id, date_id, quantity, total_amount)
-- Шаг 5: Физическая модель (Схема «Звезда»)
-- Таблица измерений: Клиенты
CREATE TABLE dim_client (
    client_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    phone VARCHAR(20),
    city VARCHAR(50)
);

-- Таблица измерений: Пациенты (питомцы)
CREATE TABLE dim_patient (
    patient_id SERIAL PRIMARY KEY,
    client_id INT REFERENCES dim_client(client_id),
    pet_name VARCHAR(50),
    species VARCHAR(30),
    breed VARCHAR(50)
);

-- Таблица измерений: Врачи
CREATE TABLE dim_doctor (
    doctor_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    specialization VARCHAR(50)
);

-- Таблица измерений: Услуги и товары
CREATE TABLE dim_service (
    service_id SERIAL PRIMARY KEY,
    service_name VARCHAR(100),
    category VARCHAR(50),
    base_price DECIMAL(10, 2)
);

-- Таблица измерений: Дата
CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    date_val DATE,
    day INT,
    month INT,
    year INT
);

-- Таблица фактов: Визиты / Продажи
CREATE TABLE fact_visits (
    fact_id SEREAL PRIMARY KEY,
    visit_id SERIAL INT NOT NULL,
    client_id INT REFERENCES dim_client(client_id),
    patient_id INT REFERENCES dim_patient(patient_id),
    doctor_id INT REFERENCES dim_doctor(doctor_id),
    service_id INT REFERENCES dim_service(service_id),
    date_id INT REFERENCES dim_date(date_id),
    quantity INT,
    total_amount DECIMAL(10, 2)
);
-- Шаг 6: Аналитические запросы

-- Запрос 1: Общая выручка клиники в разрезе специализаций врачей
SELECT 
    d.specialization,
    SUM(f.total_amount) AS total_revenue
FROM fact_visits f
JOIN dim_doctor d ON f.doctor_id = d.doctor_id
GROUP BY d.specialization
ORDER BY total_revenue DESC;

-- Запрос 2: Самые популярные услуги по количеству для кошек
SELECT 
    s.service_name,
    SUM(f.quantity) AS total_count
FROM fact_visits f
JOIN dim_service s ON f.service_id = s.service_id
JOIN dim_patient p ON f.patient_id = p.patient_id
WHERE p.species = 'Кошка'
GROUP BY s.service_name
ORDER BY total_count DESC;

-- Запрос 3: Топ-5 владельцев животных по сумме трат
SELECT 
    c.full_name AS client_name,
    c.phone,
    SUM(f.total_amount) AS total_spent
FROM fact_visits f
JOIN dim_client c ON f.client_id = c.client_id
GROUP BY c.client_id, c.full_name, c.phone
ORDER BY total_spent DESC
LIMIT 5;
