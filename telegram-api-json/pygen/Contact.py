
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#contact# ['This object represents a phone contact.']
class Contact(DefaultType):

    
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
	# @var user_id Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def user_id(self) -> Integer:
		return self._d["user_id"]
	# @var vcard Optional. Additional data about the contact in the form of a vCard
	@property
	def vcard(self) -> String:
		return self._d["vcard"]

