from telegram import Update 
from telegram.ext import CommandHandler, MessageHandler, Application, filters

TOKEN = 'YOUR_BOT_TOKEN'
BOT_USERNAME = 'YOUR_BOT_UERNAME'

async def start_command(update: Update, context):
    await update.message.reply_text(f'Hello! Thanks for chatting with me! I am an {BOT_USERNAME}')

async def help_command(update: Update, context):
    await update.message.reply_text('I am an AxvoraBot! Please type something so I can respond!')

async def menu_command(update: Update, context):
    await update.message.reply_text('Open the menu!')

# Responses
def handle_response(text: str):
    processed: str = text.lower()
    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am good!'
    
    if 'test' in processed:
        return 'test!'
    
    return 'I do not understand what you wrote...'

async def handle_message(update: Update, context):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
        
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Bot is starting...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('menu', menu_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)