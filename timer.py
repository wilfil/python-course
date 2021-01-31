#!/usr/bin/env python3.9

from time import localtime, mktime, strftime

start_time = localtime()
#print(start_time)
print(f"Timer started at {strftime('%X', start_time)}")

# Wait for user to stop timer
input("Press 'Enter' to stop timer ")

stop_time = localtime()

print(f"Timer stopped at {strftime('%X', stop_time)}")


cronometer = mktime(stop_time) - mktime(start_time)
print(f"The total time is: {cronometer} seconds.")
