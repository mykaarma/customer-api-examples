# kcustomer-core
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

import requests

KEY_USERNAME = 'username'
KEY_PASSWORD = 'password'
KEY_BASE_URL = 'base_url' #kept so this code can be used in dev and QA as well, not just prod.


def add_customer(creds, dept_uid, customer, DEBUG = False):
    """A simple method to add a new customer.

    This method will take the credentials (username, password, and base URL)
    the departmentUUID, and a DICT matching the customer object structure, and PUT it 
    in the API. An optional DEBUG boolean can be passed that will result in no network traffic, 
    but dumping of the HTTP request on stdout.
    """

    url = "%s/department/%s/customer" % (creds[KEY_BASE_URL],dept_uid)
    r = requests.put(url,auth=(creds[KEY_USERNAME],creds[KEY_PASSWORD]), json = customer)
    if DEBUG:
        print(r.json())
    return r.json()['response']


if __name__ == "__main__":
    print('Sorry, no direct usage available. Import and then call the methods.')