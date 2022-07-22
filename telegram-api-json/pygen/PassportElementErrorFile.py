
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#passportelementerrorfile# ['Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.']
class PassportElementErrorFile(DefaultType):

    
	# @var source Error source, must be file
	@property
	def source(self) -> String:
		return self._d["source"]
	# @var type The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var file_hash Base64-encoded file hash
	@property
	def file_hash(self) -> String:
		return self._d["file_hash"]
	# @var message Error message
	@property
	def message(self) -> String:
		return self._d["message"]

