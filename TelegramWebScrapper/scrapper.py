class TelegramgWebScrapper:
    """Telegram Web scrapper
    You can get informations about telegram posts by using the methods bellow
    (only for telegram channels)"""

    __BASE_URL = "https://t.me/s/"
    __BS4 = __import__("bs4")
    __REQUESTS = __import__("requests")


    def __init__(self, channel: str) -> None:
        self.channel = channel
        self.channel_url = self.__BASE_URL + str(channel)
        self.html_page = self.__REQUESTS.get(self.channel_url)
        self.soup =self.__BS4.BeautifulSoup(self.html_page.text, "html.parser")


    def get_post_views(self, message_id: int) -> str:
        """It function will recieve message_id as a post id"""
        soup = self.soup.find(class_="tgme_widget_message js-widget_message", attrs={"data-post": "%s/%s" % (self.channel, str(message_id))})
        if soup is None:
            raise self.__BS4.FeatureNotFound("Make sure that you have correct message id")
        views = soup.find(class_="tgme_widget_message_views")
        return views.text

    
        
