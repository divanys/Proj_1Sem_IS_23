import sqlite3 as sq


con = sq.connect('PZ_15/database.db')

'''
Блок выборки из таблиц
'''
with con:
    cur = con.cursor()
# 1. Вывести список всех сотрудников и их должностей
    cur.execute("""
                SELECT id_employee, firstname, surname, post FROM form
            """)
    result1_1 = cur.fetchall()

# 2. Вывести список всех сотрудников и их базовых ставок
    cur.execute("""
                SELECT id_employee, firstname, surname, base_rate FROM form
                """)
    result1_2 = cur.fetchall()

# 3. Вывести список всех сотрудников, работающих в отделе 'IT'
    cur.execute("""
                SELECT id_employee, firstname, surname FROM form WHERE department = 'IT отдел'
            """)
    result1_3 = cur.fetchall()

# 4. Вывести список всех сотрудников, принятых на работу после 1 января 2022 года
    cur.execute("""
                SELECT id_employee, firstname, surname FROM form WHERE date_of_hiring > '2022-01-01'
            """)
    result1_4 = cur.fetchall()

# 5. Вывести список всех больничных листов, выписанных сотруднику с id = 42
    cur.execute("""
                SELECT * FROM sick_leave WHERE id_employee = 42
            """)
    result1_5 = cur.fetchall()

# 6. Вывести список всех больничных листов, оплаченных компанией
    cur.execute("""
                SELECT * FROM sick_leave WHERE paid_for = TRUE
            """)
    result1_6 = cur.fetchall()

# 7. Вывести список всех сотрудников, имеющих больничные листы на текущий месяц
    cur.execute("""
            SELECT * FROM form WHERE id_employee IN (SELECT id_employee FROM sick_leave WHERE strftime('%m', start_date) = strftime('%m', 'now'))
            """)
    result1_7 = cur.fetchall()

# 8. Вывести среднюю базовую ставку всех сотрудников
    cur.execute("""
                SELECT AVG(base_rate) FROM form;
            """)
    result1_8 = cur.fetchall()

# 9. Вывести список всех сотрудников, имеющих базовую ставку выше 100000
    cur.execute("""
                SELECT id_employee, firstname, surname FROM form WHERE base_rate > 100000;
            """)
    result1_9 = cur.fetchall()

# 10. Вывести список всех сотрудников и общее количество дней, проведенных ими на больничном
    cur.execute("""
                SELECT form.id_employee, form.firstname, form.surname, SUM(julianday(sick_leave.finish_date) - julianday(sick_leave.start_date)) AS total_sick_days
                FROM form
                INNER JOIN sick_leave ON form.id_employee = sick_leave.id_employee
                WHERE strftime('%Y', sick_leave.start_date) = strftime('%Y', CURRENT_DATE)
                GROUP BY form.firstname, form.surname;
                """)
    result1_10 = cur.fetchall()

# 11. Вывести информацию о сотрудниках и их больничных листах за последний месяц
    cur.execute("""
                SELECT form.id_employee, form.firstname, form.surname, sick_leave.start_date, sick_leave.finish_date
                FROM form
                INNER JOIN sick_leave ON form.id_employee = sick_leave.id_employee
                WHERE strftime('%m', sick_leave.start_date) = strftime('%m', 'now', '-30 days');
            """)
    result1_11 = cur.fetchall()

# 12. Вывести среднюю продолжительность больничных листов сотрудников в каждом отделе
    cur.execute("""
                SELECT form.id_employee, form.department, AVG(julianday(sick_leave.finish_date) - julianday(sick_leave.start_date)) AS avg_duration
                FROM form
                INNER JOIN sick_leave ON form.id_employee = sick_leave.id_employee
                GROUP BY form.department;
                """)
    result1_12 = cur.fetchall()

