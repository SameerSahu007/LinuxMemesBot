from email import message
import logging
import os
import redditscraper
from telegram import InputMediaPhoto, __version__ as TG_VER
from dotenv import load_dotenv
load_dotenv()

try:

    from telegram import __version_info__

except ImportError:

    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]


if __version_info__ < (20, 0, 0, "alpha", 1):

    raise RuntimeError(

        f"This example is not compatible with your current PTB version {TG_VER}. To view the "

        f"{TG_VER} version of this example, "

        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"

    )

from telegram import ForceReply, Update

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext



# Enable logging

logging.basicConfig(

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO

)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and

# context.

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /start is issued."""

    user = update.effective_user

    await update.message.reply_html(

        rf"Hi {user.mention_html()}!",

        reply_markup=ForceReply(selective=True),

    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /help is issued."""

    await update.message.reply_text("Help!")


async def getMeme(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /help is issued."""
    link_urls = await redditscraper.scan_posts()

    medias = []
    caption = 'Caption : ' + link_urls[1]  + '\nPosted By : ' + link_urls[2] 
    medias.append(InputMediaPhoto(media=link_urls[0],caption = caption))

    await context.bot.send_media_group(chat_id='-1001766901487', media=medias )
        # await context.bot.send_document(chat_id = update.message.chat_id, document=links)

async def callback_minute(context: CallbackContext):
    
    link_urls = await redditscraper.scan_posts()

    medias = []
    caption = '✍Title : ' + link_urls[1]  + '\n🧒Posted By : ' + link_urls[2] + '\n\n👉@linuxmeme'
    medias.append(InputMediaPhoto(media=link_urls[0],caption = caption))

    await context.bot.send_media_group(chat_id='-1001478693451', media=medias )
    # await context.bot.send_message(chat_id='-1001766901487', text='One message every minute')



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Echo the user message."""
    await context.bot.send_message(chat_id=-1001766901487, text="I'm sorry Dave I'm afraid I can't do that.")


def main() -> None:
    """Start the bot."""

    # Create the Application and pass it your bot's token.

    application = Application.builder().token(os.environ.get('TELEGRAM_API')).build()

    job_queue = application.job_queue

    job_minute = job_queue.run_repeating(callback_minute, interval=86400, first=10)


    application.run_polling()


if __name__ == "__main__":
    main()
