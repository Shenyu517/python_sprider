import os
import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor

class ImageDownloader:
    def __init__(self):
        self.url = 'https://www.itzmx.com/{}.webp'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.237.400 QQBrowser/12.4.5621.400'
        }
        self.save_path = './itzmx_png/image'  # 设置保存路径

    # 获取所有图片链接，并返回一个包含所有图片链接的列表
    def get_image_url_list(self):
        url_list = []
        for i in range(501, 505): 
            url_list.append(self.url.format(i))
        return url_list

    # 下载图片
    def download_image(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            image_content = response.content
            image_name = url.split('/')[-1]
            self.save_image(image_content, image_name)
        else:
            print(f'{url} 下载失败')
            raise Exception(f'下载失败：{url}')

        # 随机等待1到3秒
        time.sleep(random.uniform(1, 3))

    # 保存图片
    def save_image(self, image_content, image_name):
        image_path = os.path.join(self.save_path, image_name)
        with open(image_path, 'wb') as f:
            f.write(image_content)
            print(f'{image_name} 下载完成，保存在 {self.save_path}')


    # 多线程下载图片
    def download_images_multithreading(self, url_list):
        with ThreadPoolExecutor() as executor:
            executor.map(self.download_image, url_list)


    # 主函数
    def main(self):
        # 创建保存图片的文件夹
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        url_list = self.get_image_url_list()
        try:
            self.download_images_multithreading(url_list)
            print('所有图片下载完成')
        except Exception as e:
            print(f'下载过程中发生错误：{e}')


if __name__ == '__main__':
    downloader = ImageDownloader()
    downloader.main()