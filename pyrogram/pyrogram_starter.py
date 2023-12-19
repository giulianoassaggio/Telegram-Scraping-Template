from pyrogram import Client
from dotenv import load_dotenv
import os

# Constants for chat IDs
CHAT_ID_SCRAPE1     = -100123456789
"""
chat IDs of the chats you want to scrape messages from.
You can add as many IDs as you want
"""
CHAT_ID_SEND1       = -100987654321
"""
chat IDs of the chats you want to send result files to.
You can add as many IDs as you want
"""

# configure pyrogram
load_dotenv()
CONFIG = {
    "telegram_api_id": int(os.getenv("TG_API_ID")),
    "telegram_hash": os.getenv("TG_API_HASH"),
}
app = Client("my_account",CONFIG["telegram_api_id"],CONFIG["telegram_hash"])

async def scraping(chat_id):
    """
    An asynchronous function to export all messages of a channel to a file called MessagesFromChat{chat_id}.txt.

    Args:
        chat_id (int): Unique ID of the chat you want to export messages from.
    """
    
    f = open(f"MessagesFromChat{chat_id}.txt", "w") # creates files related to chat id

    async with app:

        i = 1   # message counter
        async for message in app.get_chat_history(chat_id):

            try:

                if message.text is not None:    # messages that are plain text
                    text_to_be_written = "{\n" + f"Message no. {i} \n" + message.text + "\n}\n\n\n"
                elif message.caption is not None:   # media (copies caption)
                    text_to_be_written = "{\n" + f"Message no. {i} \n" + message.caption + "\n}\n\n\n"
                else:   # other types
                    text_to_be_written = "{\n" + f"Message no. {i} \n" + "message neither text nor media" + "\n}\n\n\n"

            except Exception as argument:   # logging exceptions

                text_to_be_written = "\n\n\n{\n" + f"Exception occurred for message no. {i} \n" + str(argument) + "\n}"
            
            finally:
            
                f.write(text_to_be_written)
                i += 1
    
    f.close()

async def send_results(chat_id, chat_file):
    """
    An asynchronous function to send the file called MessagesFromChat{chat_file}.txt to chat_id.

    Args:
        chat_file (int): Unique ID of the chat you have exported messages from.
        chat_id (int): Unique ID of the chat you want to send the document to.
    """
    async with app:
        if os.path.isfile(f"MessagesFromChat{chat_file}.txt"): # check if file exists
            await app.send_document(chat_id, f"MessagesFromChat{chat_file}.txt")
        else:
            await app.send_message(chat_id, f"file for chat {chat_file} doesn't exist")

# Run the scraping and sending functions
app.run(scraping(CHAT_ID_SCRAPE1))
app.run(send_results(CHAT_ID_SEND1, CHAT_ID_SCRAPE1))

