
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#passportelementerrordatafield# ["Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes."]
class PassportElementErrorDataField(DefaultType):

    
	# @var source Error source, must be data
	@property
	def source(self) -> String:
		return self._d["source"]
	# @var type The section of the user's Telegram Passport which has the error, one of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address"
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var field_name Name of the data field which has the error
	@property
	def field_name(self) -> String:
		return self._d["field_name"]
	# @var data_hash Base64-encoded data hash
	@property
	def data_hash(self) -> String:
		return self._d["data_hash"]
	# @var message Error message
	@property
	def message(self) -> String:
		return self._d["message"]

