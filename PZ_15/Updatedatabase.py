import sqlite3 as sq


con = sq.connect('PZ_15/database.db')

'''
Блок обновлений таблиц
'''
with con:
    cur = con.cursor()
# 1. Обновить базовую ставку сотрудника на определенной должности.

    cur.execute("""
                    UPDATE form 
                    SET base_rate = 542304
                    WHERE id_employee = 4;
                """)
    result2_1 = cur.fetchall()

# 2. Обновить отдел для всех сотрудников в определенном диапазоне возраста.

    cur.execute("""
                    UPDATE form
                    SET department = 'Отдел маркетинга'
                    WHERE birthday BETWEEN '1990-01-01' AND '1995-12-31';
                """)
    result2_2 = cur.fetchall()

# 3. Обновить дату найма для сотрудника, получившего повышение.

    cur.execute("""
                    UPDATE form
                    SET date_of_hiring = '2023-04-14'
                    WHERE id_employee = 10;
                """)
    result2_3 = cur.fetchall()


# 4. Обновить причину больничного листа для сотрудника.
    cur.execute("""
                    UPDATE sick_leave
                    SET reason = 'Травма'
                    WHERE id_employee = 39;
                """)
    result2_4 = cur.fetchall()

# 5. Обновить базовую ставку сотрудника в таблице "Анкета" на определенный
# процент, используя INNER JOIN с таблицей "Больничные листы". При этом
# необходимо исключить из обновления сотрудников, у которых были неоплаченные
# больничные листы.

    cur.execute("""
                    UPDATE form
                    SET base_rate = base_rate * (1 + 5 / 100)
                    WHERE id_employee NOT IN (
                        SELECT id_employee
                        FROM sick_leave
                    );
                """)
    result2_5 = cur.fetchall()

# # 6. Обновить дату начала больничного листа в таблице "Больничные листы" на
# # определенную дату, используя INNER JOIN с таблицей "Анкета". При этом
# # необходимо исключить из обновления больничные листы с уже пройденной датой
# # начала

#     cur.execute("""
#                     UPDATE sick_leave
#                     SET start_date = '2023-04-12'
#                     FROM sick_leave
#                     INNER JOIN form ON sick_leave.id_employee = form.id_employee
#                     WHERE start_date > '2023-04-12';
#                 """)
#     result2_6 = cur.fetchall()

# 7. Обновить причину больничного листа в таблице "Больничные листы" на
# определенное значение для всех сотрудников, работающих в отделе "Бухгалтерия".

    cur.execute("""
                    UPDATE sick_leave
                    SET reason = 'Болезнь'
                    WHERE id_employee IN (
                        SELECT id_employee
                        FROM form
                        WHERE department = 'Бухгалтерия'
                    );
                """)
    