
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#document# ['This object represents a general file (as opposed to photos, voice messages and audio files).']
class Document(DefaultType):

    
	# @var file_id Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> String:
		return self._d["file_id"]
	# @var file_unique_id Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> String:
		return self._d["file_unique_id"]
	# @var thumb Optional. Document thumbnail as defined by sender
	@property
	def thumb(self) -> PhotoSize:
		return self._d["thumb"]
	# @var file_name Optional. Original filename as defined by sender
	@property
	def file_name(self) -> String:
		return self._d["file_name"]
	# @var mime_type Optional. MIME type of the file as defined by sender
	@property
	def mime_type(self) -> String:
		return self._d["mime_type"]
	# @var file_size Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
	@property
	def file_size(self) -> Integer:
		return self._d["file_size"]

