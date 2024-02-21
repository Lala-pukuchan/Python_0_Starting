import time
from datetime import datetime

current_timestamp = f"{time.time():,.4f}"
current_timestamp_sci = f"{time.time():.2e}"

print(
    f"Seconds since January 1, 1970: {current_timestamp} or {current_timestamp_sci} in scientific notation"
)

now = datetime.now()
current_time = now.strftime("%b %d %Y")
print(current_time)
