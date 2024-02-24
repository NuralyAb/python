#1
def he():  
    from datetime import datetime, timedelta

    current_date = datetime.now()

    five_days_ago = current_date - timedelta(days=5)

    print("Current Date:", current_date.strftime("%Y-%m-%d"))
    print("Five Days Ago:", five_days_ago.strftime("%Y-%m-%d"))
he()
#2
from datetime import datetime, timedelta
def he():
    today = datetime.now().date()

    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    print("Yesterday:", yesterday)
    print("Today:", today)
    print("Tomorrow:", tomorrow)
he()
#3
from datetime import datetime

def drop_microseconds(dt):
    return dt.replace(microsecond=0)
    
current_datetime = datetime.now()
datetime_without_microseconds = drop_microseconds(current_datetime)
print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)

#4
from datetime import datetime

def date_difference_in_seconds(date1, date2):
    datetime1 = datetime.strptime(date1, "%Y-%m-%d")
    datetime2 = datetime.strptime(date2, "%Y-%m-%d")
    difference = abs((datetime2 - datetime1).total_seconds())
    
    return difference
date1 = "2024-02-19"
date2 = "2024-02-21"
difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference in seconds:", difference_seconds)