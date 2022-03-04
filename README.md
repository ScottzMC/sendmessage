# Send Message

## Description
This is a project that provides three examples in which a user can a request with the Infobip api for sending Email, SMS and WhatsApp message. The project is built on Python 3.

## Installation
This project can be installed either by downloading the file from the Github repository or by doing a pull from this project. 

## Files
### main
This is the main file that runs the project and sends the request from three methods taken from the email, sms and whatsapp module. The file can be run automatically if the Developer uses PyCharm or IDE that is specifically built for Python, or the alternative method of python {file_name} such as: python main.py

### config
This is the module that holds the configuration information of the Api key, Base url, Mobile number, Recipient and sender email. The sender email is from the demo account so this can be tweaked or replace with the Infobip account in order to make request or send email. Replacing the email variable with the demo account, and also replacing the api key and base url. 

  1. Developer Email request
  2. Developer SMS request
  3. Developer WhatsApp request

### test_formatter
This class or files carries out test from the pytest library on the various functions imported and used by the formatter module. This class checks if those functions passes or failes the objective of what they are to achieve. The file can be run automatically if the Developer uses PyCharm or IDE that is specifically built for Python, or the alternative method of python {file_name} such as: python test_formatter.py
