
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chat# ['This object represents a chat.']
class Chat(DefaultType):

    
	# @var id Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def id(self) -> Integer:
		return self._d["id"]
	# @var type Type of chat, can be either "private", "group", "supergroup" or "channel"
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var title Optional. Title, for supergroups, channels and group chats
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var username Optional. Username, for private chats, supergroups and channels if available
	@property
	def username(self) -> String:
		return self._d["username"]
	# @var first_name Optional. First name of the other party in a private chat
	@property
	def first_name(self) -> String:
		return self._d["first_name"]
	# @var last_name Optional. Last name of the other party in a private chat
	@property
	def last_name(self) -> String:
		return self._d["last_name"]
	# @var photo Optional. Chat photo. Returned only in getChat.
	@property
	def photo(self) -> ChatPhoto:
		return self._d["photo"]
	# @var bio Optional. Bio of the other party in a private chat. Returned only in getChat.
	@property
	def bio(self) -> String:
		return self._d["bio"]
	# @var has_private_forwards Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat.
	@property
	def has_private_forwards(self) -> Boolean:
		return self._d["has_private_forwards"]
	# @var join_to_send_messages Optional. True, if users need to join the supergroup before they can send messages. Returned only in getChat.
	@property
	def join_to_send_messages(self) -> Boolean:
		return self._d["join_to_send_messages"]
	# @var join_by_request Optional. True, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat.
	@property
	def join_by_request(self) -> Boolean:
		return self._d["join_by_request"]
	# @var description Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.
	@property
	def description(self) -> String:
		return self._d["description"]
	# @var invite_link Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.
	@property
	def invite_link(self) -> String:
		return self._d["invite_link"]
	# @var pinned_message Optional. The most recent pinned message (by sending date). Returned only in getChat.
	@property
	def pinned_message(self) -> Message:
		return self._d["pinned_message"]
	# @var permissions Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
	@property
	def permissions(self) -> ChatPermissions:
		return self._d["permissions"]
	# @var slow_mode_delay Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat.
	@property
	def slow_mode_delay(self) -> Integer:
		return self._d["slow_mode_delay"]
	# @var message_auto_delete_time Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.
	@property
	def message_auto_delete_time(self) -> Integer:
		return self._d["message_auto_delete_time"]
	# @var has_protected_content Optional. True, if messages from the chat can't be forwarded to other chats. Returned only in getChat.
	@property
	def has_protected_content(self) -> Boolean:
		return self._d["has_protected_content"]
	# @var sticker_set_name Optional. For supergroups, name of group sticker set. Returned only in getChat.
	@property
	def sticker_set_name(self) -> String:
		return self._d["sticker_set_name"]
	# @var can_set_sticker_set Optional. True, if the bot can change the group sticker set. Returned only in getChat.
	@property
	def can_set_sticker_set(self) -> Boolean:
		return self._d["can_set_sticker_set"]
	# @var linked_chat_id Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.
	@property
	def linked_chat_id(self) -> Integer:
		return self._d["linked_chat_id"]
	# @var location Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat.
	@property
	def location(self) -> ChatLocation:
		return self._d["location"]

