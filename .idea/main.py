from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

def dota():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito --headless")
    driver = webdriver.Chrome(options=chrome_options)

    #enter the site link
    driver.get("link to the site.")

    try:
        #enter the element to vote
        checkbox = driver.find_element(By.XPATH, "element to vote.")

        if not checkbox.is_selected():
            checkbox.click()
            print("Checkbox has been selected!")
        else:
            print("Checkbox is already selected!")

        #enter the submit button
        button = driver.find_element(By.CLASS_NAME, "submit button.")
        button.click()

    except Exception as e:
        print(f"An error occurred: {e}")

    driver.quit()

async def main():
    while True:
        await asyncio.sleep(1)
        with ThreadPoolExecutor() as executor:
            loop = asyncio.get_event_loop()
            futures = [loop.run_in_executor(executor, dota) for _ in range(5)]
            await asyncio.gather(*futures)


asyncio.run(main())