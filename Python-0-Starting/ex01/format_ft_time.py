# Import the datetime module to work with dates and times
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Convert the current date and time to a Unix timestamp
nowTT = now.timestamp()

# Convert the timestamp to a string in scientific notation
sn = "{:e}".format(nowTT)

print("Seconds since January 1, 1970:", f"{nowTT:,}", "or", sn, "in scientific notation")

# Get the current date and format it 
date = datetime.date.today().strftime('%b %d %y')

print(date)

