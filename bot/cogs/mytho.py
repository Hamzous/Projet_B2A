import discord
from discord import app_commands
from discord.ext import commands

from bot.services.data import random_myth, ENTITES
from bot.services.embeds import make_embed

class MythoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
    name="entites",
    description="Affiche la liste des entités mythologiques disponibles"
)
    async def entites(self, interaction: discord.Interaction):
        names = sorted(ENTITES.keys())
        content = ", ".join(names)

        await interaction.response.send_message(
            f"📜 Entités disponibles :\n{content}"
        )

    @app_commands.command(name="mythe", description="Affiche un récit mythologique au hasard")
    async def mythe(self, interaction: discord.Interaction):
        m = random_myth()
        embed = make_embed(
            title=f"📖 {m['titre']}",
            color=0x2E8B57,
            fields=[
                ("Culture", m["culture"], True),
                ("Résumé", m["resume"], False),
            ],
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="entite", description="Affiche une entité (héros, créature, figure mythologique)")
    @app_commands.describe(nom="Exemples: zeus, ra, odin, minotaure")
    async def entite(self, interaction: discord.Interaction, nom: str):
        key = nom.lower().strip()
        if key not in ENTITES:
            await interaction.response.send_message(
                "❌ Entité inconnue. Essaie : " + ", ".join(sorted(ENTITES.keys())),
                ephemeral=True
            )
            return

        e = ENTITES[key]
        embed = make_embed(
            title=f"📜 {e['nom']}",
            color=0xB8860B,
            fields=[
                ("Type", e["type"], True),
                ("Culture", e["culture"], True),
                ("Description", e["description"], False),
                ("Symbole", e["symbole"], False),
            ],
        )
        if "image" in e:
            embed.set_image(url=e["image"])

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(MythoCog(bot))
