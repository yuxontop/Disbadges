import discum, time 
import colorama, os

colorama.init()
os.system('cls')

token = ""

header = colorama.Fore.BLUE+'''

                ▓█████▄  ██▓  ██████  ▄▄▄▄    ▄▄▄      ▓█████▄   ▄████ ▓█████ 
                ▒██▀ ██▌▓██▒▒██    ▒ ▓█████▄ ▒████▄    ▒██▀ ██▌ ██▒ ▀█▒▓█   ▀ 
                ░██   █▌▒██▒░ ▓██▄   ▒██▒ ▄██▒██  ▀█▄  ░██   █▌▒██░▄▄▄░▒███   
                ░▓█▄   ▌░██░  ▒   ██▒▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌░▓█  ██▓▒▓█  ▄ 
                ░▒████▓ ░██░▒██████▒▒░▓█  ▀█▓ ▓█   ▓██▒░▒████▓ ░▒▓███▀▒░▒████▒
                ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒  ░▒   ▒ ░░ ▒░ ░
                ░ ▒  ▒  ▒ ░░ ░▒  ░ ░▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒   ░   ░  ░ ░  ░
                ░ ░  ░  ▒ ░░  ░  ░   ░    ░   ░   ▒    ░ ░  ░ ░ ░   ░    ░   
                ░     ░        ░   ░            ░  ░   ░          ░    ░  ░
                ░                         ░            ░                     



'''
print(str(header))

gid = str(input(colorama.Fore.YELLOW+'\n       [>] Guild ID : '))
cid = str(input(colorama.Fore.YELLOW+'\n       [>] Random Public Channel ID : '))

bot = discum.Client(token=str(token), log=False)

bot.gateway.fetchMembers(gid, cid, keep=['username','public_flags','discriminator','premium_since'], startIndex=0, method='overlap', wait=1)
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(gid):
        lenmembersfetched = len(bot.gateway.session.guild(gid).members)
        print(colorama.Fore.GREEN+f'\n       (+) Found {lenmembersfetched} Members... \n\n')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

print(colorama.Fore.YELLOW+'\n       (~) Fetching Members...')
bot.gateway.run()


def get_badges(flags):

    badges_ = {
        1 << 0:  'Discord Employee',
        1 << 1:  'Partnered Server Owner',
        1 << 2:  'HypeSquad Events',
        1 << 3:  'Bug Hunter Level 1',
        1 << 9:  'Early Supporter',
        1 << 10: 'Team User',
        1 << 12: 'System',
        1 << 14: 'Bug Hunter Level 2',
        1 << 16: 'Verified Bot',
        1 << 17: 'Early Verified Bot Developer',
        1 << 18: 'Discord Certified Moderator'
    }

    badges = []

    for badge_flag, badge_name in badges_.items():
        if flags & badge_flag == badge_flag:
            badges.append(badge_name)

    return badges

with open('result.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(gid).members:
        id = str(memberID)
        temp = bot.gateway.session.guild(gid).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(gid).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(gid).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            l = get_badges(temp)
            if len(l) != 0:
                badges = ', '.join(l)
                file.write(f'ID: <@{id}> | Username: {username} | Badges: {badges} | Account Created: {creation_date}\n')
                print(colorama.Fore.GREEN+f'      (+) {username} [{id}] Has : {badges}...')
    print(colorama.Fore.GREEN+'\n\n     (+) Result Writed In result.txt !')