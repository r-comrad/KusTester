from selenium import webdriver
from bs4 import BeautifulSoup
import json
import colorama
colorama.init()
from colorama import Fore, Style

class KusTester:
    def __init__(self, driver_path=r"C:\\chromedriver.exe", url="https://kusjournal.ru") -> None:
        self.__base_url = url
        self.__browser = webdriver.Chrome(executable_path=driver_path)
        self.__test_path = dict()

    def Add(self, path: str, ans: dict):
        self.__test_path[self.__base_url+path] = ans

    def Test(self):
        passed = 0
        for url in self.__test_path:
            self.__browser.get(url)
            page = BeautifulSoup(self.__browser.page_source, "html.parser")
            result = self.__test_path[url] == json.loads(page.find('pre').text)
            print(f'Verdict: {Fore.GREEN + "OK"+ Style.RESET_ALL if result else Fore.RED + "ERROR" + Style.RESET_ALL}, Path: {url}' )
            if not result:
                print(Fore.RED + "Data from URL:" + Style.RESET_ALL)
                print(json.loads(page.find('pre').text))
                print(Fore.RED + "Your data:" + Style.RESET_ALL)
                print(self.__test_path[url])
            else:
                passed+=1
        color = Fore.GREEN if passed == len(self.__test_path) else Fore.RED 
        print(f'Total: {color+str(passed)}/{str(len(self.__test_path))+Style.RESET_ALL} passed')

    