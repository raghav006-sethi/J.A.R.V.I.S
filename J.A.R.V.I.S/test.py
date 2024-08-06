from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Configure Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode if needed
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to your ChromeDriver
webdriver_service = Service('/path/to/chromedriver')  # Update with your path

# Initialize the WebDriver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open YouTube
driver.get('https://www.youtube.com/')

# Wait for the page to load
time.sleep(5)

# Play a specific video by searching for it
search_box = driver.find_element(By.NAME, 'search_query')
search_box.send_keys('Your favorite song or video title')
search_box.send_keys(Keys.RETURN)

# Wait for search results to load
time.sleep(5)

# Click on the first video
video = driver.find_elements(By.ID, 'video-title')[0]
video.click()

# Wait for the video to start
time.sleep(5)

# Play/Pause the video
def play_pause():
    video_player = driver.find_element(By.CLASS_NAME, 'html5-main-video')
    video_player.click()
    print("Toggled play/pause")

# Next video in playlist
def next_video():
    next_button = driver.find_element(By.CLASS_NAME, 'ytp-next-button')
    next_button.click()
    print("Next video")

# Previous video in playlist
def previous_video():
    # Note: YouTube may not allow going to a previous video if it's the first one in the list
    prev_button = driver.find_element(By.CLASS_NAME, 'ytp-prev-button')
    prev_button.click()
    print("Previous video")

# Loop the current video
def toggle_loop():
    # Open settings menu
    settings_button = driver.find_element(By.CLASS_NAME, 'ytp-settings-button')
    settings_button.click()
    
    time.sleep(1)
    
    # Toggle loop option
    menu_items = driver.find_elements(By.CLASS_NAME, 'ytp-menuitem')
    for item in menu_items:
        if 'Loop' in item.text:
            item.click()
            print("Toggled loop")
            break
    
    # Close settings menu
    settings_button.click()

# Control the media playback
play_pause()  # Toggle play/pause
time.sleep(5) # Play for 5 seconds

next_video()  # Go to the next video
time.sleep(5) # Play for 5 seconds

previous_video()  # Go to the previous video
time.sleep(5) # Play for 5 seconds

toggle_loop()  # Toggle loop on/off
time.sleep(10) # Observe the loop effect

# Close the browser
driver.quit()
