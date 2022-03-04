# Send Message

## Description
This is a project that provides three examples in which a user can a request with the Infobip api for sending Email, SMS and WhatsApp message. The project is built on Python 3.

## Installation
This project can be installed either by downloading the file from the Github repository or by doing a pull from this project. 

## Files
### main
This is the main file that runs the project and sends the request from three methods taken from the email, sms and whatsapp module. The file can be run automatically if the Developer uses PyCharm or IDE that is specifically built for Python.
    ###
    python main.py

### config
This is the module that holds the configuration information of the Api key, Base url, Mobile number, Recipient and sender email. The sender email is from the demo account so this can be tweaked or replace with the Infobip account in order to make request or send email. Replacing the email variable with the demo account, and also replacing the api key and base url. 

  ### Developer Email request: 
      1. mail_url - This is the Base Url that sends the post request for the Mail module
      2. mail_api_key - This is the Api Key that is configured from the Mail module and replaced by the developer api key
      3. sender_email - This is the service email set from the Infobip from the Mail module and can be replaced by the developer send email
      4. email - This is the recipent email from the user that can be replaced by the developer email account
  
  ### Developer SMS request -
      1. sms_url - This is the Base Url that sends the post request for the SMS module
      2. sms_api_key - This is the Api Key that is configured for the SMS module and replaced by the developer api key
      3. mobile_number - This is the mobile number set from the Infobip from the SMS module and can be replaced by the developer mobile number
  
  ### Developer WhatsApp request - 
      1. whatsapp_url - This is the Base Url that sends the post request for the WhatsApp module
      2. whatsapp_api_key - This is the Api Key that is configured from the WhatsApp module and replaced by the developer api key
      3. media_url - This is the media or thumbnail that can be set by the developer
      4. sender - This is the service mobile number from Infobip that sends the message to the WhatsApp number during test

### mail_request
This module holds the function that would send a Mail to the user by collecting the email address from the config module

### sms_request
This module holds the function that would send a SMS request to the user by collecting the mobile number from the config module

### whatsapp_request
This module holds the function that would send a WhatsApp request to the user by collecting the mobile number from the config module and uses the request template library.
