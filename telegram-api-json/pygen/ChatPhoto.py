
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatphoto# ['This object represents a chat photo.']
class ChatPhoto(DefaultType):

    
	# @var small_file_id File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
	@property
	def small_file_id(self) -> String:
		return self._d["small_file_id"]
	# @var small_file_unique_id Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def small_file_unique_id(self) -> String:
		return self._d["small_file_unique_id"]
	# @var big_file_id File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
	@property
	def big_file_id(self) -> String:
		return self._d["big_file_id"]
	# @var big_file_unique_id Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def big_file_unique_id(self) -> String:
		return self._d["big_file_unique_id"]

