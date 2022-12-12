# Read the input
calorie_lines = [line.strip() for line in open('calories.txt')]

# Split the input into a list of lists, one for each Elf
elves = []
current_elf = []
for line in calorie_lines:
    if line == '':
        # This is a blank line, indicating the start of a new Elf's inventory
        elves.append(current_elf)
        current_elf = []
    else:
        # This is the calorie count of a food item
        current_elf.append(int(line))

# Add the last Elf's inventory to the list
elves.append(current_elf)

# Keep track of the top three Elves with the most calories
top_elves = []
for elf in elves:
    total_calories = sum(elf)
    # Update the list of top Elves
    top_elves = sorted(top_elves + [total_calories], reverse=True)[:3]

# Print the result
print(f"The top three Elves are carrying {sum(top_elves)} calories.")
