import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from bot.services.embeds import make_embed

load_dotenv()

class MyBot(commands.Bot):
    async def setup_hook(self):
        # Charger les extensions (cogs) au démarrage
        await self.load_extension("bot.cogs.mytho")
        await self.load_extension("bot.cogs.archeo")
        await self.load_extension("bot.cogs.quiz")
        await self.load_extension("bot.cogs.profile")

        # Synchroniser les slash commands
        await self.tree.sync()

intents = discord.Intents.default()
bot = MyBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.tree.command(name="aide", description="Affiche les commandes du bot")
async def aide(interaction: discord.Interaction):
    embed = make_embed(
        title="📜 MythoArch Bot - Commandes",
        color=0x6A5ACD,
        fields=[
            ("/mythe", "Récit mythologique au hasard", False),
            ("/entite nom", "Fiche d’une entité (héros, créature, figure mythologique)", False),
            ("/artefact", "Artefact archéologique au hasard", False),
            ("/fact", "Fait archéo/mythologies", False),
            ("/quiz", "Quiz interactif + score", False),
            ("/profil", "Voir tes statistiques", False),
        ],
    )
    await interaction.response.send_message(embed=embed)

def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN manquant dans .env")
    bot.run(token)

if __name__ == "__main__":
    main()
