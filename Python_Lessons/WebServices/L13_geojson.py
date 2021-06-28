import urllib.error, urllib.parse, urllib.request
import json

def main():
    serviceURL = 'https://ipinfo.io/json?'

    while True:
        address = input('Enter Location, or \'quit\' to Exit - ')
        if len(address) < 1 or address.lower() == 'quit': break
        
        url = serviceURL + urllib.parse.urlencode({'ip' : address})

        print('Retrieving ', url)
        add_rqst = urllib.request.urlopen(url)
        data = add_rqst.read().decode()
        print('Retrieved ', len(data), ' characters')

        try:
            js = json.loads(data)
        except Exception as e:
            print('=== ERROR: ', e, ' ===')
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('=== FAILURE TO RETRIEVE ', url, ' ===')
            print(data)
            continue

        # print(js)


if __name__ == '__main__':
    main()