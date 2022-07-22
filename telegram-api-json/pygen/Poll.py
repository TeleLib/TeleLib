
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#poll# ['This object contains information about a poll.']
class Poll(DefaultType):

    
	# @var id Unique poll identifier
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var question Poll question, 1-300 characters
	@property
	def question(self) -> String:
		return self._d["question"]
	# @var options List of poll options
	@property
	def options(self) -> Array of PollOption:
		return self._d["options"]
	# @var total_voter_count Total number of users that voted in the poll
	@property
	def total_voter_count(self) -> Integer:
		return self._d["total_voter_count"]
	# @var is_closed True, if the poll is closed
	@property
	def is_closed(self) -> Boolean:
		return self._d["is_closed"]
	# @var is_anonymous True, if the poll is anonymous
	@property
	def is_anonymous(self) -> Boolean:
		return self._d["is_anonymous"]
	# @var type Poll type, currently can be "regular" or "quiz"
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var allows_multiple_answers True, if the poll allows multiple answers
	@property
	def allows_multiple_answers(self) -> Boolean:
		return self._d["allows_multiple_answers"]
	# @var correct_option_id Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
	@property
	def correct_option_id(self) -> Integer:
		return self._d["correct_option_id"]
	# @var explanation Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
	@property
	def explanation(self) -> String:
		return self._d["explanation"]
	# @var explanation_entities Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
	@property
	def explanation_entities(self) -> Array of MessageEntity:
		return self._d["explanation_entities"]
	# @var open_period Optional. Amount of time in seconds the poll will be active after creation
	@property
	def open_period(self) -> Integer:
		return self._d["open_period"]
	# @var close_date Optional. Point in time (Unix timestamp) when the poll will be automatically closed
	@property
	def close_date(self) -> Integer:
		return self._d["close_date"]

