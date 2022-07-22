
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#keyboardbuttonpolltype# ['This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.']
class KeyboardButtonPollType(DefaultType):

    
	# @var type Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
	@property
	def type(self) -> String:
		return self._d["type"]

