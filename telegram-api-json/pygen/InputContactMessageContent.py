
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inputcontactmessagecontent# ['Represents the content of a contact message to be sent as the result of an inline query.']
class InputContactMessageContent(DefaultType):

    
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

