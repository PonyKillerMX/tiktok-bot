# discord human impersonator 
from paths import * 
import asyncio 
from pyppeteer import * 
from time import sleep 


async def main():  
    # open browser and go to url

    browser = await launch(headless= False)
    page = await browser.newPage()
    tiktok = await page.goto(URL)
    await page.click(phone_email)
    print("done")
    '''
    browser = await  launch(headless=False);
    page = await browser.newPage();
    await page.goto('https://www.tiktok.com/login/phone-oremail/email');
    await page.type('input[name=email]', 'email', delay =20)
    await page.type('input[name=password]', 'password', delay20)'''

    '''login_button = await page.click(login)
    sleep(10)
    #await page.waitForSelector(phone_email)
    await page.click(phone_email)'''
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

    
    try:
        await page.waitForSelector(admin_role_tag)
        print("This man is an admin")
    except:
        print("Admin found")


    screen_shot = await page.screenshot(screenshot)
    print("Took ss") 
    # Select I'm not a robot'''
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

