import random
import httpx
import string
from anticaptchaofficial.hcaptchaproxyless import hCaptchaProxyless
from colorama import Fore, Style


class DiscordAcount:
    def __init__(self):
        self.solver = hCaptchaProxyless()
        self.solver.set_verbose(1)
        self.solver.set_key("d1b69290ebde738e5733b35a887916c5")
        self.solver.set_website_url("https://discord.com")
        self.solver.set_website_key("4c672d35-0701-42b2-88c3-78380b0db560")

    def data_inputs(self):
        enter_email = input(Fore.MAGENTA + 'Enter email: ')
        enter_username = input(Fore.BLUE + 'Enter username: ')
        print(Style.RESET_ALL)
        return enter_email, enter_username

    def random_password(self):
        characters = string.ascii_letters + string.punctuation + string.digits
        gen_password = "".join(random.choice(characters) for x in range(random.randint(11, 17)))
        return gen_password

    def register(self):
        email, username = self.data_inputs()
        password = self.random_password()

        while True:
            captcha_key = self.solver.solve_and_return_solution()

            headers = {
                "Host": "discord.com",
                "Connection": "keep-alive",
                "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
                "X-Fingerprint": "",
                "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
                "sec-ch-ua-mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
                "Content-Type": "application/json",
                "Authorization": "undefined",
                "Accept": "*/*",
                "Origin": "https://discord.com",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://discord.com/register",
                "X-Debug-Options": "bugReporterEnabled",
                "Accept-Encoding": "gzip, deflate, br",
                "Cookie": "OptanonConsent=version=6.17.0; locale=th"
            }

            data = {
                "fingerprint": "",
                "email": email,
                "username": username,
                "password": password,
                "invite": None,
                "consent": "true",
                "date_of_birth": "1999-11-09",
                "gift_code_sku_id": "",
                "captcha_key": captcha_key,
            }

            registration = httpx.post("https://discord.com/api/v9/auth/register", headers=headers, json=data)

            if registration.status_code == 201:
                print(Fore.GREEN + 'TOKEN IS: ')
                return registration.json()['token']
            else:
                print(Fore.YELLOW + 'Captcha not solved, trying again...status code:', registration.status_code)
                print(Style.RESET_ALL)
                continue


if __name__ == '__main__':
    launch = DiscordAcount()
    print(launch.register())
