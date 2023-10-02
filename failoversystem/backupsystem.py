import requests
import time

def check_health(primary_system_url):
    try:
        response = requests.get(f"{primary_system_url}/health-check")
        if response.status_code != 200:
            raise Exception("Health check failed")
    except:
        trigger_failover()

def trigger_failover():
    # Logic to start the bot on the backup system

while True:
    check_health("http://primary_system_url")
    time.sleep(60)  # Check every minute, for example
