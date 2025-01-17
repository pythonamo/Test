from pyrogram import Client
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
import time
import asyncio
import aiocron
import pytz
import random



new_york_timezone = pytz.timezone('America/New_York')
#Pyrogram connection specifications
admin = 5861650867
app = Client(
    'amo',
    api_id= "25444013",
    api_hash="bfbb5734526653271b8a106d046b5754",
    )
 #_______________________end______________________________
 
sentences = [
    "The sun rose over the quiet hills.",
    "Success comes to those who work hard.",
    "Every day is a new beginning.",
    "Books are a uniquely portable magic.",
    "Happiness is found in the little things.",
    "Dream big, work hard, stay focused.",
    "The leaves rustled in the gentle breeze.",
    "Knowledge is the key to unlocking potential.",
    "Believe in yourself, and anything is possible.",
    "A journey of a thousand miles begins with a single step.",
    "The stars lit up the night sky.",
    "Patience is a virtue worth cultivating.",
    "Failure is just a stepping stone to success.",
    "A kind word can brighten someone’s day.",
    "The ocean waves crashed against the shore.",
    "Time is the most valuable resource we have.",
    "The flowers bloomed in vibrant colors.",
    "Courage is not the absence of fear but the triumph over it.",
    "The best way to predict the future is to create it.",
    "Life is like a camera; focus on what’s important.",
    "The rain tapped softly against the window.",
    "Good friends are like stars; you don’t always see them, but they’re always there.",
    "Hard times build strong people.",
    "Nature always wears the colors of the spirit.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "The world is full of beautiful possibilities.",
    "Kindness is a language the deaf can hear and the blind can see.",
    "Great things take time; don’t rush the process.",
    "Laughter is the best medicine for the soul.",
    "The road to success is always under construction.",
    "Every sunset brings the promise of a new dawn.",
    "Gratitude turns what we have into enough.",
    "Don’t count the days; make the days count.",
    "The calm after the storm is always peaceful.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "The quiet moments are often the most profound.",
    "The beauty of life is in its imperfections.",
    "Success isn’t just about what you accomplish, but about what you inspire others to do.",
    "A smooth sea never made a skilled sailor.",
    "Your mindset can determine your future.",
    "It’s not about how fast you get there, but how you enjoy the journey.",
    "Sometimes, you need to step outside, get some air, and remind yourself of who you are.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "Never let the fear of striking out keep you from playing the game.",
    "Do what you can, with what you have, where you are.",
    "The greatest wealth is to live content with little.",
    "In the middle of difficulty lies opportunity.",
    "You are never too old to set another goal or to dream a new dream.",
    "Life isn’t about waiting for the storm to pass, but learning to dance in the rain.",
    "A person who never made a mistake never tried anything new.",
    "There is no elevator to success; you have to take the stairs.",
    "Be yourself; everyone else is already taken.",
    "Don’t wait for opportunity to knock; build your own door.",
    "The most beautiful things in life are not things. They’re people, places, and memories.",
    "The purpose of life is not to be happy, but to be useful, to be honorable, to be compassionate.",
    "Sometimes, the smallest things take up the most room in your heart.",
    "A goal without a plan is just a wish.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
    "Success is not how high you have climbed, but how you make a positive difference to the world.",
    "Don’t be afraid to give up the good to go for the great.",
    "Opportunities are like sunrises. If you wait too long, you miss them.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Do not go where the path may lead, go instead where there is no path and leave a trail.",
    "Great things never come from comfort zones.",
    "In the end, we only regret the chances we didn’t take.",
    "Live life as though nobody is watching, and express yourself as though everyone is listening.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Your time is limited, so don’t waste it living someone else’s life.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Act as if what you do makes a difference. It does.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "Believe you can and you’re halfway there.",
    "The best way to predict the future is to create it.",
    "The harder you work, the luckier you get.",
    "Life is what happens when you’re busy making other plans.",
    "It always seems impossible until it’s done.",
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
    "The secret of getting ahead is getting started.",
    "It’s never too late to be what you might have been.",
    "A river cuts through rock, not because of its power, but because of its persistence.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Nothing in the world can take the place of Persistence.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "The best revenge is massive success.",
    "What we think, we become.",
    "Don’t be afraid to fail. Be afraid not to try.",
    "Opportunities don’t happen. You create them.",
    "Do not wait to strike till the iron is hot, but make it hot by striking.",
    "Success is not measured by what you accomplish, but by the obstacles you overcome.",
    "The way to get started is to quit talking and begin doing."
]
 
 
import random

