import disnake
from disnake.ext import commands
import asyncio
from format import Format, toOrdinalNum

class Theatre(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(dm_permission=False)
    async def create_theatre(
        self,
        inter: disnake.ApplicationCommandInteraction,
        count: int,
        ):
        await inter.response.defer(with_message=True, ephemeral=True)
        category: disnake.CategoryChannel = None
        for i in range(count):
            if i % 50 == 0:
                category = await inter.guild.create_category(
                name="Theatres",
                position=len(inter.guild.channels) - 1,
                reason="Maximum number of channels per category is 50. We need more!"
                )
            channel = await category.create_voice_channel(
                name=f"Drew's {toOrdinalNum(i+1)} 𝕿𝖍éâ𝖙𝖗𝖊",
                position=0
            )
            await asyncio.sleep(0.01)
            await channel.move(end=True)
            await asyncio.sleep(0.01)

        await inter.original_response()
        await inter.response.edit_original_message(content="Theatres created.")

def setup(client):
    client.add_cog(Theatre(client))
    print(Format.blue + Format.italics + f"> Loaded {__name__}" + Format.reset)
