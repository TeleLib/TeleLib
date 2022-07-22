
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultcachedsticker# ['Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.', 'Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.']
class InlineQueryResultCachedSticker(DefaultType):

    
	# @var type Type of the result, must be sticker
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var sticker_file_id A valid file identifier of the sticker
	@property
	def sticker_file_id(self) -> String:
		return self._d["sticker_file_id"]
	# @var reply_markup Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]
	# @var input_message_content Optional. Content of the message to be sent instead of the sticker
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]

