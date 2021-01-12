CUSTOMERS = [
    {
      "email": "nicole@nicole.com",
      "password": "Claire",
      "name": "Nicole Flatfield",
      "id": 1
    },
    {
      "email": "something@that.com",
      "password": "Fake",
      "name": "Tera Dott",
      "id": 2
    }
]

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def get_all_customers():
    return CUSTOMERS