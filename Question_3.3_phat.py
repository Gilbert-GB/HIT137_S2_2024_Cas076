# Global variable to track the inventory
global_inventory = 100

# A dictionary to store some key-value pairs
keys = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Function to process a list of numbers
def process_numbers():
    global global_inventory  # Use global inventory variable
    numbers = [1, 2, 3, 4, 5]  # Initialize the list of numbers

    # Loop while inventory is greater than 0
    while global_inventory > 0:
        if global_inventory % 2 == 0:  # Check if inventory is even
            numbers.reverse()  # Reverse the list of numbers
        global_inventory -= 1  # Decrease inventory by 1
    return numbers  # Return the processed list

# A set of numbers (removes duplicate values automatically)
set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}

# Process the number set using the function
result = process_numbers()

# Function to update the dictionary of keys
def update_keys():
    global global_inventory  # Use global inventory variable
    global_inventory = 10  # Set inventory to 10
    keys['key4'] = global_inventory  # Add a new key to the dictionary

# Call the function to update the keys
update_keys()

# Function to increment the global inventory
def increment_global():
    global global_inventory  # Use global inventory variable
    global_inventory += 10  # Add 10 to the global inventory

# Loop to print numbers 1 to 5
for i in range(5):
    print(i + 1)

# Check if 'key4' in the dictionary is set to 10
if set is not None and keys['key4'] == 10:
    print("Codition met!")

# Check if the number 5 is not in the dictionary keys
if 5 not in keys:
    print("The number 5 is not a key in the dictionary")

# Print final values
print(global_inventory)
print(keys)
print(set)
