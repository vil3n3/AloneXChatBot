from pyrogram import Client, filters
from pyrogram.types import Message
import langdetect
import random
import asyncio
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import pymongo

# Initialize the Pyrogram bot client
bot = Client("LisaChatBot", api_id=21846639, api_hash=2cebc99bd8378b5237b31ea8e7496d79, bot_token=6329744151:AAEohfxOdNzETzCVQxgbjRzCtcNy2CxXgwQ)

# Developer's information
developer_name = "VILLIAN"  # As per your input

# Ensure to download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Ensure to download the NLTK data
nltk.download('punkt')

# Create an instance of the sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

# Additional functionalities from the second code
async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

EMOJIOS = [ 
      "❤",
      "💖",
]

START = f"""
๏ Hie Baby❣️ ๏
"""

@bot.on_message(filters.command(["start", "aistart", f"start@{Lisa_ChatBot}"]))
async def naughty_start_command_handler(client, m):
    # Starting message from the first code
    response = f"ʜᴇʏ, ɢʟᴀᴅ ᴛᴏ ᴤᴇᴇ ʏᴏᴜ'ʀᴇ ᴈᴇᴇʟɪɴɢ ᴘᴏᴤɪᴛɪᴠᴇ ᴛᴏᴅᴀʏ! 😊 ᴋᴇᴇᴘ ᴛʜᴇ ᴘᴏᴤɪᴛɪᴠɪᴛʏ ᴈʟᴏᴡɪɴɢ!"
    await bot.send_chat_action(m.chat.id, "typing")
    await m.reply_text(response)

    # Audio message and photo from the second code
    await bot.send_chat_action(m.chat.id, "upload_audio")
    audio_file_id = "CQACAgQAAxkBAAICflK1gZOa2ox4pecDVb7XoNm5hrmVAAKcAAPxQjMS0EaNVsV5JcE"  # Replace with your audio file ID
    await bot.send_audio(m.chat.id, audio=audio_file_id, caption="ᴛʜɪᴤ ɪᴤ ᴈᴏʀ ʏᴏᴜ ʙᴀʙʏ!")

    await bot.send_chat_action(m.chat.id, "upload_photo")
    photo_file_id = "AgACAgQAAxkBAAIDgV-F6M1nx82PtqNZQJieeSAwMVKZAAIstjEbhcbiUCND-sQakqIAAaBAAMCAANzAAMlDQIAARoE"  # Replace with your photo file ID
    await bot.send_photo(m.chat.id, photo=photo_file_id, caption="ɪ ᴀᴍ ʟɪᴤᴀ ʏᴏᴜʀ ɢɪʀʟᴈʀɪᴇɴᴅ.")

    # Additional functionalities from the second code
    accha = await m.reply_text(
                text = random.choice(EMOJIOS),
    )
    await asyncio.sleep(1)
    await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠..")
    await asyncio.sleep(0.1)
    await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠...")
    await asyncio.sleep(0.1)
    await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠....")
    await asyncio.sleep(0.1)
    await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐞𝐝.✓")
    await asyncio.sleep(0.2)
    await accha.edit("𝙷ᴇʟʟᴏ ɢᴜʏs ᴛʜɪs ɪs ʟɪᴤᴀ ʏᴏᴜʀ ɢɪʀʟᴈʀɪᴇɴᴅ ꝛᴏʙᴏᴛ⛓️❤️...sᴜᴘᴘᴏʀᴛ :- @AlonesHeaven "

@bot.on_message(
    filters.command(["chatbot on", f"chatbot@{Lisa_ChatBot} on"], prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    Alonedb = pymongo.MongoClient(MONGO_URL)
    alone = Alonedb["AloneDb"]["Alone"]
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(str(chat_id))
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_alone = alone.find_one({"chat_id": message.chat.id})
    if not is_alone:
        alone.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Chatbot Enabled!")
    if is_alone:
        await message.reply_text(f"ChatBot Already Enabled")

@bot.on_message(
    filters.command(["chatbot", f"chatbot@{Lisa_ChatBot}"], prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"ᴜsᴀɢᴇ:\n/chatbot [on/off]\nᴄʜᴀᴛ-ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ(s) ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!")

@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def aloneai(client, message):
    chatdb = pymongo.MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        words = word_tokenize(message.text)
        naughty_words = ["bad", "naughty", "rude", "offensive"]  # Replace with your custom list of naughty words
        if any(word.lower() in naughty_words for word in words):
            response = "Be nice! Let's keep the conversation friendly. 😊"
            await message.reply_text(response)

    if message.reply_to_message:
        # You should define the 'alone' collection here
        alone = chatai["Alone"]  # Or whichever collection you're fetching data from
        is_alone = alone.find_one({"chat_id": message.chat.id})
        
        getme = await bot.get_me()
        bot_id = getme.id

        if message.reply_to_message.from_user.id == bot_id:
            response = "I'm here to bring charm and joy to the conversation!"
            await message.reply_text(response)
        else:
            response = "Let's keep the conversation lively and engaging! 💬"
            await message.reply_text(response)

@bot.on_message(
    (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def alonestickerai(client: Client, message: Message):
    chatdb = pymongo.MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        words = message.text.split()
        supportive_words = ["awesome", "great", "cool", "impressive"]  # Add more supportive words as needed
        if any(word.lower() in supportive_words for word in words):
            response = "Happiness is contagious! 🌟 Thanks for spreading the positivity. 😊"
            await message.reply_text(response)

    if message.reply_to_message:
        # Custom logic for handling replies
        # Example: Handling replies to specific types of messages or extracting information from the replied message
        response = "Let's keep the conversations positive and encouraging! 🌈✨"
        # Add desired logic for handling replies
        await message.reply_text(response)

@bot.on_message(filters.private & ~filters.bot)
async def handle_private_messages(client, message):
    if not message.reply_to_message:
        await bot.send_chat_action(message.chat.id, "typing")
        user_name = message.from_user.first_name if message.from_user.first_name else "there"
        response = f"Hey {user_name}! I'm Lisa, {developer_name}'s masterpiece. Chat with me to experience the magic of love and fun."
        await message.reply_text(response)
    else:
        await bot.send_chat_action(message.chat.id, "typing")
        user_name = message.from_user.first_name if message.from_user.first_name else "there"
        response = f"Hey {user_name}, I'm here to spread love! Let's enjoy some lovely moments together."
        await message.reply_text(response)
        
        # Language detection
        user_input_language = langdetect.detect(message.text)

        if user_input_language == 'en':  # English language
            # Check for specific words and provide custom responses in English
            if "love" in message.text.lower():
                love_responses = ["Love is in the air! 💕", "Love makes the world go round. Let's spread love!", "In the mood for love? Let's chat and have a lovely time together."]
                random_love_response = random.choice(love_responses)
                await bot.send_chat_action(message.chat.id, "typing")
                await message.reply_text(random_love_response)
            
            if "18+" in message.text.lower():
                adult_response = "I'm here to keep the chat friendly and fun! Let's stick to entertaining and light-hearted topics. 😊"
                await bot.send_chat_action(message.chat.id, "typing")
                await message.reply_text(adult_response)

        elif user_input_language == 'hi':  # Hindi language
            # Provide responses in Hindi
            response_in_hindi = "आपकी भाषा समझ ली गई है। आपके साथ बातचीत का आनंद लें!"
            await bot.send_chat_action(message.chat.id, "typing")
            await message.reply_text(response_in_hindi)

# Run the bot
bot.run()

