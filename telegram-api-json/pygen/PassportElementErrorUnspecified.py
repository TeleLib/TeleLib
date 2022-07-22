
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#passportelementerrorunspecified# ['Represents an issue in an unspecified place. The error is considered resolved when new data is added.']
class PassportElementErrorUnspecified(DefaultType):

    
	# @var source Error source, must be unspecified
	@property
	def source(self) -> String:
		return self._d["source"]
	# @var type Type of element of the user's Telegram Passport which has the issue
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var element_hash Base64-encoded element hash
	@property
	def element_hash(self) -> String:
		return self._d["element_hash"]
	# @var message Error message
	@property
	def message(self) -> String:
		return self._d["message"]

