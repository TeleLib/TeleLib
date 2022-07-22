
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#encryptedcredentials# ['Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.']
class EncryptedCredentials(DefaultType):

    
	# @var data Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication
	@property
	def data(self) -> String:
		return self._d["data"]
	# @var hash Base64-encoded data hash for data authentication
	@property
	def hash(self) -> String:
		return self._d["hash"]
	# @var secret Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption
	@property
	def secret(self) -> String:
		return self._d["secret"]

