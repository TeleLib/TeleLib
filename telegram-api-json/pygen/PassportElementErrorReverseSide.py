
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#passportelementerrorreverseside# ['Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.']
class PassportElementErrorReverseSide(DefaultType):

    
	# @var source Error source, must be reverse_side
	@property
	def source(self) -> String:
		return self._d["source"]
	# @var type The section of the user's Telegram Passport which has the issue, one of "driver_license", "identity_card"
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var file_hash Base64-encoded hash of the file with the reverse side of the document
	@property
	def file_hash(self) -> String:
		return self._d["file_hash"]
	# @var message Error message
	@property
	def message(self) -> String:
		return self._d["message"]

