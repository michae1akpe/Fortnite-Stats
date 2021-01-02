import requests

username = input("\nPlease enter username of player you wish to search up: ")  # user enters the username they want to
# view stats on
platform = input("\nPlease choose the platform of the user. "
                 "(pc on a PC; psn on PlayStation; Xbox is xbl:")  # user enters the platform they suspect they are on

url = 'https://api.fortnitetracker.com/v1/profile/' + platform + '/' + username
headers = {
    'TRN-Api-Key': 'fill with your api key'  # This can be gotten at fortnitetracker.com
}

response = requests.get(url, headers=headers)  # send request with api key
info = response.json()  # prints the output as a json file

if response.status_code == 200:  # Successful request
    print('Account ID:', info['accountId'])
    print('Country:', info['country'])
    print('Avatar:', info['avatar'])
    print('Platform ID:', info['platformId'])
    print('Last Game Stat:', info['recentMatches'])
elif response.status_code == 401:
    print(
        "The server could not authenticate your 'API-key'.")  # Request could not be made due to the api key being wrong
    print(response.status_code)
elif response.status_code == 404:  # Failed request most likely due to user not existing
    print("Could not find that user. Please ensure you typed in the right gamertag and platform.")
    print(response.status_code)

