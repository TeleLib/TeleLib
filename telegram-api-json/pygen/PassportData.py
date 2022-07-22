
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#passportdata# ['Describes Telegram Passport data shared with the bot by the user.']
class PassportData(DefaultType):

    
	# @var data Array with information about documents and other Telegram Passport elements that was shared with the bot
	@property
	def data(self) -> Array of EncryptedPassportElement:
		return self._d["data"]
	# @var credentials Encrypted credentials required to decrypt the data
	@property
	def credentials(self) -> EncryptedCredentials:
		return self._d["credentials"]

