#tik tok video uploader
from paths import * 
import asyncio 
from pyppeteer import * 
from time import sleep

async def main(): 
    # Let's open browser and go to url 
    browser = await launch()
    page = await browser.newPage() 
    tiktok = await page.goto(URL)
    print("Opened tiktok")    
    # Click on login button 
    click_upload_video = await page.click(upload_video) 
    # Click on the login with username button
    print("Clicked on upload video") 
    sleep(5) 
    click_user_await = await page.waitForSelector(login_username)
    click_user = await page.click(login_username) 
    print("Clicked on username login") 
    screen_shot = await page.screenshot(screenshot)
    print("Took ss") 
    await browser.close() 


asyncio.get_event_loop().run_until_complete(main())
