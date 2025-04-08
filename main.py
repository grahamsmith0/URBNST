import time
import urllib.request
from datetime import datetime

from google.transit import gtfs_realtime_pb2

feed = gtfs_realtime_pb2.FeedMessage()

INTERVAL = 60

# while True:
#     now = datetime.now().strftime("%Y%m%d_%H%M%S")
#     with urllib.request.urlopen(
#         "https://api-public.odpt.org/api/v4/gtfs/realtime/ToeiBus"
#     ) as response:
#         data = response.read()
#         with open(f"data/{now}.pb", "wb") as f:
#             f.write(data)
#     print(f"Saved snapshot at {now}")
#     time.sleep(INTERVAL)


# Helper to convert UNIX timestamp to readable format
def format_time(ts):
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S") if ts else "N/A"


with open("data/20250407_225311.pb", "rb") as f:
    feed.ParseFromString(f.read())

# Parse vehicle entities
for entity in feed.entity:
    if entity.HasField("vehicle"):
        v = entity.vehicle
        trip = v.trip
        position = v.position
        vehicle_info = v.vehicle

        print(f"Vehicle ID: {vehicle_info.id} ({vehicle_info.label})")
        print(f"\tTrip ID: {trip.trip_id}")
        print(f"\tRoute ID: {trip.route_id}")
        print(f"\tDirection: {trip.direction_id}")
        print(f"\tSchedule Relationship: {trip.schedule_relationship}")
        print(f"\tCurrent Stop Sequence: {v.current_stop_sequence}")
        print(f"\tCurrent Stop ID: {v.stop_id}")
        print(f"\tTimestamp: {format_time(v.timestamp)}")
        print(f"\tLocation: lat {position.latitude}, lon {position.longitude}")
