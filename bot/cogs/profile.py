import discord
from discord import app_commands
from discord.ext import commands

from bot.services.storage import load_users, get_user
from bot.services.embeds import make_embed


class ProfileCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="profil",
        description="Affiche tes statistiques personnelles"
    )
    async def profil(self, interaction: discord.Interaction):
        users = load_users()
        user_data = get_user(users, interaction.user.id)

        embed = make_embed(
            title=f"👤 Profil de {interaction.user.display_name}",
            color=0x6A5ACD,
            fields=[
                ("Quiz réalisés", str(user_data["quiz_done"]), True),
                ("Score total", str(user_data["quiz_score"]), True),
            ],
        )

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(ProfileCog(bot))
