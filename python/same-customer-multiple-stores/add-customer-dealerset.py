#add-customer-dealerset.py
'''
Copyright 2020 myKaarma

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

from optparse import OptionParser
from mkauth import username, password, base_url
import kcustomercore

creds = {kcustomercore.KEY_USERNAME:username, kcustomercore.KEY_PASSWORD:password, kcustomercore.KEY_BASE_URL:base_url}

import pprint


# Global, set to true by the parser if needed
DEBUG = False
SIMULATION = False

def prettyprint(message, width=280):
    '''pretty prints the text'''
    pprint.pprint(message,width = width)

def debug_print(message):
    '''Prints the message if the DEBUG flag is set'''
    if DEBUG:
        prettyprint(message)


def read_dealer_info(dealer_file):
    """reads the dealer information into a list of department UIDs"""
    
    #"Dealer Name","DealerUID","Department Name","DepartmentUID"
    import csv
    with open(dealer_file) as csvfile:
        department_uids = []
        deptreader = csv.DictReader(csvfile)
        for row in deptreader:
            department_uids.append(row["DepartmentUID"])
    return department_uids  

def row_to_customer(row):
    '''converts the row to a customer dict'''
    # First Name,Last Name,Phone,Address Line 1,Address Line 2,City,State,Zip,Country
    customer = dict()
    customer["firstName"] = row["First Name"]
    customer["lastName"] = row["Last Name"]
    officePhone = {
        "label": "work",
        "okToCall": True,
        "okToText": False,
        "isPreferred": True,
        "phoneNumber": row["Phone"]
    }
    customer["phoneNumbers"] = [officePhone]

    address = dict()
    address["line1"] = row["Address Line 1"]
    address["line2"] = row["Address Line 2"]
    address["city"] = row["City"]
    address["state"] = row["State"]
    address["country"] = row["Country"]
    address["zip"] = row["Zip"]
    address["addressType"] = "B"
    customer["addresses"] = [address]
    return customer

def add_customers_to_dealers(customer_file,dealer_file):
    """Adds the customers in the customer_file to each dealer specified in dealer_file"""
    department_uids = read_dealer_info(dealer_file)
    debug_print(department_uids)
    #read and insert customers for each department 
    import csv
    with open(customer_file) as csvfile:
        customer_reader = csv.DictReader(csvfile)
        for row in customer_reader:
            customer_info = row_to_customer(row)
            customer = {"customer":customer_info}
            debug_print(customer)
            for dept_uid in department_uids:
                kcustomercore.add_customer(creds, dept_uid, customer, DEBUG = DEBUG, SIMULATION = SIMULATION)
    
def main():
    global DEBUG #important, otherwise the global var DEBUG won't be set.
    global SIMULATION #important, otherwise the global var SIMULATION won't be set.
    
    usage = "usage: python3 %prog [-v|--verbose] [-s|--simulation] -d dealers.csv -c customers.csv >> out.log"
    parser = OptionParser(usage)
    parser.add_option("-d", "--dealers", dest="dealer_file",
                      help="read config from DEALERCSV")
    parser.add_option("-c", "--customers", dest="customer_file",
                      help="read list of customers from CUSTOMERCSV")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
    parser.add_option("-s", "--simulation",
                      action="store_true", dest="simulation")
    (options, args) = parser.parse_args()
    DEBUG = options.verbose
    SIMULATION = options.simulation
    
    if options.dealer_file == None:
        parser.error("missing dealer_file")
    if options.customer_file == None:
        parser.error("missing customer_file")
    debug_print('# adding customers now')
    prettyprint(add_customers_to_dealers(options.customer_file,options.dealer_file))

if __name__ == "__main__":
    main()