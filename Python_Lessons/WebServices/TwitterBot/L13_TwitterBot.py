import urllib.error, urllib.parse, urllib.request
import json
import twurl
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
NUM_OF_USERS = 10

def main():
    
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        print('')
        acct = input('Enter Twitter Account: ')
        if (len(acct) < 1): break

    # asking for the first 5 freinds of specified user
        url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': str(NUM_OF_USERS)})

        print('Retrieving ', url)

        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()


        js = json.loads(data)
        # print JSON tree
        # print(json.dumps(js, indent = 4))

        # print sought data
        print('\n=================================================')
        for usr in js['users']:
            if 'screen_name' not in usr:
                print('\t* No screen-name found *')
                continue
            print(usr['screen_name'])
            if 'status' not in usr:
                print('\t* No status found *')
                continue
            s = usr['status']['text']
            print('  ', s[:120])
        print('=================================================')

        # prints requests left
        headers = dict(connection.getheaders())
        print('Remaining ', headers['x-rate-limit-remaining'])


if __name__ == '__main__':
    main()