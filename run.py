import asyncio,discord,os,random,threading,log,lol,myfunction,db,sys,time
from discord.ext import commands
from discord.utils import get

## Set Bot 테스트시 Token키 및 Command_prefix 변경
token = myfunction.GET_KEY("token.txt")
game = discord.Game("!!도움말 ver.1.0.0")
bot = commands.Bot(command_prefix='-',status=discord.Status.online,activity=game)

## Default Value ##
apptitle = "LoLJa"
footer = f"{apptitle} ver.1.0.0 | ⓒ 2019 깜뭉이"
bot.STATUS_START = False
bot.myGuild = None
myVoiceChannels = [654500798281023493, 654493633608810527,654493745554784276,654493812860780544,654825518461354004,662909933112524824]
normal_Channel = 654337874207965184
chess_Channel = 654337910979559426
rank_Channel = 654507949774995459
waiting_Channel = 654825518461354004
team_category = 376628550041731072
caution_Channel = 506395577815138304
civilwar_Channel = 654952875583209502
academy_Channel = 657017538965667867
streamer_Channel = 663912768738557992
emoji_url = "https://cdn.discordapp.com/emojis/"
emblem_Id = [654644195260366848,654644204978307072,654644217284526091,654644225706557470,654644237278773258,654644245277442048,654644294019448832,654644301975912479,654644310054273036]
emblem_Index = ["IRON","BRONZE","SILVER","GOLD","PLATINUM","DIAMOND","MASTER","GRANDMASTER","CHALLENGER"]
winners = [248123112472838144,338203400271560704,275126185745186816,614752807639187475,244372339930693632]


## Default Function ##
def check(ctx,type):
    check = False
    member = ctx.message.author
    if type == "admin":
        admin = get(member.roles,name="관리자")
        if admin != None:
            check = True
            return check
    elif type == "leader":
        leader = get(member.roles,name="파티장")
        if leader != None:
            check = True
            return check
    elif type == "streamer": 
        streamer = get(member.roles,name="스트리머")
        if streamer != None:
            check = True
            return check
    elif type == "wait":
        wait = get(member.roles,name="대기")
        if wait != None:
            check = True
            return check
    elif type == "auth":
        auth = get(member.roles,name="인증")
        if auth != None:
            check = True
            return check
    elif type == "teacher":
        teacher = get(member.roles,name="선생님")
        if teacher != None:
            check = True
            return check
    elif type == "student":
        student = get(member.roles,name="학생")
        if student != None:
            check = True
            return check

## Start Bot ##
@bot.event
async def on_ready():
    #os.system('cls')
    os.system('clear')
    bot.myGuild = bot.get_guild(316770615644389376)
    myVoiceChannels = bot.myGuild.voice_channels
    print("       @ Discord Bot LOLJA")
    print("       @ MADE BY. 깜뭉이")
    print("       @ Copyright 깜뭉이. 2019")
    print("       @ Start!")
    print("       GUILD -")
    #print(myVoiceChannels)
    bot.STATUS_START = True
'''
## Discord error ##
@bot.listen('on_command_error')
async def on_command_error(ctx,ex):
    log.logger.error(f"!!!!!!!!!!Discord Error :: {ex}")
'''
## Discord Event##
'''
@bot.event
async def on_member_ban(guild,user):
    print(guild,user)
    admin = get(guild.roles,name="관리자")
    channel= guild.get_channel(caution_Channel)
    print(channel)
    embed=discord.Embed(title= f":no_entry: 제재조치 : 차단",description=f"{user.id}", color=0xe74c3c)
    embed.add_field(name="관리자", value=f"{admin.mention}", inline=True)
    embed.add_field(name="제재자", value=f"{user.mention}", inline=True)
    embed.add_field(name="제재사유", value=f"경고 누적 혹은 스팸, 악성유저로 서버에서 차단되었습니다.", inline=False)
    await channel.send(embed=embed)

@bot.event
async def on_voice_state_update(member,before,after):
    left_channel = before.channel
    now_channel = after.channel
    print(left_channel,now_channel)
    if bot.STATUS_START:
        if left_channel != None:
            if left_channel.id in myVoiceChannels:
                log.logger.info(f"C : {member} F : Left VoiceChannel")
                pass
            else:
                print(len(left_channel.members))
                if len(left_channel.members) < 1:
                    log.logger.info(f"C : {member} F : Left VoiceChannel and Delete Channel")
                    await left_channel.delete()
        if now_channel != None:
            log.logger.info(f"C : {member} F : In VoiceChannel")
            print(now_channel.id,type(now_channel.id))
            print(now_channel.id == 654500798281023493)
            if now_channel.id in myVoiceChannels:
                embed=discord.Embed(title= f":video_game: 게임 개설!", description=f"아래 초대코드를 사용해서 유저들을 모아보세요!", color=0xf3bb76)
                if now_channel.id == 654500798281023493 :
                    log.logger.info(f"C : {member} F : StartGame Normal Game")
                    category = now_channel.category
                    overwrite = {
                        member : discord.PermissionOverwrite(manage_channels=True)
                    }
                    new_channel = await category.create_voice_channel(name="일반 방제 미정",overwrites=overwrite,bitrate=bot.myGuild.bitrate_limit,user_limit=5)
                    invite = await new_channel.create_invite(max_age=360)
                    channel = bot.myGuild.get_channel(normal_Channel)
                    await member.move_to(new_channel)
                    embed.add_field(name=":hammer: 개설자",value=f"{member.mention}",inline=True)
                    embed.add_field(name=":crossed_swords: 게임방식",value=f"일반게임",inline=True)
                    embed.add_field(name=":love_letter: 초대코드", value=f"{invite.url}", inline=False)
                    await channel.send(embed=embed)

                elif now_channel.id == 654493633608810527 :
                    log.logger.info(f"C : {member} F : StartGame LOLChess")
                    category = now_channel.category
                    overwrite = {
                        member : discord.PermissionOverwrite(manage_channels=True)
                    }
                    new_channel = await category.create_voice_channel(name="TFT 방제 미정",overwrites=overwrite,bitrate=bot.myGuild.bitrate_limit,user_limit=8)
                    invite = await new_channel.create_invite(max_age=360)
                    channel = bot.myGuild.get_channel(chess_Channel)
                    await member.move_to(new_channel)
                    embed.add_field(name=":hammer: 개설자",value=f"{member.mention}",inline=True)
                    embed.add_field(name=":crossed_swords: 게임방식",value=f"전략적 팀 전투",inline=True)
                    embed.add_field(name=":love_letter: 초대코드", value=f"{invite.url}", inline=False)
                    await channel.send(embed=embed)

                elif now_channel.id == 654493745554784276 :
                    log.logger.info(f"C : {member} F : StartGame Duo Rank")
                    category = now_channel.category
                    overwrite = {
                        member : discord.PermissionOverwrite(manage_channels=True)
                    }
                    new_channel = await category.create_voice_channel(name="듀오 방제 미정",overwrites=overwrite,bitrate=bot.myGuild.bitrate_limit,user_limit=2)
                    invite = await new_channel.create_invite(max_age=360)
                    channel = bot.myGuild.get_channel(rank_Channel)
                    await member.move_to(new_channel)
                    embed.add_field(name=":hammer: 개설자",value=f"{member.mention}",inline=True)
                    embed.add_field(name=":crossed_swords: 게임방식",value=f"솔로/듀오 랭크",inline=True)
                    embed.add_field(name=":love_letter: 초대코드", value=f"{invite.url}", inline=False)
                    await channel.send(embed=embed)

                elif now_channel.id == 654493812860780544  :
                    log.logger.info(f"C : {member} F : StartGame Free Rank")
                    category = now_channel.category
                    overwrite = {
                        member : discord.PermissionOverwrite(manage_channels=True)
                    }
                    new_channel = await category.create_voice_channel(name="자유 방제 미정",overwrites=overwrite,bitrate=bot.myGuild.bitrate_limit,user_limit=5)
                    invite = await new_channel.create_invite(max_age=360)
                    channel = bot.myGuild.get_channel(rank_Channel)
                    await member.move_to(new_channel)
                    embed.add_field(name=":hammer: 개설자",value=f"{member.mention}",inline=True)
                    embed.add_field(name=":crossed_swords: 게임방식",value=f"자유 랭크",inline=True)
                    embed.add_field(name=":love_letter: 초대코드", value=f"{invite.url}", inline=False)
                    await channel.send(embed=embed)
            else:
                pass
'''

