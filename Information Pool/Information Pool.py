import requests
from base64 import b64encode
import random
class Information_Pool:
    def __init__(self, url, user_agents_file, ip_addresses_file, accounts_file):
        self.url = url
        self.user_agents_file = user_agents_file
        self.ip_addresses_file = ip_addresses_file
        self.accounts_file = accounts_file
        self.sessions = []

    def _read_file(self, filename):
        with open(filename, 'r') as f:
            return f.read().splitlines()
        
    def _create_sessions(self, user_agents, ip_addresses, accounts):
        min_length = min(len(user_agents), len(ip_addresses), len(accounts))
        for _ in range(min_length):
            session = requests.Session()

            # 随机选择一个用户代理、IP地址和账号
            user_agent = random.choice(user_agents)
            ip = random.choice(ip_addresses)
            account = random.choice(accounts)

            headers = {
                'User-Agent': user_agent,
                'X-Forwarded-For': ip,
                'Authorization': 'Basic ' + b64encode(f"{account['username']}:{account['password']}".encode()).decode()
            }
            session.headers.update(headers)
            self.sessions.append(session)

    def send_requests(self):
        user_agents = self._read_file(self.user_agents_file)
        ip_addresses = self._read_file(self.ip_addresses_file)

        accounts = []
        with open(self.accounts_file, 'r') as f:
            for line in f:
                username, password = line.strip().split(',')
                accounts.append({'username': username, 'password': password})

        self._create_sessions(user_agents, ip_addresses, accounts)

        for session in self.sessions:
            response = session.get(self.url)
            # 检查响应状态码等...
            print(response.text)  # 这里仅作示例，你可以根据实际需求进行处理

    def close_sessions(self):
        for session in self.sessions:
            session.close()

if __name__ == "__main__":
    url = 'http://example.com'
    user_agents_file = 'user_agents.txt'
    ip_addresses_file = 'ip_addresses.txt'
    accounts_file = 'accounts.txt'

    multi_session_requests = Information_Pool(url, user_agents_file, ip_addresses_file, accounts_file)
    multi_session_requests.send_requests()
    multi_session_requests.close_sessions()