# Import required libraries
import os
from telegram import Update  # For handling Telegram updates
from telegram.ext import (
    Application,  # Main application class for the bot
    CommandHandler,  # Handler for command messages (e.g., /start)
    MessageHandler,  # Handler for regular text messages
    filters,  # For filtering different types of messages
    ContextTypes,  # For context in handlers
)

# Configuration section - replace these with your actual values
TOKEN = 'YOUR_TELEGRAM_TOKEN'  # Your bot's API token from BotFather
TARGET_USER_ID = TARGET_USER_ID  # The user ID where messages will be forwarded

# Async handler for the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the /start command is issued."""
    await update.message.reply_text('Please ask your question and it will be reviewed.')

# Async handler for the /setuser command
async def set_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Set the target user ID where messages will be forwarded."""
    global TARGET_USER_ID  # Access the global variable
    
    # Check if user provided an argument
    if not context.args:
        await update.message.reply_text('Please specify the user ID: /setuser <user_id>')
        return
    
    try:
        # Try to convert the argument to an integer (user IDs are numbers)
        TARGET_USER_ID = int(context.args[0])
        await update.message.reply_text(f'Target user set to: {TARGET_USER_ID}')
    except ValueError:
        # Handle case where argument isn't a valid number
        await update.message.reply_text('Please provide a valid user ID')

# Async handler for regular messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all non-command messages and forward them to the target user."""
    # Check if target user is set
    if not TARGET_USER_ID:
        await update.message.reply_text('Target user is not set. Use /setuser <user_id>')
        return

    try:
        # Only forward messages from private chats (not groups/channels)
        if update.message.chat.type == 'private':
            # Forward the message to the target user
            await context.bot.forward_message(
                chat_id=TARGET_USER_ID,
                from_chat_id=update.effective_chat.id,
                message_id=update.message.message_id
            )
            # Confirm to the sender that message was forwarded
            await update.message.reply_text('Message forwarded successfully')
        else:
            # Respond if message comes from a group/channel
            await update.message.reply_text('Bot only works in private messages')
    except Exception as e:
        # Handle any errors that occur during forwarding
        await update.message.reply_text(f'Error forwarding message: {str(e)}')

def main():
    """Main function to set up and run the bot."""
    # Initialize the Telegram bot application with your token
    application = Application.builder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler('start', start_command))  # /start
    application.add_handler(CommandHandler('setuser', set_user_command))  # /setuser
    
    # Register message handler for all non-command messages
    # filters.ALL means all message types, ~filters.COMMAND excludes commands
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))

    # Start the bot
    print('Bot is running...')
    application.run_polling()  # Continuously check for new updates

if __name__ == '__main__':
    # Only run the bot if this script is executed directly (not imported)
    main()