@bot.event
async def on_member_update(before,after):
    if after.activity == None:
        pass
    else:
        print(after.activity)
        if str(after.activity.type)== "ActivityType.streaming":
            if get(after.roles,name="스트리머") == None:
                pass
            else:
                log.logger.info(f"C: 방송알림 S: 시작 W:{after}")
                channel= after.guild.get_channel(streamer_Channel)
                embed=discord.Embed(title= f"{after.name}님이 방송중!",description=after.activity.twitch_name,url=after.activity.url, color=0x6441A5)
                embed.set_thumbnail(url=after.avatar_url)
                embed.add_field(name=after.activity.name, value=after.activity.detail, inline=False)
                embed.set_footer(text=":balloon: LOL PARTY STEAMER")
                await channel.send(content=f"여기에요! {after.activity.name}님이 방송을 시작했다구요! @here ",embed=embed)
                log.logger.info(f"C: 방송알림 S: 완료 W:{after}")

## Discord Command ##
@bot.command()
async def 아이디(ctx,mention:discord.Member):
    await ctx.message.delete()
    member_id =  mention.id
    await ctx.message.author.send(mention,member_id)

@bot.command()
async def 테스트(ctx):
    stream = discord.Streaming(name="쏘기자",url=" https://www.twitch.tv/sso_lovely91")
    print(stream)

@bot.command()
async def 도움말(ctx,detail=None):
    await ctx.message.delete()
    url=bot.myGuild.icon_url
    log.logger.info(f"call: {ctx.message.author} func: 도움")
    embed=discord.Embed(title= f"{apptitle} 사용서" if detail==None else f"{apptitle} {detail} 사용서" , description=f"명령어 내 값은 띄어쓰기로 구분, @은 호출", color=0xf3bb76)
    embed.set_thumbnail(url=url)
    if (detail == "파티"):
        embed.add_field(name="!!파티가입 '@유저'", value="파티장) 해당 유저를 본인 파티 소속으로 추가합니다.", inline=False)
        embed.add_field(name="!!파티탈퇴", value="파티에서 탈퇴합니다. 파티장인 경우 관리자에게 문의해주세요.", inline=False)
        embed.add_field(name="!!파티탈퇴 '@유저'", value="파티장) 파티에서 추방합니다. ", inline=False)
        embed.add_field(name="!!파티목록", value="서버내 파티 목록을 보여줍니다. ", inline=False)
        embed.add_field(name="!!파티 '팀명'", value="해당 파티정보와 파티원들을 소개합니다.", inline=False)
        embed.add_field(name="!!파티편집 '소개글'", value="파티장) 파티정보에 보여질 소개글을 작성합니다.", inline=False)
    elif (detail == "관리자"):
        embed.add_field(name="!!경고 '@유저'", value="해당 유저에게 경고를 부여합니다. 경고 3번시 차단을 부여합니다.", inline=False)
        embed.add_field(name="!!파티등록 '@팀명' '@유저'", value="파티를 생성하며, 파티장을 선정합니다.\n사전에 해당 팀의 역할 추가 및 역할멘션을 허용해주세요.", inline=False)
        embed.add_field(name="!!교직이수 '라인' '소개글'", value="선생님을 등록합니다. 라인Top,Jungle,Mid,Bot,Sup 소개글 띄워쓰기 가능", inline=False)
    elif (detail =="아카데미"):
        embed.add_field(name="!!선생님", value="아카데미에서 가르치는 선생님 목록을 보여줍니다.", inline=False)
        embed.add_field(name="!!입학 '@유저'", value="선생님)유저를 명령어를 호출한 선생님의 학생으로 등록합니다.", inline=False)
        embed.add_field(name="!!퇴학", value="학생에서 탈퇴합니다.", inline=False)

    elif (detail == "인증"):
        embed.add_field(name="!!인증시작 '소환사명'", value="서버내 디스코드와 소환사를 연결하기 위한 절차 Step.1", inline=False)
        embed.add_field(name="!!인증완료", value="서버내 디스코드와 소환사를 연결하기 위한 절차 Step.2", inline=False)
        embed.add_field(name="!!티어갱신", value="소환사 티어 역할을 갱신합니다.", inline=False)
    elif (detail == "일반"):
        embed.add_field(name="!!공지", value="서버 공지사항을 알려줍니다.", inline=False)
        embed.add_field(name="!!주사위", value="1~100까지의 값 중 하나를 표시합니다.", inline=False)
        embed.add_field(name="!!뽑기 '최대 값(숫자)'", value="1~최대 값까지 숫자 하나를 표시합니다.", inline=False)
        embed.add_field(name="!!스트리머", value="해당 서버에 소속된 스트리머를 표시합니다.", inline=False)
        embed.add_field(name="!!소환사 '소환사명'", value="해당 소환사의 정보를 표시합니다.", inline=False)
        embed.add_field(name="!!명예의전당", value="롤파티 리그 우승팀을 소개합니다.", inline=False)
        embed.add_field(name="!!내전", value="내전 대기실에 있는 인원을 자동으로 팀을 편성해줍니다.", inline=False)
        embed.add_field(name="!!정보 '@유저'", value="인증된 유저에 한해 정보를 보여줍니다.", inline=False)
    else:
        embed.add_field(name="!!도움말 일반", value="일반 및 유틸 명령어을 보여줍니다.", inline=False)
        embed.add_field(name="!!도움말 파티", value="파티와 관련된 명령어를 보여줍니다.", inline=False)
        embed.add_field(name="!!도움말 인증", value="인증과 관련된 명령어를 보여줍니다.", inline=False)
        embed.add_field(name="!!도움말 아카데미", value="인증과 관련된 명령어를 보여줍니다.", inline=False)
    embed.set_footer(text=footer)
    await ctx.message.author.send(embed=embed)