# 13. Вывести список сотрудников и информацию о последнем больничном листе, который они оформляли
    cur.execute("""
                WITH last_sick_leaves AS (
                    SELECT id_employee,
                        MAX(start_date) AS last_start_date
                    FROM sick_leave
                    GROUP BY id_employee
                )
            SELECT f.id_employee, 
                f.firstname,
                f.surname,
                sl.start_date,
                sl.finish_date,
                sl.reason,
                sl.diagnosis,
                sl.paid_for
            FROM last_sick_leaves lsl
            INNER JOIN sick_leave sl ON lsl.id_employee = sl.id_employee AND lsl.last_start_date = sl.start_date
            INNER JOIN form f ON lsl.id_employee = f.id_employee;
                """)
    result1_13 = cur.fetchall()

# 14. Вывести список сотрудников и информацию о первом больничном листе, который они оформляли
    cur.execute("""
                    WITH first_sick_leaves AS (
                        SELECT id_employee,
                            MIN(start_date) AS first_start_date
                        FROM sick_leave
                        GROUP BY id_employee
                    )
                    SELECT f.id_employee,  
                        f.firstname,
                        f.surname,
                        sl.start_date,
                        sl.finish_date,
                        sl.reason,
                        sl.diagnosis,
                        sl.paid_for
                    FROM first_sick_leaves fsl
                    INNER JOIN sick_leave sl ON fsl.id_employee = sl.id_employee AND fsl.first_start_date = sl.start_date
                    INNER JOIN form f ON fsl.id_employee = f.id_employee;             
                """)
    result1_14 = cur.fetchall()

# 15. Вывести список сотрудников и суммарную продолжительность их больничных листов в текущем году
    cur.execute("""
                SELECT form.id_employee, form.firstname, form.surname, SUM(julianday(sick_leave.finish_date) - julianday(sick_leave.start_date)) AS total_duration
                FROM form
                INNER JOIN sick_leave ON form.id_employee = sick_leave.id_employee
                WHERE strftime('%Y', sick_leave.start_date) = strftime('%Y', 'now')
                GROUP BY form.firstname, form.surname;
                """)
    result1_15 = cur.fetchall()

with open('PZ_15/SelectOutput.txt', 'w') as f:
    f.write('1. Вывести список всех сотрудников и их должностей\n')
    for row in result1_1:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('2. Вывести список всех сотрудников и их базовых ставок\n')
    for row in result1_2:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('3. Вывести список всех сотрудников, работающих в отделе "IT"\n')
    for row in result1_3:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('4. Вывести список всех сотрудников, принятых на работу после 1 января 2022 года\n')
    for row in result1_4:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('5. Вывести список всех больничных листов, выписанных сотруднику с id = 42\n')
    for row in result1_5:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('6. Вывести список всех больничных листов, оплаченных компанией\n')
    for row in result1_6:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('7. Вывести список всех сотрудников, имеющих больничные листы на текущий месяц\n')
    for row in result1_7:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('8. Вывести среднюю базовую ставку всех сотрудников\n')
    for row in result1_8:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('9. Вывести список всех сотрудников, имеющих базовую ставку выше 100000\n')
    for row in result1_9:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('10. Вывести список всех сотрудников и общее количество дней, проведенных ими на больничном\n')
    for row in result1_10:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('11. Вывести информацию о сотрудниках и их больничных листах за последний месяц\n')
    for row in result1_11:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('12. Вывести среднюю продолжительность больничных листов сотрудников в каждом отделе\n')
    for row in result1_12:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('13. Вывести список сотрудников и информацию о последнем больничном листе, который они оформляли\n')
    for row in result1_13:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('14. Вывести список сотрудников и информацию о первом больничном листе, который они оформляли\n')
    for row in result1_14:
        f.write(str(row) + '\n')
    f.write('\n')
    f.write('15. Вывести список сотрудников и суммарную продолжительность их больничных листов в текущем году\n')
    for row in result1_15:
        f.write(str(row) + '\n')