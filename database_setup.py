from transaction_db import TransactionDb

def setup_database():
    """
    Sets up the database by creating tables and seeding them with sample data.
    """
    print("Setting up the database...")
    db_path = os.environ.get("TRANSACTION_DB_PATH", "./transactions.db")
    db = TransactionDb(db_path)
    db.create_tables()
    db.seed_data()
    db.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()