@bot.command()
async def 인증(ctx):
    await ctx.message.delete()
    await ctx.send("`!!인증시작 소환사명` 명령어로 인증을 시작할 수 있습니다.")

@bot.command()
async def 인증시작(ctx,*,summoner=""):
    await ctx.message.delete()
    log.logger.info(f"C: 인증시작 S: 시작 W:{ctx.author.name}") #시작
    member = ctx.message.author #info 
    discord_id = member.id
    discord_name = member.name
    if check(ctx,"auth"): #소환사 계정 변경 방지. 이미 인증되어 있다면 못하게 제한합니다.
        log.logger.info(f"C: 인증시작 S:실패 R: 이미 인증된 유저")
        return await ctx.send(f"{member.mention}\n:octagonal_sign: 이미 인증이 되어있습니다.\n:exclamation: 연동된 소환사를 변경하길 원하신다면 **깜뭉이**에게 문의해주세요.")
    try:
        summoner_id = lol.get_summoner_id(summoner)
        print(summoner_id) # 소환사 명을 통해 소환사ID 키 값을 가져옵니다.
        if summoner_id == None: # 잘못된 소환사 명을 입력 했을 경우 인증 실패로 반환합니다.
            raise Exception('소환사 명 잘못됨')
        db.set_member(discord_id,discord_name,summoner_id) # DB에 디스코드id , 디스코드 별명, 소환사 아이디를 기록합니다.
        role = get(ctx.guild.roles, name="대기") #대기 역할 가져오기
    except Exception as ex:
        log.logger.error(f"C: 인증시작 S:실패 R: {ex}")
        return await ctx.send (f"{member.mention}\n:x: 인증이 실패하였습니다.\n:ballot_box_with_check: **소환사 명**을 정확히 입력해주세요.")
    else:
        await member.add_roles(role) # 대기 라는 역할을 부여하여 유저에게 인증 시작 단계임을 표시합니다.
        embed=discord.Embed(title= f":white_check_mark: LOL PARTY 소환사 인증", description=f"대표하는 소환사 계정을 인증합니다.", color=0xf3bb76)
        embed.set_thumbnail(url=bot.myGuild.icon_url)
        embed.add_field(name=":pencil2: 인증번호", value=f"{discord_id}", inline=False)
        embed.add_field(name=":bangbang: 주의사항", value=f"클라이언트에서 반드시 동의 버튼을 눌러야합니다. 이후 인증채널에서 '!!인증완료' 명령어를 입력해주세요.", inline=False)
        embed.set_image(url="https://i.imgur.com/XQFFBm1.png")
        embed.set_footer(text=footer)
        await member.send(embed=embed)
        await ctx.send (f"{member.mention}\n:green_square: 인증을 시작합니다. 개인메세지를 확인해주세요.")
        log.logger.info(f"C: 인증시작 S: 완료 W:{ctx.author.name}")

