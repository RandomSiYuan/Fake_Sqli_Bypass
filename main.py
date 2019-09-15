import requests
from core import core_rule
from config import settings
from core import core


def meun():
    print("\r\r\r--------------------------------------------")
    print("\r\r\r--------------------------------------------")
    print("\r\r\r               Author:SiYuan                ")
    print("\r\r\r           08sec https://www.08sec.org/     ")
    print("\r\r\r                  @xzbgs                    ")
    print("\r\r\r--------------------------------------------")
    print("\r\r\r--------------------------------------------")



if __name__ == '__main__':
    meun()
    core.fuzz.fuzz_start(object,settings.settings.url,settings.settings.str)