
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#encryptedpassportelement# ['Describes documents or other Telegram Passport elements shared with the bot by the user.']
class EncryptedPassportElement(DefaultType):

    
	# @var type Element type. One of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration", "phone_number", "email".
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var data Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for "personal_details", "passport", "driver_license", "identity_card", "internal_passport" and "address" types. Can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def data(self) -> String:
		return self._d["data"]
	# @var phone_number Optional. User's verified phone number, available only for "phone_number" type
	@property
	def phone_number(self) -> String:
		return self._d["phone_number"]
	# @var email Optional. User's verified email address, available only for "email" type
	@property
	def email(self) -> String:
		return self._d["email"]
	# @var files Optional. Array of encrypted files with documents provided by the user, available for "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and "temporary_registration" types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def files(self) -> Array of PassportFile:
		return self._d["files"]
	# @var front_side Optional. Encrypted file with the front side of the document, provided by the user. Available for "passport", "driver_license", "identity_card" and "internal_passport". The file can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def front_side(self) -> PassportFile:
		return self._d["front_side"]
	# @var reverse_side Optional. Encrypted file with the reverse side of the document, provided by the user. Available for "driver_license" and "identity_card". The file can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def reverse_side(self) -> PassportFile:
		return self._d["reverse_side"]
	# @var selfie Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for "passport", "driver_license", "identity_card" and "internal_passport". The file can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def selfie(self) -> PassportFile:
		return self._d["selfie"]
	# @var translation Optional. Array of encrypted files with translated versions of documents provided by the user. Available if requested for "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and "temporary_registration" types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def translation(self) -> Array of PassportFile:
		return self._d["translation"]
	# @var hash Base64-encoded element hash for using in PassportElementErrorUnspecified
	@property
	def hash(self) -> String:
		return self._d["hash"]

