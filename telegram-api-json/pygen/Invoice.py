
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#invoice# ['This object contains basic information about an invoice.']
class Invoice(DefaultType):

    
	# @var title Product name
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var description Product description
	@property
	def description(self) -> String:
		return self._d["description"]
	# @var start_parameter Unique bot deep-linking parameter that can be used to generate this invoice
	@property
	def start_parameter(self) -> String:
		return self._d["start_parameter"]
	# @var currency Three-letter ISO 4217 currency code
	@property
	def currency(self) -> String:
		return self._d["currency"]
	# @var total_amount Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
	@property
	def total_amount(self) -> Integer:
		return self._d["total_amount"]

