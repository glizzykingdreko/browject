import logging
from typing import Dict, Union, Optional
from requests import post
from re import search

from .utils import Dict2Object
from .models import (
    BaseClass, 
    Timezone, 
    Navigator, 
    Screen, 
    WindowProps, 
    DocumentProps,
    BrowserName,
    OperatingSystem
)

def load_browser_data(data: Dict[str, str]) -> Dict:
    response = post('https://takionapi.tech/browser', json=data)
    response_data = response.json()

    if 'error' in response_data:
        logging.debug(response_data['error'])
    
    return response_data

class BrowJect(BaseClass):
    operatingSystem: str
    browserName: str
    browserVersion: str
    browserVersionFull: str
    userAgent: str
    timezone: Timezone
    navigator: Navigator
    screen: Screen
    window: WindowProps
    document: DocumentProps

    def __init__(
        self, 
        user_agent: Optional[str] = None,
        browser_version: Optional[Union[str, int]] = None,
        browser_name: Optional[Union[str, BrowserName]] = None,
        operating_system: Optional[Union[str, OperatingSystem]] = None
    ):
        """# BrowJect
        The main class for BrowJect. This class is used to access and emulate browser attributes. Ideal for reverse engineering antibots. Powered by TakionAPI for up-to-date browser data.

        ## Parameters
        - `user_agent` - The user agent to use. If not specified, a random user agent will be used.
        - `browser_version` - The browser version to use. If not specified, a random browser version will be used.
        - `browser_name` - The browser name to use. If not specified, a random browser name will be used.
        - `operating_system` - The operating system to use. If not specified, a random operating system will be used.

        ## Example

        ### With a random browser
        ```py
        from browject import BrowJect

        browser = BrowJect() # No parameters = random browser
        print(browser.browserName)
        ```

        ### With a specific browser
        ```py
        from browject import BrowJect, Chrome, Mac

        browser = BrowJect(browser_name=Chrome, operating_system=Mac)
        print(browser.browserName)
        ```

        ## Attributes
        - `operatingSystem` - The operating system of the browser.
        - `browserName` - The name of the browser.
        - `browserVersion` - The version of the browser.
        - `browserVersionFull` - The full version of the browser.
        - `userAgent` - The user agent of the browser.
        - `timezone` - The timezone of the browser.
        - `navigator` - The navigator of the browser.
        - `screen` - The screen of the browser.
        - `window` - The window of the browser.
        - `document` - The document of the browser.
        - `sec_ch_ua` - The `Sec-CH-UA` header of the browser.
        - `sec_ch_ua_platform` - The `Sec-CH-UA-Platform` header of the browser.
        """
        browser_data = load_browser_data({
            'userAgent': user_agent,
            'browserVersion': str(browser_version),
            'operatingSystem': str(operating_system),
            'browserName': str(browser_name)
        })

        obj = Dict2Object(browser_data)
        self.browserName = obj.browserName
        self.browserVersion = obj.browserVersion
        self.browserVersionFull = obj.browserVersionFull
        self.operatingSystem = obj.operatingSystem
        self.userAgent = obj.userAgent
        self.timezone = Timezone(**obj.timezone.to_dict())
        self.navigator = Navigator(**obj.navigator.to_dict())
        self.screen = Screen(**obj.screen.to_dict())
        self.window = WindowProps(**obj.window.to_dict())
        self.document = DocumentProps(**obj.document.to_dict())
    
    @property
    def sec_ch_ua(self):
        browser_name = ""
        secondary_name = ""
        version = ""
        
        if "Firefox" in self.userAgent:
            browser_name = "Firefox"
            version = search("Firefox/(\d+)", self.userAgent).group(1)
        elif "Chrome" in self.userAgent:
            browser_name = "Chromium"
            secondary_name = "Google Chrome"
            version = search("Chrome/(\d+)", self.userAgent).group(1)
        elif "Safari" in self.userAgent and "Chrome" not in self.userAgent:
            browser_name = "Safari"
            version = search("Version/(\d+)", self.userAgent).group(1)
        elif "Edge" in self.userAgent:
            browser_name = "Microsoft Edge"
            version = search("Edg/(\d+)", self.userAgent).group(1)
        elif "Opera" in self.userAgent or "OPR" in self.userAgent:
            browser_name = "Opera"
            if "OPR" in self.userAgent:
                version = search("OPR/(\d+)", self.userAgent).group(1)
            else:
                version = search("Version/(\d+)", self.userAgent).group(1)
        elif "Yandex" in self.userAgent:
            browser_name = "Yandex"
            version = search("YaBrowser/(\d+)", self.userAgent).group(1)

        sec_ch_ua = f'"{browser_name}";v="{version}", "Not;A Brand";v="99"'
        if browser_name == "Chromium":
            sec_ch_ua = f'"{browser_name}";v="{version}", "{secondary_name}";v="{version}", "Not;A Brand";v="99"'

        return sec_ch_ua
    
    @property
    def sec_ch_ua_platform(self):
        return "\"Windows\"" if "Windows" in self.operatingSystem else "\"macOS\""