import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

if not os.path.exists('dataset'):
    os.mkdir('dataset')

def download_images(class_name, num_images):
    class_path = os.path.join('dataset', class_name)
    if not os.path.exists(class_path):
        os.mkdir(class_path)

    search_query = f'https://yandex.ru/images/search?text={class_name}&type=photo'
    response = requests.get(search_query)
    soup = BeautifulSoup(response.text, 'html.parser')

    image_elements = soup.find_all('img', class_='serp-item__thumb justifier__thumb')
    image_links = [urljoin(search_query, img['src']) for img in image_elements if 'src' in img.attrs]

    image_links = image_links[:num_images]

    for i, image_link in enumerate(image_links):
        image_response = requests.get(image_link)
        image_filename = f'{str(i).zfill(4)}.jpg'
        image_path = os.path.join(class_path, image_filename)

        with open(image_path, 'wb') as img_file:
            img_file.write(image_response.content)

download_images('tiger', 1000)
download_images('leopard', 1000)

print("Изображения успешно загружены.")

for class_name in ['tiger', 'leopard']:
    class_path = os.path.join('dataset', class_name)
    for filename in os.listdir(class_path):
        image_path = os.path.join(class_path, filename)
