import sqlite3 as s

conn = s.Connection('database.db')
cursor = conn.cursor()

cursor.execute('''
               create table if not exists users(
                   id integer primary key autoincrement,
                   name varchar(128),
                   salary integer,
                   deleted_flg integer default 0
               )
               ''')

cursor.execute('''
               create view if not exists v_users as
                   select
                   id,
                   name,
                   salary
                   from users
                   where deleted_flg = 0
               ''')

def add_user(name, salary):
    cursor.execute('''
                   insert into users (name, salary)
                   values (?, ?)
                   ''', [name, salary])
    conn.commit()


def show_users():
    cursor.execute('select * from users')
    for row in cursor.fetchall():
        print(row)


# add_user('Hayk', '10000')
# add_user('Misa', 10000)
# add_user('Lika', 10000)
# add_user('Nata', 10000)

def delete_user(name):
    cursor.execute('''
                   update users set 
                   deleted_flg = 1
                   where name = ?
                   ''', [name])
    conn.commit()

def restore_user(name):
    cursor.execute('''
                   update users set 
                   deleted_flg = 0
                   where name = ?
                   ''', [name])
    conn.commit()

show_users()
print('-'*50)
delete_user('Lika')
show_users()
restore_user('Lika')
show_users()