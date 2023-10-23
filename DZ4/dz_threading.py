import threading
import requests
import time

urls = ['https://hips.hearstapps.com/hmg-prod/images/wisteria-in-bloom-royalty-free-image-1653423554.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/a/a5/Flower_poster_2.jpg',
        'https://hips.hearstapps.com/hmg-prod/images/summer-flowers-64418cf119d36.jpg',
        'https://images.immediate.co.uk/production/volatile/sites/10/2018/02/5984c00b-1474-4218-b327-59490057a7b6-f3cff11.jpg',
        'https://hips.hearstapps.com/hmg-prod/images/flower-meanings-1671510935.jpg',
        'https://hips.hearstapps.com/hmg-prod/images/close-up-of-purple-crocus-flowers-united-kingdom-uk-royalty-free-image-1674159456.jpg',
        'https://grangettos.com/cdn/shop/articles/IMG_2019_2000x.jpg', ]


def download(url):
    response = requests.get(url)
    filename = 'threding_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.jpg'

    with open('flaskk/f4/f4_images_thread/' + filename, "wb") as f:
        f.write(response.content)

    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()