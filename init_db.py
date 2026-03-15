import os
from utils.db import get_connection

def initialize_database():
    os.makedirs("data", exist_ok=True)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS renewable_metrics")
    cursor.execute(
        '''
        CREATE TABLE renewable_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT NOT NULL,
            year INTEGER NOT NULL,
            renewable_share_percent REAL NOT NULL,
            ghg_reduction_percent REAL NOT NULL,
            jobs_supported INTEGER NOT NULL,
            investment_billion_eur REAL NOT NULL
        )
        '''
    )

    rows = [
        ("Germany", 2024, 49.5, 21.0, 320000, 28.0),
        ("France", 2024, 31.0, 16.0, 180000, 16.5),
        ("Spain", 2024, 56.0, 24.0, 210000, 18.0),
        ("Italy", 2024, 41.0, 19.0, 190000, 14.2),
        ("Netherlands", 2024, 39.0, 18.0, 110000, 10.8),
        ("Sweden", 2024, 68.0, 29.0, 95000, 8.5),
        ("Denmark", 2024, 72.0, 31.0, 85000, 7.9),
        ("Poland", 2024, 24.0, 11.0, 140000, 11.2),
    ]

    cursor.executemany(
        '''
        INSERT INTO renewable_metrics
        (country, year, renewable_share_percent, ghg_reduction_percent, jobs_supported, investment_billion_eur)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        rows
    )

    conn.commit()
    conn.close()
    print("Database initialized successfully at data/renewable_energy.db")

if __name__ == "__main__":
    initialize_database()
