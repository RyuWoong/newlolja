import asyncio,discord,os,random,threading,log,lol,myfunction,db,sys
from discord.ext import commands
from discord.utils import get

## Set Bot
token = myfunction.GET_KEY("token.txt")
game = discord.Game("!!도움말 ver.OpenBeta")
bot = commands.Bot(command_prefix='!!',status=discord.Status.online,activity=game)

## Default Value ##
apptitle = "LoLJa"
footer = f"{apptitle} ver.Beta | ⓒ 2019 깜뭉이"

## Default Function ##
def check_admin(ctx):
    admin = ctx.message.author.permissions_in(ctx.channel)
    check = admin.administrator
    return check

def check_leader(ctx):
    member = ctx.message.author
    leader = get(member.roles,name="파티장")
    check = False
    if leader != None:
        check = True
    return check

def check_streamer(ctx):
    member = ctx.message.author
    streamer = get(member.rolse,name="스트리머")
    check = False
    if streamer != None:
        check = True
    return check

## Start Bot ##
@bot.event
async def on_ready():
    clear = lambda : os.system('cls')
    clear()
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
        embed.add_field(name="!!파티생성 '@팀명' '@유저'", value="파티를 생성하며, 파티장을 선정합니다.\n사전에 해당 팀의 역할 추가 및 역할멘션허용을 해주세요.", inline=False)
        embed.add_field(name="!!경기등록 '@팀명' '@팀명' '설명'", value="경기일정을 추가합니다. 설정된 경기는 리그일정으로 볼 수 있습니다.", inline=False)
        embed.add_field(name="!!경기결과 '매치업번호' '@팀명'", value="경기 결과 등록 및 승점 반영. 승자를 입력해주시고,무승부라면 @팀명에 무승부를 입력.", inline=False)
    else:
        embed.add_field(name="!!공지", value="해당 서버에 등록된 공지를 표시합니다.", inline=False)
        embed.add_field(name="!!인증시작 '소환사명'", value="서버내 디스코드와 소환사를 연결하기 위한 절차 Step.1", inline=False)
        embed.add_field(name="!!인증완료", value="서버내 디스코드와 소환사를 연결하기 위한 절차 Step.2", inline=False)
        embed.add_field(name="!!주사위", value="1~100까지의 값 중 하나를 표시합니다.", inline=False)
        embed.add_field(name="!!뽑기 '최대 값(숫자)'", value="1~최대 값까지 숫자 하나를 표시합니다.", inline=False)
        embed.add_field(name="!!스트리머", value="해당 서버에 소속된 스트리머를 표시합니다.", inline=False)
        embed.add_field(name="!!소환사 '소환사명'", value="해당 소환사의 정보를 표시합니다.", inline=False)
        embed.add_field(name="!!도움말 '파티' 또는 '관리자'", value="파티 또는 리그 명령어 도움말을 표시합니다.", inline=False)
    embed.set_footer(text=footer)
    await ctx.author.send(embed=embed)

@bot.command()
async def 인증시작(ctx,*,summoner):
    await ctx.message.delete()
    log.logger.info(f"C: 인증시작 S: 시작 W:{ctx.author.name}")
    member = ctx.message.author
    discord_id = member.id
    discord_name = member.name
    try:
        summoner_id = lol.get_summoner_id(summoner)
        if summoner_id == None:
            raise Exception
        db.set_member(discord_id,discord_name,summoner_id)
        role = get(ctx.guild.roles, name="대기")
    except IndexError as ex:
        log.logger.error(f"C: 인증시작 S:실패 R: {ex}")
        return await member.send (f"{member.memtion}님 인증이 실패하였습니다. \n**소환사 명**을 확인해주세요. 반복될 시 **관리자**에게 문의해주세요.")
    else:
        await member.add_roles(role)
        await member.send(f"LOL PARTY 서버 인증을 시작합니다.\nLOL 클라이언트에서 인증을 해주세요.\n```cs\n인증번호 : {discord_id}```\n 이후 채널에서 인증확인 명령어를 입력해주세요.\n https://i.imgur.com/XQFFBm1.png")

