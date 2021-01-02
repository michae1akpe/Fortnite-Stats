import requests

username = input("\nPlease enter username of player you wish to search up: ")  # user enters the username they want to
# view power record on
platform = input("\nPlease choose the platform of the user. "
                 "('pc', 'console', 'mobile): ")  # user enters the platform they suspect they are on

url = 'https://api.fortnitetracker.com/v1/powerrankings/' + platform + '/' + 'EU' + '/' + username
headers = {
    'TRN-Api-Key': 'fill with your api key'  # This can be gotten at fortnitetracker.com
}

"""This two lines sends the request to attain platform name, country and epic username"""

response = requests.get(url, headers=headers)
info = response.json()
try:
    if response.status_code == 200:
        print('Region:', info['region'])
        print('Username:', info['name'])
        print('Platform:', info['platform'])
        print('Points:', info['points'])
        print('Cash Price Acquired:', info['cashPrize'])
        print('Event Played in:', info['events'])
        print('Rank in Region:', info['rank'])
        print('Win Percentage in Tournaments:', info['percentile'])
    elif response.status_code == 404:
        print("Unable to preform that. ")

except:
    print("Could not find the Power ranking for that user.")
