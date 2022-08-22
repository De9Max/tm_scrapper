import time
import requests
from bs4 import BeautifulSoup
import database
import telegram

URL = "https://www.tesmanian.com/blogs/tesmanian-blog"


def check_new_posts():
    page = requests.get(URL)
    print(page.status_code)
    soup = BeautifulSoup(page.content, "html.parser")
    main_frame = soup.find("div", class_="twelve")
    articles = main_frame.find_all("div", class_="eleven")
    if articles:
        for article in articles:
            current_article = article.find_next("a")
            if not database.check_exist_article(current_article.text):
                name = current_article.text
                url = "https://www.tesmanian.com" + current_article.attrs["href"]
                database.add_article(name, url)
                telegram.send_notification(name, url)


def main():
    while True:
        try:
            check_new_posts()
            time.sleep(15)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
