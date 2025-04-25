# Message Collector Bot

A Telegram bot that facilitates question and answer interactions through message forwarding. This bot allows users to send messages that are automatically forwarded to a designated admin user.

## Features
- Forward messages to a designated admin user
- Private chat support
- Simple command interface
- Secure message handling
- Easy configuration

## Requirements
- Python 3.7 or higher
- python-telegram-bot library

## Setup and Configuration

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure the bot:
   - Get your bot token from [@BotFather](https://t.me/botfather)
   - Set the token in `bot.py`
   - Note your admin's Telegram user ID (you can get this by messaging [@userinfobot](https://t.me/userinfobot))

3. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

### For Admins
1. Start a private chat with the bot
2. Use `/setuser <user_id>` to configure the admin user ID
3. You will now receive all forwarded messages from users

### For Users
1. Start a chat with the bot using `/start`
2. Send your messages
3. The bot will forward your messages to the admin


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support:
- Open an issue in the GitHub repository
- Contact the maintainers through GitHub