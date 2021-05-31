# Adding the same customers to multiple stores
This program takes two inputs: 
- a list of customers to be added, and 
- a list of stores to add them to.

The code then iterates through the customers and adds them to each of the stores.

# Dependencies
- python3
- optparse
- pprint
- requests

# Scopes Needed
- `customer.update`, at the department level.

# Authentication
- save creds in mkauth.py (created by making a copy of mkauth.py.sample). Do NOT commit this file.

# Steps before running
- Make copies of the two files customers.csv.sample and dealers.csv.sample with the names customers.csv and
dealers.csv respectively and make sure that you update the sample details inside them with applicable details for your use case. Do NOT commit these files.

# How to run
```
python3 add-customers-dealerset.py -d dealers.csv -c customers.csv >> out.log
```
If you get an invalid auth credentials error then make sure to check both your credentials and the Department and Dealer UIDs which you have entered in the dealers.csv file. 

