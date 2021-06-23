from selenium import webdriver
import time
import random


driver = webdriver.Chrome('G:\\python\\chromedriver.exe')


videos =[
        'https://www.youtube.com/watch?v=lCllcYDcWuE',
        'https://www.youtube.com/watch?v=X198qltxEq0' ,
        'https://www.youtube.com/watch?v=N3Zh8JwuJ-E',
        'https://www.youtube.com/watch?v=1zOzuFhnrTs',
        'https://www.youtube.com/watch?v=Z4eXDbwVFY0',
        'https://www.youtube.com/watch?v=CUl6SeDT8ho',
        'https://www.youtube.com/watch?v=e5m30JAPp7g'
]



for i in range(100):
    print("Running the Video for {} time".format(i))
    random_video = random.randint(0, 6)
    driver.get(videos[random_video])
    sleep_time = random.randint(10, 20)
    time.sleep(sleep_time)


driver.quit()
