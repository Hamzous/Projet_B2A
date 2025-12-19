import discord
from discord import app_commands
from discord.ext import commands

from bot.services.data import random_quiz
from bot.services.embeds import make_embed
from bot.services.storage import load_users, save_users, get_user


class QuizView(discord.ui.View):
    def __init__(self, question_data: dict):
        super().__init__(timeout=30)
        self.q = question_data
        self.answered = False

        for choice in self.q["choix"]:
            self.add_item(QuizButton(label=choice))


class QuizButton(discord.ui.Button):
    def __init__(self, label: str):
        super().__init__(style=discord.ButtonStyle.primary, label=label)

    async def callback(self, interaction: discord.Interaction):
        view: QuizView = self.view  # type: ignore

        if view.answered:
            await interaction.response.send_message("⏳ Déjà répondu !", ephemeral=True)
            return

        view.answered = True
        correct = view.q["bonne_reponse"]

        # update stats
        users = load_users()
        u = get_user(users, interaction.user.id)
        u["quiz_done"] += 1

        if self.label == correct:
            u["quiz_score"] += 1
            msg = f"✅ Correct ! (+1) Réponse : **{correct}**."
        else:
            msg = f"❌ Faux. Réponse : **{correct}**."

        save_users(users)

        # disable buttons
        for item in view.children:
            item.disabled = True

        await interaction.response.edit_message(content=msg, view=view)


class QuizCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="quiz", description="Lance un mini quiz interactif")
    async def quiz(self, interaction: discord.Interaction):
        q = random_quiz()
        embed = make_embed(
            title="🧩 Quiz MythoArch",
            color=0x1E90FF,
            description=q["question"],
        )
        await interaction.response.send_message(embed=embed, view=QuizView(q))


async def setup(bot: commands.Bot):
    await bot.add_cog(QuizCog(bot))
