
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultarticle# ['Represents a link to an article or web page.']
class InlineQueryResultArticle(DefaultType):

    
	# @var type Type of the result, must be article
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 Bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var title Title of the result
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var input_message_content Content of the message to be sent
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]
	# @var reply_markup Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]
	# @var url Optional. URL of the result
	@property
	def url(self) -> String:
		return self._d["url"]
	# @var hide_url Optional. Pass True, if you don't want the URL to be shown in the message
	@property
	def hide_url(self) -> Boolean:
		return self._d["hide_url"]
	# @var description Optional. Short description of the result
	@property
	def description(self) -> String:
		return self._d["description"]
	# @var thumb_url Optional. Url of the thumbnail for the result
	@property
	def thumb_url(self) -> String:
		return self._d["thumb_url"]
	# @var thumb_width Optional. Thumbnail width
	@property
	def thumb_width(self) -> Integer:
		return self._d["thumb_width"]
	# @var thumb_height Optional. Thumbnail height
	@property
	def thumb_height(self) -> Integer:
		return self._d["thumb_height"]

