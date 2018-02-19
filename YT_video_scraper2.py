from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from operator import itemgetter

browser = webdriver.Firefox()
browser.get('https://www.youtube.com/watch?v=hZBqEbswI3M&list=PLpeTkJgdk3szUqK8vBObS9LHWtfb2ka4r&index=1')


class element_text_changed(object):
    def __init__(self, locator, oldTitle):
        self.locator = locator
        self.oldTitle = oldTitle

    def __call__(self, browser):
        wait = WebDriverWait(browser, 20)
        titleElement = wait.until(EC.visibility_of_element_located(self.locator))
        newTitle = titleElement.text.strip()
        print("OLD: " + self.oldTitle + ", NEW: " + newTitle)
        if len(self.oldTitle) == 0 or (self.oldTitle != newTitle):
            return titleElement
        else:
            return False


oldTitle = ''
videosInPlaylist = []
for x in range(1, 24):
    wait = WebDriverWait(browser, 20)
    title = wait.until(element_text_changed((By.CSS_SELECTOR, 'h1.title'), oldTitle)).text
    print(title)
    oldTitle = title

    wait = WebDriverWait(browser, 10)
    positiveVotes = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'ytd-toggle-button-renderer.style-text:nth-child(1) > a:nth-child(1) > yt-formatted-string:nth-child(2)'))).text
    negativeVotes = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'ytd-toggle-button-renderer.style-text:nth-child(2) > a:nth-child(1) > yt-formatted-string:nth-child(2)'))).text
    videosInPlaylist.append([title, positiveVotes, negativeVotes])
    browser.find_element_by_xpath('//body').send_keys(Keys.SHIFT+"n")

browser.close()
print(videosInPlaylist)
