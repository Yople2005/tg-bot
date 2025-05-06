# Deploying to PythonAnywhere

Follow these steps to deploy your Telegram bot to PythonAnywhere:

## 1. Create PythonAnywhere Account
1. Go to [PythonAnywhere](https://www.pythonanywhere.com)
2. Sign up for a free account
3. Verify your email address

## 2. Set Up Your Files
1. Go to the "Files" tab in PythonAnywhere
2. Click "Open Bash console here"
3. Clone your repository or create new files:
   ```bash
   git clone <your-repo-url>  # If using git
   # OR manually create files:
   mkdir telegram_bot
   cd telegram_bot
   ```
4. Upload these files to your directory:
   - `bot.py`
   - `requirements.txt`
   - `.env` (create this with your bot token)

## 3. Install Dependencies
1. In the Bash console:
   ```bash
   pip3 install --user python-telegram-bot python-dotenv
   pip3 install --user -r requirements.txt
   ```

## 4. Set Up Environment Variables
1. Create a `.env` file in your project directory:
   ```bash
   nano .env
   ```
2. Add your bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```
3. Save and exit (Ctrl+X, then Y, then Enter)

## 5. Configure Always-on Task
1. Go to the "Tasks" tab
2. Under "New Task", set:
   - Schedule: Always on (+$5/month)
   - Command: python3 ~/telegram_bot/bot.py
   - Working directory: ~/telegram_bot
3. Click "Create"

## 6. Start Your Bot
1. The bot will start automatically with the Always-on task
2. Monitor the task's log for any errors

## Important Notes
- Free accounts have CPU and memory limitations
- Always-on tasks require a paid account
- Keep your bot token secret
- Monitor your bot's logs regularly

## Troubleshooting
- Check the error log in the "Tasks" tab
- Ensure all dependencies are installed
- Verify your bot token is correct
- Check PythonAnywhere's system status page for any issues