# Telegram Group Bot

A Telegram bot that can be used in group chats with the following features:
- Greeting new members when they join the group
- Generating random numbers between 10000-30000 with 1000 increments only (e.g., 10000, 11000, 12000, etc.)

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- A Telegram account
- A Telegram Bot Token (obtained from BotFather)

### Installation

1. Clone or download this repository

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Open the `bot.py` file and replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual bot token

4. Run the bot:
   ```
   python bot.py
   ```

### Creating a Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Start a chat with BotFather and send the command `/newbot`
3. Follow the instructions to create a new bot
4. Once created, BotFather will provide you with a token - copy this token
5. Use this token in the `bot.py` file

## Usage

### Adding the Bot to a Group
1. Open your Telegram group
2. Add the bot as a member
3. Make sure to give the bot admin privileges to read messages

### Available Commands
- `/start` - Start the bot
- `/help` - Show help message
- `/random` - Generate a random number between 10000-30000 with 1000 increments
- `/chit_lrr` - Show 'chit tl'
- `/e_shu` - Send a health message in Burmese
- `/benefits_of_e` - Send a message about the benefits of 'e' in Burmese

### Love Commands (Burmese)
- `/love_quote` - Get a random love quote in Burmese
- `/love_poem` - Get a love poem in Burmese
- `/love_message` - Get a sweet love message in Burmese

### Features
- The bot will automatically greet new members when they join the group
- The random number generator will only produce numbers with 1000 increments (10000, 11000, 12000, etc.)