import json
import random as rd

import requests

from .basic_word import BasicWord
from .settings import URL


def load_random_word(verify_certifi=True) -> BasicWord:
    try:
        response: requests.Response = requests.get(URL, verify=verify_certifi)

        if response.status_code == 200:
            data: list[dict[str, str]] = json.loads(response.text)

            return BasicWord(**rd.choice(data))

    except requests.exceptions.SSLError:
        print("Ошибка SSL-сертификата, подключение выполнится без его проверки")
        requests.urllib3.disable_warnings()

        return load_random_word(verify_certifi=False)
