from utils.db import get_connection

def get_economic_summary_from_db() -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(renewable_share_percent) FROM renewable_metrics")
    avg_renewable_share = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(ghg_reduction_percent) FROM renewable_metrics")
    avg_ghg_reduction = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(jobs_supported) FROM renewable_metrics")
    total_jobs = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(investment_billion_eur) FROM renewable_metrics")
    total_investment = cursor.fetchone()[0]

    conn.close()

    return {
        "avg_renewable_share": avg_renewable_share,
        "avg_ghg_reduction": avg_ghg_reduction,
        "total_jobs": total_jobs,
        "total_investment": total_investment
    }
