import asyncio
from pyppeteer import launch
import time

import requests

TOKEN = '7473102298:AAFvb8NVvq5P6hZVix2v8XenFaxfx4i-hZ4'
chat_id = '-4258369848'


def send_message(msg: str):
    message = f'Randevu acik({msg}): \nhttps://vizedefterim.com/randevuTakip/Hollanda'
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())


async def main():
    browser = await launch(executablePath='/usr/bin/google-chrome-stable', headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://vizedefterim.com/randevuTakip/Hollanda')
    time.sleep(10)
    result = await page.evaluate('''()=>{ 
    var xl = document.getElementsByClassName('MuiTypography-h4'); 
    const max_len = xl.length; 
    for(var i = 0; i < max_len; i++)
    {
        if ('Antalya' == xl[i].outerText)
        {
            console.log('Found it!!'); 
            return xl[i].nextElementSibling.textContent;
        }
    }
    return 'Antalya bulunamadi';
    }
    ''')

    print(result)
    if ('Uygun' not in result and 'Antalya bulunamadi' not in result):
        send_message(result)
    else:
        pass
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()


for _ in range(999):
    print('starting!!!')
    asyncio.get_event_loop().run_until_complete(main())
    time.sleep(30)
