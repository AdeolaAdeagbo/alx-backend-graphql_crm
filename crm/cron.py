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

import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    import datetime
    GRAPHQL_URL = "http://localhost:8000/graphql"
    transport = RequestsHTTPTransport(url=GRAPHQL_URL, verify=False)
    client = Client(transport=transport, fetch_schema_from_transport=False)
    query = gql("query { hello }")
    try:
        response = client.execute(query)
        msg = response.get("hello", "No response")
    except Exception:
        msg = "GraphQL not reachable"
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')} CRM is alive - {msg}\n")


def update_low_stock():
    """
    Executes GraphQL mutation to update low stock products (<10)
    and logs updates to /tmp/low_stock_updates_log.txt
    """
    GRAPHQL_URL = "http://localhost:8000/graphql"

    transport = RequestsHTTPTransport(url=GRAPHQL_URL, verify=False)
    client = Client(transport=transport, fetch_schema_from_transport=False)

    mutation = gql("""
        mutation {
            updateLowStockProducts {
                success
                updatedProducts {
                    name
                    stock
                }
            }
        }
    """)

    try:
        result = client.execute(mutation)
        updated_products = result["updateLowStockProducts"]["updatedProducts"]
        with open("/tmp/low_stock_updates_log.txt", "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for p in updated_products:
                f.write(f"{timestamp} - {p['name']} restocked to {p['stock']}\n")
    except Exception as e:
        with open("/tmp/low_stock_updates_log.txt", "a") as f:
            f.write(f"Error running update_low_stock: {e}\n")
