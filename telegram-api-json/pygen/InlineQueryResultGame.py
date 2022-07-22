
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultgame# ['Represents a Game.', 'Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.']
class InlineQueryResultGame(DefaultType):

    
	# @var type Type of the result, must be game
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var game_short_name Short name of the game
	@property
	def game_short_name(self) -> String:
		return self._d["game_short_name"]
	# @var reply_markup Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]

