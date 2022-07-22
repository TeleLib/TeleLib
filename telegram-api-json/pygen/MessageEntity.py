
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#messageentity# ['This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.']
class MessageEntity(DefaultType):

    
	# @var type Type of the entity. Currently, can be "mention" (@username), "hashtag" (#hashtag), "cashtag" ($USD), "bot_command" (/start@jobs_bot), "url" (https://telegram.org), "email" (do-not-reply@telegram.org), "phone_number" (+1-212-555-0123), "bold" (bold text), "italic" (italic text), "underline" (underlined text), "strikethrough" (strikethrough text), "spoiler" (spoiler message), "code" (monowidth string), "pre" (monowidth block), "text_link" (for clickable text URLs), "text_mention" (for users without usernames)
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var offset Offset in UTF-16 code units to the start of the entity
	@property
	def offset(self) -> Integer:
		return self._d["offset"]
	# @var length Length of the entity in UTF-16 code units
	@property
	def length(self) -> Integer:
		return self._d["length"]
	# @var url Optional. For "text_link" only, URL that will be opened after user taps on the text
	@property
	def url(self) -> String:
		return self._d["url"]
	# @var user Optional. For "text_mention" only, the mentioned user
	@property
	def user(self) -> User:
		return self._d["user"]
	# @var language Optional. For "pre" only, the programming language of the entity text
	@property
	def language(self) -> String:
		return self._d["language"]

