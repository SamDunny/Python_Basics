# need this to develop XML tree from string
import xml.etree.ElementTree as ET

def main():
    # practice data 1
    data = '''<person>
        <name>Sam</name>
        <phone type="intl">
            +1 999 999 9999
        </phone>
        <email hide="yes"/>
    </person>'''

    # practice data 2
    user_input = '''<stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Jeff</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Bob</name>
            </user>
        </users>
    </stuff>'''

    # extract practice data 1
    try:
        tree = ET.fromstring(data)
    except Exception as e:
        print('ERROR practice data 1:[ ', e.__class__, ' ]')
        exit(1)

    # extract practice data 2
    try:
        stuff = ET.fromstring(user_input)
    except Exception as e:
        print('ERROR practice data 2:[ ', e.__class__, ' ]')
        exit(2)

    # extract attributes from practice data 1
    # find name attribute, convert to text
    print('Name:', tree.find('name').text)
    # find email attribute, return hide status
    print('Attr:', tree.find('email').get('hide'))

    # extract attributes from practice data 2
    # find all user subcategories
    user_list = stuff.findall('users/user')
    print('\nUser Count: ', len(user_list), "\n")
    for indv in user_list:
        print('Name:\t\t', indv.find('name').text)
        print('ID:\t\t', indv.find('id').text)
        print('Attribute:\t', indv.get("x"), "\n")

if __name__ == '__main__':
    main()
