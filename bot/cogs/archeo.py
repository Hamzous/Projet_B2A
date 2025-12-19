import discord
from discord import app_commands
from discord.ext import commands

from bot.services.data import random_artifact, random_fact
from bot.services.embeds import make_embed

class ArcheoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="artefact", description="Affiche un artefact archéologique au hasard")
    async def artefact(self, interaction: discord.Interaction):
        a = random_artifact()
        embed = make_embed(
            title=f"🏺 {a['nom']}",
            color=0x8B4513,
            fields=[
                ("Période", a["periode"], False),
                ("Lieu", a["lieu"], False),
                ("Info", a["info"], False),
            ],
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="fact", description="Affiche un fait archéo/mythologies")
    async def fact(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"🧠 {random_fact()}")

async def setup(bot: commands.Bot):
    await bot.add_cog(ArcheoCog(bot))
