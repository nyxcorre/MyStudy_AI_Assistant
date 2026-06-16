import sqlite3


# Connect database
def connect_db():
    conn = sqlite3.connect("mystudy.db")
    return conn


# Create users table
def create_table():

    conn = connect_db()
    c = conn.cursor()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        branch TEXT,
        semester TEXT

        )
        """
    )

    conn.commit()
    conn.close()



# Signup function
def add_user(name,email,password,branch,semester):

    conn = connect_db()
    c = conn.cursor()

    c.execute(
        """
        INSERT INTO users
        (name,email,password,branch,semester)

        VALUES(?,?,?,?,?)
        """,

        (
            name,
            email,
            password,
            branch,
            semester
        )
    )

    conn.commit()
    conn.close()



# Login checking
def login_user(email,password):

    conn = connect_db()
    c = conn.cursor()

    c.execute(
        """
        SELECT *
        FROM users

        WHERE email=?
        AND password=?
        """,

        (
            email,
            password
        )
    )


    data = c.fetchone()

    conn.close()

    return data

# ============================
# ATTENDANCE TABLE
# ============================

def create_attendance_table():

    conn = connect_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS attendance(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    total INTEGER,
    attended INTEGER

    )
    """)

    conn.commit()
    conn.close()



def add_attendance(subject,total,attended):

    conn = connect_db()
    c = conn.cursor()

    c.execute(
    """
    INSERT INTO attendance
    (subject,total,attended)

    VALUES(?,?,?)
    """,

    (subject,total,attended)

    )

    conn.commit()
    conn.close()



def view_attendance():

    conn = connect_db()
    c = conn.cursor()

    c.execute(
        "SELECT * FROM attendance"
    )

    data = c.fetchall()

    conn.close()

    return data



# ============================
# ASSIGNMENTS TABLE
# ============================

def create_assignment_table():

    conn = connect_db()
    c = conn.cursor()


    c.execute("""
    CREATE TABLE IF NOT EXISTS assignments(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    subject TEXT,
    deadline TEXT

    )
    """)


    conn.commit()
    conn.close()



def add_assignment(name,subject,deadline):

    conn=connect_db()
    c=conn.cursor()


    c.execute(
    """
    INSERT INTO assignments
    (name,subject,deadline)

    VALUES(?,?,?)
    """,

    (name,subject,deadline)

    )


    conn.commit()
    conn.close()



def view_assignments():

    conn=connect_db()
    c=conn.cursor()

    c.execute(
    "SELECT * FROM assignments"
    )

    data=c.fetchall()

    conn.close()

    return data
