import discord,asyncio,youtube_dl
from discord.ext import commands
import os
import logging
import traceback
import string
import typing
from logging.handlers import RotatingFileHandler
import random
import i18n
import psutil
import sentry_sdk
import wavelink
from discord.ext.commands import AutoShardedBot
from discord.utils import get
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from discord.ext.commands import has_permissions, CheckFailure
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
import requests
import calendar
from pyowm import OWM
from pyowm.utils import timestamps
from pyowm.owm import OWM
import time
from datetime import datetime
from datetime import date
from os import system, name 


def get_prefix(bot, msg):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['>']

    return commands.when_mentioned_or(*prefixes)(bot, msg)

bot=commands.Bot(command_prefix=get_prefix,description='Harnaś | xstiff#8062', help_command=None)




exts=['music', 'poll']


@bot.event
async def on_ready():
    print("bot.py | Loaded \n")
    print(bot.user.name + " | Loaded")
    
    song_name='Harnaś | >help' 
    activity_type=discord.ActivityType.listening
    await bot.change_presence(activity=discord.Activity(type=activity_type,name=song_name))
    


@bot.command(pass_context=True)
async def who(ctx, Member: discord.Member=None):
#Variables to view #
# user
# user.id
# profile_pic
#Variables to view #
    if not Member:
        Member = ctx.message.author
    
    #    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    today = date.today()
    time_run =  date.today() - Member.created_at.date()
    time_run = int(time_run.total_seconds()/3600/24)
    
    time_is =  date.today() - Member.joined_at.date()
    time_is = int(time_is.total_seconds()/3600/24)
    

    pfp = Member.avatar_url
    
    embed=discord.Embed(title=str(Member), color=3058376)
    embed.set_thumbnail(url=(pfp))
    embed.add_field(name="ID", value=str(Member.id), inline=True)
    embed.add_field(name="Data założenia", value=str(Member.created_at.date()), inline=False)
    embed.add_field(name="Wiek konta", value=str(time_run)+ ' dni', inline=False)
    embed.add_field(name="Dołączył do serwera:", value=str(Member.joined_at.date()), inline=False)
    embed.add_field(name="Czas przebywania na serwerze:", value=str(time_is)+ ' dni', inline=False)
    embed.add_field(name="Avatar: ", value=f'[URL]({pfp})', inline=True)
    embed.set_footer(text="Harnaś | xstiff#8062\nZnika za 30 sekund ")
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=30)
# #0099E1





@bot.command(pass_context=True)
async def inv(ctx):
    invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
    await ctx.message.delete()
    await ctx.send(str(invitelink) + " :wink: \nUżyć: 1", delete_after=30)
    

@bot.command(pass_context=True)
async def powiedz(ctx, message):
    if ctx.message.author.id == 404731929104089111:
        await ctx.message.delete()
        await ctx.send(message)
        return
    else:
        await ctx.message.delete()
        await ctx.send(':x: Nie możesz')
        return


@bot.command()
async def ping(ctx):
    await ctx.send(f':signal_strength:   harnaś   > > >    serwer | ***{round(bot.latency * 1000)} ms ***     ')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=5):
    await ctx.message.delete()
    if (amount > 101):
        await ctx.send(':x: Max: 100' + ' wiadomości ' + '( ' + str(ctx.message.author) + ' )', delete_after=5)
    if (amount < 101):
        await ctx.channel.purge(limit=amount)
        await ctx.send(':white_check_mark:  Usunięto: ' + str(amount) + ' wiadomości ' + '( ' + str(ctx.message.author) + ' )', delete_after=5)




