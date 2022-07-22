
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#user# ['This object represents a Telegram user or bot.']
class User(DefaultType):

    
	# @var id Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def id(self) -> Integer:
		return self._d["id"]
	# @var is_bot True, if this user is a bot
	@property
	def is_bot(self) -> Boolean:
		return self._d["is_bot"]
	# @var first_name User's or bot's first name
	@property
	def first_name(self) -> String:
		return self._d["first_name"]
	# @var last_name Optional. User's or bot's last name
	@property
	def last_name(self) -> String:
		return self._d["last_name"]
	# @var username Optional. User's or bot's username
	@property
	def username(self) -> String:
		return self._d["username"]
	# @var language_code Optional. IETF language tag of the user's language
	@property
	def language_code(self) -> String:
		return self._d["language_code"]
	# @var is_premium Optional. True, if this user is a Telegram Premium user
	@property
	def is_premium(self) -> Boolean:
		return self._d["is_premium"]
	# @var added_to_attachment_menu Optional. True, if this user added the bot to the attachment menu
	@property
	def added_to_attachment_menu(self) -> Boolean:
		return self._d["added_to_attachment_menu"]
	# @var can_join_groups Optional. True, if the bot can be invited to groups. Returned only in getMe.
	@property
	def can_join_groups(self) -> Boolean:
		return self._d["can_join_groups"]
	# @var can_read_all_group_messages Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
	@property
	def can_read_all_group_messages(self) -> Boolean:
		return self._d["can_read_all_group_messages"]
	# @var supports_inline_queries Optional. True, if the bot supports inline queries. Returned only in getMe.
	@property
	def supports_inline_queries(self) -> Boolean:
		return self._d["supports_inline_queries"]

