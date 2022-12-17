from twilio.rest import Client 
import config  
 


def set_twilio_connection():
    client = Client(config.account_sid, config.auth_token) 
    return client
def send_whatsapp_text(client, quote):
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=quote,      
                                to=config.phone_number 
                            ) 
    return message.sid
     

client = set_twilio_connection()
