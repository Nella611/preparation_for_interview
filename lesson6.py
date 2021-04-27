import sqlite3

db_path = 'catalog.sqlite3'

conn = sqlite3.connect(db_path)
cur = conn.cursor()


cur.executescript("""
    CREATE TABLE IF NOT EXISTS categories(
        category_name TEXT NOT NULL PRIMARY KEY, 
        category_description TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS units(
        unit TEXT NOT NULL PRIMARY KEY
    );
    CREATE TABLE IF NOT EXISTS positions(
        position TEXT NOT NULL PRIMARY KEY
    );
    CREATE TABLE IF NOT EXISTS goods(
        good_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        good_name TEXT,
        good_unit TEXT,
        good_cat TEXT,
        FOREIGN KEY(good_unit) REFERENCES units(unit),
        FOREIGN KEY(good_cat) REFERENCES categories(category_name)
    );
    CREATE TABLE IF NOT EXISTS employees(
        employee_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        employee_fio TEXT,
        employee_position TEXT,
        FOREIGN KEY(employee_position) REFERENCES positions(position)
    );
    CREATE TABLE IF NOT EXISTS vendors(
        vendor_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        vendor_name TEXT NOT NULL,
        vendor_ownerchipform TEXT NOT NULL,
        vendor_address TEXT NOT NULL,
        vendor_phone TEXT NOT NULL,
        vendor_email TEXT NOT NULL
    );
""")
conn.commit()
conn.close()
