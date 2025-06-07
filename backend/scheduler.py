from apscheduler.schedulers.background import BackgroundScheduler
from scraper import scrape_ecommercetimes
import time

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_ecommercetimes, 'interval', hours=1)
    scheduler.start()
    print("Scheduler started. Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown() 