
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#choseninlineresult# ['Represents a result of an inline query that was chosen by the user and sent to their chat partner.', 'Note: It is necessary to enable inline feedback via @BotFather in order to receive these objects in updates.']
class ChosenInlineResult(DefaultType):

    
	# @var result_id The unique identifier for the result that was chosen
	@property
	def result_id(self) -> String:
		return self._d["result_id"]
	# @var from The user that chose the result
	@property
	def from(self) -> User:
		return self._d["from"]
	# @var location Optional. Sender location, only for bots that require user location
	@property
	def location(self) -> Location:
		return self._d["location"]
	# @var inline_message_id Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
	@property
	def inline_message_id(self) -> String:
		return self._d["inline_message_id"]
	# @var query The query that was used to obtain the result
	@property
	def query(self) -> String:
		return self._d["query"]

