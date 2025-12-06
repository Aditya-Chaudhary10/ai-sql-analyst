import psycopg

# Connect using parameters to avoid URL quoting issues
conn = psycopg.connect(host="localhost", port=5432, dbname="ai_sql_db", user="postgres", password="Adi@2004")
cur = conn.cursor()

# Drop alembic_version table if it exists to fully reset migration state
cur.execute("DROP TABLE IF EXISTS public.alembic_version;")
conn.commit()
print("Dropped table public.alembic_version (if it existed).")

# Optional: show whether ai_queries exists before regenerating migrations
cur.execute("SELECT to_regclass('public.ai_queries');")
exists = cur.fetchone()[0] is not None
print("ai_queries exists before migrations?", exists)

cur.close()
conn.close()