@bot.command()
async def 인증완료(ctx):
    await ctx.message.delete()
    log.logger.info(f"C: 인증완료 S: 시작 W: {ctx.author.name}") #시작
    member = ctx.message.author #info
    discord_id = member.id
    if check(ctx,"auth"):
        return await ctx.send(f"{member.mention}\n:octagonal_sign: 이미 인증이 되어있습니다.\n:exclamation: 연동된 소환사를 변경하길 원하신다면 **깜뭉이**에게 문의해주세요.")
    if not check(ctx,"wait"):
        return await ctx.send(f"{member.mention}\n:exclamation: !!인증시작부터 먼저 입력해주세요.\n:question: 자세한 사항은 `!!도움말 인증`을 확인해주세요.")
    wait = get(member.roles,name="대기")
    try:
        channel = ctx.guild.get_channel(654855564521897984)
        member_info = db.get_member(discord_id)
        summoner_id = member_info[5]
        auth = lol.get_auth_value(summoner_id) #소환사id로 인증 값 불러오기
        

    except Exception as ex:
        log.logger.error(f"C: 인증완료 S: 실패 R: {ex}")
        return await ctx.send(f"{member.mention}\n:red_square: 소환사 인증을 실패 하였습니다. :sweat: ")

    else:
        if True: #인증 단계 str(discord_id)==auth
            await member.remove_roles(wait) #대기 역활 삭제
            auth_role = get(ctx.guild.roles,name="인증") #인증역할 찾기
            await member.add_roles(auth_role) #인증역할 부여
            summoner_name = lol.get_summoner_name(summoner_id)
            leagues = lol.get_summoner_league(summoner_id)
            if len(leagues) < 1:
                tier_role = get(ctx.guild.roles,name=f"UNRANKED")
                db.renew(discord_id,None)
                await member.add_roles(tier_role)
                solo_tier = "UNRANKED"
                solo_rank = ""
            else:
                for league in leagues:
                    if league['queueType'] == "RANKED_SOLO_5x5":
                        solo = True
                        solo_tier = league['tier']
                        solo_rank = league['rank']
                        break
                    else:
                        solo = False
                if solo:
                    tier_role = get(ctx.guild.roles,name=f"{solo_tier}")
                    db.renew(discord_id,f"{solo_tier} {solo_rank}")
                    await member.add_roles(tier_role)
                else:
                    tier_role = get(ctx.guild.roles,name=f"UNRANKED")
                    db.renew(discord_id,None)
                    await member.add_roles(tier_role)

            url=bot.myGuild.icon_url
            embed=discord.Embed(title= f":white_check_mark: LOL PARTY 소환사 인증서", color=0xf3bb76)
            embed.set_thumbnail(url=url)
            embed.add_field(name=":smiley: **유저 정보**", value=f"디스코드: {member.mention}\n소환사명: {summoner_name}", inline=False)
            if tier_role.name == "UNRANKED":
                embed.add_field(name=":medal: **티어 정보**", value=f"현재티어: UNRANKED", inline=False)
            else:
                index = emblem_Index.index(solo_tier)
                embed.add_field(name=":medal: **티어 정보**", value=f"현재티어: <:LOLPARTY:{emblem_Id[index]}> {solo_tier} {solo_rank}", inline=False)
            await channel.send(embed=embed)
            await ctx.send(f":white_check_mark: {member.mention}님 소환사 인증이 완료되었습니다.")
        else:
            await ctx.send(f"{member.mention}\n:red_square: **인증번호**가 일치하지 않습니다. :sweat:")
            log.logger.info(f"C: 인증확인결과 S: 실패 W: {member.name} ID: {discord_id} KEY : {auth}")

@bot.command()
async def 티어갱신(ctx):
    await ctx.message.delete() 
    if check(ctx,"auth"):
        log.logger.info(f"C: 티어갱신 S: 시작 W: {ctx.author.name}")
        member = ctx.message.author
        discord_id = member.id
        channel = ctx.guild.get_channel(654855564521897984)
        try:
            member_info = db.get_member(discord_id)
            summoner_id = member_info[5]
            summoner_name = lol.get_summoner_name(summoner_id)

            if member_info[6]==None:
                get_lasttier = "UNRANKED"
            else:
                get_lasttier = member_info[6]
            
            leagues = lol.get_summoner_league(summoner_id)
            if len(leagues) < 1:
                solo = False
            else:
                for league in leagues:
                    if league['queueType'] == "RANKED_SOLO_5x5":
                        solo = True
                        solo_tier = league['tier']
                        solo_rank = league['rank']
                        break
                    else:
                        solo = False
        except Exception as ex:
            log.logger.error(f"C: 티어갱신 S: 실패 R: {ex}")
            return await ctx.send(f"{member.mention}\n:red_square: 갱신을 실패하였습니다. X( ")
        else:
            url=bot.myGuild.icon_url
            lasttier = get_lasttier.split()
            tier_role = get(ctx.guild.roles,name=f"{lasttier[0]}")
            await member.remove_roles(tier_role)

            if solo:
                tier_role = get(ctx.guild.roles,name=f"{solo_tier}")
                await member.add_roles(tier_role)
                db.renew(discord_id,f"{solo_tier} {solo_rank}")
                embed=discord.Embed(title= f":white_check_mark: LOL PARTY 티어 갱신", color=0xf3bb76)
                embed.set_thumbnail(url=url)
                embed.add_field(name=":smiley: **유저 정보**", value=f"디스코드: {member.mention}\n 소환사명: {summoner_name}", inline=False)
                if lasttier[0] == "UNRANKED":
                    index = emblem_Index.index(solo_tier)
                    embed.add_field(name=":medal: **티어 정보**", value=f"이전티어. UNRANKED\n현재티어: <:LOLPARTY:{emblem_Id[index]}> {solo_tier} {solo_rank}", inline=False)
                else:    
                    bindex = emblem_Index.index(lasttier[0]) 
                    index = emblem_Index.index(solo_tier)
                    embed.add_field(name=":medal: **티어 정보**", value=f"이전티어: <:LOLPARTY:{emblem_Id[bindex]}> {get_lasttier}\n현재티어: <:LOLPARTY:{emblem_Id[index]}> {solo_tier} {solo_rank}", inline=False)
                await channel.send(embed=embed)
                await ctx.send(f":white_check_mark: {member.mention}님 티어갱신이 완료 되었습니다.")
                
            else:
                tier_role = get(ctx.guild.roles,name=f"UNRANKED")
                db.renew(discord_id,None)
                await member.add_roles(tier_role)
                index = emblem_Index.index(lasttier[0])
                embed=discord.Embed(title= f":white_check_mark: LOL PARTY 티어 갱신", color=0xf3bb76)
                embed.set_thumbnail(url=url)
                embed.add_field(name=":smiley: **유저 정보**", value=f"디스코드. {member.mention}\n 소환사명. {summoner_name}", inline=False)
                if lasttier == "UNRANKED":
                    embed.add_field(name=":medal: **티어 정보**", value=f"이전티어. UNRANKED\n현재티어. UNRANKED", inline=False)
                else:    
                    embed.add_field(name=":medal: **티어 정보**", value=f"이전티어. <:LOLPARTY:{emblem_Id[index]}> {get_lasttier}\n현재티어. UNRANKED", inline=False)
                await ctx.send(embed=embed)
            log.logger.info(f"C: 티어갱신 S: 완료 W: {member.name}")
            

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
    if check(ctx,'admin'):
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
            return await ctx.message.author.send(f"{streamer.mention}님 스트리머 등록 실패했습니다.")
        else:
            await streamer.add_roles(role)
            await ctx.message.author.send(f"{streamer.mention}님을 스트리머로 등록 했습니다.")
            await ctx.streamer.send(f"**{name}**님 안녕하세요? 저희 **LOL PARTY**와 함께 하시게 된 것을 진심으로 환영합니다.\n도움이 필요하시면 **깜뭉이**에게 문의 부탁드립니다! 또한 필요한 기능이 있으시다면 언제든 말씀해주세요.\n\n:gift: 서버내 혜택\n1. 스트리머 역할 부여 및 `!!스트리머` 명령어로 스트리머 소개 (`!!스트리머인사말 '인사말'` 명령어로 스트리머 인사말을 편집 할 수 있습니다.)\n2. 스트리머 채널 및 채팅 채널에서 방송 공지 가능 (향후 봇이 자동적으로 알리도록 변경)\n\n:octagonal_sign: 서버 요청사항\n1. 싹둑이로 서버 초대코드 노출\n2. 간간히 서버내 시참방송")
            log.logger.info(f"C: 스트리머등록 S: 완료 W: {ctx.author.name} T: {streamer.name}")
    else:
        pass

