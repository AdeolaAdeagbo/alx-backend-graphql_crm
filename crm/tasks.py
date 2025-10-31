from celery import shared_task
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime

@shared_task
def generate_crm_report():
    GRAPHQL_URL = "http://localhost:8000/graphql"
    transport = RequestsHTTPTransport(url=GRAPHQL_URL, verify=False)
    client = Client(transport=transport, fetch_schema_from_transport=False)

    query = gql("""
        query {
            totalCustomers
            totalOrders
            totalRevenue
        }
    """)

    try:
        result = client.execute(query)
        customers = result.get("totalCustomers", 0)
        orders = result.get("totalOrders", 0)
        revenue = result.get("totalRevenue", 0)
        log = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Report: {customers} customers, {orders} orders, {revenue} revenue\n"
    except Exception as e:
        log = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Error: {e}\n"

    with open("/tmp/crm_report_log.txt", "a") as f:
        f.write(log)
