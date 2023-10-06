from urllib.parse import urlencode
import requests
import json
from tqdm import tqdm
import datetime
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN_VK = os.getenv('VK')



class VKPhotoDownloader:
    API_BASE_URL = 'https://api.vk.com/method'
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_common_params(self):
        return {
            'access_token': self.token,
            'v': '5.131'
        }

    def build_url(self, api_method):
        return f'{self.API_BASE_URL}/{api_method}'


    def get_profile_photo(self):
        params = self.get_common_params()
        params.update({
            'owner_id': self.user_id,
            'album_id': 'profile',
            'extended': 1
        })
        response = requests.get(self.build_url('photos.get'), params=params)
        return response.json()


    def photo_save(self):
        photo_info = vk_client.get_profile_photo()
        all_photos = photo_info['response']['items']
        # pprint(all_photos)
        best_resolution_all = {}
        num = 0
        print('По умолчанию сохраняется 5 фотографий.')
        print('Хотите изменить значение по умолчанию?')
        desision = input('Введите да или нет: ')
        names = []
        if desision.lower() == 'да':
            num = int(input('Введите количество сохраняемых фото: '))
        elif desision.lower() != 'да':
            print('Принято значение по умолчанию')
            num = 5
        for index, photo in enumerate(all_photos):
            if index == num:
                break
            else:
                photo_id = photo['id']
                url = photo['sizes'][-1]['url']
                name = str(photo['likes']['count'])
                if name in names:
                    name = f"{name}_{datetime.datetime.fromtimestamp(photo['date']).strftime('%Y-%m-%d')}"
                names.append(name)
                size = photo['sizes'][-1]['type']
        file_info = []
        for path, data in tqdm(best_resolution_all.items(), desc="Downloading files", unit="file"):
            response = requests.get(data['url'])
            file_name = data['name']
            with open(str(file_name) + '.jpg', 'wb') as f:
                f.write(response.content)
            file_info.append({
                'file_name': (str(file_name) + '.jpg'),
                'size': data['size']
            })
        with open('photos_info.json', 'w') as f:
            json.dump(file_info, f, ensure_ascii=False, indent=4)


class YandexDiskUploader():
    YA_BASE_URL = 'https://cloud-api.yandex.net'
    def __init__(self, token):
        self.token = token


    def create_folder(self):
        url = f'{self.YA_BASE_URL}/v1/disk/resources/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': YA_TOKEN}
        params = {'path': 'VKPhotosBackUp',
                  'overwrite': 'false'}
        response = requests.put(url=url, headers=headers, params=params)

    def upload_photo(self):
        with open('photos_info.json', 'r') as f:
            data = json.load(f)

        for file in tqdm(data, desc="Uploading files", unit="file"):
            file_name = file['file_name']
            headers = {
                       'Authorization': YA_TOKEN
            }
            params = {
                'path': f'VKPhotosBackUp/{file_name}'
            }

            try:
                response = requests.get(
                    f'{self.YA_BASE_URL}/v1/disk/resources/upload',
                                        params=params,
                                        headers=headers
                )
                response.raise_for_status()  # Проверка на ошибку
                path_to_upload = response.json().get('href', '')

                with open(file_name, 'rb') as file_content:
                    upload_response = requests.put(
                        path_to_upload, files={"file": file_content}
                    )
                    upload_response.raise_for_status()  # Проверка на ошибку
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")


class GDriveUploader():

    def __init__(self, token):
        self.token = token




if __name__ == '__main__':
    print('Профиль пользователя ВК должен быть открытым')
    user_id = input('Укажите id пользователя ВК: ')
    YA_TOKEN = 'OAuth ' + input('Укажите ваш токен для Я.Диск: ')
    vk_client = VKPhotoDownloader(TOKEN_VK, user_id)
    vk_client.photo_save()
    ya_client = YandexDiskUploader(YA_TOKEN)
    ya_client.create_folder()
    ya_client.upload_photo()