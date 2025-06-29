print("=== Menstral Cycle Tracker ===")
print("Enter the date of your last period started:")
year = int(input("  year (e.g 2024): "))
month = int(input("  Month (1 to 12): "))
day = int(input("  day (1 to 31): "))


cycle_length = int(input("How many days is your usual cycle? (e.g 28): "))

days_In_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

next_year = year;

next_month = month;

next_day = day + cycle_length;

while True:
	
	max_days_this_month = days_In_month[next_month];

	if next_day <= max_days_this_month:		
		break;


	next_day = next_day - max_days_this_month;
	next_month += 1;
	if next_month > 12:
		next_month = 1;
		
		next_year += 1;




after_year = next_year
after_month = next_month
after_day = next_day + cycle_length

while True:

	max_Days_this_month = days_In_month[after_month];

	if after_day <= max_days_this_month:		
		break;


	after_day = after_day - max_days_this_month;
	after_month += 1;
	if after_month > 12:
		after_month = 1;
		
		after_year += 1;


print("\n--- predicted period dates ---")
print(f"your last period started on:  {year}-{month:02d}-{day:02d}")
print(f"your next period should start on:  {next_year}-{next_month:02d}-{next_day:02d}")
print(f"your one after that should start on:  {after_year}-{after_month:02d}-{after_day:02d}")