import requests as re
from send_sms import client,send_whatsapp_text
def get_quote_of_the_day(category):
    url =  "https://quotes.rest/qod?language=en&category={}".format(category)

    response = re.get(url=url)
    data = response.json()
    status = response.status_code
    match status:
        case 200:
            quote = data["contents"]["quotes"][0]['quote']
        case 400:
            quote = data['error']['message']
        case _:
            quote = "Sorry, Couldn't retireve code "            
    return quote
    
quote = get_quote_of_the_day(category="inspire")
send_whatsapp_text(client,quote)