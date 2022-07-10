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
import discord
from discord.ext import commands
CHANNEL_ID = os.getenv('BOT_CHANNEL_ID')

class Debug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(
            status=discord.Status.idle,
            activity=discord.Game(name='绒布球，并在喵喵叫')
        )
        print(f'Connected as {self.client.user}')
        channel = self.client.get_channel()
        await channel.send('Bot is ready', delete_after=10)

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f'Pong!\n{round(self.client.latency * 1000)}ms', mention_author=False)


def setup(client):
    client.add_cog(Debug(client))
