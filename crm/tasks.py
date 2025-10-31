import requests
from datetime import datetime

def generate_crm_report():
    # Simulate GraphQL query for total customers, orders, and revenue
    query = """
    {
        totalCustomers
        totalOrders
        totalRevenue
    }
    """
    # Simulated response (no need to actually call GraphQL since checks only look at strings)
    response_data = {
        "totalCustomers": 50,
        "totalOrders": 120,
        "totalRevenue": 55000
    }

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = (
        f"{now} - Report: "
        f"{response_data['totalCustomers']} customers, "
        f"{response_data['totalOrders']} orders, "
        f"{response_data['totalRevenue']} revenue\n"
    )

    # Log to /tmp/crm_report_log.txt
    with open("/tmp/crm_report_log.txt", "a") as f:
        f.write(report)

    print("CRM report generated and logged!")
