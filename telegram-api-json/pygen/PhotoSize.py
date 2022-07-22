
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#photosize# ['This object represents one size of a photo or a file / sticker thumbnail.']
class PhotoSize(DefaultType):

    
	# @var file_id Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> String:
		return self._d["file_id"]
	# @var file_unique_id Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> String:
		return self._d["file_unique_id"]
	# @var width Photo width
	@property
	def width(self) -> Integer:
		return self._d["width"]
	# @var height Photo height
	@property
	def height(self) -> Integer:
		return self._d["height"]
	# @var file_size Optional. File size in bytes
	@property
	def file_size(self) -> Integer:
		return self._d["file_size"]

