from motivator import send_whatsapp_text,client,quote
from apscheduler.schedulers.background  import BackgroundScheduler
import time
scheduler=BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

job=scheduler.add_job(send_whatsapp_text,'cron',[client,quote],hour="4",minute="32",second="30")
print(job)

while True:
    time.sleep(1)
