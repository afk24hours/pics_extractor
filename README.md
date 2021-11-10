# Web image parser with multiprocessing downloads

Parses given URL and tries to find *.jpeg , *.jpg, *.png files on a webpage which are not bigger than 512KB. Limited to download 25 images by default.
Uses process pool executor to run concurrent downloads
Saves images to /images folder

Just paste a URL inside main.py and test what you get :)

    imgs = ImagesLink("URL HERE")

*OPTIONAL* 
You can add filter to downloaded images using Pillow and save processed images to /filtered-images folder. Also uses multiprocessing for speed purposes. 

## How to test this:
    
    ```sh
    $ gh repo clone afk24hours/pics_extractor
    cd to folder
    $ python3.9 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ python3.9 main.py
    ```

Try to find websites with unprotected content (e.g. non dynamic img src and protected static links)
