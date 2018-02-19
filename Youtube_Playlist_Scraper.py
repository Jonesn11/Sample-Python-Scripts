# Description: I want to make a program that takes names,and ratings from a series of videos in a playlist
# saves the content into a list, and then applies a metric to them to get a rating for each video

# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from operator import itemgetter


#  open the firefox webbrowser and type in the playlist I want

#: make a for loop for going through webpages and have a list variable declared
# inspect and select the css selector for title,likes,dislikes and next keys
# saving all to different variables


def initializeScraping(url, number_of_vids):
    browser = webdriver.Firefox()
    browser.get(url)
    videosInPlaylist = []
    for x in range(1, number_of_vids):
        wait = WebDriverWait(browser, 20)
        if x != 1:
            capture = wait.until(EC.url_changes(url))
        url = browser.current_url
        positiveVotes = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'ytd-toggle-button-renderer.style-text:nth-child(1) > a:nth-child(1) > yt-formatted-string:nth-child(2)'))).text
        negativeVotes = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'ytd-toggle-button-renderer.style-text:nth-child(2) > a:nth-child(1) > yt-formatted-string:nth-child(2)'))).text
        title = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'h1.title'))).text
        currentVideo = [title, positiveVotes, negativeVotes]
        # nextVideo = wait.until(EC.element_to_be_clickable(
        #     (By.CSS_SELECTOR, "ytd-playlist-panel-video-renderer.style-scope:nth-child(3) > a:nth-child(1)")))
        browser.find_element_by_xpath('//body').send_keys(Keys.SHIFT+"n")
        videosInPlaylist.append(currentVideo)
        # nextVideo.click()
    browser.close()
    return videosInPlaylist

# TODO: write a function that takes the list and returns a list of lists with the name and the average rating


def getTop5Ratings(listOfLists):
    updatedListOfLists = []
    for x in listOfLists:
        try:
            positiveRating = float(x[1])
            negativeRating = float(x[2])
        except ValueError:
            pass
        if 'K' in x[1]:
            variable = list(x[1])
            variable.remove('K')
            positiveRating = float(''.join(variable) + '000')
        if 'K' in x[2]:
            variable2 = list(x[2])
            variable2.remove('K')
            negativeRating = float(''.join(variable2) + '000')
        average = "%.3f" % (positiveRating / (positiveRating + negativeRating))
        updatedListOfLists.append([x[0], average])
    updatedListOfLists.sort(key=itemgetter(1), reverse=True)
    return updatedListOfLists[0:5]


# print(initializeScraping(
#     'https://www.youtube.com/watch?v=2bnMiScBRfQ&list=PLx1Dr6w7DLoLfPixTug9c8xrTkGUsyhkQ&index=1', 11))
listOfLists2 = [['Higher We Go (Intro)', '11K', '352'], ['Migos - Supastars (Audio)', '84K', '2K'], ['Narcos', '31K', '870'], ['BBO (Bad Bitches Only)', '13K', '272'], ['Auto Pilot', '8K', '215'], ['Walk It Talk It', '43K', '1K'], ['Emoji A Chain', '8K', '207'], ['CC', '5K', '120'], ['Migos - Stir Fry (Audio)', '161K', '6K'], ['Too Much Jewelry', '8K', '158'], ['Gang Gang', '16K', '462'], [
    'White Sand', '9K', '186'], ['Crown the Kings', '4K', '86'], ['Flooded', '5K', '137'], ['Beast', '11K', '275'], ['Open It Up', '5K', '102'], ['Migos, Nicki Minaj, Cardi B - MotorSport (Official)', '1M', '90K'], ["Movin' Too Fast", '6K', '87'], ['Work Hard', '4K', '87'], ['Notice Me', '23K', '473'], ['Too Playa', '10K', '270'], ['Made Men', '6K', '124'], ['Top Down On Da NAWF', '4K', '95']]


print(getTop5Ratings(listOfLists2))
# After getting a rating for each video, I want the program to give me the top five videos based on rating
