import discord
import asyncio
import random

client = discord.Client()

token = "OTU3MjU3NDQ5Mjg1NDg0NjA0.Yj8JeA.wiCv6FUr-pnH_5jsStfk6Q4v4g4"

@client.event
async def on_ready():

        print(client.user.name)
        print*"봇이 커졌습니다"
        game = discord.Game("안녕하세요 :D")
        await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
        if message.content == "!핑":
            await message.channel.send("퐁!")

        if message.content == "소우야 도움말":
                embed = discord.Embed(title="도움말", description="---", color=0x00ff00)
                embed.add_field(name="도움 명령어: ", value="소우야 도움말",inline=False)
                embed.add_field(name="운세 명령어: ", value="소우야 운세",inline=True)
                embed.add_field(name="투표 명령어: ", value="s/투표 투표이름,투표내용,투표내용",inline=True)
                embed.add_field(name="초대: ", value="https://discord.com/api/oauth2/authorize?client_id=957257449285484604&permissions=0&scope=bot",inline=False)
                embed.set_footer(text="수정일 : 21/07/10")
                await message.channel.send(embed=embed)


        if message.content == "소우야 운세":
                ran = random.randint(0,3)
                if ran == 0:
                    d = "좋아요! 오늘 하루는 느낌이 좋아요!"
                if ran == 1:
                    d = "으스스.....오늘 하루 조심해요...!"
                if ran == 2:
                    d = "흠...오늘하루 물을 조심해요!"
                if ran == 3:
                    d = "흠...오늘하루 불을 조심해요!"
                await message.channel.send(d)


        if message.content.startswith("s/투표"):
            vote = message.content[4:].split(",")
            await message.channel.send("투표 - " + vote[0])
            for i in range(1, len(vote)):
                choose = await message.channel.send("```" + vote[i] + "```")
                await choose.add_reaction('👍')

        if message.content == "소우야":
            await message.channel.send("네!")

        if message.content == "소우야!":
            await message.channel.send("네!")

        if message.content == "소우야?":
            await message.channel.send("네!")


        if message.content == "소우야 안녕":
            await message.channel.send(f"{message.author.mention}님, 하위!")

        if message.content == "소우야 안녕!":
            await message.channel.send(f"{message.author.mention}님, 하위!")

        if message.content == "소우야 안녕?":
            await message.channel.send(f"{message.author.mention}님, 하위!")



        if message.content == "소우야 사랑해":
            await message.channel.send("저도 사랑해요:heart:")

        if message.content == "소우야 사랑해!":
            await message.channel.send("저도 사랑해요:heart:")

        if message.content == "소우야 더워":
            await message.channel.send("저두 더워용ㅠㅠ")

        if message.content == "소우야 ":
            await message.channel.send("저도 사랑해요:heart:")

client.run(token)