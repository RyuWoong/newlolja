import asyncio,discord,os,random,threading,log,lol,myfunction,db,sys
from discord.ext import commands
from discord.utils import get

## Set Bot
token = myfunction.GET_KEY("token.txt")
game = discord.Game("!!도움말 ver.OpenBeta")
bot = commands.Bot(command_prefix='-',status=discord.Status.online,activity=game)

## Default Value ##
apptitle = "LoLJa"
footer = f"{apptitle} ver.Beta | ⓒ 2019 깜뭉이"
bot.STATUS_START = False
bot.myGuild = None
myVoiceChannels = [654500798281023493, 654493633608810527,654493745554784276, 654493812860780544]
normal_Channel = 654337874207965184
chess_Channel = 654337910979559426
rank_Channel = 654507949774995459

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
    streamer = get(member.roles,name="스트리머")
    check = False
    if streamer != None:
        check = True
    return check

def check_auth(ctx):
    member = ctx.message.author
    auth = get(member.roles,name="인증")
    check = False
    if auth != None:
        check = True
    return check

## Start Bot ##
@bot.event
async def on_ready():
    #os.system('cls')
    os.system('clear')
    bot.myGuild = bot.get_guild(316770615644389376)
    #myVoiceChannels = bot.myGuild.voice_channels
    print("       @ Discord Bot LOLJA")
    print("       @ MADE BY. 깜뭉이")
    print("       @ Copyright 깜뭉이. 2019")
    print("       @ Start!")
    print("       GUILD -")
    bot.STATUS_START = True

## Discord error ##
@bot.listen('on_command_error')
async def on_command_error(ctx,ex):
    log.logger.error(f"!!!!!!!!!!Discord Error :: {ex}")

## Discord Event##
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
                if now_channel.id == 654500798281023493 :
                    log.logger.info(f"C : {member} F : StartGame Normal Game")
                    category = now_channel.category
                    overwrite = {
                        member : discord.PermissionOverwrite(manage_channels=True)
                    }
                    new_channel = await category.create_voice_channel(name="일반게임 - 미정",overwrites=overwrite,bitrate=bot.myGuild.bitrate_limit,user_limit=5)
                    invite = await new_channel.create_invite(max_age=360)
                    channel = bot.myGuild.get_channel(normal_Channel)
                    await member.move_to(new_channel)
                    await channel.send(f"{member.mention}\n{invite.url} ```일반 게임방이 생성 되었습니다.\n초대코드를 사용하여 유저를 모아보세요!```")

                elif now_channel.id == 654493633608810527 :
                    log.logger.info(f"C : {member} F : StartGame LOLChess")
                    category = now_channel.category
                    overwrite = {
                        member : discord.PermissionOverwrite(manage_channels=True)
                    }
                    new_channel = await category.create_voice_channel(name="롤토체스 - 미정",overwrites=overwrite,bitrate=bot.myGuild.bitrate_limit,user_limit=8)
                    invite = await new_channel.create_invite(max_age=360)
                    channel = bot.myGuild.get_channel(chess_Channel)
                    await member.move_to(new_channel)
                    await channel.send(f"{member.mention}\n{invite.url} ```롤토체스 방이 생성 되었습니다.\n초대코드를 사용하여 유저를 모아보세요!```")

                elif now_channel.id == 654493745554784276 :
                    log.logger.info(f"C : {member} F : StartGame Duo Rank")
                    category = now_channel.category
                    overwrite = {
                        member : discord.PermissionOverwrite(manage_channels=True)
                    }
                    new_channel = await category.create_voice_channel(name="듀오랭크 - 미정",overwrites=overwrite,bitrate=bot.myGuild.bitrate_limit,user_limit=2)
                    invite = await new_channel.create_invite(max_age=360)
                    channel = bot.myGuild.get_channel(rank_Channel)
                    await member.move_to(new_channel)
                    await channel.send(f"{member.mention}\n{invite.url} ```듀오 랭크방이 생성 되었습니다.\n초대코드를 사용하여 유저를 모아보세요!```")

                elif now_channel.id == 654493812860780544  :
                    log.logger.info(f"C : {member} F : StartGame Free Rank")
                    category = now_channel.category
                    overwrite = {
                        member : discord.PermissionOverwrite(manage_channels=True)
                    }
                    new_channel = await category.create_voice_channel(name="자유랭크 - 미정",overwrites=overwrite,bitrate=bot.myGuild.bitrate_limit,user_limit=5)
                    invite = await new_channel.create_invite(max_age=360)
                    channel = bot.myGuild.get_channel(rank_Channel)
                    await member.move_to(new_channel)
                    await channel.send(f"{member.mention}\n{invite.url} ```자유 랭크방이 생성 되었습니다.\n초대코드를 사용하여 유저를 모아보세요!```")
            else:
                pass



