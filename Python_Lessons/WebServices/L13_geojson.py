import urllib.error, urllib.parse, urllib.request
import json
import configparser

def main():
    serviceURL = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # retrieve hidden api key
    config = configparser.RawConfigParser()
    config.read(filenames = 'hidden.txt')
    # print(config.sections())
    apikey = config.get('Google','googleapikey')

    while True:
        address = input('Enter Location, or \'quit\' to Exit - ')
        if len(address) < 1 or address.lower() == 'quit': break
        addP = urllib.parse.urlencode({'address' : address})
        
        # build request url from address and key components
        url = serviceURL + addP + "&key=" + apikey
        print('Retrieving ', url)
        
        # open url
        add_rqst = urllib.request.urlopen(url)

        # read all decoded (from UTF-8) data into data
        data = add_rqst.read().decode()
        print('Retrieved ', len(data), ' characters')

        try:
            # format string data into JSON 'tree'
            js = json.loads(data)
        except Exception as e:
            print('ERROR:\t\t ', e)
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('FAILURE TO RETRIEVE:\t ', url)
            print(data)
            continue

        # prints out JSON tree with indent=4
        # print(json.dumps(js, indent=4))
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print('Lat:\t', lat, '\nLng:\t', lng)
        location = js["results"][0]["formatted_address"]
        print(location)

if __name__ == '__main__':
    main()