import time
import urllib.request
from datetime import datetime

from google.transit import gtfs_realtime_pb2

feed = gtfs_realtime_pb2.FeedMessage()

INTERVAL = 60

while True:
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    with urllib.request.urlopen(
        "https://api-public.odpt.org/api/v4/gtfs/realtime/ToeiBus"
    ) as response:
        data = response.read()
        with open(f"data/{now}.pb", "wb") as f:
            f.write(data)
    print(f"Saved snapshot at {now}")
    time.sleep(INTERVAL)
