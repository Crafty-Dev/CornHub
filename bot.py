import discord
from corn_api import CornAPI


class CornBot(discord.Client):

    def __init__(self, **options):
        super().__init__(**options)
        self.corn_api = CornAPI()

    async def on_ready(self):
        print(f'Discord Bot started as {self.user}')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Geräuschen'))

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        msg = str(message.content)

        if not msg.startswith("!corn"):
            return

        args = msg.split(' ')
        args.pop(0)

        if len(args) == 0:
            url = self.corn_api.search_for_randomcorn()
            if not url is None:
                await message.channel.send(f':smirk: Here is a random **corn** for you: {url}')
            else:
                await message.channel.send('No corn was found :sob:')

        if len(args) >= 1:

            query = ''
            for x in range(0, len(args)):
                query += args[x]
                if x != len(args) - 1:
                    query += ' '

            print(query)
            url = self.corn_api.search_for_corn(query, 'weekly')
            if not url is None:
                await message.channel.send(f'Here is the most viewed weekly corn for **{query}**: {url}')
            else:
                await message.channel.send(f'No corn was found for **{query}** :sob:')
