#tik tok video uploader
from paths import * 
import asyncio 
from pyppeteer import * 
from time import sleep

async def main(): 
    # Let's open browser and go to url 
    browser = await launch()
    page = await browser.newPage() 
    tiktok = await page.goto("https://www.tiktok.com")
    
    # Click on login button 
    click_upload_video = await page.click("#main > div.jsx-1217828260.header-container.white.middle > div > div.jsx-2365341634.menu-right > div > div > span > svg > path") 

    sleep(5) 
    screen_shot = await page.screenshot(screenshot)
    print("Took ss") 
    await browser.close() 


asyncio.get_event_loop().run_until_complete(main())
