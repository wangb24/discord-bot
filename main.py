# Copyright (c) 2022 https://github.com/wangb24

# https://github.com/wangb24/discord-bot is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.

# You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2

# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY,
# OR FIT FOR A PARTICULAR PURPOSE.

# See the Mulan PSL v2 for more details.

import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
client = commands.Bot(command_prefix='$')
available_cogs = [filename[:-3] for filename in os.listdir('./cogs') if filename.endswith('.py')]
autoload_cogs = ['debug']


for cog in autoload_cogs:
    if cog in available_cogs:
        try:
            client.load_extension(f'cogs.{cog}')
        except Exception as err:
            print(f'ERROR in {cog}: {err}')
    else:
        print(f'AUTOLOAD: Cog {cog} not found')


@client.command(aliases=['load'])
@commands.has_permissions(administrator=True)
async def load_cog(ctx, extension):
    client.load_extension(name=f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'Loaded {extension}', delete_after=5)

@client.command(aliases=['unload'])
@commands.has_permissions(administrator=True)
async def unload_cog(ctx, extension):
    client.unload_extension(name=f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'Loaded {extension}', delete_after=5)

@client.command(aliases=['reload'])
@commands.has_permissions(administrator=True)
async def reload_cog(ctx, extension):
    client.unload_extension(name=f'cogs.{extension}')
    client.load_extension(name=f'cogs.{extension}')
    await ctx.message.delete()
    await ctx.send(f'Reloaded {extension}', delete_after=5)

@client.command(aliases=['cogs'])
@commands.has_permissions(administrator=True)
async def list_cogs(ctx):
    _em = discord.Embed()
    _em.add_field(name='Available cogs', value='\n'.join(available_cogs))
    await ctx.reply(embed=_em, mention_author=False)


client.run(DISCORD_TOKEN)
