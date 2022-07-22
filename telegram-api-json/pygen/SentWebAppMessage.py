
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#sentwebappmessage# ['Describes an inline message sent by a Web App on behalf of a user.']
class SentWebAppMessage(DefaultType):

    
	# @var inline_message_id Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message.
	@property
	def inline_message_id(self) -> String:
		return self._d["inline_message_id"]

