import datetime

print("=== Menstral Cycle Tracker ===")
print("Enter the date of your last period started:")
year = int(input("  year (e.g 2024): "))
month = int(input("  Month (1 to 12): "))
day = int(input("  day (1 to 31): "))


cycle_length = int(input("How many days is your usual cycle? (e.g 28): "))

last_date = datetime.date(year, month, day)

next_date = last_date + datetime.timedelta(days=cycle_length)

next_next_date = next_date + datetime.timedelta(days=cycle_length)

print("\n--- predicted period dates ---")
print("your last period started on:", last_date)
print("your next period should start on:", next_date)
print("your one after that should start on:", next_next_date)