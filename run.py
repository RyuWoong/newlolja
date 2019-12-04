import asyncio,discord,os,random,threading,log,lol,myfunction,db
from discord.ext import commands
from discord.utils import get

## Set Bot
token = myfunction.GET_KEY("token.txt")
game = discord.Game("봇 업데이트 중입니다.")
bot = commands.Bot(command_prefix='-',status=discord.Status.online,activity=game)

## Default Value ##
apptitle = "LoLJa"
footer = f"{apptitle} ver.Beta | ⓒ 2019 깜뭉이"

## Default Function ##
def check_admin(ctx):
    admin = ctx.message.author.permissions_in(ctx.channel)
    check = admin.administrator
    return check

def check_leader(ctx,team_name):
    member = ctx.message.author
    leader = get(member.roles,name="파티장")
    check = False
    if leader != None:
        check = True
    return check

## Start Bot ##
@bot.event
async def on_ready():
    clear = lambda : os.system('cls')
    clear()
    print("\n")
    print("       @ Discord Bot LOLJA ")
    print("       @ MADE BY. 깜뭉이 ")
    print("       @ Copyright 깜뭉이. 2019 \n\n")
    print("       봇 Start!\n")

## Discord error ##
@bot.listen('on_command_error')
async def on_command_error(ctx,ex):
    log.logger.error(f"!!!!!!!!!!Discord Error :: {ex}")

## Discord Command ##

@bot.command()
async def 도움말(ctx,detail=None):
    await ctx.message.delete()
    log.logger.info(f"call: {ctx.message.author} func: 도움")
    embed=discord.Embed(title= f"{apptitle} 일반 사용법" if detail==None else f"{apptitle} {detail} 사용법" , description=f"명령어 각 값 띄어쓰기 구분함!, @은 Mention", color=0xf3bb76)
     #embed.set_thumbnail(URL="https://cdn.discordapp.com/attachments/611717026893004810/625911756018941963/NO_.png")
    if (detail == "파티"):
        embed.add_field(name="!!파티가입 '@팀명'@유저'", value="해당 유저를 해당 파티 소속으로 추가합니다.", inline=False)
        embed.add_field(name="!!파티탈퇴", value=" :: 파티에서 탈퇴합니다.", inline=False)
        embed.add_field(name="!!파티정보 '팀명'", value=" :: 해당 파티정보와 파티원들을 소개합니다.", inline=False)
        embed.add_field(name="!!파티추방 '@유저'", value="파티장 -> 해당 유저를 팀에서 추방합니다.", inline=False)
        embed.add_field(name="!!파티소개 '@팀명' '소개글'", value="파티장 -> 파티정보에 보여질 소개글을 작성합니다. (100자 이내)", inline=False)
    elif (detail == "관리자"):
        embed.add_field(name="!!파티원등록 '@유저' '소환사명'", value="파티원으로 해당 유저를 등록합니다.", inline=False)
        embed.add_field(name="!!파티생성 '@팀명' '@유저'", value="파티를 생성하며, 파티장을 선정합니다.\n사전에 해당 팀의 역할 추가 및 역할멘션허용을 해주세요.", inline=False)
        embed.add_field(name="!!경기등록 '@팀명' '@팀명' '설명'", value="경기일정을 추가합니다. 설정된 경기는 리그일정으로 볼 수 있습니다.", inline=False)
        embed.add_field(name="!!경기결과 '매치업번호' '@팀명'", value="경기 결과 등록 및 승점 반영. 승자를 입력해주시고,무승부라면 @팀명에 무승부를 입력.", inline=False)
    else:
        embed.add_field(name="!!공지", value="해당 서버에 등록된 공지를 표시합니다.", inline=False)
        embed.add_field(name="!!주사위", value="1~100까지의 값 중 하나를 표시합니다.", inline=False)
        embed.add_field(name="!!뽑기 '최대 값(숫자)'", value="1~최대 값까지 숫자 하나를 표시합니다.", inline=False)
        embed.add_field(name="!!스트리머", value="해당 서버에 소속된 스트리머를 표시합니다.", inline=False)
        embed.add_field(name="!!소환사 '소환사명'", value="해당 소환사의 정보를 표시합니다.", inline=False)
        embed.add_field(name="!!도움말 '파티' 또는 '관리자'", value="파티 또는 리그 명령어 도움말을 표시합니다.", inline=False)
    embed.set_footer(text=footer)
    await ctx.author.send(embed=embed)

@bot.command()
async def 스트리머(ctx):
    await ctx.message.delete()
    steamers = db.get_streamer()
    if steamers != None:
        for streamer in steamers:
            embed=discord.Embed(title= f"{streamer[1]}", description=f"{streamer[2]}",url=f"{streamer[3]}", color=0xf3bb76)
            embed.set_image(url=f"{streamer[4]}")
            await ctx.message.author.send(embed=embed)
    else:
        await ctx.message.author.send(f"서버와 연결된 스트리머가 없습니다. 저희 서버와 제휴 하실 스트리머는 관리자에게 연락 부탁드립니다.")

@bot.command()
async def 스트리머등록(ctx,streamer: discord.Member,url):
    await ctx.message.delete()
    if check_admin(ctx)==True:
        log.logger.info(f"C: 스트리머등록 S: 시작 W: {ctx.author.name}")
        id = streamer.id
        name = streamer.name
        url = f"https://twitch.tv/{url}/profile"
        dec = f"안녕하세요. LOL PARTY 스트리머 {name} 입니다."
        get_avatar = str(streamer.avatar_url)
        image = get_avatar.split("'")
        streamer_info = [id,name,dec,url,image[0]]
        try:
            db.set_streamer(streamer_info)
            role = get(ctx.guild.roles, name="스트리머")
        except Exception as ex:
            log.logger.error(f"C: 스트리머등록 S: 실패 R: {ex}")
            return await ctx.send(f"{streamer.mention}님 스트리머 등록 실패했습니다.")
        else:
            await streamer.add_roles(role)
            log.logger.info(f"C: 스트리머등록 S: 완료 W: {ctx.author.name} T: {streamer.name}")
            await ctx.send(f"{streamer.mention}님을 스트리머로 등록 했습니다.")
    else:
        pass

@bot.command()
async def 스트리머인사말(ctx):
    await ctx.message.delete()

@bot.command()
async def 주사위(ctx):
    num = random.randrange(1,101)
    log.logger.info(f"call : {ctx.message.author} func : 주사위")
    await ctx.send(f"{ctx.message.author.mention} :game_die:**{num}**")

@bot.command()
async def 뽑기(ctx,number: int):
    num = random.randrange(1,number)
    log.logger.info(f"call : {ctx.message.author} func : 뽑기")
    await ctx.send(f"선택된 번호는! **{num}**")

@bot.command()
async def 소환사(ctx,*,lolname):
    solo_tier,solo_rank = lol.get_summoner_tear(lolname)
    log.logger.info(f"call: {ctx.message.author} func: 소환사정보")
    await ctx.send(f"**{lolname}**의 티어는 {solo_tier} {solo_rank}")

bot.run(token[0])