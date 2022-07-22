
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#videonote# ['This object represents a video message (available in Telegram apps as of v.4.0).']
class VideoNote(DefaultType):

    
	# @var file_id Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> String:
		return self._d["file_id"]
	# @var file_unique_id Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> String:
		return self._d["file_unique_id"]
	# @var length Video width and height (diameter of the video message) as defined by sender
	@property
	def length(self) -> Integer:
		return self._d["length"]
	# @var duration Duration of the video in seconds as defined by sender
	@property
	def duration(self) -> Integer:
		return self._d["duration"]
	# @var thumb Optional. Video thumbnail
	@property
	def thumb(self) -> PhotoSize:
		return self._d["thumb"]
	# @var file_size Optional. File size in bytes
	@property
	def file_size(self) -> Integer:
		return self._d["file_size"]

