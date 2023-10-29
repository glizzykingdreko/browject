from browject import BrowJect, Chrome, Mac

browser = BrowJect(browser_name=Chrome, operating_system=Mac)
print(browser.userAgent)