@bot.command()
async def 스트리머인사말(ctx,*,dec):
    await ctx.message.delete()
    if check(ctx,'streamer'):
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
    if check(ctx,'admin'):
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
async def 파티(ctx,*,party_name):
    await ctx.message.delete()
    member = ctx.message.author
    log.logger.info(f"C: 파티 S: 시작 W: {member.name}")
    try:
        party_info = db.get_partyInfo(party_name)
        party_role = get(ctx.guild.roles,name=f"{party_info[2]}")
        party_leader = ctx.guild.get_member(int(party_info[1]))
        party_members = party_role.members
        print(party_leader)
    except Exception as ex:
        log.logger.error(f"C: 파티 S: 에러 {ex}")
        return await ctx.send(f"**{party_name}** 이름을 가진 파티가 없습니다.")
    else:
        embed=discord.Embed(title= f":tada: {party_name}", description=f"{party_info[3]}", color=party_role.color)
        embed.add_field(name=f":man_mage: 파티장", value=f"{party_leader}", inline=True)
        embed.add_field(name=f":clock3: 활동시간", value=f"{party_info[4]}", inline=True)
        embed.add_field(name=f":dizzy: 티어대", value=f"{party_info[5]}", inline=True)
        embed.add_field(name=f":crossed_swords: 파티유형", value=f"{party_info[6]}", inline=False)
        embed.add_field(name=f":family_mmbb: 파티인원({len(party_members)}/10)", value=f" / ".join(map(str,party_members)))
        embed.set_footer(text=footer)
        await ctx.message.author.send(embed=embed)


