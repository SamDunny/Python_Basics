# JSON represents data as nested "lists" and "dictionaries"
import json

def main():
    # practice data 1
    data = '''{
        "name" : "Sam",
        "phone" : {
            "type" : "intl",
            "number" : "+1 999 999 9999"
        },
        "email" : {
            "hide" : "yes"
        }
    }'''

    # practice data 2
    user_input = '''[
        {
            "id" : "001",
            "x" : "2",
            "name" : "Sam"
        },
        {
            "id" : "009",
            "x" : "7",
            "name" : "John"
        }
    ]'''

    # loads is "load string", loads a dictionary into info
    # extracts practice data 1
    try:
        info = json.loads(data)
    except Exception as e:
        print('ERROR practice data 1:[ ', e.__class__, ' ]')
        exit(1)

    # extracts practice data 2
    try:
        user_info = json.loads(user_input)
    except Exception as e:
        print('ERROR practice data 2:[ ', e.__class__, ' ]')
        exit(2)

    # extract attributes from practice data 1
    print('Name: ', info["name"])
    print('Hide: ', info["email"]["hide"])

    # extract attributes from practice data 2
    # find all user subcategories
    print('\nUser Count: ', len(user_info))
    for indv in user_info:
        print('Name:\t\t', indv['name'])
        print('ID:\t\t', indv['id'])
        print('Attribute:\t', indv['x'])


if __name__ == '__main__':
    main()