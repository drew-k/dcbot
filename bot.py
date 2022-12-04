import disnake
from disnake.ext import commands
import os
from core.format import Format
from dotenv import load_dotenv

load_dotenv()

class Bot(commands.InteractionBot):
    def __init__(self):
        super().__init__(
            intents=disnake.Intents().default(),
        )

    def init_cogs(self, folder: str = "cogs") -> None:
        """ Initialize cogs in provided folder """
        for file in os.listdir(folder):
            if file.endswith(".py"):
                self.load_extension(f"{folder}.{file[:-3]}")

    async def on_connect(self):
        print(Format.yellow + Format.bold + f"{self.user}" + Format.reset + Format.yellow + " has connected." + Format.reset)

    async def on_disconnect(self):
        print(Format.red + Format.bold + f"{self.user}" + Format.reset + Format.red + " has disconnected." + Format.reset)

    async def on_ready(self):
        print(Format.green + Format.bold + f"{self.user}" + Format.reset + Format.green + " is ready." + Format.reset)

def main():
    bot = Bot()
    bot.init_cogs()
    bot.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    main()
