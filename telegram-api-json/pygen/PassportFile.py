
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#passportfile# ["This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB."]
class PassportFile(DefaultType):

    
	# @var file_id Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> String:
		return self._d["file_id"]
	# @var file_unique_id Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> String:
		return self._d["file_unique_id"]
	# @var file_size File size in bytes
	@property
	def file_size(self) -> Integer:
		return self._d["file_size"]
	# @var file_date Unix time when the file was uploaded
	@property
	def file_date(self) -> Integer:
		return self._d["file_date"]

