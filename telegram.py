from api_keys import BOT_KEY
import requests
import json


class Telegram:

    def __init__(self):

        self.base_url = "https://api.telegram.org/bot{}/".format(BOT_KEY)

        self.bot_id = int()
        self.first_name = str()
        self.username = str()
        self.update_offset = int()

    def get_me(self):

        url = self.base_url + 'getMe'
        print('\nTrying getMe')
        response = requests.get(url)
        if response.status_code == 200:
            print('getMe successful. Populating class variables.\n')
            response_as_json = response.json()['result']
            self.bot_id = response_as_json['id']
            self.first_name = response_as_json['first_name']
            self.username = response_as_json['username']
        else:
            print("Error during request. Status code {}\n".format(response.status_code))

    def get_updates(self):

        print('\nGetting updates.')
        updates_url = self.base_url + 'getUpdates?timeout=100&limit=10'
        if self.update_offset:
            updates_url = updates_url + '&offset={}'.format(str(self.update_offset))

        response = requests.get(updates_url)
        if requests.status_codes == 200:
            print('Updates received. Working on them now.\n')
            self.update_offset = response.json()['result'][-1]['update_id'] + 1

            return response.json()['result']
        else:
            print("Error during request. Status code {}\n".format(response.status_code))

    def send_message(self, chat_id, text_message):
        chat_id = 15746192
        text_message = 'testing, hello DK'

        message_as_json = self.format_json(text_message, chat_id)
        response = requests.get(self.base_url + 'sendMessage', data=message_as_json)
        print(response)


    @staticmethod
    def format_json(text_message, chat_id):
        message_to_send_data = {
            'text': text_message,
            'chat_id': chat_id
        }

        return message_to_send_data


    def check_response(self):
        pass
