
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#passportelementerrorselfie# ['Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.']
class PassportElementErrorSelfie(DefaultType):

    
	# @var source Error source, must be selfie
	@property
	def source(self) -> String:
		return self._d["source"]
	# @var type The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport"
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var file_hash Base64-encoded hash of the file with the selfie
	@property
	def file_hash(self) -> String:
		return self._d["file_hash"]
	# @var message Error message
	@property
	def message(self) -> String:
		return self._d["message"]

