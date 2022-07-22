
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#menubuttonwebapp# ['Represents a menu button, which launches a Web App.']
class MenuButtonWebApp(DefaultType):

    
	# @var type Type of the button, must be web_app
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var text Text on the button
	@property
	def text(self) -> String:
		return self._d["text"]
	# @var web_app Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery.
	@property
	def web_app(self) -> WebAppInfo:
		return self._d["web_app"]