names = [
    "Vanguard", "Nexus", "Inferno", "Eclipse", "Titan", "Radiance", "Legacy", "Aether", "Zenith", "Valor",
    "Phoenix", "Rebirth", "Specter", "Nova", "Genesis", "Onyx", "Nebula", "Solace", "Maverick", "Odyssey",
    "Aurora", "Apex", "Equinox", "Prism", "Momentum", "Revolution", "Fortitude", "Ascend", "Vortex", "Summit",
    "Ember", "Courage", "Reign", "Serenity", "Horizon", "Eminence", "Synergy", "Legacy", "Eclipse", "Dominion",
    "Mirage", "Rapture", "Uprising", "Valor", "Radiance", "Crest", "Aether", "Harmonia", "Vortex", "Titan",
    "Equinox", "Pinnacle", "Destiny", "Endurance", "Vigilance", "Eminence", "Fortress", "Champion", "Phoenix",
    "Revolt", "Genesis", "Summit", "Astral", "Crusade", "Sovereign", "Odyssey", "Pursuit", "Rebirth", "Serenity",
    "Excalibur", "Resolve", "Aegis", "Infinity", "Vanguard", "Clarity", "Infinity", "Apex", "Momentum", "Reign",
    "Legion", "Storm", "Eon", "Noble", "Ascendant", "Specter", "Raven", "Griffin", "Nova", "Talon",
    "Oblivion", "Specter", "Harbinger", "Crusader", "Titan", "Alliance", "Enigma", "Sentinel", "Mystic",
    "Tempest", "Exodus", "Ember", "Resilience", "Requiem", "Sovereign", "Momentum", "Dynasty", "Pioneers",
    "Valor", "Infinity", "Celestial", "Rogue", "Knight", "Eternal", "Legacy", "Primal", "Revolution", "Luminous",
    "Fortitude", "Cinder", "Vigil", "Celestia", "Spectral", "Arise", "Omega", "Dynasty", "Pinnacle", "Excalibur",
    "Fury", "Eclipse", "Frost", "Vortex", "Solaris", "Vigil", "Courage", "Noble", "Aether", "Onyx",
    "Reign", "Griffon", "Tempest", "Uprising", "Zenith", "Phoenix", "Vanguard", "Solace", "Valor", "Specter",
    "Astral", "Rebirth", "Vigilance", "Eon", "Celestial", "Aegis", "Maverick", "Nebula", "Vortex", "Exodus",
    "Legion", "Apex", "Destiny", "Crescent", "Sovereign", "Titan", "Fury", "Revolution", "Nexus", "Solstice",
    "Eternal", "Aether", "Phoenix", "Radiance", "Legacy", "Prism", "Valor", "Odyssey", "Apex", "Zenith",
    "Onyx", "Momentum", "Crusade", "Luminous", "Eclipse", "Oblivion", "Excalibur", "Eminence", "Reign",
    "Pioneers", "Horizon", "Summit", "Sovereign", "Spectral", "Prism", "Nova", "Dynasty", "Vanguard", "Aether",
    "Valor", "Specter", "Eon", "Cinder", "Momentum", "Astral", "Zenith", "Legacy", "Rapture", "Phoenix",
    "Vigilance", "Genesis", "Uprising", "Apex", "Tempest", "Rebirth", "Radiance", "Summit", "Titan", "Griffin",
    "Noble", "Mirage", "Momentum", "Pursuit", "Dominion", "Frost", "Requiem", "Sentinel", "Specter", "Revolt",
    "Radiance", "Phoenix", "Valor", "Crusade", "Eon", "Nova", "Luminous", "Eminence", "Spectral", "Horizon",
    "Summit", "Pioneers", "Dynasty", "Maverick", "Noble", "Courage", "Eclipse", "Crusade", "Valor", "Eternal",
    "Pinnacle", "Synergy", "Legion", "Crest", "Momentum", "Summit", "Prism", "Rebirth", "Radiance", "Destiny"
]

 
 
async def file_saver(type:int,inp=None):
  if type == 1:
    with open("data.txt","w") as file:
      file.write(str(inp))
    
  if type == 0:
    with open("data.txt","r") as filer:
      readet = int(filer.read())
    return readet
 
started = False
number = 0
m=1
amo = "hi"
@app.on_message(filters.command('on') & filters.user(admin))
async def start(bot, message):
  global started
  global number
  started = True
  m =message.chat.id
  amo = await file_saver(0)
  number = await file_saver(0)
  await bot.send_message(message.chat.id,f'mess: {amo} num:{number}')
  await bot.send_message(message.chat.id, f'{m}')
  await bot.send_message(message.chat.id,'im on')

ok = "ok"


async def create_supergroup():
    global number
    number += 1
    await file_saver(1,number)
    random_name = random.choice(names)
    group_title = random_name
    group_description = random_name

    # Create the supergroup
    supergroup = await app.create_supergroup(group_title, group_description)

    # Send two messages to the created supergroup
    for i in range(31+1):
      ia = random.choice(sentences)
      await app.send_message(supergroup.id, f'{ia}')
      await asyncio.sleep(1.1)
      
    await asyncio.sleep(1.1)
    await app.send_message(-1001937227929,f'{group_title}')
# Define the job and schedule it


@aiocron.crontab('0 * * * *',new_york_timezone)
async def scheduled_job():
  if started:
    await create_supergroup()

app.run()
