import os
import logging
import random
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get token from environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am a group bot. Add me to a group to see my features!')

async def e_shu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a health message in Burmese when the command /e_shu is issued."""
    await update.message.reply_text('အီးရှူလျှင်ကျန်းမာရေးကောင်းသည်')

async def benefits_of_e(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message about the benefits of 'e' in Burmese when the command /benefits_of_e is issued."""
    await update.message.reply_text('အီးပေါက်တဲ့ဖင်ကျေးဇူးရှင် အီးရှူတဲ့နှာခေါင်းကျန်းမာရေးကောင်း')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/random - Generate a random number between 10000-30000 with 1000 increments\n"
        "/chit_lrr - Show 'chit tl'\n"
        "/e_shu - Send a health message in Burmese\n"
        "/benefits_of_e - Send a message about the benefits of 'e' in Burmese\n"
        "\nLove Commands (Burmese):\n"
        "/love_quote - Get a random love quote in Burmese\n"
        "/love_poem - Get a love poem in Burmese\n"
        "/love_message - Get a sweet love message in Burmese"
    )
    await update.message.reply_text(help_text)

async def random_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Generate a random number between 10000-30000 with 1000 increments."""
    # Generate numbers from 10000 to 30000 with 1000 increments
    possible_numbers = list(range(10000, 31000, 1000))
    random_num = random.choice(possible_numbers)
    await update.message.reply_text(f'Random number: {random_num}')

async def chit_lrr(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send 'chit tl' message when the command /chit_lrr is issued."""
    await update.message.reply_text('chit tl')

async def love_quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random love quote in Burmese."""
    quotes = [
        "ချစ်ခြင်းမေတ္တာသည် အရာအားလုံးကို အောင်မြင်စေသည်။",  # Love conquers all
        "နှလုံးသားကို နားထောင်ပါ?",  # Listen to your heart, it knows
        "ချစ်ခြင်းမေတ္တာသည် အချိန်နှင့်အမျှ ကြီးထွားလာသည်။",  # Love grows with time
        "ချစ်သူအတွက် ကျွန်ုပ်၏နှလုံးသားသည် အမြဲတမ်း ခုန်နေမည်။",  # My heart will always beat for you
        "သင့်အပေါ် ကျွန်ုပ်၏ချစ်ခြင်းမေတ္တာသည် ကြယ်များကဲ့သို့ အဆုံးမရှိပါ။"  # My love for you is endless like the stars
    ]
    await update.message.reply_text(random.choice(quotes))

async def love_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a love poem in Burmese."""
    poems = [
        "သင့်မျက်လုံးများသည်\nကြယ်များကဲ့သို့ တောက်ပသည်\nသင့်အပြုံးသည်\nကျွန်ုပ်၏နေ့ရက်များကို လင်းစေသည်",  # Your eyes shine like stars, your smile brightens my days
        "ချစ်ခြင်းမေတ္တာသည်\nနက်ရှိုင်းသောပင်လယ်ကဲ့သို့\nအဆုံးမရှိ\nအတိုင်းအတာမရှိ",  # Love is like a deep ocean, endless and immeasurable
        "သင့်ကို တွေ့သောအခါ\nကျွန်ုပ်၏နှလုံးသားသည် ခုန်သည်\nသင့်အသံကို ကြားသောအခါ\nကျွန်ုပ်၏ဝိညာဉ်သည် ပျော်ရွှင်သည်"  # When I see you my heart jumps, when I hear your voice my soul rejoices
    ]
    await update.message.reply_text(random.choice(poems))

async def love_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a sweet love message in Burmese."""
    messages = [
        "သင်သည် ကျွန်ုပ်၏အကောင်းဆုံး အိပ်မက်ဖြစ်သည်။",  # You are my best dream
        "သင့်ကို တွေ့ရသည့်အတွက် ကျွန်ုပ် ကံကောင်းပါသည်။",  # I am lucky to have met you
        "သင့်မရှိဘဲ ဘဝကို မတွေးတတ်ပါ။",  # I can't imagine life without you
        "သင်သည် ကျွန်ုပ်၏နှလုံးသား၏ ပိုင်ရှင်ဖြစ်သည်။",  # You are the owner of my heart
        "သင့်ကို အမြဲတမ်း ချစ်နေမည်။"  # I will always love you
    ]
    await update.message.reply_text(random.choice(messages))

async def greet_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Greets new members when they join the group."""
    # In v20+, new chat members are accessed differently
    new_user = update.effective_user
    chat = update.effective_chat
    
    # Don't greet the bot itself
    if new_user.id == context.bot.id:
        return
    
    greeting_message = f"Welcome to the group, {new_user.first_name}! 👋"
    await context.bot.send_message(chat_id=chat.id, text=greeting_message)

async def set_commands(application: Application) -> None:
    """Set bot commands to enable suggestion feature when typing /."""
    commands = [
        ("start", "Start the bot"),
        ("help", "Show help message"),
        ("random", "Generate a random number between 10000-30000 with 1000 increments"),
        ("chit_lrr", "Show 'chit tl'"),
        ("e_shu", "Send a health message in Burmese"),
        ("benefits_of_e", "Send a message about the benefits of 'e' in Burmese"),
        ("love_quote", "Get a random love quote in Burmese"),
        ("love_poem", "Get a love poem in Burmese"),
        ("love_message", "Get a sweet love message in Burmese")
    ]
    
    from telegram import BotCommand
    await application.bot.set_my_commands([BotCommand(command, description) for command, description in commands])
    logger.info("Bot commands have been set successfully")

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("random", random_number))
    application.add_handler(CommandHandler("chit_lrr", chit_lrr))
    application.add_handler(CommandHandler("e_shu", e_shu))
    application.add_handler(CommandHandler("benefits_of_e", benefits_of_e))
    application.add_handler(CommandHandler("love_quote", love_quote))
    application.add_handler(CommandHandler("love_poem", love_poem))
    application.add_handler(CommandHandler("love_message", love_message))
    
    # Add handler for new members
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, greet_new_member))
    
    # Set commands for suggestion feature
    application.post_init = set_commands

    # Start the Bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()