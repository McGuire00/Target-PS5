import requests
import time
from datetime import datetime
import os


#input your zip code
zip_code = input('Please enter your zip code. ')
#this is how many seconds you would like to wait
poll = input("Polling interval? ")
poll = int(poll)


def clock():
    current = datetime.now()
    return(str(current) + " EST")


def target_scrape():
    standard_url = 'https://api.target.com/fulfillment_aggregator/v1/fiats/81114595?key=ff457966e64d5e877fdbad070f276d18ecec4a01&nearby=' + zip_code +'&limit=20&requested_quantity=1&radius=50&fulfillment_test_mode=grocery_opu_team_member_test'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'referer':'https://www.target.com/p/playstation-5-console/-/A-81114595',
    }


    req = requests.get(standard_url, headers=headers)
    data = req.json()

    for product in data['products']:
        for info in product['locations']:
            distance = info['distance']
            store_name = info['store_name']
            store_address = info['store_address']
            order_pickup_stock = info['order_pickup']['availability_status']
            #checks if in stock or not
            if str(order_pickup_stock) == 'OUT_OF_STOCK':
                print(clock(), ':::', ' Trying again in', poll, 'seconds')
                time.sleep(poll)
            #Verbal cue if in stock
            if str(order_pickup_stock) != 'OUT_OF_STOCK':
                os.system('say "Found item in stock"')
                print(store_name)
                print(store_address)
                print('The store is ' + distance + 'miles away')
                print(order_pickup_stock)
                print()

while True:
    target_scrape()
