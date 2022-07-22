
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#webappdata# ['Describes data sent from a Web App to the bot.']
class WebAppData(DefaultType):

    
	# @var data The data. Be aware that a bad client can send arbitrary data in this field.
	@property
	def data(self) -> String:
		return self._d["data"]
	# @var button_text Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field.
	@property
	def button_text(self) -> String:
		return self._d["button_text"]

