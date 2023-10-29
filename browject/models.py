from typing import List, Dict, Optional
import logging

class BaseClass:
    def __getattr__(self, item):
        logging.debug(f"'{type(self).__name__}' object has no attribute '{item}'")
        return None
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class Timezone(BaseClass):
    timezone: str
    timezoneOffset: int
    timezoneOffsetName: str

class Connection(BaseClass):
    effectiveType: str
    rtt: int
    downlink: float
    saveData: bool

class MimeType(BaseClass):
    type: str
    suffixes: str
    description: str
    enabledPlugin: bool

class Plugin(BaseClass):
    name: str
    filename: str
    description: str
    length: int
    item: bool
    namedItem: bool
    mimeTypes: List[MimeType]

class Navigator(BaseClass):
    connection: Connection
    deviceMemory: int
    webGL: Dict  # Can be defined more explicitly if keys are known
    battery: Dict  # Can be defined more explicitly if keys are known
    appCodeName: str
    appName: str
    appVersion: str
    userAgent: str
    platform: str
    language: str
    languages: List[str]
    product: str
    productSub: str
    vendor: str
    vendorSub: str
    plugins: List[Plugin]
    mimeTypes: List[MimeType]
    clipboard: bool
    cookieEnabled: bool
    doNotTrack: Optional[str]
    geolocation: bool
    hardwareConcurrency: int
    maxTouchPoints: int
    mediaCapabilities: bool
    mediaDevices: bool
    permissions: bool
    serviceWorker: bool
    storage: bool
    userAgentData: bool
    webdriver: bool
    webkitPersistentStorage: bool
    webkitTemporaryStorage: bool
    getBattery: bool
    getGamepads: bool
    webkitGetUserMedia: bool
    registerProtocolHandler: bool
    unregisterProtocolHandler: bool
    vibrate: bool
    javaEnabled: bool
    taintEnabled: bool

class Screen(BaseClass):
    width: int
    height: int
    availWidth: int
    availHeight: int
    availLeft: int
    availTop: int
    colorDepth: int
    pixelDepth: int

class VisualViewport(BaseClass):
    width: int
    height: int
    offsetLeft: int
    offsetTop: int
    pageLeft: int
    pageTop: int
    scale: float

class Scrollbars(BaseClass):
    visible: bool

class WindowProps(BaseClass):
    visualViewport: VisualViewport
    innerWidth: int
    innerHeight: int
    outerWidth: int
    outerHeight: int
    devicePixelRatio: float
    screenLeft: int
    screenTop: int
    scrollX: int
    scrollY: int
    screen: Screen
    sessionStorage: bool
    localStorage: bool
    indexedDB: bool
    crypto: bool
    performance: bool
    requestAnimationFrame: bool
    cancelAnimationFrame: bool
    requestIdleCallback: bool
    cancelIdleCallback: bool
    matchMedia: bool
    getComputedStyle: bool
    getMatchedCSSRules: bool
    getSelection: bool
    open: bool
    openDatabase: bool
    postMessage: bool
    scroll: bool
    scrollTo: bool
    scrollBy: bool
    scrollbars: Scrollbars
    

class DocumentProps(BaseClass):
    clientHeight: int
    clientWidth: int
    characterSet: str
    compatMode: str
    contentType: str
    defaultView: bool
    scrollingElement: bool
    fullscreenElement: bool
    pointerLockElement: bool
    hidden: bool

class BrowserName:
    pass

class Chrome(BrowserName):
    def __str__(self):
        return 'Chrome'

class Firefox(BrowserName):
    def __str__(self):
        return 'Firefox'

class Safari(BrowserName):
    def __str__(self):
        return 'Safari'

class Edge(BrowserName):
    def __str__(self):
        return 'Edge'

class Opera(BrowserName):
    def __str__(self):
        return 'Opera'

class InternetExplorer:
    def __str__(self):
        return 'Internet Explorer'

class OperatingSystem:
    pass

class Windows(OperatingSystem):
    pass

    def __str__(self):
        return 'Windows'

class Mac(OperatingSystem):
    pass

    def __str__(self):
        return 'MacOs'