@bot.command()
async def 인증완료(ctx):
    await ctx.message.delete()
    log.logger.info(f"C: 인증확인 S: 시작 W: {ctx.author.name}")
    discord_id = ctx.message.author.id
    wait = get(ctx.message.author.roles,name="대기")
    try:
        member_info = db.get_member(discord_id)
        summoner_id = member_info[5]
        auth = lol.get_auth_value(summoner_id)
        role1 = get(ctx.guild.roles,name="인증")
    except Exception as ex:
        log.logger.error(f"C: 멤버인증 S: 실패 R: {ex}")
        return await ctx.send(f"멤버인증을 실패하였습니다. 에러 X( ")
    else:
        if str(discord_id) == auth:
            if wait != None:
                await ctx.message.author.remove_roles(wait)
                await ctx.message.author.add_roles(role1)
                await ctx.message.author.send(f"**{ctx.message.author.name}님** 인증되셨습니다.")
                log.logger.info(f"C: 멤버인증 S: 완료 W: {ctx.message.author.name}")
            else:
                await ctx.message.author.send(f"**{ctx.message.author.name}님** 우선 인증 명령어를 입력해주세요.\n자세한 사항은 도움말을 입력해주세요.")
        else:
            print()
            await ctx.message.author.send(f"**{ctx.message.author.name}님** 인증에 실패하였습니다. 인증번호를 정확히 입력해주세요.")
            log.logger.info(f"C: 멤버인증결과 S: 실패 W: {ctx.message.author.name} ID: {discord_id} KEY : {auth}")

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
    if check_admin(ctx):
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
            await ctx.send(f"{streamer.mention}님을 스트리머로 등록 했습니다.")
            log.logger.info(f"C: 스트리머등록 S: 완료 W: {ctx.author.name} T: {streamer.name}")
    else:
        pass

@bot.command()
async def 스트리머인사말(ctx,*,dec):
    await ctx.message.delete()
    if check_streamer(ctx):
        log.logger.info(f"C: 스트리머인사말 S: 시작 W: {ctx.author.name}")
        author = ctx.message.author
        discord_id = author.id
        try:
            db.up_streamer(discord_id,dec)
        except Exception as ex:
            log.logger.error(f"C: 스트리머인사말 S: 실패 R: {ex}")
            return await ctx.send(f"{author}님의 인사말을 설정하지 못했습니다.")
        else:
            await ctx.send(f"{author}님의 인사말을 설정했습니다.")
            log.logger.info(f"C: 스트리머인사말 S: 완료 W: {ctx.author.name}")
    else:
        pass

@bot.command()
async def 스트리머해제(ctx,streamer: discord.Member):
    await ctx.message.delete()
    if check_admin(ctx):
        log.logger.info(f"C: 스트리머해제 S: 시작 W: {ctx.author.name}")
        discord_id = streamer.id
        try:
            db.del_streamer(discord_id)
            role = get(ctx.guild.roles, name="스트리머")
        except Exception as ex:
            log.logger.error(f"C: 스트리머해제 S: 실패 R: {ex}")
            return await ctx.send(f"스트리머해제를 실패하였습니다.")
        else:
            await streamer.remove_roles(role)
            await ctx.send(f"{streamer.mention}님이 스트리머해제 되었습니다.")
            log.logger.info(f"C: 스트리머해제 S: 완료 W: {ctx.author.name} T: {streamer}")
    else:
        pass

@bot.command()
async def 파티등록(ctx,role_name:discord.Role,discord:discord.Member):
    await ctx.message.delete()
    if check_admin(ctx):
        log.logger.info(f"C: 파티등록 S: 시작 W: {ctx.author.name}")
        party_name = role_name.name
        discord_id = discord.id
        discord_name = discord.name
        party_dec = f"안녕하세요. {party_name}입니다!"
        print(discord_name,discord_id,party_name,party_dec)
        try:
            db.set_party(discord_name,discord_id,party_name,party_dec)
            db.set_partymemeber(party_name,discord_id)
            role = get(ctx.guild.roles, name="파티장")
        except Exception as ex:
            log.logger.error(f"C: 파티등록 S: 실패 R: {ex}")
            return await ctx.send("파티등록에 실패했습니다.")
        else:
            await discord.add_roles(role)
            await discord.add_roles(role_name)
            await discord.send(f"**{discord_name}**님께서 신청해주신 파티가 승인 되었습니다.\n파티장 역할이 부여 되었으며, 파티 역할 및 채널이 생성 되었습니다. 자세한 운영은 관리자에게 문의해주시거나 **LOLJA** 명령어를 확인해주세요.")
            log.logger.info(f"C: 파티등록 S: 완료 W: {ctx.author.name} T: {discord}")
    else:
        pass

@bot.command()
async def 파티가입(ctx,member:discord.Member):
    await ctx.message.delete()
    if check_leader(ctx):
        log.logger.info(f"C: 파티가입 S: 시작 W: {ctx.author.name}")
        try:
            party_name = db.get_party(ctx.author.id)
            role = get(ctx.guild.roles,name=party_name)
        except Exception as ex:
            log.logger.error(f"C: 파티가입 S: 실패 R: {ex}")
            return await ctx.send("파티가입에 실패했습니다.")
            
        else:
            await member.add_roles(role)
            await ctx.send(f"{member.mention}님이 **{party_name}**에 가입되셨습니다.")
            log.logger.info(f"C: 파티가입 S: 완료 W: {ctx.author.name} T: {member}")

@bot.command()
async def 파티탈퇴(ctx):
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