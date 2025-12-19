import discord

def make_embed(title: str, color: int, fields=None, description: str | None = None):
    embed = discord.Embed(title=title, color=color, description=description)
    if fields:
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
    return embed
