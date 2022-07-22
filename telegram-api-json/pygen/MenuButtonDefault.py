
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#menubuttondefault# ['Describes that no specific value for the menu button was set.']
class MenuButtonDefault(DefaultType):

    
	# @var type Type of the button, must be default
	@property
	def type(self) -> String:
		return self._d["type"]

