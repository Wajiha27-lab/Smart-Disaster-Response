import sqlite3

DATABASE = "disaster_reports.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            report TEXT,
            ai_response TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_report(location, report, ai_response):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO reports(location, report, ai_response) VALUES (?, ?, ?)",
        (location, report, ai_response)
    )

    conn.commit()
    conn.close()


def get_reports():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reports ORDER BY id DESC")

    data = cursor.fetchall()

    conn.close()

    return data