import requests
import logging

def generate_crm_report():
    log_file = "/tmp/crmreportlog.txt"
    logging.basicConfig(filename=log_file, level=logging.INFO)
    logging.info("CRM report generation started.")

    try:
        response = requests.get("https://example.com/graphql")
        if response.status_code == 200:
            logging.info("CRM report generated successfully.")
        else:
            logging.warning(f"Failed to fetch CRM data. Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Error generating CRM report: {e}")
