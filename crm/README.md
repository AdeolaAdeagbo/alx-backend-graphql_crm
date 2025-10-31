# CRM Celery and Cron Setup

## Setup Steps

1. **Install Redis and dependencies**
   - Install Redis (`sudo apt install redis-server` or download for Windows).
   - Confirm Redis is running at `redis://localhost:6379/0`.

2. **Install requirements**
   ```bash
   pip install -r requirements.txt

3. Run migrations
 python manage.py migrate
Start Celery worker

celery -A crm worker -l info


Start Celery Beat

celery -A crm beat -l info


Add Cron Jobs

The heartbeat and low-stock cron jobs are configured in crm/cron.py and scheduled via django-crontab.

Run:

python manage.py crontab add
python manage.py crontab show


Verify logs

Heartbeat: /tmp/crm_heartbeat_log.txt

Low stock updates: /tmp/low_stock_updates_log.txt

Celery report: /tmp/crm_report_log.txt

Summary

This README covers:

Installing Redis

Running migrations

Starting Celery worker and Celery Beat

Setting up django-crontab

Verifying log files