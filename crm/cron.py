import datetime
import requests

def log_crm_heartbeat():
    """Log a heartbeat message and check the GraphQL endpoint."""
    now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{now} CRM is alive\n"

    # Append heartbeat to log file
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(message)

    # Optional GraphQL check
    try:
        response = requests.post("http://localhost:8000/graphql", json={"query": "{ hello }"})
        if response.status_code == 200:
            print("GraphQL endpoint responsive.")
        else:
            print("GraphQL endpoint error.")
    except Exception:
        print("GraphQL check failed.")
