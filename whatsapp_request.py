import requests
import config

def send_chat():
    # Configuring the payload to display the message and send the request to the recipient
    payload = {
        "messages":
            [
                {
                    "from": config.sender,
                    "to": config.mobile_number,
                    "content": {
                        "templateName": "registration_success",
                        "templateData": {
                            "body": {"placeholders": ["sender", "message", "delivered", "testing"]},
                            "header": {"type": "IMAGE","mediaUrl": config.media_url},
                            "buttons": [
                                {"type": "QUICK_REPLY","parameter": "yes-payload"},
                                {"type": "QUICK_REPLY","parameter": "no-payload"},
                                {"type": "QUICK_REPLY", "parameter": "later-payload"}
                            ]
                        },
                        "language": "en"
                    }
                }
            ]
    }

    # Setting the API key
    headers = {'Authorization': config.whatsapp_api_key, 'Content-Type': 'application/json', 'Accept': 'application/json'}
    # Setting the base url and loading the payload that is in a JSON format
    requests.post(config.whatsapp_url, json = payload, headers = headers)
    print("WhatsApp message sent")