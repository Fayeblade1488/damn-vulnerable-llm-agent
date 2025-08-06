###############################
##  TOOLS
from langchain.agents import Tool
from transaction_db import TransactionDb
from functools import partial
import json

def get_current_user(db: TransactionDb, input: str):
    """Gets the current user from the database."""
    user = db.get_user(1)
    return json.dumps(user)

def get_transactions(db: TransactionDb, userId: str):
    """Returns the transactions associated to the userId provided by running this query: SELECT * FROM Transactions WHERE userId = ?."""
    try:
        transactions = db.get_user_transactions(userId)
        return json.dumps(transactions)
    except Exception as e:
        logging.exception("Exception occurred in get_transactions")
        return f"Error: {e}"

def get_tools(db: TransactionDb):
    """Initializes and returns the tools for the agent."""
    tools = [
        Tool(
            name='GetCurrentUser',
            func=partial(get_current_user, db),
            description="Returns the current user for querying transactions."
        ),
        Tool(
            name='GetUserTransactions',
            func=partial(get_transactions, db),
            description="Returns the transactions associated to the userId provided by running this query: SELECT * FROM Transactions WHERE userId = provided_userId."
        )
    ]
    return tools