## Discord Command ##
@bot.command()
async def 도움말(ctx,detail=None):
    await ctx.message.delete()
    url=bot.myGuild.icon_url
    log.logger.info(f"call: {ctx.message.author} func: 도움")
    embed=discord.Embed(title= f"{apptitle} 사용서" if detail==None else f"{apptitle} {detail} 사용서" , description=f"명령어 내 값은 띄어쓰기로 구분, @은 호출", color=0xf3bb76)
    embed.set_thumbnail(url=url)
    if (detail == "팀"):
        embed.add_field(name="!!파티가입 '@유저'", value="파티장) 해당 유저를 본인 파티 소속으로 추가합니다.", inline=False)
        embed.add_field(name="!!파티탈퇴", value="파티에서 탈퇴합니다. 파티장인 경우 관리자에게 문의해주세요.", inline=False)
        embed.add_field(name="!!파티탈퇴 '@유저'", value="파티장) 파티에서 추방합니다. ", inline=False)
        embed.add_field(name="!!파티정보 '팀명'", value="해당 파티정보와 파티원들을 소개합니다.", inline=False)
        #embed.add_field(name="!!파티소개 '소개글'", value="파티장 -> 파티정보에 보여질 소개글을 작성합니다. (100자 이내)", inline=False)
    elif (detail == "관리자"):
        embed.add_field(name="!!파티생성 '@팀명' '@유저'", value="파티를 생성하며, 파티장을 선정합니다.\n사전에 해당 팀의 역할 추가 및 역할멘션을 허용해주세요.", inline=False)
        embed.add_field(name="!!경기등록 '@팀명' '@팀명' '설명'", value="경기일정을 추가합니다. 설정된 경기는 리그일정으로 볼 수 있습니다.", inline=False)
        embed.add_field(name="!!경기결과 '매치업번호' '@팀명'", value="경기 결과 등록 및 승점 반영. 승자를 입력해주시고,무승부라면 @팀명에 무승부를 입력.", inline=False)
    elif (detail == "인증"):
        embed.add_field(name="!!인증시작 '소환사명'", value="서버내 디스코드와 소환사를 연결하기 위한 절차 Step.1", inline=False)
        embed.add_field(name="!!인증완료", value="서버내 디스코드와 소환사를 연결하기 위한 절차 Step.2", inline=False)
    elif (detail == "일반"):
        embed.add_field(name="!!주사위", value="1~100까지의 값 중 하나를 표시합니다.", inline=False)
        embed.add_field(name="!!뽑기 '최대 값(숫자)'", value="1~최대 값까지 숫자 하나를 표시합니다.", inline=False)
        embed.add_field(name="!!스트리머", value="해당 서버에 소속된 스트리머를 표시합니다.", inline=False)
        embed.add_field(name="!!소환사 '소환사명'", value="해당 소환사의 정보를 표시합니다.", inline=False)
        embed.add_field(name="!!도움말 '파티' 또는 '인증'", value="다른 주제의 명령어 도움말을 표시합니다.", inline=False)
    else:
        #embed.add_field(name="!!공지", value="해당 서버 공지사항을 알려줍니다.", inline=False)
        embed.add_field(name="!!도움말 일반", value="일반 및 유틸 명령어을 보여줍니다.", inline=False)
        embed.add_field(name="!!도움말 팀", value="팀과 관련된 명령어를 보여줍니다.", inline=False)
        embed.add_field(name="!!도움말 인증", value="인증과 관련된 명령어를 보여줍니다.", inline=False)
    embed.set_footer(text=footer)
    await ctx.author.send(embed=embed)

@bot.command()
async def 인증시작(ctx,*,summoner):
    log.logger.info(f"C: 인증시작 S: 시작 W:{ctx.author.name}") #시작
    member = ctx.message.author #info 
    discord_id = member.id
    discord_name = member.name
    if check_auth(ctx): #소환사 계정 변경 방지. 이미 인증되어 있다면 못하게 제한합니다.
        log.logger.info(f"C: 인증시작 S:실패 R: 이미 인증된 유저")
        return await ctx.send(f"{member.mention}님은 이미 인증이 되어있습니다.\n 만약 연동된 소환사 변경을 원하신다면 **깜뭉이**에게 문의해주세요.")
    try:
        summoner_id = lol.get_summoner_id(summoner) # 소환사 명을 통해 소환사ID 키 값을 가져옵니다.
        if summoner_id == None: # 잘못된 소환사 명을 입력 했을 경우 인증 실패로 반환합니다.
            raise Exception
        db.set_member(discord_id,discord_name,summoner_id) # DB에 디스코드id , 디스코드 별명, 소환사 아이디를 기록합니다.
        role = get(ctx.guild.roles, name="대기") #대기 역할 가져오기
    except Exception as ex:
        log.logger.error(f"C: 인증시작 S:실패 R: {ex}")
        return await member.send (f"{member.mention}님 인증이 실패하였습니다. \n**소환사 명**을 확인해주세요. 반복될 시 **관리자**에게 문의해주세요.")
    else:
        await member.add_roles(role) # 대기 라는 역할을 부여하여 유저에게 인증 시작 단계임을 표시합니다.
        await member.send(f"**LOL PARTY 서버 인증을 시작합니다.**\n 본인 명의 계정으로 인증해주세요. 본인 명의 계정이 아닐 시 향후 이벤트 참가에서 불이익이 생길 수도 있습니다. ```cs\n인증코드 : {discord_id}```\n https://i.imgur.com/XQFFBm1.png")
        await ctx.send (f"**{discord_name}님** 인증을 시작합니다. 개인메세지를 확인해주세요.")
        log.logger.info(f"C: 인증시작 S: 완료 W:{ctx.author.name}")

