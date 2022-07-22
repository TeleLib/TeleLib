
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#dice# ['This object represents an animated emoji that displays a random value.']
class Dice(DefaultType):

    
	# @var emoji Emoji on which the dice throw animation is based
	@property
	def emoji(self) -> String:
		return self._d["emoji"]
	# @var value Value of the dice, 1-6 for "🎲", "🎯" and "🎳" base emoji, 1-5 for "🏀" and "⚽" base emoji, 1-64 for "🎰" base emoji
	@property
	def value(self) -> Integer:
		return self._d["value"]

