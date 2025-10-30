#!/bin/bash
# clean_inactive_customers.sh
# Deletes customers with no orders in the last year and logs the count.

# Go to the project directory (replace this with your actual path)
cd /absolute/path/to/your/project || exit 1

# Run the cleanup command using Django shell
deleted_count=$(python manage.py shell -c "
from datetime import datetime, timedelta
from crm.models import Customer
cutoff = datetime.now() - timedelta(days=365)
deleted, _ = Customer.objects.filter(last_order_date__lt=cutoff).delete()
print(deleted)
")

# Log the action
echo \"[$(date '+%Y-%m-%d %H:%M:%S')] Deleted $deleted_count inactive customers\" >> /tmp/customer_cleanup_log.txt
