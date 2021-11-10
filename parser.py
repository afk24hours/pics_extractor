import urllib3
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# SIMPLE IMAGE LINK PROCESSOR
class ImagesLink:
    base_url = ""
    img_block = []
    img_links = []

    # INIT POOL MANAGER AND BASIC ATTRS
    def __init__(self, url) -> None:
        self.http = urllib3.PoolManager()
        self.url = url

    # EXTRACT BASE URL FROM FULL URL
    def get_base_url(self):
        parsed_uri = urlparse(self.url)
        result = f'{parsed_uri.scheme}://{parsed_uri.netloc}/'
        self.base_url = str(result)
        return str(result)

    # GET RAW IMAGE URLS
    def get_image_urls(self) -> list:
        response = self.http.request("GET", self.url)
        response = str(response.data).replace('\\n', '')
        soup = BeautifulSoup(response, 'html.parser')
        self.img_blocks = soup.findAll('img',{"src":True})
        return self.img_blocks

    # SAVE CLEAN IMAGE URLS
    def get_complete_image_urls(self): # SIMPLE CHECK TO OBTAIN RELATIVE AND ABSOLUTE URLS FOR IMAGES
        for i in self.img_blocks:
            if len(self.img_links) > 25:
                break
            if str(i.attrs['src']) == None:
                continue
            if str(i.attrs['src']).startswith("http") and \
                (str(i.attrs['src']).endswith(".jpg") or \
                    str(i.attrs['src']).endswith(".jpg") or \
                        str(i.attrs['src']).endswith(".jpg")):
                full_url = str(i.attrs['src'])
                self.img_links.append(full_url)
            elif str(i.attrs['src']).endswith(".jpg") or \
                str(i.attrs['src']).endswith(".jpeg") or \
                str(i.attrs['src']).endswith(".png"):
                if str(i.attrs['src']).startswith("/"):
                    full_url = self.base_url + str(i.attrs['src'])[1:]
                elif not(str(i.attrs['src']).startswith("http")):
                    full_url = str(i.attrs['src'])
                self.img_links.append(full_url)
        return self.img_links




