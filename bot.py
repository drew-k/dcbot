import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os
from format import Format


class Bot(commands.InteractionBot):
    def __init__(self):
        super().__init__()

    async def on_connect(self):
        print(Format.yellow + f"{self.user} has connected." + Format.reset)

    async def on_disconnect(self):
        print(Format.red + f"{self.user} has disconnected." + Format.reset)

    async def on_ready(self):
        print(Format.green + f"{self.user} is ready." + Format.reset)

if __name__ == "__main__":
    bot = Bot()
    bot.run(os.getenv("TOKEN"))
