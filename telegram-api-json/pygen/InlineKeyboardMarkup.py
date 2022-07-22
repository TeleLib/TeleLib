
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinekeyboardmarkup# ['This object represents an inline keyboard that appears right next to the message it belongs to.', 'Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.']
class InlineKeyboardMarkup(DefaultType):

    
	# @var inline_keyboard Array of button rows, each represented by an Array of InlineKeyboardButton objects
	@property
	def inline_keyboard(self) -> Array of Array of InlineKeyboardButton:
		return self._d["inline_keyboard"]

