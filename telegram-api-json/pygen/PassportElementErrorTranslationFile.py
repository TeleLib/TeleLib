
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#passportelementerrortranslationfile# ['Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.']
class PassportElementErrorTranslationFile(DefaultType):

    
	# @var source Error source, must be translation_file
	@property
	def source(self) -> String:
		return self._d["source"]
	# @var type Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
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

