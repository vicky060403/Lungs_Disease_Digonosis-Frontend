import sqlite3

DB_NAME = "lung_disease.db"


def get_connection():

    conn = sqlite3.connect(DB_NAME)

    return conn


def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            patient_name TEXT,

            age INTEGER,

            gender TEXT,

            doctor TEXT,

            symptoms TEXT,

            prediction TEXT,

            confidence REAL,

            created_at TEXT

        )
    """)

    conn.commit()

    conn.close()


def save_prediction(

    patient,

    prediction,

    confidence,

    created_at

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO predictions(

            patient_name,

            age,

            gender,

            doctor,

            symptoms,

            prediction,

            confidence,

            created_at

        )

        VALUES(?,?,?,?,?,?,?,?)

    """, (

        patient["name"],

        patient["age"],

        patient["gender"],

        patient["doctor"],

        patient["symptoms"],

        prediction,

        confidence,

        created_at

    ))

    conn.commit()

    conn.close()


def get_predictions():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

        patient_name,

        age,

        gender,

        doctor,

        symptoms,

        prediction,

        confidence,

        created_at

        FROM predictions

        ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data