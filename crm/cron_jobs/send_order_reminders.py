#!/usr/bin/env python3
import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# GraphQL endpoint
GRAPHQL_URL = "http://localhost:8000/graphql"

def main():
    # Calculate the date 7 days ago
    seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")

    # Define GraphQL query
    query = gql("""
        query {
            orders(orderDate_Gte: "%s") {
                id
                customer {
                    email
                }
            }
        }
    """ % seven_days_ago)

    # Configure GraphQL client
    transport = RequestsHTTPTransport(url=GRAPHQL_URL, verify=False)
    client = Client(transport=transport, fetch_schema_from_transport=False)

    # Execute query
    result = client.execute(query)

    # Log reminders
    with open("/tmp/order_reminders_log.txt", "a") as f:
        for order in result.get("orders", []):
            log_line = f"{datetime.datetime.now()} - Order ID: {order['id']}, Customer: {order['customer']['email']}\n"
            f.write(log_line)

    print("Order reminders processed!")

if __name__ == "__main__":
    main()
