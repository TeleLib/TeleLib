
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#keyboardbutton# ['This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields web_app, request_contact, request_location, and request_poll are mutually exclusive.', 'Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.', 'Note: request_poll option will only work in Telegram versions released after 23 January, 2020. Older clients will display unsupported message.', 'Note: web_app option will only work in Telegram versions released after 16 April, 2022. Older clients will display unsupported message.']
class KeyboardButton(DefaultType):

    
	# @var text Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
	@property
	def text(self) -> String:
		return self._d["text"]
	# @var request_contact Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only.
	@property
	def request_contact(self) -> Boolean:
		return self._d["request_contact"]
	# @var request_location Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only.
	@property
	def request_location(self) -> Boolean:
		return self._d["request_location"]
	# @var request_poll Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only.
	@property
	def request_poll(self) -> KeyboardButtonPollType:
		return self._d["request_poll"]
	# @var web_app Optional. If specified, the described Web App will be launched when the button is pressed. The Web App will be able to send a "web_app_data" service message. Available in private chats only.
	@property
	def web_app(self) -> WebAppInfo:
		return self._d["web_app"]

