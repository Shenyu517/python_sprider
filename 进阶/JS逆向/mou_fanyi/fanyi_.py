import re
import json
import requests  
import execjs

class BaiduTranslator:
    """
    Baidu Translator class for translating text from English to Chinese using Baidu Translate API.
    """

    def __init__(self):
        """
        Initialize BaiduTranslator class.
        """
        self.session = requests.Session()
        self.headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'X-Requested-With': "XMLHttpRequest",
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        }
        self.token, self.cookies = self._get_token_and_cookies()
        self.script_path = r'BaiDu_fanyi\config\fanyi_sign.js'

    def _get_token_and_cookies(self):
        """
        Get token and cookies required for translation.
        """
        url = 'https://fanyi.baidu.com/'
        response = self.session.get(url, headers=self.headers)
        response = self.session.get(url, headers=self.headers)
        token = re.findall(r"token:\s*'(\w+)'", response.text)[0]
        cookies = self.session.cookies.get_dict()
        return token, cookies


    def _get_sign(self, text):
        """
        Calculate sign for translation.
        """
        with open(self.script_path, 'r', encoding='utf-8') as f:
            js_code = f.read()
            sign = execjs.compile(js_code).call('get_sign', text)
            return sign

    def _prepare_data(self, text):
        """
        Prepare data for translation.
        """
        sign = self._get_sign(text)
        data = {
            'query': text,
            'from': 'en',
            'to': 'zh',
            'token': self.token,
            'sign': sign,
        }
        return data

    def translate(self, text):
        """
        Translate English text to Chinese.
        """
        url = 'https://fanyi.baidu.com/basetrans'
        translation_data = self._prepare_data(text)
        try:
            response = self.session.post(url, data=translation_data, headers=self.headers, cookies=self.cookies)
            result = json.loads(response.text)['trans'][0]['dst']
            print("翻译中文结果为：", result)
        except Exception as e:
            print("翻译出错:", e)

if __name__ == '__main__':
    while True:    
        translator = BaiduTranslator()
        text = input("请输入你要翻译的英语:")
        translator.translate(text)