@bot.command()
async def 파티목록(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    log.logger.info(f"C: 파티목록 S: 시작 W: {member.name}")
    partyList = db.get_partyList()
    embed=discord.Embed(title= f":scroll: 파티목록", description=f"LOL PARTY 서버 내 파티 목록입니다.", color=0xf3bb76)
    for party in partyList:
        party_leader = ctx.guild.get_member(int(party[1]))
        party_name = party[2]
        party_time = party[4]
        party_tier = party[5]
        party_type = party[6]
        embed.add_field(name=f":tada: **{party_name}**", value=f"파티장 : {party_leader}\n시간대: {party_time}\n티어대: {party_tier}\n유형: {party_type}", inline=False)
    embed.set_footer(text=footer)
    await ctx.message.author.send(embed=embed)

@bot.command()
async def 파티등록(ctx,role_name:discord.Role,member:discord.Member):
    await ctx.message.delete()
    if check(ctx,'admin'):
        log.logger.info(f"C: 파티등록 S: 시작 W: {ctx.message.author.name}")
        party_name = role_name.name
        discord_id = member.id
        discord_name = member.name
        party_dec = f"안녕하세요. {party_name}입니다!"
        print(discord_name,discord_id,party_name,party_dec)
        try:
            db.set_party(discord_name,discord_id,party_name,party_dec)
            db.set_partymemeber(party_name,discord_id)
            role = get(ctx.guild.roles, name="파티장")
            category = get(ctx.guild.categories,id=376628550041731072)
            overwrite={
                ctx.guild.default_role : discord.PermissionOverwrite(send_messages=False),
                role_name : discord.PermissionOverwrite(send_messages=True)
            }
        except Exception as ex:
            log.logger.error(f"C: 파티등록 S: 실패 R: {ex}")
            return await ctx.send("파티등록에 실패했습니다.")
        else:
            await member.add_roles(role)
            await member.add_roles(role_name)
            await category.create_text_channel(name=f"🎉{party_name}",overwrites=overwrite,topic=f"{party_name} 파티의 채널입니다.")
            await member.send(f"**{discord_name}**님께서 신청해주신 파티가 승인 되었습니다.\n파티장 역할이 부여 되었으며, 파티 역할 및 채널이 생성 되었습니다. 자세한 운영은 관리자에게 문의해주시거나 **LOLJA** 명령어를 확인해주세요.")
            log.logger.info(f"C: 파티등록 S: 완료 W: {ctx.message.author.name} T: {member.name}")
    else:
        pass

@bot.command()
async def 파티가입(ctx,member:discord.Member):
    await ctx.message.delete()
    leader = ctx.message.author
    leader_id = leader.id
    if check(ctx,'leader'):
        log.logger.info(f"C: 파티가입 S: 시작 W: {leader.name}")
        try:
            party = db.get_member(member.id)
            if party[7] != None:
                return await ctx.send("해당 유저는 이미 파티가 있습니다.")
            if get(member.roles,name="인증")==None:
                return await ctx.send("해당 유저는 인증 되지 않았습니다.")
            else:
                party_name = db.get_party(leader_id)
                role = get(ctx.guild.roles,name=party_name)
                if len(role.members) > 10:
                    return await ctx.send("파티에 최대 인원은 **10명** 입니다.")
                else:
                    db.set_partymemeber(party_name,member.id)
        except Exception as ex:
            log.logger.error(f"C: 파티가입 S: 실패 R: {ex}")
            return await ctx.send("파티가입에 실패했습니다.")
        else:
            await member.add_roles(role)
            await ctx.send(f"{member.mention}님이 **{party_name}**에 가입되셨습니다.")
            log.logger.info(f"C: 파티가입 S: 완료 W: {leader.name} T: {member}")

@bot.command()
async def 파티탈퇴(ctx,member:discord.Member=None):
    await ctx.message.delete()
    leader = ctx.message.author
    leader_id = leader.id
    log.logger.info(f"C: 파티탈퇴 S: 시작 W: {leader.name}")
    try:
        party_name = db.get_party(leader_id)
        role = get(ctx.guld.roles,name=party_name)
    except Exception as ex:
        log.logger.error(f"C: 파티탈퇴 S: 실패 W: {leader.name} R: {ex}")
    else:
        if check(ctx,'leader'):
            if member == None:
                await ctx.send(f"{leader}는 파티를 탈퇴 할 수 없습니다. 필요하신 사항은 관리자에게 문의해주세요.")
                log.logger.info(f"C: 파티탈퇴 S: 실패 W: {leader.name} R: 파티장은 탈퇴 불가")
            else:
                db.del_partymember(member.id)
                await member.remove_roles(role)
                await ctx.send(f"{member.mention}님을 파티에서 추방했습니다.")
                log.logger.info(f"C: 파티탈퇴 S: 성공 W: {leader.name} R: 파티에서 {member.name} 추방")
        else:
            if member == None:
                db.del_partymember(leader_id)
                await leader.remove_roles(role)
                await ctx.send(f"{member.mention}님을 파티에서 탈퇴했습니다.")
                log.logger.info(f"C: 파티탈퇴 S: 성공 W: {leader.name} R: 파티에서 탈퇴")
            else:
                await ctx.send(f"{leader.mention}님은 권한이 없습니다.")
                log.logger.info(f"C: 파티탈퇴 S: 실패 W: {leader.name} R: 파티장이 아님")

@bot.command()
async def 파티편집(ctx,*,dec):
    await ctx.message.delete()
    leader = ctx.message.author
    log.logger.info(f"C: 파티편집 S: 시작 W: {leader}")
    if check(ctx,"leader"):
        try:
            db.set_partydec(leader.id,dec)
            
        except Exception as ex:
            log.logger.error(f"C: 파티편집 S: 실패 R: {ex}")
            await ctx.send("파티 소개글 변경을 실패하였습니다.")
        else:
            await ctx.send("파티 소개글 변경을 완료했습니다.")
            log.logger.error(f"C: 파티편집 S: 완료")
    else:
        pass


@bot.command()
async def 롤아카데미(ctx):
    await ctx.message.delete()

@bot.command()
async def 교직이수(ctx,member:discord.Member,line,*,dec):
    await ctx.message.delete()
    if check(ctx,"admin"):
        log.logger.error(f"C: 교직이수 S: 시작")
        role = get(member.roles,name="인증")
        if role != None:
            role = get(ctx.guild.roles,name="선생님")
            try:
                db.set_teacher(member.id,member.name,line,dec)
                await member.add_roles(role)
            except Exception as ex:
                log.logger.error(f"C: 교직이수 S: 실패 R: {ex}")
            else:
                print("완료")
                await member.send(f":confetti_ball: 축하합니다! 선생님이 되셨습니다.\n이제 학생을 받고 가르칠 수 있습니다. 롤자명령어를 확인해주세요.")
                log.logger.error(f"C: 교직이수 S: 완료 T: {member}")
        else:
            await ctx.author.send(f"{member}는 인증된 유저가 아닙니다.")
            log.logger.error(f"C: 교직이수 S: 실패 R: 인증된 유저가 아님")
    else:
        pass



@bot.command()
async def 선생님(ctx):
    await ctx.message.delete()
    try:
        teachers = db.get_teacher()
    except Exception as ex:
        log.logger.error(f"C: 선생님 S: 실패 R: {ex}")
    else:
        embed=discord.Embed(title= f":man_teacher: 선생님 목록", description=f"입학을 원하시는 분은 마음에 드는 선생님께 문의하세요.", color=0xf3bb76)
        for teacher in teachers:
            discord_id = teacher[0]
            _discord = ctx.guild.get_member(int(discord_id))
            line = teacher[2]
            dec = teacher[3]
            embed.add_field(name=f"{_discord} 선생님", value=f"Line. {line}\n:speech_left: {dec}", inline=False)
        embed.set_footer(text="롤 아카데미 | 2019.12.19")
        await ctx.message.author.send(embed=embed)
        log.logger.info(f"C: 선생님 S: 완료 W: {ctx.message.author}")

@bot.command()
async def 입학(ctx,member:discord.Member):
    await ctx.message.delete()
    if check(ctx,"teacher"):
        role = get(member.roles,name="인증")
        if role != None:
            teacher = ctx.message.author
            Channel = ctx.guild.get_channel(academy_Channel)
            try:
                db.set_student(member.id,teacher.id)
                member_info = db.get_member(member.id)
                tier = member_info[6]
                summoner_id = member_info[5]
                summoner_name = lol.get_summoner_name(summoner_id)
            except Exception as ex:
                log.logger.error(ex)
            else:
                role = get(ctx.guild.roles,name="학생")
                await member.add_roles(role)
                embed=discord.Embed(title= f":receipt: 입학증서",description=f"LOL Academy 입학을 환영합니다.", color=0xf3bb76)
                embed.add_field(name=":man_student: 학생이름", value=f"{member.mention}", inline=True)
                embed.add_field(name=":label: 소환사명", value=f"{summoner_name}", inline=True)
                if tier == None:
                    embed.add_field(name=":star: 티어", value=f"UNRANKED", inline=False)
                else:
                    embed.add_field(name=":star: 티어", value=f"{tier}", inline=False)
                embed.add_field(name=":man_mage: 선생님", value=f"{teacher.mention}", inline=False)
                embed.set_footer(text="LOL Academy | 개교. 2019.12.19")
                await Channel.send(embed=embed)
        else:
            await ctx.message.author.send(f"{member}는 인증되지 않았습니다.")
    else:
        pass
            

@bot.command()
async def 퇴학(ctx,member:discord.Member):
    await ctx.message.delete()
    log.logger.info(f"C: 퇴학 S: 시작 W: {ctx.message.author}")
    if check(ctx,"teacher"):
        teacher = ctx.message.author
        Channel = ctx.guild.get_channel(academy_Channel)
        teacher_id = db.find_teacher(member.id)
        print(teacher_id)
        if teacher_id == str(teacher.id):
            try:
                db.del_student(member.id)
            except Exception as ex:
                log.logger.error(ex)
            else:
                role = get(ctx.guild.roles,name="학생")
                await member.remove_roles(role)
                await Channel.send(f"{member.mention}님이 퇴학 처리되었습니다.")
                log.logger.info(f"C: 퇴학 S: 완료 W: {ctx.message.author} T: {member}")

@bot.command()
async def 졸업(ctx,member:discord.Member):
    await ctx.message.delete()
    if check(ctx,"admin"):
        teacher = ctx.message.author
        Channel = ctx.guild.get_channel(academy_Channel)
        role = get(member.roles,name="학생")
        if role != None:
            try:
                db.del_student(member.id)
                member_info = db.get_member(member.id)
                tier = member_info[6]
                summoner_id = member_info[5]
                summoner_name = lol.get_summoner_name(summoner_id)
            except Exception as ex:
                log.logger.error(ex)
            else:
                await member.remove_roles(role)
                embed=discord.Embed(title= f":military_medal:  졸업증서",description=f"LOL Academy 졸업을 축하합니다.", color=0xf3bb76)
                embed.add_field(name=":man_student: 학생이름", value=f"{member.mention}", inline=True)
                embed.add_field(name=":label: 소환사명", value=f"{summoner_name}", inline=True)
                embed.add_field(name=":star: 티어", value=f"{tier}", inline=False)
                embed.add_field(name=":man_mage: 선생님", value=f"{teacher.mention}", inline=False)
                embed.set_footer(text="LOL Academy | 개교. 2019.12.19")
                await Channel.send(embed=embed)

@bot.command()
async def 공지(ctx):
    log.logger.info(f"C: 공지 S: 시작 W: {ctx.message.author}")
    try:
        notices = db.get_notice()
        url=bot.myGuild.icon_url
        notice = notices[1]
        date = notices[2]
    except:
        log.logger.error(f"C: 공지 S: 에러 W: {ctx.message.author}")
    else:
        embed=discord.Embed(title= f":tada: LOL PARTY 공지사항", description=f"작성일: {date}", color=0xf3bb76)
        embed.set_thumbnail(url=url)
        embed.add_field(name=":pushpin: 공지사항", value=f"{notice}", inline=False)
        embed.set_footer(text=footer)
        await ctx.message.author.send(embed=embed)
        log.logger.info(f"C: 공지 S: 완료 W: {ctx.message.author}")

@bot.command()
async def 공지설정(ctx,*,notice=""):
    await ctx.message.delete() 
    if check(ctx,"admin"):
        log.logger.info(f"C: 공지설정 S: 시작 W: {ctx.message.author}")
        if notice == "":
            return await ctx.message.author.send("공지사항을 입력해주세요.")
        else:
            try:
                print(notice)
                db.set_notice(notice)
            except Exception as ex:
                log.logger.error(f"C: 공지설정 S: 에러 W: {ctx.message.author} {ex}")
            else:
                await ctx.message.author.send("공지사항 설정이 완료 되었습니다.")
                log.logger.info(f"C: 공지 S: 완료 W: {ctx.message.author}")
    else:
        pass

@bot.command()
async def 경고(ctx,member:discord.Member,*,reason):
    await ctx.message.delete()
    if check(ctx,"admin"):
        log.logger.info(f"C: 경고시작 S: 시작 W: {ctx.message.author}")
        admin = ctx.message.author
        channel=ctx.guild.get_channel(caution_Channel)
        first_caution = get(member.roles,name="1차 경고")
        if first_caution == None:
            role = get(ctx.guild.roles,name="1차 경고")
        else:
            second_caution = get(member.roles,name="2차 경고")
            if second_caution == None:
                role = get(ctx.guild.roles,name="2차 경고")
            else:
                role = get(ctx.guild.roles,name="차단")

        await member.add_roles(role)
        embed=discord.Embed(title= f":no_entry: 제재조치 : {role.name}",description=f"{member.id}", color=role.color)
        embed.add_field(name="관리자", value=f"{admin.mention}", inline=True)
        embed.add_field(name="제재자", value=f"{member.mention}", inline=True)
        embed.add_field(name="제재사유", value=f"{reason}", inline=False)
        embed.set_footer(text=footer)
        await channel.send(embed=embed)
        if role.name == "차단":
            await admin.send("해당 유저를 차단해주세요.")
        log.logger.info(f"C: 경고완료 S: 완료 W: {admin} T: {member}")

@bot.command()
async def 내전(ctx):
    await ctx.message.delete()
    log.logger.info(f"C: 내전 S: 시작 W: {ctx.message.author}")
    channel = ctx.guild.get_channel(waiting_Channel)
    text_Channel = ctx.guild.get_channel(civilwar_Channel)
    members = channel.members
    print(members)
    if len(members) == 0:
        return await ctx.send(":octagonal_sign: 내전 대기실에 인원이 없습니다.")
    category = channel.category
    teams = list()
    team = list()
    for member in members: #멤버 수 만큼 반복하여
        print(member)
        team.append(member)
        members.remove(member)
        print(team)
        print(members)
        if len(team) == 5: #팀의 멤버수가 5명이라면 팀을 저장하고 팀을 비운다.
            teams.append(team)
            team.clear()
        if len(members)==0: #만약 members의 수가 0명이라면 반복을 끝낸다.
            if len(team) > 0:
                teams.append(team)
                team.clear
            break
    embed=discord.Embed(title= f"LOL Party 내전",description=f"LOL PARTY 내전 랜덤 팀 배정", color=0xf3bb76) 
    team_num = 1 
    for team1 in teams: #팀 수 만큼 반복한다. 팀 음성 채널을 개설하고
        team_Channel = await category.create_voice_channel(name=f"🔥TEAM. {team_num}",bitrate=bot.myGuild.bitrate_limit,user_limit=5)
        member_mention = list()
        print(member_mention)
        for member in team1: #팀내 멤버수 만큼 반복한다. 멤버 멘션 값을 저장하고 멤버를 채널로 옮긴다.
            member_mention.append(member.mention)
            await member.move_to(team_Channel)
            print(f"완료:{member_mention}")
        embed.add_field(name=f"🔥TEAM. {team_num}", value=",".join(map(str,member_mention)), inline=False)
        team_num = team_num+1
    embed.set_footer(text=footer)
    await text_Channel.send(embed=embed)
    log.logger.info(f"C: 내전 S: 완료 W: {ctx.message.author}")

@bot.command()
async def 내전참가(ctx):
    await ctx.message.delete()
    log.logger.info(f"C: 내전참가 S: 시작 W: {ctx.message.author}")
    member = ctx.message.author
    role = get(ctx.guild.roles,name="내전참가자")
    await member.add_roles(role)
    await member.send(":white_check_mark: LOL PARTY 내전참가 신청이 완료되었습니다\n공지사항에 적힌 내전 시간을 꼭 확인해주세요.\n:octagonal_sign: **지각,무단 불참**은 향후 내전 참가 시 **불이익**을 받을 수도 있습니다.")
    log.logger.info(f"C: 내전참가 S: 완료 W: {ctx.message.author}")

@bot.command()
async def 내전인원(ctx):
    await ctx.message.delete()
    if check(ctx,"admin"):
        text_Channel = ctx.guild.get_channel(civilwar_Channel)
        role = get(ctx.guild.roles,name="내전참가자")
        members = role.members
        member_mention = list()
        for member in members:
            member_mention.append(member.mention)
        embed=discord.Embed(title= f"LOL Party 내전",description=f"참가자 목록입니다.", color=0xf3bb76)
        if len(members) == 0:
            embed.add_field(name=f"🔥참가자", value="참가자가 없습니다.", inline=False)
        else:
            embed.add_field(name=f"🔥참가자", value=",".join(map(str,member_mention))+" ", inline=False)
        await text_Channel.send(embed=embed)

@bot.command()
async def 내전종료(ctx):
    await ctx.message.delete()
    if check(ctx,"admin"):
        text_Channel = ctx.guild.get_channel(civilwar_Channel)
        role = get(ctx.guild.roles,name="내전참가자")
        members = role.members
        for member in members:
            await member.remove_roles(role)
        await text_Channel.send("내전 참가자를 초기화 했습니다.")


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
async def 명예의전당(ctx):
    await ctx.message.delete()
    role = get(ctx.guild.roles,name="Sparkle")
    members = role.members
    leader = get(members,id=248123112472838144) #승오
    mvp = get(members,id =338203400271560704) #경상
    member1 = get(members,id=275126185745186816) #투킬
    member2 = get(members,id=614752807639187475) #우혁
    member3 = get(members,id=244372339930693632) #잠자는숲속의준위
    embed=discord.Embed(title= f"명예의 전당 :trophy:",description=f"LOL PARTY 리그 Season3 우승팀", color=role.color)
    embed.set_image(url="https://media.discordapp.net/attachments/624997033362849827/654935380738703361/Sparkle.gif")
    embed.add_field(name=":star: 팀장", value=f"**{leader}**", inline=False)
    embed.add_field(name=":family_mmbb: 팀원", value=f"**{member1}\n{member2}\n{member3}\n{mvp}**", inline=False)
    embed.add_field(name=":medal: MVP", value=f"**{mvp}**", inline=False)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command()
async def 소환사(ctx,*,lolname):
    summoner = lol.get_summoner_info(lolname)
    if summoner == None:
        await ctx.send(f"**{lolname}** 소환사를 찾을 수 없습니다.")
    else:
        log.logger.info(f"call: {ctx.message.author} func: 소환사정보")
        summoner_level = summoner['summonerLevel']
        summoner_Icon = summoner['profileIconId']
        summoner_id = summoner['id']
        #account_id = summoner['accountId']
        leagues = lol.get_summoner_league(summoner_id)
        embed=discord.Embed(title= f"{lolname}",description=f"Lv. {summoner_level}", color=0xf3bb76)
        embed.set_thumbnail(url=f"http://ddragon.leagueoflegends.com/cdn/9.24.2/img/profileicon/{summoner_Icon}.png")
        if len(leagues) < 1:
            embed.add_field(name="**SOLO RANK**", value=f"소환사 랭크 정보가 없습니다.", inline=True)
        else:
            for league in leagues:
                if league['queueType'] == "RANKED_SOLO_5x5":
                    solo = True
                    solo_wins = league['wins']
                    solo_losses = league['losses']
                    solo_tier = league['tier']
                    solo_rank = league['rank']
                    solo_point = league['leaguePoints']
                    break
                else:
                    solo = False
            if solo:
                percent = solo_wins/(solo_wins+solo_losses)*100
                index = emblem_Index.index(solo_tier)
                embed.add_field(name="**SOLO RANK**", value=f"<:LOLPARTY:{emblem_Id[index]}> {solo_tier} {solo_rank} {solo_point} LP\n:blue_circle: **{solo_wins} :red_circle: {solo_losses} :green_circle: {int(percent)}%**" , inline=False)
            else:
                embed.add_field(name="**SOLO RANK**", value=f"정보가 없습니다.", inline=True)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

@bot.command()
async def 내정보(ctx):
    await ctx.message.delete()
    await ctx.send("해당 명령어는 `!!정보 @유저` 명령어로 변경되었습니다.")


@bot.command()
async def 정보(ctx,member:discord.Member):
    await ctx.message.delete()
    member_info = db.get_member(member.id)
    if member_info == None:
        await member.send("서버에서 인증된 유저가 아닙니다.")
    else:
        summoner_name = lol.get_summoner_name(member_info[5])
        embed=discord.Embed(title= f"{member}",description=f"서버 가입일. **{member.joined_at.year}-{member.joined_at.month}-{member.joined_at.day}**", color=0xf3bb76)
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name="서버 별명", value=f"{member.display_name}",inline=True)
        if member_info[7] == None:
            embed.add_field(name="소속된 파티", value="없음",inline=True)
        else:
            embed.add_field(name="소속된 파티", value=f"{member_info[7]}",inline=True)
        embed.add_field(name="소환사 명",value=f"{summoner_name}",inline=False)
        if member_info[6] == None:
            embed.add_field(name="랭크 정보",value=f"UNRANKED",inline=True)
        else:
            tier=member_info[6].split(" ")
            index = emblem_Index.index(tier[0])
            embed.add_field(name="랭크 정보",value=f"<:LOLPARTY:{emblem_Id[index]}> {member_info[6]}",inline=True)
        if member.id in winners:
            embed.set_image(url="https://media.discordapp.net/attachments/624997033362849827/654935380738703361/Sparkle.gif")
        embed.set_footer(text=f"{member.id}")
        await ctx.send(content="",embed=embed)

bot.run(token[1])