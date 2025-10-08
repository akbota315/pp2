#1
from datetime import datetime, timedelta

current_date = datetime.today()
new_date = current_date - timedelta(days=5)  # 5 күн азайту

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Date 5 days ago:", new_date.strftime("%Y-%m-%d"))

#2
from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:    ", today.strftime("%Y-%m-%d"))
print("Tomorrow: ", tomorrow.strftime("%Y-%m-%d"))


#3
from datetime import datetime

current_datetime = datetime.now()

clean_datetime = current_datetime.replace(microsecond=0)

print(current_datetime)
print(clean_datetime)

#4
from datetime import datetime

date1 = datetime(2025, 2, 15, 14, 30, 0) 
date2 = datetime(2025, 2, 15, 16, 45, 30) 

time_difference = date2 - date1

seconds_difference = time_difference.total_seconds()

print("Difference in seconds:", seconds_difference)