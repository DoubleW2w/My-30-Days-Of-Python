from datetime import datetime

# Get the current day, month, year, hour, minute and timestamp from datetime module
day = datetime.today().day
month = datetime.today().month
year = datetime.today().year
hour = datetime.today().time().hour
minute = datetime.today().time().minute
timestamp = datetime.today().timestamp()
print(day, month, year, hour, minute, timestamp)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

# Today is 5 December, 2019. Change this time string to time.

date_string = "5 December 2019"
print(datetime.strptime(date_string, "%d %B %Y"))

# Calculate the time difference between now and new year.
now = datetime.now()
new_year = datetime(2025, 1, 1)
diff = new_year - now
print(new_year - now)

# Calculate the time difference between 1 January 1970 and now.
epoch = datetime(1970, 1, 1)
diff = now - epoch
# 打印结果
print(diff)
