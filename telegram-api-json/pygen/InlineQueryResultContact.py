
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultcontact# ['Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.', 'Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.']
class InlineQueryResultContact(DefaultType):

    
	# @var type Type of the result, must be contact
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 Bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var phone_number Contact's phone number
	@property
	def phone_number(self) -> String:
		return self._d["phone_number"]
	# @var first_name Contact's first name
	@property
	def first_name(self) -> String:
		return self._d["first_name"]
	# @var last_name Optional. Contact's last name
	@property
	def last_name(self) -> String:
		return self._d["last_name"]
	# @var vcard Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
	@property
	def vcard(self) -> String:
		return self._d["vcard"]
	# @var reply_markup Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]
	# @var input_message_content Optional. Content of the message to be sent instead of the contact
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]
	# @var thumb_url Optional. Url of the thumbnail for the result
	@property
	def thumb_url(self) -> String:
		return self._d["thumb_url"]
	# @var thumb_width Optional. Thumbnail width
	@property
	def thumb_width(self) -> Integer:
		return self._d["thumb_width"]
	# @var thumb_height Optional. Thumbnail height
	@property
	def thumb_height(self) -> Integer:
		return self._d["thumb_height"]

