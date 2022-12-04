import disnake
from disnake.ext import commands
import asyncio
from core.format import Format
from core.ordinals import toOrdinalNum

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
        try:
            category: disnake.CategoryChannel = None
            for i in range(count if count <= 500 else 500):
                if i % 50 == 0:
                    category = await inter.guild.create_category(
                    name="Theatres",
                    position=500,
                    reason="Maximum number of channels per category is 50. We need more!"
                    )
                channel = await category.create_voice_channel(
                    name=f"Drew's {toOrdinalNum(i+1)} 𝕿𝖍éâ𝖙𝖗𝖊",
                    position=500
                )
                await asyncio.sleep(0.2)
            await inter.edit_original_message(content="Theatres created.")
        except disnake.HTTPException:
            await inter.edit_original_message(content="Could not create any more channels.")
        except disnake.Forbidden:
            await inter.edit_original_message(content="You do not have the proper permissions to create channels.")

    @commands.slash_command(dm_permission=False)
    async def destroy_theatre(
        self,
        inter: disnake.ApplicationCommandInteraction,
        ):
        await inter.response.defer(with_message=True, ephemeral=True)
        try:
            logs = await inter.guild.audit_logs(action=disnake.AuditLogAction.channel_create, user=self.client.user, limit=None).flatten()
            log_ids = []
            for log in logs:
                log_ids.append(log.target.id)
            for channel in inter.guild.channels:
                if channel.id in log_ids:
                    await channel.delete(reason="Purging...")
            await inter.edit_original_message(content="Channels deleted...")
        except disnake.HTTPException as exception:
            await inter.edit_original_message(content=exception.text)
        except disnake.NotFound as exception:
            await inter.edit_original_message(content=exception.text)
        except disnake.Forbidden as exception:
            await inter.edit_original_message(content=exception.text)
        except disnake.InvalidData as exception:
            await inter.edit_original_message(content=exception.text)



def setup(client):
    client.add_cog(Theatre(client))
    print(Format.blue + Format.italics + f"> Loaded {__name__}" + Format.reset)
