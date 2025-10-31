#!/usr/bin/env python3
import requests
import datetime

# GraphQL endpoint
GRAPHQL_URL = "http://localhost:8000/graphql"

# Calculate the date 7 days ago
seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")

# GraphQL query to get pending orders from the last week
query = """
query GetRecentPendingOrders($date: Date!) {
  orders(orderDate_Gte: $date, status: "PENDING") {
    id
    customer {
      email
    }
  }
}
"""

# Send the GraphQL query
response = requests.post(GRAPHQL_URL, json={"query": query, "variables": {"date": seven_days_ago}})

if response.status_code == 200:
    data = response.json()
    orders = data.get("data", {}).get("orders", [])
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log results
    with open("/tmp/order_reminders_log.txt", "a") as log:
        log.write(f"\n[{timestamp}] Found {len(orders)} pending orders\n")
        for order in orders:
            order_id = order.get("id")
            email = order.get("customer", {}).get("email")
            log.write(f"Order ID: {order_id} | Customer: {email}\n")

    print("Order reminders processed!")
else:
    print(f"GraphQL query failed! Status code: {response.status_code}")
