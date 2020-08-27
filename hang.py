import discord,asyncio,youtube_dl
from discord.ext import commands
import os
import logging
import traceback
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
import discord
from discord.ext import commands
import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout

class hang(commands.Cog):

    
    with open("list.txt") as file:
        lines = [line.strip() for line in file]


    
    #global variables :>
    is_playing = False
    word = 'abcdef'
    wyrazy = lines
    zgaduj = str(random.choice(wyrazy))
    word_cenz = '?' * len(zgaduj) 
    word_cenz_list = list(word_cenz)
    word_list = list(zgaduj)
    players = []
    letters_used = []
    current_player = 0
    hw_ch = 744936390973718630
    liczba = 0
    is_open = False
    

    
    
    
    
    
    
    
    
    
    def __init__(self, bot):
        self.bot = bot
        
    kanalek = None
    
    
    
    #     for i in self.players:
     #          role = get(message.author.guild.roles, id=744926474628366338)
     #               await i.remove_roles(role)
     #                         return
    
    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print('hangman is online')
        
        
    #command
    

    @commands.command()
    async def hangman(self, ctx, message_1: str="help"):
        member = ctx.message.author
        hangman_start_role = get(member.guild.roles, id=744926300980117545)
        hangman_player_role = get(member.guild.roles, id=744926474628366338)
        #variables:
        global is_playing
        global players
        global is_open
        global zgaduj
        global wyrazy
        global word_cenz_list
        global kanalek
        
        if message_1 == None:
            embed=discord.Embed(title="Hangman", color=0x00fbff)
            embed=discord.Embed(title="Hangman", color=0x00fbff)
            embed.add_field(name=">hangman start", value="Roczpoczyna grę", inline=False)
            embed.add_field(name=">hangman join", value="Dołącza do puli graczy", inline=True)
            embed.add_field(name=">guess [a-z]", value="Zgaduj litere jeżeli jest twoja kolej", inline=False)
            embed.set_footer(text="Harnaś | xstiff#8062\nStart: 17.08.2020 01:23\nKoniec: 21:48 17.08.2020")
            await ctx.send(embed=embed)
            return
        if message_1 == "help":
            embed=discord.Embed(title="Hangman", color=0x00fbff)
            embed.add_field(name=">hangman start", value="Roczpoczyna grę", inline=False)
            embed.add_field(name=">hangman join", value="Dołącza do puli graczy", inline=True)
            embed.add_field(name=">guess [a-z]", value="Zgaduj litere jeżeli jest twoja kolej", inline=False)
            embed.set_footer(text="Harnaś | xstiff#8062\nStart: 17.08.2020 01:23\nKoniec: 21:48 17.08.2020")
            await ctx.send(embed=embed)
            return
            
       
        if message_1 == "start" and self.is_playing == False:
            if hangman_start_role in member.roles:
                self.is_playing = True
                self.is_open = True
                await ctx.send(":thumbsup:  Gra rozpoczęta! \n:point_right: Dołącz >hangman join", delete_after=25)
                await ctx.send(":eyes: [ 30 sekund ] ", delete_after=25)
                kanalll = self.bot.get_channel(744936390973718630)
                
                #await ctx.send(self.is_playing)
                await asyncio.sleep(25)
                await ctx.send(":eyes: [ 5 sekund ] ", delete_after=5)
                await asyncio.sleep(5)
                
               
                self.is_open = False
                if len(self.players) < 2:
                    await ctx.send(":warning: Zbyt mało graczy żeby rozpocząć [min. 2] ", delete_after=8)
                    return
                else:
                    
                    self.zgaduj = str(random.choice(self.wyrazy))
                    print(self.zgaduj)
                    print(self.zgaduj)
                    print(self.zgaduj)
                    print(self.zgaduj)
                    await ctx.send(":warning: Gra zamknięta <#744936390973718630>", delete_after=5)
                    await kanalll.send(':warning: >guess [a-z]')
                    await kanalll.send(':warning: ? = litera | Ilosc liter: ' + str(len(self.word_cenz_list)))
                    await kanalll.send('***Wyraz: ' + str(self.word_cenz) + '***')
            if not hangman_start_role in member.roles:
                await ctx.send(":x: Brak roli | Hangman starter")
        
        
                
    
    @commands.Cog.listener()
    async def on_message(self, message):
        global is_open
        global players
        if not message.author.bot:  #role = get(member.guild.roles, id=643922879322390589)  #await member.remove_roles(role)
            if message.content.startswith('>hangman ') and message.content.endswith('join'):
                
                if self.is_playing == True and message.author not in self.players:
                    if self.is_open == True:
                        role = get(message.author.guild.roles, id=744926474628366338)
                        await message.author.add_roles(role)
                        await message.channel.send(':white_check_mark:  + ' + str(message.author.name) + '\n  <#744936390973718630>')
                        self.players.append(message.author)
                        print('+')
                        print(self.players)
                        return
                    else:
                        await message.channel.send(':x: Zapisy zamknięte  <#744936390973718630>' )
                        return
                if self.is_playing == False:
                    await message.channel.send(':x: Gra nie trwa')
                    return 
                if self.is_playing == True and message.author in self.players:
                    #await message.channel.send(self.players)
                    await message.channel.send(':exclamation: Juz jestes, czekaj na gre [min. 2 osoby] <#744936390973718630>')
                    return
                    



    @commands.command()
    async def haslo(self, ctx):
        global zgaduj
        print (self.zgaduj)
        return


    @commands.command()
    async def guess(self, message, litera: str=None):
        global players # gracze
        global hw_ch # kanal
        global word_list # wyraz bez cenz lista
        global word_cenz # wyraz ocenzurowany
        global word_cenz_list # wyraz ocenzurowany lista
        global letters_used # uzyte litery
        global is_playing # czy gra trwa
        global current_player # kogo ruch
        global liczba #numer gracza w liscie
        global word #wyraz oryg.
        global zgaduj
        
        
        
        if self.is_playing == True:
            if ((self.liczba) >= len(self.players)):
                self.liczba = 0
                self.current_player = self.players[self.liczba]
        self.current_player = self.players[self.liczba]
        print('numer w kolejce: '+ str(self.liczba) + ' / ' + str(len(self.players)-1))
        
        
        
        alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if message.channel.id == self.hw_ch:
            if self.is_playing == True:
                if self.current_player == message.author:
                    if message.author in self.players:
                        if not litera:
                            await message.channel.send(':exclamation: Podaj litere ' + str(message.author.name))
                            return
                        if litera:
                            litera = litera.lower()
                            if litera == str(self.zgaduj).lower():
                                    self.is_playing = False
                                    await message.channel.send(':bangbang:  Koniec gry hasło to: ' + str(self.zgaduj) +'\nZgadł: ' + str(message.author.name))
                                    self.players = []
                                    self.zgaduj = str(random.choice(self.wyrazy))
                                    self.word_cenz = '?' * len(self.zgaduj) 
                                    self.word_cenz_list = list(self.word_cenz)
                                    self.word_list = list(self.zgaduj)
                                    
                            if litera in alfabet:
                                if len(litera) == len(litera): #self.word_list
                                    if litera in self.word_list:
                                        if litera in self.letters_used:
                                            await message.channel.send(':x: Juz była litera: ' + str(litera) + '\n:exclamation: Spróbuj jeszcze raz')
                                            await message.channel.send(':point_right: Użyte litery: ' + str(self.letters_used))
                                        else:
                                            gen = (i for i,x in enumerate(self.word_list) if x == litera)
                                            for i in gen: 
                                                print(i)
                                                self.word_cenz_list[int(i)] = litera
                                                self.letters_used.append(str(litera))
                                            await message.channel.send(self.word_cenz_list)
                                            self.liczba = self.liczba + 1
                                            if self.is_playing == True:
                                                if ((self.liczba) >= len(self.players)):
                                                    self.liczba = 0
                                                    self.current_player = self.players[self.liczba]
                                            await message.channel.send(':point_right: Użyte litery: ' + str(self.letters_used))
                                            if not '?' in self.word_cenz_list:
                                                await message.channel.send(':exclamation: Wygrał: ' + str(message.author.name) + ' :clap: :clap: ')
                                                self.is_playing = False
                                                await message.channel.send(':bangbang:  Koniec gry! ' + str(self.is_playing))
                                                self.players = []
                                                self.zgaduj = str(random.choice(self.wyrazy))
                                                self.word_cenz = '?' * len(self.zgaduj) 
                                                self.word_cenz_list = list(self.word_cenz)
                                                self.word_list = list(self.zgaduj)
                                                return
                                            
                                            

                                    else:
                                        if not litera in self.letters_used:
                                            self.letters_used.append(str(litera))
                                            await message.channel.send(':x: Źle! ' + str(message.author.name) + '\n:point_right:  Użyte litery: ' + str(self.letters_used))
                                            await message.channel.send(self.word_cenz_list)
                                            self.liczba = self.liczba+1
                                            if self.is_playing == True:
                                                if ((self.liczba) >= len(self.players)):
                                                    self.liczba = 0
                                                    self.current_player = self.players[self.liczba]
                                                    return

                                            
                            else:
                                self.liczba = self.liczba + 1
                                await message.channel.send(':x: Nie zgadłes! ' + str(message.author.name))
                                
                    else:
                        await self.delete_message(message)
                        await message.channel.send(':warning: Nie twoja kolej! ' + str(message.author.name), delete_after=3)
                        return
                        
                else:
                    await message.channel.send(':warning: Nie twoja kolej! ' + str(message.author.name), delete_after=3)
                    return
            else:
                await message.channel.send(':x: Gra nie rozpoczęta! ')
                return
                
        else:
            await message.channel.send(':x: Zły kanał!\n:point_right: <#744936390973718630> ')
            return
            
            
        


def setup(bot):
    bot.add_cog(hang(bot))
    print('hang.py | Loaded')
