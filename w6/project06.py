"""
Author: Karina Santos Felippe

Exceeding requirements: Allow the user to type in a filter, then show the minimum and maximum for this filter.
"""

life_expectancy_list = []

with open("sources/life-expectancy.csv") as f:
    for line in f:
        life_expectancy_list.append(line.strip().split(","))

# Removing head table
life_expectancy_list.pop(0)

year_interest = input("Enter the year of interest: ")
print()

def find_min_max(the_list, type, to_print):
    response = the_list[0]
    if type == 'max':
        for item in the_list:
            item_expectancy = float(item[3])
            if item_expectancy > float(response[3]):
                response = item
    if type == 'min':
        for item in the_list:
            item_expectancy = float(item[3])
            if item_expectancy < float(response[3]):
                response = item
    if to_print:
        print(f"The {type} life expectancy in {response[0]} ({response[1]}), {response[2]}, is {response[3]}")
    return response

exp_data = find_min_max(life_expectancy_list, 'max', False)
print(f"The overall max life expectancy is: {exp_data[3]} from {exp_data[0]} in {exp_data[2]}")

exp_data = find_min_max(life_expectancy_list, 'min', False)
print(f"The overall min life expectancy is: {exp_data[3]} from {exp_data[0]} in {exp_data[2]}")

print()

# For the final requirement
def list_filter(the_list, index, filter):
    filtered_list = []
    for item in the_list:
        if item[index] == filter:
            filtered_list.append(item)
    return filtered_list

average_exp = 0
year_filter_list = list_filter(life_expectancy_list, 2, year_interest)
print(f"For the year {year_interest}:")

for item in year_filter_list:
    average_exp += float(item[3])
average_exp /= len(year_filter_list)
print(f"The average life expectancy across all countries was {average_exp:.2f}")

exp_data = find_min_max(year_filter_list, 'max', False)
print(f"The max life expectancy was in {exp_data[0]} with {exp_data[3]}")

exp_data = find_min_max(year_filter_list, 'min', False)
print(f"The min life expectancy was in {exp_data[0]} with {exp_data[3]}")

## EXCEEDING REQUIREMENTS
user_input = input("\nDo you want to filter the life expectancy list again? (yes/no) ")
while user_input == 'yes':
    print("\nOptions:")
    print("0. Country")
    print("1. Country code")
    print("2. Year")
    index_input = int(input("Type the index: "))
    if index_input >= 0 and index_input <= 2:
        user_input = input(f"Type the filter: ")
        filter_list = list_filter(life_expectancy_list, index_input, user_input)
        find_min_max(filter_list, 'max', True)
        find_min_max(filter_list, 'min', True)
    else:
        print("Invalid answer! Please try again.")
        continue

    user_input = input("\nDo you want to filter the life expectancy list again? (yes/no) ")
