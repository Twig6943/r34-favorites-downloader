#Made by owosu
#Version 1.00
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from os import system, path
from time import sleep, time_ns
import requests
import pathlib
import os

print('r34 favorites downloader!')
print('[!] DO NOT PRESS/CLICK ANYTHING IN THE BROWSER WINDOW THAT WILL OPEN! IT OPERATES ITSELF :)')

print('\nYou can find your Profile ID in the URL of the "My Profile" page.')
user_id = input('Profile ID: ')

print('\nEnter the page numbers you want to download, separated by commas (e.g., 1,2,3):')
pages = input('Pages: ').split(',')

# Set up Firefox options to use Cloudflare DNS and enable extensions
options = Options()
options.set_preference("network.trr.mode", 2)  # Enable DoH
options.set_preference("network.trr.uri", "https://cloudflare-dns.com/dns-query")  # Set Cloudflare DoH URI
options.set_preference("network.trr.bootstrapAddress", "1.1.1.1")  # Use Cloudflare DNS for initial lookup
options.set_preference("network.dns.disablePrefetch", True)  # Disable DNS prefetching

# Enable loading of extensions
options.set_preference("extensions.autoDisableScopes", 0)
options.set_preference("extensions.enabledScopes", 15)

# Path to uBlock Origin XPI (alternatively, download and store locally)
ublock_origin_url = "https://addons.mozilla.org/firefox/downloads/file/4070280/ublock_origin-1.50.0.xpi"
ublock_origin_path = os.path.join(pathlib.Path().resolve(), "ublock_origin.xpi")
if not os.path.exists(ublock_origin_path):
    response = requests.get(ublock_origin_url)
    with open(ublock_origin_path, 'wb') as file:
        file.write(response.content)

# Initialize the WebDriver with uBlock Origin loaded
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.install_addon(ublock_origin_path, temporary=True)

download_folder = f'./r34download_{time_ns()}'
pathlib.Path(download_folder).mkdir(parents=True, exist_ok=True)  # create download folder

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

num_errors = 0
all_found_ids = []

for page in pages:
    page = int(page.strip())
    pid = page * 50 - 50
    driver.get(f"https://rule34.xxx/index.php?page=favorites&s=view&id={user_id}&pid={pid}")

    sleep(1)

    source_code = driver.page_source  # save the source code of the favorites page

    found_ids = []
    for i in range(len(source_code)):  # this loop goes through every character of the source code,
        text_to_check = source_code[i: i + 44]

        if text_to_check == 'href="index.php?page=post&amp;s=view&amp;id=':
            found_id_begin_index = i + 44
            offset = 0
            while True:
                offset += 1
                if source_code[i + 44 + offset] == '"':
                    break
                else:
                    continue
            found_id_end_index = i + 44 + offset
            found_id = source_code[found_id_begin_index: found_id_end_index]
            found_ids.append(found_id)

    all_found_ids.extend(found_ids)

print(f'\nFound images: {", ".join(all_found_ids)}\n')

total_posts = len(all_found_ids)

for index, post_id in enumerate(all_found_ids, start=1):
    print(f'Downloading post {index} of {total_posts}...')

    driver.get(f"https://rule34.xxx/index.php?page=post&s=view&id={post_id}")  # load page

    sleep(1)

    try:
        max_res_script = "Post.highres(); $('resized_notice').hide(); Note.sample=false; return false;"
        driver.execute_script(max_res_script)  # load maximum resolution
    except selenium.common.exceptions.JavascriptException:
        pass

    sleep(1)

    try:
        img_element = driver.find_element(By.ID, "image")  # find image link
        image_link = img_element.get_attribute('src')

        response = requests.get(image_link, headers=headers)
        if response.status_code == 200:
            with open(os.path.join(download_folder, image_link.split('/')[-1]), 'wb') as file:
                file.write(response.content)
            print(f'Downloaded {image_link}')
        else:
            print(f'Failed to download {image_link} - HTTP {response.status_code}')
            num_errors += 1

    except selenium.common.exceptions.NoSuchElementException:
        try:
            vidsrc_elem = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[1]/div[3]/div/video/source')  # locate video source element
            video_link = vidsrc_elem.get_attribute('src')

            response = requests.get(video_link, headers=headers)
            if response.status_code == 200:
                with open(os.path.join(download_folder, video_link.split('/')[-1]), 'wb') as file:
                    file.write(response.content)
                print(f'Downloaded {video_link}')
            else:
                print(f'Failed to download {video_link} - HTTP {response.status_code}')
                num_errors += 1
        except selenium.common.exceptions.NoSuchElementException:
            print(f'{post_id} could not be downloaded!\n')
            num_errors += 1

driver.quit()
print(f'Finished with {num_errors} errors (Check output for more info).')
input()  # pause
