import requests
from bs4 import BeautifulSoup


class TelegramgWebScrapper:
    """Telegram Web scrapper
    You can get informations about telegram posts by using the methods bellow
    (only for telegram channels)"""

    __PARSE_MODE = "html.parser"
    __WIDGET_VIEWS = "tgme_widget_message_views"
    __WIDGET_MESSAGE = "tgme_widget_message js-widget_message"
    __NOT_FOUND_MESSAGE = "Make sure that you have correct message id"

    def __init__(self, base_url: str,  channel: str) -> None:
        self.channel_url = base_url + channel
        self.soup = BeautifulSoup(requests.get(
            self.channel_url).text, self.__PARSE_MODE)

    def get_post_views(self, message_id: int) -> str:
        kwargs: dict = {
            "class_": self.__WIDGET_MESSAGE,
            "attrs": {
                {"data-post": f"{self.channel_url}/({str(message_id)})"}
            }
        }
        soup = self.soup.find(**kwargs)
        if soup is None:
            raise BeautifulSoup.FeatureNotFound(self.__NOT_FOUND_MESSAGE)

        return soup.find(class_=self.__WIDGET_VIEWS).text