@bot.command(pass_context=True)
async def pogoda(ctx, message_1: str='Góra', message_2: str='PL'):

    #Variables
    #place = 'Góra,PL'

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # Embed message | Dzisiaj
    
    place = ''
    country = ''
    
    
    if not place:
        place = 'Góra'
    if place:
        place = message_1
        
    if not country:
        country = 'PL'
    if country:
        country = message_2
     
    
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    owm = OWM('30263e3dafe66553a6e9866631c68148')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(str(place)+','+str(country))
    w = observation.weather
    forecaster = mgr.forecast_at_place((str(place)+','+str(country)), '3h')
    tomorrow_a = timestamps.tomorrow(8, 0)
    tomorrow_b = timestamps.tomorrow(14, 0)
    tomorrow_c = timestamps.tomorrow(20, 0)
    weather_a = forecaster.get_weather_at(tomorrow_a)
    weather_b = forecaster.get_weather_at(tomorrow_b)
    weather_c = forecaster.get_weather_at(tomorrow_c)   
    jutro_a = weather_a.temperature('celsius')
    jutro_b = weather_b.temperature('celsius')
    jutro_c = weather_c.temperature('celsius')
    dzisiaj = w.temperature('celsius')
    
    
    
    embed=discord.Embed(title=str(place)+' '+str(country)+"  Pogoda | Dzisiaj :sunny: ", color=0x00ffd9)
    embed.set_thumbnail(url="https://media.istockphoto.com/vectors/flat-vector-icon-of-small-fluffy-cloud-with-lights-and-shadows-for-vector-id1041846560?k=6&m=1041846560&s=170667a&w=0&h=MHeemIguvfetILsRpDYqV26sd6-Iki8c8EhZzYyd9CE=")
    embed.set_author(name='☁️   Dzisiaj')
    embed.add_field(name=str(time), value=str(int(dzisiaj['temp'])) + '°C', inline=False)
    embed.set_footer(text="Harnaś | \nxstiff#8062 | OpenWeatherMap\n>pogoda (miasto) (państwo[2 Litery]) | NP: >pogoda Wrocław PL\n ⚠️  Użyta komenda 👉 " + ctx.message.content + ' ⚠️ ')
    wiadomosc_1 = await ctx.send(embed=embed, delete_after=300)
    wiadomosc_1
    await wiadomosc_1.add_reaction('😎')
    
    # Embed message | Jutro
    embed=discord.Embed(title=str(place)+' '+str(country)+"  Pogoda | Jutro :sunny: ", color=0x00ffd9)
    embed.set_thumbnail(url="https://media.istockphoto.com/vectors/flat-vector-icon-of-small-fluffy-cloud-with-lights-and-shadows-for-vector-id1041846560?k=6&m=1041846560&s=170667a&w=0&h=MHeemIguvfetILsRpDYqV26sd6-Iki8c8EhZzYyd9CE=")
    embed.set_author(name='☁️  Jutro ')
    embed.add_field(name='8:00', value='Temperatura:      ' + str(int(jutro_a['temp'])) + '°C' + '\nOdczuwalne:      ' + str(int(jutro_a['feels_like'])) + '°C', inline=False)
    embed.add_field(name='14:00', value='Temperatura:      ' + str(int(jutro_b['temp'])) + '°C' + '\nOdczuwalne:      ' + str(int(jutro_b['feels_like'])) + '°C', inline=False)
    embed.add_field(name='20:00', value='Temperatura:      ' + str(int(jutro_c['temp'])) + '°C' + '\nOdczuwalne:      ' + str(int(jutro_c['feels_like'])) + '°C', inline=False)
    embed.set_footer(text="Harnaś |  \nxstiff#8062 | OpenWeatherMap\n>pogoda (miasto) (państwo[2 Litery]) | NP: >pogoda Wrocław PL\n ⚠️  Użyta komenda 👉 " + ctx.message.content + ' ⚠️ ')
    wiadomosc_2 = await ctx.send(embed=embed, delete_after=300)
    wiadomosc_2
    await wiadomosc_2.add_reaction('😎')
    await ctx.message.delete()


kys = [
 "SPIERDALAJ :joy: ",
 "CHUJ CI W DUPE :joy: ",
 "DZIWKO :joy: "
 ]
 
kanal = [
 "721106140515139735",
 "643930813951377438",
 "643930814924718100",
 "643930816094928922",
 "643930816094928922",
 "742492808933539880",
 "643917943817764938",
 "687744437450965039",
 "687744572042117243"
]
#@bot.event
#async def on_message(message):
#
#   if not message.author.bot:
#        await message.channel.send(random.choice(kys))

@commands.cooldown(1, 3)
@bot.command(pass_context=True)
async def move(ctx, member: discord.Member=None, channel: discord.VoiceChannel=None):
    los = random.choice(kanal)
    channel = channel if channel else bot.get_channel(int(los))
    member = member if member else get(bot.get_all_members(), id=394905584224174080)
    await ctx.message.delete()
    if not (member == get(bot.get_all_members(), id=404731929104089111)) and not (ctx.message.author.id == 394905584224174080):
        await member.edit(voice_channel=channel)
        if not member and not channel: 
            wiadomosc = ':wind_blowing_face:  poof [ 3 sek ] \n' + str(int(los))
        if member and not channel:
            wiadomosc = ':wind_blowing_face:  poof [ 3 sek ] \n' + str(int(los))
        if member and channel:
            wiadomosc = ':wind_blowing_face:  poof [ 3 sek ] \n'
        await ctx.send(wiadomosc, delete_after=3)
    else:
        await ctx.send(':x: ', delete_after=5)
        
@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member=None):
    role_mute = get(member.guild.roles, id=643929413926256708)
    if role_mute in member.roles or ctx.message.author.id == 404731929104089111:
        if not member or member==None:
            await ctx.send(':x: Podaj użytkownika')
        if member.id == bot.user.id:
            await ctx.send(':x: Harnaś odporny :>')
        if not member.id == bot.user.id:
            if member:
                role = get(member.guild.roles, id=643922879322390589)
                if role in member.roles:
                    await member.remove_roles(role)
                    await ctx.send(f':white_check_mark: Odmutowano {str(member)} :>', delete_after=10)
                    await member.edit(voice_channel=None)
                    await member.send(f':white_check_mark: Zostałeś odmutowany przez {ctx.message.author}', delete_after=30)
                    return
                if not role in member.roles:
                    await member.add_roles(role)
                    await ctx.send(f':white_check_mark: Zmutowano {str(member)} :>', delete_after=10)
                    await member.edit(voice_channel=None)
                    await member.send(f':x: Zostałeś zmutowany przez {ctx.message.author}', delete_after=30)
                    return
    else:
        await ctx.send(':x: Wymagana rola do mutowania')


