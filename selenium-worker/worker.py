import time

print("WhatsApp worker started")

while True:
    print("Polling SQS queue...")
    time.sleep(10)