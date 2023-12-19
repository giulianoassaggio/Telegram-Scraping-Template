# Telegram Scraper

**This is a simple example of a program that extracts all (textual in this case) messages from a telegram channel and send them as a file to a specified chat.**

***
## Functions:
* ***scraping(chat_id)***: given the channel univoque ID (int type, starting with `-100`), it saves all the messages in a file named `MessagesFromChat{chat_id}.txt`.
* ***send_results(chat_id, chat_file)***: it sends to `chat_id` the file containing the messages from the chat `chat_file`. Both arguments are univoque IDs (int type). In case of groups and channel ID starts with `-100`, in case of private chats, ID starts with `-`. It must be used after the use of `scraping()` function for the relative chat.

***
## Packages, dependencies and preliminary actions

### Telegram API keys
In order to be able to run this script, the prerequisite is having a telegram account and a API setup. [Click Here](https://core.telegram.org/api/obtaining_api_id) to obtain your unique API keys, if you don't have them yet. Store `App api_id` and `App api_hash` in a safe place as you will be needing them further.

### .env
Once you have your API keys, you have to create a new folder called `pyrogram` and within that folder you have to create a `.env` file to save your API keys. File must have this template:
```
TG_API_ID="Your api id" 
TG_API_HASH="Your api hash"
```

Now your folder should look like this:
```
.
└── pyrogram
    └── .env
```

### Packages
You will need to install a few packages. Copy and paste this lines on your command prompt:
```
pip install os-sys 
pip install pyrogram 
pip install python-dotenv
pip install tgcrypto
```

### Cloning python file
Once everything is done, you can copy the python script of this repository into your pyrogram directory.
***
## Script

### chat IDs
You can get chat univoque IDs from your telegram client, if you are using one that shows it (some examples are Telegram Foss, Nekogram, Forkgram). Alternatively, from the [web version](web.telegram.org) you can obtain it from the url, when you open the chat. It should be something like `web.telegram.org/z/#-123456789`. If the chat is a channel or a group, for the API call to work you have to add `100` between the `-` and the first number. in this case, `-100123456789`. More information on [Telegram ID Github](https://github.com/GabrielRF/telegram-id#web-channel-id).

### Run it!

To configure the script, you'll have to change `CHAT_ID_1` field. You can also add as many chat IDs you want, and call the functions for every chat. Remember to set the right function parameters in the last two lines of code.

On running the script for the first time it asks for your telegram number. Insert it and confirm the action from your telegram account. 
This step won't need to be repeated.

My suggestion is to run the script from the parent directory, in order to keep separated source code and output files.
This way, you will have the resulting folder looking like this:
```
.
├── messaggi_chat_-1001111111111.txt
├── messaggi_chat_-1002222222222.txt
└── pyrogram
    ├── my_account.session
    └── pyrogram_starter.py
```