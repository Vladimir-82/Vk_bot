import vk_api
from token_VK import _token
import vk_api.bot_longpoll

group_id = 203288690

class Bot:
    def __init__(self, group_id, _token):
        self.group_id = group_id
        self.token = _token
        self.vk = vk_api.VkApi(token=_token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)

    def run(self):
        for event in self.long_poller.listen():
            print('Получено событие')
            try:
                self.on_event(event)
            except Exception as err:
                print(err)

    def on_event(self, event):
        print(event)

if __name__ == '__main__':
    bot = Bot(group_id, _token)
    bot.run()
