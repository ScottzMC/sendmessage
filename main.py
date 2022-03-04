import mail_request
import sms_request
import whatsapp_request

# This runs the Mail request function
mail_request.send_mail()
# This runs the SMS request function
sms_request.send_sms_to_phone()
# This runs the WhatsApp request function
whatsapp_request.send_chat()