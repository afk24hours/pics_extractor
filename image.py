import urllib.request
import random
import string
from PIL import Image, ImageFilter

#GENERATE UNIQUE STRING AND ADD EXTENSION TO THE PICTURE
def generate_name(img_type: str): # GENERATE RANDOM 8 LETTERS TO ADD TO FILENAME
    unique_string = ''.join(random.choice(string.ascii_letters) for i in range(8))
    img_name = 'images/image_' + unique_string + f".{img_type}"
    return img_name

# FUNCTION TO DETECT FILE SIZE AND EXTENSION
def get_imgsize_extension(img_url): 
    data = urllib.request.urlopen(img_url)
    ext = data.getheader('Content-Type').rsplit('/', 1)[-1]
    return data, ext

# SIMPLE DOWNLOAD
def retrieve_image(img_url): 
    data, ext = get_imgsize_extension(img_url)
    if len(data.read()) <= 256000:
        urllib.request.urlretrieve(img_url, generate_name(ext))

# FUNCTIONALITY TO FILTER WHOLE IMAGES FOLDER
def filter_image(img_location): 
    img = Image.open(f"images/{img_location}")
    img = img.filter(ImageFilter.ModeFilter(size=9))
    img.save(f"filtered-images/filtered_{ImageFilter.ModeFilter.__name__}_{img_location}")

