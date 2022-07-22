
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#gamehighscore# ['This object represents one row of the high scores table for a game.']
class GameHighScore(DefaultType):

    
	# @var position Position in high score table for the game
	@property
	def position(self) -> Integer:
		return self._d["position"]
	# @var user User
	@property
	def user(self) -> User:
		return self._d["user"]
	# @var score Score
	@property
	def score(self) -> Integer:
		return self._d["score"]

