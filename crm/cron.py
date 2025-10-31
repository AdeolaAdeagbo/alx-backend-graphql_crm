import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    """
    Logs a heartbeat message and checks the GraphQL hello field.
    """
    GRAPHQL_URL = "http://localhost:8000/graphql"

    # Prepare GraphQL client
    transport = RequestsHTTPTransport(url=GRAPHQL_URL, verify=False)
    client = Client(transport=transport, fetch_schema_from_transport=False)

    # Optional GraphQL query
    query = gql("""
        query {
            hello
        }
    """)

    try:
        response = client.execute(query)
        hello_msg = response.get("hello", "No response")
    except Exception:
        hello_msg = "GraphQL not reachable"

    # Write heartbeat log
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        f.write(f"{timestamp} CRM is alive - {hello_msg}\n")
