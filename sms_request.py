import config

from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException

def send_sms_to_phone():
    sender = "Scott SMS"
    message = "This is a test message that has been sent from my local device"

    # Sets the base url and api key from the config module
    client_config = Configuration(
        host = config.sms_url,
        api_key = {"APIKeyHeader": config.sms_api_key},
        api_key_prefix = {"APIKeyHeader": "App"}
    )

    api_client = ApiClient(client_config)

    # It creates the request on the target destination
    sms_request = SmsAdvancedTextualRequest(
        messages = [
            SmsTextualMessage(
                destinations = [SmsDestination(to = config.mobile_number)],
                _from = sender,
                text = message,
            )
        ]
    )

    api_instance = SendSmsApi(api_client)

    # It does a check to see if the API request was successful or failed
    try:
        api_instance.send_sms_message(sms_advanced_textual_request = sms_request)
        print("SMS sent")
    except ApiException as ex:
        print("Error occurred while trying to send SMS message.", ex)