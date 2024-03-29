info_form = [
    (1, 'Александр', 'Иванов', '1990-01-01', 'Мужской', '2020-01-01', 'Менеджер', 'Отдел продаж', 100000),
    (2, 'Андрей', 'Петров', '1991-02-02', 'Мужской', '2020-02-02', 'Менеджер', 'Отдел продаж', 100000),
    (3, 'Дмитрий', 'Сидоров', '1992-03-03', 'Мужской', '2020-03-03', 'Менеджер', 'Отдел продаж', 100000),
    (4, 'Евгений', 'Смирнов', '1993-04-04', 'Мужской', '2020-04-04', 'Менеджер', 'Отдел продаж', 100000),
    (5, 'Иван', 'Кузнецов', '1994-05-05', 'Мужской', '2020-05-05', 'Менеджер', 'Отдел продаж', 100000),
    (6, 'Константин', 'Васильев', '1995-06-06', 'Мужской', '2020-06-06', 'Менеджер по закупкам и снабжению', "Отдел закупок", 120000),
    (7, "Алексей", "Попов", "1996-07-07", "Мужской", "2020-07-07", "Менеджер по закупкам и снабжению", "Отдел закупок", 120000),
    (8, "Антон", "Смирнов", "1997-08-08", "Мужской", "2020-08-08", "Менеджер по закупкам и снабжению", "Отдел закупок", 120000),
    (9, "Владимир", "Кузнецов", "1998-09-09", "Мужской", "2020-09-09", "Менеджер по закупкам и снабжению", "Отдел закупок", 120000),
    (10, "Денис", "Васильев", "1999-10-10", "Мужской", "2020-10-10", "Менеджер по закупкам и снабжению", "Отдел закупок", 120000),
    (11, "Елизавета", "Попова", "2000-11-11", "Женский", "2020-11-11", "Главный бухгалтер", "Финансовый отдел", 150000),
    (12, "Ирина", "Смирнова", "2001-12-12", "Женский", "2020-12-12", "Заместитель главного бухгалтера", "Финансовый отдел", 140000),
    (13, "Ксения", "Кузнецова","2002-01-13","Женский","2021-01-13","Бухгалтер","Финансовый отдел", 130000),
    (14, "Людмила", "Васильева", "2003-02-14", "Женский", "2021-02-14", "Бухгалтер", "Финансовый отдел", 130000),
    (15, "Мария", "Попова", "2004-03-15", "Женский", "2021-03-15", "Бухгалтер", "Финансовый отдел", 130000),
    (16, "Наталья", "Смирнова", "2003-04-16", "Женский", "2021-04-16", "Бухгалтер", "Финансовый отдел", 130000),
    (17, "Ольга", "Кузнецова","2001-05-17","Женский","2021-05-17","Бухгалтер","Финансовый отдел", 130000),
    (18, 'Павел', 'Васильев', '2001-06-18', 'Мужской', '2021-06-18', 'Менеджер по продажам', 'Отдел продаж', 100000),
    (19, 'Роман', 'Попов', '2002-07-19', 'Мужской', '2021-07-19', 'Менеджер по продажам', 'Отдел продаж', 100000),
    (20, 'Сергей', 'Смирнов', '2001-08-20', 'Мужской', '2021-08-20', 'Менеджер по продажам', 'Отдел продаж', 100000),
    (21, 'Тимофей', 'Кузнецов', '2000-09-21', 'Мужской', '2021-09-21', 'Менеджер по продажам','Отдел продаж', 100000),
    (22, 'Ульяна', 'Васильева','2001-10-22','Женский','2021-10-22','Менеджер по закупкам и снабжению', 'Отдел закупок',120000),
    (23, 'Федор','Попов','2002-11-23','Мужской','2021-11-23','Менеджер по закупкам и снабжению','Отдел закупок',120000),
    (24, 'Христина','Смирнова','2000-12-24','Женский','2021-12-24', 'Менеджер по закупкам и снабжению','Отдел закупок',120000),
    (25, 'Цветана','Кузнецова','2000-01-25','Женский','2022-01-25', 'Менеджер по закупкам и снабжению','Отдел закупок',120000),
    (26, 'Вячеслав','Васильев','2002-02-26','Мужской','2022-02-26', 'Менеджер по закупкам и снабжению','Отдел закупок',120000),
    (27, 'Шарлотта','Попова','2001-03-27','Женский','2022-03-27','Главный бухгалтер','Финансовый отдел',150000),
    (28, 'Эдуард', 'Смирнов', '2001-04-28', 'Мужской', '2022-04-28', 'Главный бухгалтер', 'Финансовый отдел', 150000),
    (29, 'Юлия', 'Кузнецова','1992-05-29','Женский','2022-05-29','Заместитель главного бухгалтера', 'Финансовый отдел',140000),
    (30, 'Ярослав', 'Васильев','1999-06-30','Мужской','2022-06-30','Заместитель главного бухгалтера','Финансовый отдел',140000),
    (31, "Александра", "Попова", "2000-07-01", "Женский", "2022-07-01", "Бухгалтер", "Финансовый отдел", 130000),
    (32, "Анна", "Смирнова", "2001-08-02", "Женский", "2022-08-02", "Бухгалтер", "Финансовый отдел", 130000),
    (33, "Дарья", "Кузнецова","2001-09-03","Женский","2022-09-03","Бухгалтер","Финансовый отдел", 130000),
    (34, "Иван", "Иванов", "1999-01-01", "Мужской", "2022-10-04", "Системный администратор", "IT отдел", 150000),
    (35, "Петр", "Петров", "2000-02-02", "Мужской", "2022-11-05", "Программист","IT отдел", 150000),
    (36, "Сидор", "Сидоров", "2001-03-06", "Мужской", "2022-12-06", "Тестировщик","IT отдел", 150000),
    (37, 'Александр', 'Иванов', '1990-01-01', 'Мужской', '2020-01-01', 'Разработчик', 'IT отдел', 100000),
    (38, 'Андрей', 'Петров', '1991-02-02', 'Мужской', '2020-02-02', 'Тестировщик', 'IT отдел', 90000),
    (39, 'Дмитрий', 'Сидоров', '1992-03-03', 'Мужской', '2020-03-03', 'Аналитик', 'IT отдел', 110000),
    (40, 'Евгения', 'Смирнова', '1993-04-04', 'Женский', '2020-04-04', 'Разработчик интерфейсов', 'IT отдел', 120000),
    (41, 'Екатерина', 'Васильева', '1994-05-05', 'Женский', '2020-05-05', 'Системный администратор', 'IT отдел', 95000),
    (42, 'Инна', 'Кузнецова', '1995-06-06', 'Женский', '2020-06-06', 'Разработчик баз данных', 'IT отдел', 105000),
    (43, 'Ксения', 'Новикова', '1996-07-07','Женский','2020-07-07','Тестировщик','IT отдел' , 90000),
    (44, "Мария", "Попова", "1997-08-08", "Женский", "2020-08-08", "Аналитик", "IT отдел", 110000),
    (45, "Николай", "Козлов", "1998-09-09", "Мужской", "2020-09-09", "Разработчик интерфейсов", "IT отдел", 120000.00),
    (46, "Ольга", "Лебедева", "1999-10-10", "Женский", "2020-10-10", "Системный администратор", "IT отдел", 95000),
    (47, "Павел", "Соколов", "2000-11-11", "Мужской", "2020-11-11", "Разработчик баз данных", "IT отдел", 105000),
    (48, "Сергей", "Кузьмин", "2001-12-12","Мужской","2020-12-12","Тестировщик","IT отдел" , 90000),
    (49, "Татьяна","Иванова","2002-01-13","Женский","2021-01-13","Аналитик","IT отдел" , 110000),
    (50, "Федор","Петров","2003-02-14","Мужской","2021-02-14","Разработчик интерфейсов","IT отдел" ,120000),
    (51, "Юлия","Сидорова","2004-03-15","Женский","2021-03-15","Системный администратор","IT отдел" ,95000),
    (52, 'Александр', 'Иванов', '1960-01-01', 'Мужской', '2020-01-01', 'Разработчик', 'IT отдел', 100000),
    (53, 'Андрей', 'Петров', '1961-02-02', 'Мужской', '2020-02-02', 'Тестировщик', 'IT отдел', 90000),
    (54, 'Дмитрий', 'Сидоров', '1962-03-03', 'Мужской', '2020-03-03', 'Аналитик', 'IT отдел', 110000),
    (55, 'Евгений', 'Смирнова', '1963-04-04', 'Женский', '2020-04-04', 'Разработчик интерфейсов', 'IT отдел', 120000),
    (56, 'Екатерина', 'Васильева', '1964-05-05', 'Женский', '2020-05-05', 'Системный администратор', 'IT отдел', 95000),
    (57, "Диана", "Галушкина", "2006-03-12", "Женский", "2023-03-31","Директор", "Главный отдел", 1000000),
]


import random
import datetime


start_date = datetime.date(2022, 10, 20)
end_date = datetime.date(2023, 4, 20)

def generate_data(id, end):
    id_employee = random.randint(1, 56)
    start_dat = generate_date(end)
    finish_date = generate_date(end, start_dat)
    reason = random.choice(['Болезнь', 'Травма'])
    if reason == 'Болезнь':
        diagnosis = random.choice(['Грипп', 'ОРВИ', 'Простуда', 'Мигрень', 'Аллергия', 'Ангина'])
    elif reason == 'Травма':
        diagnosis = random.choice(['Ушиб', 'Перелом', 'Ожог', 'Растяжение', 'Вывих'])
    paid_for = random.choice([True, False])
    return (id, id_employee, start_dat.strftime('%Y-%m-%d'), finish_date.strftime('%Y-%m-%d'), reason, diagnosis, paid_for)

def generate_date(end, start=None):
    if start is None:
        start = start_date
    return start + datetime.timedelta(days=random.randint(2, (end - start).days))
    

data_sick_leave = [generate_data(i+1, end_date) for i in range(50)]

# print(data)