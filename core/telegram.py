from security.api_keys import BOT_KEY
import requests


class Telegram:

    def __init__(self):

        self.base_url = "https://api.telegram.org/bot{}/".format(BOT_KEY)

        self.bot_id = int()
        self.first_name = str()
        self.username = str()
        self.update_offset = int()

    def get_me(self):
        """
        This function requests the getMe endpoint, which sends the information about
        the bot related to the current API_KEY being used, like bot_id, and name of the bot.
        :return:
        """

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
        """
        Get the new messages the bot received on chat. The JSON containing the chat and text info are called
        by the API, "updates".
        :return: array with bot last received updates
        """

        print('\nGetting updates.')
        updates_url = self.base_url + 'getUpdates?timeout=100&limit=10'
        if self.update_offset:
            updates_url = updates_url + '&offset={}'.format(str(self.update_offset))

        response = requests.get(updates_url)
        if response.status_code == 200:
            print('Updates received. Working on them now.\n')
            updates_array = response.json()['result']
            self.update_offset = updates_array[-1]['update_id'] + 1
            print(updates_array[0])

            return updates_array
        else:
            print("Error during request. Status code {}\n".format(response.status_code))

    def send_message(self, chat_id, text_message):
        """
        Sends a text message for the chat with the param ID

        :param chat_id: ID of chat, identifier for a chat with a given user or a group
        :param text_message: message to be sent
        :return:
        """

        # chat_id = 15746192
        # text_message = 'testing, hello DK'

        message_as_json = self.format_json(text_message, chat_id)
        response = requests.get(self.base_url + 'sendMessage', data=message_as_json)

        if response.status_code == 200:
            print('Message was sent for the chat {}'.format(chat_id))
        else:
            print('Error sending message to chat {}'.format(chat_id))

    @staticmethod
    def format_json(text_message, chat_id):
        message_to_send_data = {
            'text': text_message,
            'chat_id': chat_id
        }

        return message_to_send_data

    @staticmethod
    def update_log(single_update):
        message = '\nUpdate ID {} from Chat ID {}: \n' \
                  'User {}, which has the id {}, has sent the following message:\n' \
                  '{}'.format(single_update['update_id'],
                              single_update['message']['chat']['id'],
                              single_update['message']['from']['username'],
                              single_update['message']['from']['id'],
                              single_update['message']['text'])
        print(message)

        return message
