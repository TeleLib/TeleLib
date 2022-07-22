
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#responseparameters# ['Describes why a request was unsuccessful.']
class ResponseParameters(DefaultType):

    
	# @var migrate_to_chat_id Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def migrate_to_chat_id(self) -> Integer:
		return self._d["migrate_to_chat_id"]
	# @var retry_after Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
	@property
	def retry_after(self) -> Integer:
		return self._d["retry_after"]

