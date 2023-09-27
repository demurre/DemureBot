import oc
import discord
from random import randint, choice
import random
from discord.ext import commands
import time
import typing
import asyncio

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
PREFIX = "Your prefix"
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.remove_command("help")


# login
@bot.event
async def on_ready():
    print("Logged in as", bot.user.name, "id:", bot.user.id)
    info_prefix = PREFIX + "info"
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.listening, name=info_prefix
        ),
    )


# voice ch
@bot.event
async def on_voice_state_update(member, before, after):
    target_channel_id = #Your channel id
    category_id = #Your category id

    if after.channel and after.channel.id == target_channel_id:
        new_channel_name = f"{member.name}'s Channel"
        guild = member.guild
        category = discord.utils.get(guild.categories, id=category_id)

        new_channel = await guild.create_voice_channel(
            new_channel_name, category=category
        )
        await member.move_to(new_channel)

    if before.channel and before.channel.id != target_channel_id:
        left_channel = before.channel

        if left_channel and not left_channel.members:
            await left_channel.delete()


# info
@bot.command(pass_context=True)
async def info(ctx):
    emb = discord.Embed(title="Command", colour=discord.Color.purple())
    emb.add_field(name="{}clear amount".format(PREFIX), value="`Chat clear`")
    emb.add_field(name="{}ban reason".format(PREFIX), value="`Ban User`")
    emb.add_field(name="{}unban".format(PREFIX), value="`Unban User`")
    emb.add_field(name="{}kick reason".format(PREFIX), value="`Kick User`")
    emb.add_field(name="{}mute time reason".format(PREFIX), value="`Mute User`")
    emb.add_field(name="{}unmute".format(PREFIX), value="`Unmute User`")
    await ctx.send(embed=emb)


# clear chat
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    channel = bot.get_channel(logs channel)

    await ctx.channel.purge(limit=1)
    deleted = await ctx.message.channel.purge(limit=amount)
    deleted_channel_id = ctx.message.channel.id
    deleted_by = ctx.author.mention

    await channel.send(
        f"{len(deleted)} messages have been deleted from channel: <#{deleted_channel_id}> by: {deleted_by}"
    )


# ban
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason):
    channel = bot.get_channel(logs channel)
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    await channel.send(f"ban user {member.mention} reason {reason}")


# unban
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unban(ctx, *, user):
    channel = bot.get_channel(logs channel)
    await ctx.channel.purge(limit=1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        await channel.send(f"unbanned user {user.mention}")
        return


# kick
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason):
    channel = bot.get_channel(logs channel)
    await ctx.channel.purge(limit=1)
    await member.kick()
    await channel.send(f"kick user {member.mention} reason {reason}")


# mute
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member, time: int, reason):
    channel = bot.get_channel(logs channel)
    await ctx.channel.purge(limit=1)
    muterole = discord.utils.get(ctx.message.guild.roles, name="mute")
    await member.add_roles(muterole)
    await channel.send(
        f"mute user {member.mention} for {time} second, reason: {reason}"
    )
    await asyncio.sleep(time)
    await member.remove_roles(muterole)


# unmute
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
    channel = bot.get_channel(logs channel)
    muterole = discord.utils.get(ctx.message.guild.roles, name="mute")
    await ctx.channel.purge(limit=1)
    await member.remove_roles(muterole)
    await channel.send(f"unmute user {member.mention}")


bot.run("Your bot token")
