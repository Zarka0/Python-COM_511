#Create a database using lists and tuples.
# Define the database as a list of tuples
employee_database = [
    (1, "John Doe", 50000),
    (2, "Jane Smith", 60000),
    (3, "Bob Johnson", 55000),
    # Add more entries as needed
]

# Function to display all entries in the database
def display_database(database):
    for entry in database:
        print(f"Employee ID: {entry[0]}, Name: {entry[1]}, Salary: {entry[2]}")

# Function to add a new entry to the database
def add_entry(database, employee_id, name, salary):
    new_entry = (employee_id, name, salary)
    database.append(new_entry)
    print("Entry added successfully.")

# Function to search for an entry by employee ID
def search_by_id(database, employee_id):
    for entry in database:
        if entry[0] == employee_id:
            return entry
    return None

# Example usage:
display_database(employee_database)

print("\nAdding a new entry:")
add_entry(employee_database, 4, "Alice Johnson", 70000)
display_database(employee_database)

print("\nSearching for employee with ID 2:")
result = search_by_id(employee_database, 2)
if result:
    print(f"Employee found - Employee ID: {result[0]}, Name: {result[1]}, Salary: {result[2]}")
else:
    print("Employee not found.")