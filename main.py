from bot import CornBot
import json

bot = None


def get_data(key):
    content = json.loads(open("./data.json").read())
    return content[key]


if __name__ == '__main__':
    token = get_data("discord_token")

    bot = CornBot()
    bot.run(token)
