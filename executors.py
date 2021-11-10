from image import *
from concurrent.futures import ProcessPoolExecutor


# PROCESS POOL TO SPEED UP EXECUTION 
def download_images(page_image_links):
    with ProcessPoolExecutor(max_workers=10) as executor:
        for url in page_image_links:
            future = executor.submit(retrieve_image, url)

def filter_and_save_images(images_list):
    with ProcessPoolExecutor(max_workers=10) as executor:
        for url in images_list:
            future = executor.submit(filter_image, url)