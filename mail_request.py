import requests
import re
import config

def send_mail():
    try:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # A check is carried out on the email to see if it is valid
        if re.fullmatch(regex, config.email):
            subject = "Scott Email"
            body = "This is sent from my local device."

            # The data is sent to be post
            data = {
                "from": config.sender_email,
                "to": config.email,
                "subject": subject,
                "text": body
            }

            # It sets the api key and base url from the config library
            headers = {"Authorization": config.mail_api_key}
            response = requests.post(config.mail_url, files = data, headers = headers)

            # It checks if the response was successful and returns an output
            if response.status_code == 200:
                print("Email sent to: ", config.email)
            else:
                print("Email failed")
        else:
            print("Email is Invalid")
            exit()
    except ConnectionError:
        print("Connection failed")