@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, id=643920142128119818)
    await member.add_roles(role)

#@bot.command(pass_context=True)
#async def clear(ctx, lol=0):
#    t = int(lol) or 800
#    if ctx.message.author.id == bot.user.id:
#        async for m in bot.logs_from(ctx.message.channel,limit=t):
#            if m.author.id == bot.user.id:
#                try:
#                    await bot.delete_message(m)
#                except:
#                    pass


@bot.command(pass_context=True)
async def help(ctx):
    author_msg = ctx.message.author
    # Podstawowe await ctx.channel.purge(limit=amount)
    await ctx.message.delete()
    embed=discord.Embed(title=":notepad_spiral:  Podstawowe komendy", url="http://kysnigger.xyz/", description=" ", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/743267328069730406/968a963d95b8b6fb7c3366df7a404405.png?size=128")
    embed.add_field(name=":point_right: >help", value="To okno", inline=False)
    embed.add_field(name=":point_right: >inv", value="Tworzy zaproszenie", inline=False)
    embed.add_field(name=":point_right: >pogoda (Miasto) (Kod_Kraju)", value="Puste miasto = Góra, Pusty kod_kraju = PL | Aktualna pogoda i jutrzejsza w danym miejscu", inline=False)
    embed.add_field(name=":point_right: >join", value="Dołączam, tak o bez powodu", inline=False)
    embed.add_field(name=":point_right: >who [user]", value="Pokazuje informacji o osobie, Puste = ty", inline=False)
    embed.add_field(name=":point_right: >clean [ 1 - 100 ]", value="Usuwa 1 - 100 wiadomości [ administator ]", inline=False)
    embed.add_field(name=":point_right: Zacznij wiadomosc od ```poll  / ankieta```", value="Tworzy ankiete TAK/NIE/NIE WIEM", inline=False)
    embed.add_field(name=":point_right:  >move [user] [channel_id]", value="Przenosi kogoś(puste = perez) do kanału(puste = losowe)", inline=False)
    embed.set_footer(text="Harnaś | xstiff#8062 ")
    await author_msg.send('```= = = = = = = = = Harnaś = = = = = = = = = ```')
    await author_msg.send(embed=embed)
    # Muzyka
    embed=discord.Embed(title=":musical_note:  Muzyka", url="http://kysnigger.xyz/", description=" ", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/743267328069730406/968a963d95b8b6fb7c3366df7a404405.png?size=128")
    embed.add_field(name=":point_right:  >play [ link / tytuł / playlista ]", value="Dodaje piosenke do kolejki", inline=False)
    embed.add_field(name=":point_right:  >pause", value="Pauzuje piosenke", inline=False)
    embed.add_field(name=":point_right:  >resume", value="Wznawaia piosenke", inline=False)
    embed.add_field(name=":point_right:  >skip", value="Pomija aktualną piosenke", inline=False)
    embed.add_field(name=":point_right:  >np / > current", value="Pokazuje aktualną piosenke", inline=False)
    embed.add_field(name=":point_right:  >volume / >vol [ 0 - 100 ]", value="Zwiększa głośność  0% - 100%", inline=False)
    embed.add_field(name=":point_right:  >connect [ id ]", value="Dołącza do kanału [ Puste = twój kanał ]", inline=False)
    embed.add_field(name=":point_right:  >stop", value="Zatrzymuje wszystko", inline=False)
    embed.set_footer(text="Harnaś | xstiff#8062 ")
    #wiadomosc_help = await ctx.send(embed=embed, delete_after=30)
    #wiadomosc_help
    await author_msg.send(embed=embed, delete_after=180)
    await author_msg.send(':white_check_mark: Znikną za 180 sekund')
    await author_msg.send('```= = = = = = = = = Harnaś = = = = = = = = = ```')
    await ctx.send(':white_check_mark:  Wysłałem ci wiadomość prywatną :) | ' + str(author_msg))




        
        
        

graja = []
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

hasla = [
'pralka',
'telefon',
'zmywarka'
]
#@bot.command()
#@commands.has_permissions(administrator=True)
#async def reset(ctx):
#    system('cls')
#    bot.unload_extension('hang')
#    bot.load_extension('hang')
#    await ctx.send(':hourglass: hang.py')
#    await ctx.send(':white_check_mark: przeładowano!')
#    return

for i in exts:
    bot.load_extension(i)


bot.run('NzQzMjY3MzI4MDY5NzMwNDA2.XzSLpA.d9za0mPuVQ2Ev_dIkJHB-UtV9ok')
