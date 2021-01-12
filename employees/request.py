EMPLOYEES = [
    {
      "name": "Billy",
      "locationId": 1,
      "animalId": 3,
      "id": 1
    },
    {
      "name": "Bob",
      "locationId": 2,
      "animalId": 1,
      "id": 2
    },
    {
      "name": "Joe",
      "locationId": 1,
      "animalId": 2,
      "id": 3
    }
]

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def get_all_employees():
    return EMPLOYEES