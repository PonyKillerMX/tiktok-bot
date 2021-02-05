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

    screen_shot = await page.screenshot(screenshot)
    print("Took ss") 
    await browser.close() 


asyncio.get_event_loop().run_until_complete(main())
