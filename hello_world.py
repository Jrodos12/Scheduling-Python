import os,schedule,requests,datetime,time

def hello_world():
    timestamp = datetime.datetime.now()
    print(f"Hello world! at: {timestamp}")

schedule.every().minute.do(hello_world)

while True:
    schedule.run_pending()
    time.sleep(1)