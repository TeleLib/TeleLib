
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#passportelementerrorfiles# ['Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.']
class PassportElementErrorFiles(DefaultType):

    
	# @var source Error source, must be files
	@property
	def source(self) -> String:
		return self._d["source"]
	# @var type The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var file_hashes List of base64-encoded file hashes
	@property
	def file_hashes(self) -> Array of String:
		return self._d["file_hashes"]
	# @var message Error message
	@property
	def message(self) -> String:
		return self._d["message"]

