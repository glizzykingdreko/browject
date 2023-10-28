import json
from typing import Any, Dict, Union
from requests import post

from utils import Dict2Object
from models import BaseClass, Timezone, Navigator, Screen, WindowProps, DocumentProps

def load_browser_data(data: Dict[str, str]) -> Dict:
    response = post('https://takionapi.tech/browser/', json=data)
    response_data = response.json()

    if 'error' in response_data:
        raise ValueError(response_data.get('error'))
    
    return response_data

class BrowJect(BaseClass):
    chromeVersion: str
    userAgent: str
    timezone: Timezone
    navigator: Navigator
    screen: Screen
    window: WindowProps
    document: DocumentProps

    def __init__(
        self, 
        user_agent: str = None,
        chrome_version: str = None,
        operating_system: str = None,
    ):
        browser_data = load_browser_data({
            'userAgent': user_agent,
            'chromeVersion': chrome_version,
            'operatingSystem': operating_system,
        })

        obj = Dict2Object(browser_data)
        self.chromeVersion = obj.chromeVersion
        self.userAgent = obj.userAgent
        self.timezone = Timezone(**obj.timezone.to_dict())
        self.navigator = Navigator(**obj.navigator.to_dict())
        self.screen = Screen(**obj.screen.to_dict())
        self.window = WindowProps(**obj.window.to_dict())
        self.document = DocumentProps(**obj.document.to_dict())

    def sec_ch_ua(self) -> str:
        chrome_index = self.chromeVersion.split('.')[0]
        return f'''"Not.A/Brand";v="8", "Chromium";v="{chrome_index}", "Google Chrome";v="{chrome_index}"'''

    def sec_ch_ua_platform(self) -> str:
        return '''"macOS"''' if self.navigator.platform == 'MacIntel' else '''"Windows"'''

if __name__ == '__main__':
    browser = BrowJect(user_agent='YourUserAgentHere')
    print(browser.navigator.userAgent)
