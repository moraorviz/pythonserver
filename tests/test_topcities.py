from datetime import datetime

date = datetime.strptime("20100108000001", "%Y%m%d%H%M%S")
epoch = date.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


print(date)
print(unix_time_millis(date))
