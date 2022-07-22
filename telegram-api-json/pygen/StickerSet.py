
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#stickerset# ['This object represents a sticker set.']
class StickerSet(DefaultType):

    
	# @var name Sticker set name
	@property
	def name(self) -> String:
		return self._d["name"]
	# @var title Sticker set title
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var is_animated True, if the sticker set contains animated stickers
	@property
	def is_animated(self) -> Boolean:
		return self._d["is_animated"]
	# @var is_video True, if the sticker set contains video stickers
	@property
	def is_video(self) -> Boolean:
		return self._d["is_video"]
	# @var contains_masks True, if the sticker set contains masks
	@property
	def contains_masks(self) -> Boolean:
		return self._d["contains_masks"]
	# @var stickers List of all set stickers
	@property
	def stickers(self) -> Array of Sticker:
		return self._d["stickers"]
	# @var thumb Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format
	@property
	def thumb(self) -> PhotoSize:
		return self._d["thumb"]

