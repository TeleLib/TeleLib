
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#game# ['This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.']
class Game(DefaultType):

    
	# @var title Title of the game
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var description Description of the game
	@property
	def description(self) -> String:
		return self._d["description"]
	# @var photo Photo that will be displayed in the game message in chats.
	@property
	def photo(self) -> Array of PhotoSize:
		return self._d["photo"]
	# @var text Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
	@property
	def text(self) -> String:
		return self._d["text"]
	# @var text_entities Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
	@property
	def text_entities(self) -> Array of MessageEntity:
		return self._d["text_entities"]
	# @var animation Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
	@property
	def animation(self) -> Animation:
		return self._d["animation"]

