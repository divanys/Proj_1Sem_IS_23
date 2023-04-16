import sqlite3 as sq


con = sq.connect('PZ_15/database.db')

with con:
    cur = con.cursor()
# 1. Удалить все записи о больничных листах для сотрудника с именем "Иван" 
    cur.execute("""
                DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE firstname = 'Иван');
            """)
    result1_1 = cur.fetchall()

# 2. Удалить все записи о больничных листах для сотрудника с фамилией "Петров"
    cur.execute("""
                DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE surname = 'Петров');
                """)
    result1_2 = cur.fetchall()

# 3. Удалить все записи о больничных листах для сотрудника с должностью "Менеджер"
    cur.execute("""
                DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE post = 'Менеджер');
            """)
    result1_3 = cur.fetchall()

# 4. Удалить все записи о больничных листах для сотрудника с отделом "Отдел продаж"
    cur.execute("""
                DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE department = 'Отдел продаж');
            """)
    result1_4 = cur.fetchall()

# 5. Удалить все записи о больничных листах для сотрудника женского пола 
    cur.execute("""
                DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE sex = 'женский');
            """)
    result1_5 = cur.fetchall()

# 6. Удалить все записи о больничных листах для сотрудников старше 50 лет
    cur.execute("""
                DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE birthday < DATE('now', '-50 years'));
            """)
    result1_6 = cur.fetchall()

# 7.  Удалить все записи о неоплаченных больничных листах
    cur.execute("""
            DELETE FROM sick_leave WHERE paid_for = 0;
            """)
    result1_7 = cur.fetchall()

# 8. Удалить все записи о больничных листах, дата окончания которых прошла
    cur.execute("""
                DELETE FROM sick_leave WHERE finish_date < DATE('now');
            """)
    result1_8 = cur.fetchall()

# 9. ВУдалить все записи о больничных листах, начиная с определенной даты
    cur.execute("""
                DELETE FROM sick_leave WHERE start_date >= '2023-01-01';
            """)
    result1_9 = cur.fetchall()

# 10. Удалить все записи о больничных листах, закончившихся до определенной даты
    cur.execute("""
                DELETE FROM sick_leave WHERE finish_date < '2023-04-16';
                """)
    result1_10 = cur.fetchall()

# 11. Удалить все больничные листы сотрудника с именем "Иван" из таблицы "Больничные листы"
    cur.execute("""
                DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE firstname = 'Иван');
            """)
    result1_11 = cur.fetchall()

# 12. Удалить все больничные листы сотрудников, чьи фамилии начинаются на букву "С" из таблицы "Больничные листы" 
    cur.execute("""
                DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE surname LIKE 'С%');
                """)
    result1_12 = cur.fetchall()

# 13. Удалить все больничные листы, которые еще не были оплачены, у сотрудников с должностью "Менеджер" из таблицы "Больничные листы"
    cur.execute("""
                DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE post = 'Менеджер') AND paid_for = 0;
                """)
    result1_13 = cur.fetchall()

# 14. Удалить все больничные листы, выписанные сотрудникам отдела "IT" в период с 1 января
    cur.execute("""DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE department = 'IT') AND start_date >= '2023-01-01';    
                """)
    result1_14 = cur.fetchall()

# 15. Удалить все больничные листы, связанные со сотрудниками старше 50 лет из таблицы "Больничные листы"
    cur.execute("""
                DELETE FROM sick_leave WHERE id_employee IN (SELECT id_employee FROM form WHERE birthday < DATE('now', '-50 years'));
                """)
    result1_15 = cur.fetchall()