@bot.command()
async def 인증완료(ctx):
    log.logger.info(f"C: 인증확인 S: 시작 W: {ctx.author.name}") #시작
    member = ctx.message.author #info
    discord_id = member.id
    wait = get(member.roles,name="대기")
    if wait == None: # 인증 시작 하였는지 확인
        return await ctx.send(f"**{member.mention}님** 인증시작을 먼저 입력해주세요.\n자세한 사항은 도움말을 확인해주세요.")
    try:
        member_info = db.get_member(discord_id)
        summoner_id = member_info[5]
        auth = lol.get_auth_value(summoner_id) #소환사id로 인증 값 불러오기
        auth_role = get(ctx.guild.roles,name="인증") #인증 역할 가져오기
    except Exception as ex:
        log.logger.error(f"C: 멤버인증 S: 실패 R: {ex}")
        return await ctx.send(f"멤버인증을 실패하였습니다. 에러 X( ")
    else:
        if str(discord_id) == auth:
            await member.remove_roles(wait)
            await member.add_roles(auth_role)
            db.renew(discord_id)
            await ctx.send(f"{member.mention} 인증되었습니다.```파티를 생성하거나 가입해보세요!\n파티생성은 이용방법 채널에서 확인 할 수 있습니다.\n파티가입은 파티모집 채널에서 구할 수 있습니다.```")
            log.logger.info(f"C: 멤버인증 S: 완료 W: {member.name}")
        else:
            await ctx.send(f"**{member.mention}님** 인증에 실패하였습니다.")
            log.logger.info(f"C: 멤버인증결과 S: 실패 W: {member.name} ID: {discord_id} KEY : {auth}")

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
        log.logger.info(f"C: 파티등록 S: 시작 W: {ctx.message.author.name}")
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
            log.logger.info(f"C: 파티등록 S: 완료 W: {ctx.message.author.name} T: {discord}")
    else:
        pass

@bot.command()
async def 파티가입(ctx,member:discord.Member):
    await ctx.message.delete()
    leader = ctx.message.author
    leader_id = leader.id
    if check_leader(ctx):
        log.logger.info(f"C: 파티가입 S: 시작 W: {leader.name}")
        try:
            party_name = db.get_party(leader_id)
            role = get(ctx.guild.roles,name=party_name)
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
        if check_leader(ctx):
            if member == None:
                await ctx.send(f"{leader}는 파티를 탈퇴 할 수 없습니다. 필요하신 사항은 관리자에게 문의해주세요.")
                log.logger.info(f"C: 파티탈퇴 S: 실패 W: {leader.name} R: 파티장은 탈퇴 불가")
            else:
                await member.remove_roles(role)
                await ctx.send(f"{member.mention}님을 파티에서 추방했습니다.")
                log.logger.info(f"C: 파티탈퇴 S: 성공 W: {leader.name} R: 파티에서 {member.name} 추방")
        else:
            if member == None:
                await leader.remove_roles(role)
                await ctx.send(f"{member.mention}님을 파티에서 탈퇴했습니다.")
                log.logger.info(f"C: 파티탈퇴 S: 성공 W: {leader.name} R: 파티에서 탈퇴")
            else:
                await ctx.send(f"{leader.mention}님은 권한이 없습니다.")
                log.logger.info(f"C: 파티탈퇴 S: 실패 W: {leader.name} R: 파티장이 아님")



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
    summoner_id = lol.get_summoner_id(lolname)
    if summoner_id == None:
        await ctx.send(f"**{lolname}**은 찾을 수 없는 소환사 입니다.")
    else:
        solo_tier,solo_rank = lol.get_summoner_tear(summoner_id)
        log.logger.info(f"call: {ctx.message.author} func: 소환사정보")
        if solo_rank == None:
            await ctx.send(f"**{lolname}**의 랭크 정보가 없습니다.")
        else:
            await ctx.send(f"**{lolname}**의 티어는 **{solo_tier} {solo_rank}** 입니다.")

bot.run(token[0])