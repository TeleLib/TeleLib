
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#maskposition# ['This object describes the position on faces where a mask should be placed by default.']
class MaskPosition(DefaultType):

    
	# @var point The part of the face relative to which the mask should be placed. One of "forehead", "eyes", "mouth", or "chin".
	@property
	def point(self) -> String:
		return self._d["point"]
	# @var x_shift Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
	@property
	def x_shift(self) -> Float:
		return self._d["x_shift"]
	# @var y_shift Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
	@property
	def y_shift(self) -> Float:
		return self._d["y_shift"]
	# @var scale Mask scaling coefficient. For example, 2.0 means double size.
	@property
	def scale(self) -> Float:
		return self._d["scale"]

