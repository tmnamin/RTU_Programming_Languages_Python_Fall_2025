"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [15, 14, 12, 16, 17, 18, 15]
city_population = {"LA": 4100000, "Amsterdam": 1000000, "London": 10000000, "Paris": 2040000, "Berlin": 3900000}

# TODO: Compute aggregates
average_temperature = sum(temperatures) / len(temperatures)
largest_city, largest_population = max(
    city_population.items(), key=lambda item: item[1]
)
smallest_city, smallest_population = min(
    city_population.items(), key=lambda item: item[1]
)
total_population = sum(city_population.values())

# TODO: Print results
print("Average temperature:", average_temperature)
print("Largest city:", largest_city, "-", largest_population)
print("Smallest city:", smallest_city, "-", smallest_population)
print("Total population:", total_population)
