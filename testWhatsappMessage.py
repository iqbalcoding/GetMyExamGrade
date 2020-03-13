from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client('AC5feaff7948a64e99e3f9b83f0790f465','530a1cda40368fc79e8cdc0355db509b')

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+4915736367003'

client.messages.create(body='Ahoy, world!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)