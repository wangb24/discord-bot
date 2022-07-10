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

import discord
from discord.ext import commands
import requests


class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['hito'])
    async def hitokoto(self, ctx):
        try:
            embed = self.get_hitokoto()
        except requests.exceptions.ConnectTimeout as err:
            await ctx.send('Ops, something went wrong. Please try again later.', delete_after=5)
            await ctx.message.delete()
            print(err)
            return
        await ctx.reply(embed=embed)

    def get_hitokoto(self):
        URL = 'https://v1.hitokoto.cn/'
        res = requests.get(URL, timeout=5)
        if str(res.status_code).startswith('4'):
            print(res.status_code, 'error')
            raise requests.exceptions.ConnectTimeout('Unable to get hitokoto')
        else:
            res = res.json()
        rtn = []
        try:
            rtn.append(res['hitokoto'])
            if res['from_who'] is None:
                rtn.append(f'*{res["from"]}*')
            else:
                rtn.append(f'{res["from_who"]}, *{res["from"]}*')
        except (KeyError, AttributeError):
            rtn.append(f'*{res["from"]}*')
        except Exception as err:
            print(f'ERROR in miscellaneous: {err}')
            raise err
        return discord.Embed(title=rtn[0], description=rtn[1])


def setup(client):
    client.add_cog(Miscellaneous(client))
