


temperatures_celsius = np.array([
    [22, 25, 21],
    [23, 26, 24],
    [20, 22, 23]
])


average_temp_per_day = np.mean(temperatures_celsius, axis=1)
for day_index, avg_temp in enumerate(average_temp_per_day):
    print(f"Average temperature for day {day_index+1}: {avg_temp:.2f}°C")


temperatures_fahrenheit = temperatures_celsius * 9/5 + 32
print("\nTemperatures in Fahrenheit:")
print(temperatures_fahrenheit)
