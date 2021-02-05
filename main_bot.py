# discord human impersonator 
from paths import * 
import asyncio 
from pyppeteer import * 
from time import sleep 


async def main():  
    # open browser and go to url
    
    # personal preference emi: headless True
    browser = await launch(headless=True)
    page = await browser.newPage()
    tiktok = await page.goto(URL)
    await page.click(phone_email)
    print("done")
    sleep(30)

    screen_shot = await page.screenshot(screenshot)
    # username
    '''await page.waitForSelector(email_selector)
    await page.click(email_selector)
    await page.type(email_selector, username)
    
    # password
    await page.waitForSelector(pass_selector)
    await page.click(pass_selector)
    await page.type(pass_selector, password)

    # login button after putting usrname and pass
    await page.waitForSelector(login_button_string) 
    login_button2 = await page.click(login_button_string)   
    sleep(5) 


    screen_shot = await page.screenshot(screenshot)
    print("Took ss") '''
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

