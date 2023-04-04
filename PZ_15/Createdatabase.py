import sqlite3 as sq


from infodate import info_form as inF, data_sick_leave as dSL

'''
Блок создания и заполнения таблиц 
'''

con = sq.connect('PZ_15/database.db')


with con:
    data = con.execute("select count(*) from sqlite_master where type='table' and name='form'")
    for row in data:
        if row[0] == 0:
            with con:
                con.execute("""
                            CREATE TABLE IF NOT EXISTS form (
                                    id_employee INTEGER PRIMARY KEY NOT NULL,
                                    firstname VARCHAR NOT NULL,
                                    surname VARCHAR NOT NULL,
                                    birthday DATE NOT NULL,
                                    sex VARCHAR NOT NULL,
                                    date_of_hiring DATE NOT NULL,
                                    post VARCHAR NOT NULL,
                                    department VARCHAR NOT NULL,
                                    base_rate DECIMAL NOT NULL
                            )"""
                           )
                
    data = con.execute("select count(*) from sqlite_master where type='table' and name='sick_leave'")
    for row in data:
        if row[0] == 0:         
            with con:
                con.execute("""
                            CREATE TABLE IF NOT EXISTS sick_leave (
                                    id INTEGER PRIMARY KEY NOT NULL,
                                    id_employee INTEGER,
                                    start_date DATE NOT NULL,
                                    finish_date DATE NOT NULL,
                                    reason VARCHAR NOT NULL,
                                    diagnosis VARCHAR NOT NULL,
                                    paid_for BOOLEAN NOT NULL,
                                    FOREIGN KEY (id_employee) REFERENCES forma (id_employee)
                            )"""
                            )

    cur = con.cursor()

    # заполняем таблицу form
    cur.executemany("INSERT INTO form VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",  inF)

    # заполняем таблицу sick_leave
    cur.executemany("INSERT INTO sick_leave VALUES (?, ?, ?, ?, ?, ?, ?)",  dSL)
 


# '''
# Блок обновления таблиц
# '''


# '''
# Блок удаления из таблиц
# '''
