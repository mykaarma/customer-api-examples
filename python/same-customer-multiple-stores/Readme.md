# Adding the same customers to multiple stores
This program takes two inputs: 
- a list of customers to be added, and 
- a list of stores to add them to.

The code then iterates through the customers and adds them to each of the stores.

# Dependencies
- python3
- pprint
- requests

# Scopes Needed
- `customer.update`, at the department level.

# Authentication
- save creds in mkauth.py (created by making a copy of mkauth.py.sample). Do NOT commit this file.

# How to run
```
python3 add-customers-dealerset.py -d dealers.csv -c customers.csv >> out.log
```