# Open the file in read mode.
with open('input.txt', 'r') as file:
  # Read the contents of the file into a list of strings, where each string
  # represents a rucksack.
  rucksacks = file.read().strip().split('\n')

def find_errors(rucksacks):
  # Initialize a variable to keep track of the sum of the priorities of the
  # item types that appear in both compartments of each rucksack.
  sum_priorities = 0

  # Iterate over each rucksack.
  for rucksack in rucksacks:
    # Split the rucksack into its two compartments.
    first_compartment = rucksack[:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]

    # Check if there are any common items between the two compartments.
    common_items = set(first_compartment) & set(second_compartment)
    if common_items:
      # If there are common items, add their priorities to the sum.
      for item in common_items:
        # Lowercase item types have priorities 1 through 26, while uppercase
        # item types have priorities 27 through 52.
        if item.islower():
          sum_priorities += ord(item) - ord('a') + 1
        else:
          sum_priorities += ord(item) - ord('A') + 27

  # Return the sum of the priorities of the item types that appear in both
  # compartments of each rucksack.
  return sum_priorities

def find_badges(rucksacks):
  # Initialize a variable to keep track of the sum of the priorities of the
  # badge item types, and a set to store the priorities that have already
  # been counted.
  sum_priorities = 0
  counted_priorities = set()

  # Iterate over each group of three rucksacks.
  for i in range(0, len(rucksacks), 3):
    # Initialize a set to store the common items between the three rucksacks.
    common_items = set()

    # Iterate over the three rucksacks in the group.
    for j in range(i, i+3):
      # Add the items in the rucksack to the set of common items.
      common_items |= set(rucksacks[j])

    # Find the items that appear in all three rucksacks by taking the
    # intersection of the set of common items with itself three times.
    badge_items = common_items & common_items & common_items

    # Add the priority of the badge item to the sum of priorities, if it has
    # not already been counted.
    for item in badge_items:
      # Lowercase item types have priorities 1 through 26, while uppercase
      # item types have priorities 27 through 52.
      if item.islower():
        priority = ord(item) - ord('a') + 1
      else:
        priority = ord(item) - ord('A') + 27
      if priority not in counted_priorities:
        sum_priorities += priority
        counted_priorities.add(priority)

  # Return the sum of the priorities of the badge item types.
  return sum_priorities



print(find_errors(rucksacks))
print(find_badges(rucksacks))
