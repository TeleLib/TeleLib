
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#passportelementerrortranslationfiles# ['Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.']
class PassportElementErrorTranslationFiles(DefaultType):

    
	# @var source Error source, must be translation_files
	@property
	def source(self) -> String:
		return self._d["source"]
	# @var type Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
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

