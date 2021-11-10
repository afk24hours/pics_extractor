from parser import ImagesLink
from image import *
from executors import download_images, filter_and_save_images


def main():

    imgs = ImagesLink("https://mirpozitiva.ru/photo/43190-kamennoe-iskusstvo.html")
    imgs.get_base_url()
    imgs.get_image_urls()
    page_image_links = imgs.get_complete_image_urls()
    print(page_image_links)
    download_images(page_image_links)

    # OPTIONAL 
    # CAN FILTER ALL IMAGES IN IMAGES FOLDER AND SAVE TO FILTERED-IMAGES

    #images_list = os.listdir('images')
    #filter_and_save_images(images_list)

if __name__ == '__main__':
    main()