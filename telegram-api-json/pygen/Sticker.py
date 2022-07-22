
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#sticker# ['This object represents a sticker.']
class Sticker(DefaultType):

    
	# @var file_id Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> String:
		return self._d["file_id"]
	# @var file_unique_id Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> String:
		return self._d["file_unique_id"]
	# @var width Sticker width
	@property
	def width(self) -> Integer:
		return self._d["width"]
	# @var height Sticker height
	@property
	def height(self) -> Integer:
		return self._d["height"]
	# @var is_animated True, if the sticker is animated
	@property
	def is_animated(self) -> Boolean:
		return self._d["is_animated"]
	# @var is_video True, if the sticker is a video sticker
	@property
	def is_video(self) -> Boolean:
		return self._d["is_video"]
	# @var thumb Optional. Sticker thumbnail in the .WEBP or .JPG format
	@property
	def thumb(self) -> PhotoSize:
		return self._d["thumb"]
	# @var emoji Optional. Emoji associated with the sticker
	@property
	def emoji(self) -> String:
		return self._d["emoji"]
	# @var set_name Optional. Name of the sticker set to which the sticker belongs
	@property
	def set_name(self) -> String:
		return self._d["set_name"]
	# @var premium_animation Optional. Premium animation for the sticker, if the sticker is premium
	@property
	def premium_animation(self) -> File:
		return self._d["premium_animation"]
	# @var mask_position Optional. For mask stickers, the position where the mask should be placed
	@property
	def mask_position(self) -> MaskPosition:
		return self._d["mask_position"]
	# @var file_size Optional. File size in bytes
	@property
	def file_size(self) -> Integer:
		return self._d["file_size"]

