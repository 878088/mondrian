from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from termcolor import colored, cprint
from pyfiglet import figlet_format

def main():
    cprint(colored(figlet_format('Telegram', "smslant"), "cyan", attrs=['bold']))
    cprint(colored("会话生成\n", "magenta", attrs=['bold']))
    cprint("运行 Telethon 会话生成", "magenta")
    APP_ID = int(input(colored("Enter APP ID here: ", "green")))
    API_HASH = input(colored("Enter API HASH here: ", "green"))
    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        session_str = client.session.save()
        if client.is_bot():
            user_name = input("Enter the username: ")
            msg = client.send_message(user_name, session_str)
        else:
            msg = client.send_message("me", session_str)
        msg.reply(
            "⬆️ This String Session is generated using "
        )
        cprint("please check your Telegram Saved Messages/User's PM for the StringSession ", "yellow")

if __name__ == "__main__":
    main()