
import requests
import time
import telebot
from bs4 import BeautifulSoup

# Telegram bot token and user ID
BOT_TOKEN = '7799039818:AAHzDcSMpip7cijRN-mtKfoowTrFw-2mRsk'
USER_ID = 7817914750

# Aviator game URL (scraping target)
AVIATOR_URL = 'https://aviator-next.spribegaming.com/?user=34292367&token=9c24fe84-be11-4443-a36f-56f419b6401b&lang=en&currency=BDT&operator=1xbetcore&return_url=https://1xlite-545087.top/slots?locale=en_GB'

bot = telebot.TeleBot(BOT_TOKEN)

def get_latest_crash_point():
    try:
        response = requests.get(AVIATOR_URL, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        # This part will depend on actual structure; we assume placeholder below:
        latest_point = float(soup.find('div', class_='crash-point').text.replace('x', ''))
        return latest_point
    except:
        return None

def send_signal(message):
    bot.send_message(USER_ID, message)

def main():
    last_signal_time = 0
    while True:
        point = get_latest_crash_point()
        if point:
            current_time = time.time()
            if point >= 2.20 and current_time - last_signal_time > 60:
                send_signal(f"SAFE SIGNAL: Crash predicted above 2.20x! (Last: {point}x)")
                last_signal_time = current_time
            elif point < 2.20 and current_time - last_signal_time > 60:
                send_signal(f"WARNING: Don't bet now! Crash may happen below 2.20x. (Last: {point}x)")
                last_signal_time = current_time
        time.sleep(10)

if __name__ == '__main__':
    send_signal("Bot started and monitoring Aviator rounds...")
    main()
