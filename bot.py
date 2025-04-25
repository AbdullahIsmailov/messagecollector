import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# Configuration
TOKEN = 'YOUR_TELEGRAM_TOKEN'
TARGET_USER_ID = TARGET_USER_ID

# Async handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Please ask your question and it will be reviewed.')

async def set_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global TARGET_USER_ID
    if not context.args:
        await update.message.reply_text('Please specify the user ID: /setuser <user_id>')
        return
    
    try:
        TARGET_USER_ID = int(context.args[0])
        await update.message.reply_text(f'Target user set to: {TARGET_USER_ID}')
    except ValueError:
        await update.message.reply_text('Please provide a valid user ID')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not TARGET_USER_ID:
        await update.message.reply_text('Target user is not set. Use /setuser <user_id>')
        return

    try:
        if update.message.chat.type == 'private':
            await context.bot.forward_message(
                chat_id=TARGET_USER_ID,
                from_chat_id=update.effective_chat.id,
                message_id=update.message.message_id
            )
            await update.message.reply_text('Message forwarded successfully')
        else:
            await update.message.reply_text('Bot only works in private messages')
    except Exception as e:
        await update.message.reply_text(f'Error forwarding message: {str(e)}')

def main():
    # Initialize application
    application = Application.builder().token(TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('setuser', set_user_command))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))

    # Start the bot
    print('Bot is running...')
    application.run_polling()

if __name__ == '__main__':
    main()