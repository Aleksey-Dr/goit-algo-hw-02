from queue import Queue
import uuid
import datetime

q = Queue()

def generate_request():
    # create new request
    request_id = str(uuid.uuid4())
    now = datetime.datetime.now()
    creation_time = now.strftime("%H:%M:%S")
    creation_date = now.strftime("%Y-%m-%d")
    request = {
        "id": request_id,
        "time": creation_time,
        "date": creation_date,
    }
    # add request to queue
    q.put(request)

def process_request():
    # is the queue empty?
    if not q.empty():
        current_request = q.get()
        print(f"Request of {current_request} has been processed")
    else:
        print("Queue is empty")


for _ in range(2):
    generate_request()
    print(q.queue)
    process_request()
    print(q.queue)