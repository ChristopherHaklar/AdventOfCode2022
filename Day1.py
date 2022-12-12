# Read in the list of caloric values from the file
caloric_values = []
with open("Input.txt", "r") as f:
    for line in f:
        caloric_value = int(line.strip())
        caloric_values.append(caloric_value)

# Keep track of the total caloric value for each Elf
elf_caloric_totals = {}
current_elf = ""
for caloric_value in caloric_values:
    if caloric_value == 0:
        # The caloric value of 0 indicates a new Elf
        current_elf = ""
    else:
        if current_elf == "":
            # This is the first caloric value for this Elf, so create a new entry
            current_elf = caloric_value
            elf_caloric_totals[current_elf] = 0
        else:
            # Update the total caloric value for this Elf
            elf_caloric_totals[current_elf] += caloric_value

# Find the Elf with the highest total caloric value
highest_caloric_total = 0
highest_caloric_elf = ""
for elf, caloric_total in elf_caloric_totals.items():
    if caloric_total > highest_caloric_total:
        highest_caloric_total = caloric_total
        highest_caloric_elf = elf

# Output the total caloric value for the Elf with the highest caloric value
print(highest_caloric_total)
