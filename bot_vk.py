import vk_api
from token_VK import _token

group_id = 203288690

class Bot:
    def __init__(self, group_id, _token):
        self.group_id = group_id
        self.token = _token
        self.vk = vk_api.VkApi(token=_token)
        self.long_poller = vk_api.bot_L

    def run(self):
        pass

if __name__ == 'main':
    bot = Bot(group_id, _token)
    bot.run()
