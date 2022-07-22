
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#message# ['This object represents a message.']
class Message(DefaultType):

    
	# @var message_id Unique message identifier inside this chat
	@property
	def message_id(self) -> Integer:
		return self._d["message_id"]
	# @var from Optional. Sender of the message; empty for messages sent to channels. For backward compatibility, the field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
	@property
	def from(self) -> User:
		return self._d["from"]
	# @var sender_chat Optional. Sender of the message, sent on behalf of a chat. For example, the channel itself for channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
	@property
	def sender_chat(self) -> Chat:
		return self._d["sender_chat"]
	# @var date Date the message was sent in Unix time
	@property
	def date(self) -> Integer:
		return self._d["date"]
	# @var chat Conversation the message belongs to
	@property
	def chat(self) -> Chat:
		return self._d["chat"]
	# @var forward_from Optional. For forwarded messages, sender of the original message
	@property
	def forward_from(self) -> User:
		return self._d["forward_from"]
	# @var forward_from_chat Optional. For messages forwarded from channels or from anonymous administrators, information about the original sender chat
	@property
	def forward_from_chat(self) -> Chat:
		return self._d["forward_from_chat"]
	# @var forward_from_message_id Optional. For messages forwarded from channels, identifier of the original message in the channel
	@property
	def forward_from_message_id(self) -> Integer:
		return self._d["forward_from_message_id"]
	# @var forward_signature Optional. For forwarded messages that were originally sent in channels or by an anonymous chat administrator, signature of the message sender if present
	@property
	def forward_signature(self) -> String:
		return self._d["forward_signature"]
	# @var forward_sender_name Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
	@property
	def forward_sender_name(self) -> String:
		return self._d["forward_sender_name"]
	# @var forward_date Optional. For forwarded messages, date the original message was sent in Unix time
	@property
	def forward_date(self) -> Integer:
		return self._d["forward_date"]
	# @var is_automatic_forward Optional. True, if the message is a channel post that was automatically forwarded to the connected discussion group
	@property
	def is_automatic_forward(self) -> Boolean:
		return self._d["is_automatic_forward"]
	# @var reply_to_message Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
	@property
	def reply_to_message(self) -> Message:
		return self._d["reply_to_message"]
	# @var via_bot Optional. Bot through which the message was sent
	@property
	def via_bot(self) -> User:
		return self._d["via_bot"]
	# @var edit_date Optional. Date the message was last edited in Unix time
	@property
	def edit_date(self) -> Integer:
		return self._d["edit_date"]
	# @var has_protected_content Optional. True, if the message can't be forwarded
	@property
	def has_protected_content(self) -> Boolean:
		return self._d["has_protected_content"]
	# @var media_group_id Optional. The unique identifier of a media message group this message belongs to
	@property
	def media_group_id(self) -> String:
		return self._d["media_group_id"]
	# @var author_signature Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
	@property
	def author_signature(self) -> String:
		return self._d["author_signature"]
	# @var text Optional. For text messages, the actual UTF-8 text of the message
	@property
	def text(self) -> String:
		return self._d["text"]
	# @var entities Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
	@property
	def entities(self) -> Array of MessageEntity:
		return self._d["entities"]
	# @var animation Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
	@property
	def animation(self) -> Animation:
		return self._d["animation"]
	# @var audio Optional. Message is an audio file, information about the file
	@property
	def audio(self) -> Audio:
		return self._d["audio"]
	# @var document Optional. Message is a general file, information about the file
	@property
	def document(self) -> Document:
		return self._d["document"]
	# @var photo Optional. Message is a photo, available sizes of the photo
	@property
	def photo(self) -> Array of PhotoSize:
		return self._d["photo"]
	# @var sticker Optional. Message is a sticker, information about the sticker
	@property
	def sticker(self) -> Sticker:
		return self._d["sticker"]
	# @var video Optional. Message is a video, information about the video
	@property
	def video(self) -> Video:
		return self._d["video"]
	# @var video_note Optional. Message is a video note, information about the video message
	@property
	def video_note(self) -> VideoNote:
		return self._d["video_note"]
	# @var voice Optional. Message is a voice message, information about the file
	@property
	def voice(self) -> Voice:
		return self._d["voice"]
	# @var caption Optional. Caption for the animation, audio, document, photo, video or voice
	@property
	def caption(self) -> String:
		return self._d["caption"]
	# @var caption_entities Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
	@property
	def caption_entities(self) -> Array of MessageEntity:
		return self._d["caption_entities"]
	# @var contact Optional. Message is a shared contact, information about the contact
	@property
	def contact(self) -> Contact:
		return self._d["contact"]
	# @var dice Optional. Message is a dice with random value
	@property
	def dice(self) -> Dice:
		return self._d["dice"]
	# @var game Optional. Message is a game, information about the game. More about games: https://core.telegram.org/bots/api#games
	@property
	def game(self) -> Game:
		return self._d["game"]
	# @var poll Optional. Message is a native poll, information about the poll
	@property
	def poll(self) -> Poll:
		return self._d["poll"]
	# @var venue Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
	@property
	def venue(self) -> Venue:
		return self._d["venue"]
	# @var location Optional. Message is a shared location, information about the location
	@property
	def location(self) -> Location:
		return self._d["location"]
	# @var new_chat_members Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
	@property
	def new_chat_members(self) -> Array of User:
		return self._d["new_chat_members"]
	# @var left_chat_member Optional. A member was removed from the group, information about them (this member may be the bot itself)
	@property
	def left_chat_member(self) -> User:
		return self._d["left_chat_member"]
	# @var new_chat_title Optional. A chat title was changed to this value
	@property
	def new_chat_title(self) -> String:
		return self._d["new_chat_title"]
	# @var new_chat_photo Optional. A chat photo was change to this value
	@property
	def new_chat_photo(self) -> Array of PhotoSize:
		return self._d["new_chat_photo"]
	# @var delete_chat_photo Optional. Service message: the chat photo was deleted
	@property
	def delete_chat_photo(self) -> Boolean:
		return self._d["delete_chat_photo"]
	# @var group_chat_created Optional. Service message: the group has been created
	@property
	def group_chat_created(self) -> Boolean:
		return self._d["group_chat_created"]
	# @var supergroup_chat_created Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
	@property
	def supergroup_chat_created(self) -> Boolean:
		return self._d["supergroup_chat_created"]
	# @var channel_chat_created Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
	@property
	def channel_chat_created(self) -> Boolean:
		return self._d["channel_chat_created"]
	# @var message_auto_delete_timer_changed Optional. Service message: auto-delete timer settings changed in the chat
	@property
	def message_auto_delete_timer_changed(self) -> MessageAutoDeleteTimerChanged:
		return self._d["message_auto_delete_timer_changed"]
	# @var migrate_to_chat_id Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def migrate_to_chat_id(self) -> Integer:
		return self._d["migrate_to_chat_id"]
	# @var migrate_from_chat_id Optional. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def migrate_from_chat_id(self) -> Integer:
		return self._d["migrate_from_chat_id"]
	# @var pinned_message Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
	@property
	def pinned_message(self) -> Message:
		return self._d["pinned_message"]
	# @var invoice Optional. Message is an invoice for a payment, information about the invoice. More about payments: https://core.telegram.org/bots/api#payments
	@property
	def invoice(self) -> Invoice:
		return self._d["invoice"]
	# @var successful_payment Optional. Message is a service message about a successful payment, information about the payment. More about payments: https://core.telegram.org/bots/api#payments
	@property
	def successful_payment(self) -> SuccessfulPayment:
		return self._d["successful_payment"]
	# @var connected_website Optional. The domain name of the website on which the user has logged in. More about Telegram Login: https://core.telegram.org/widgets/login
	@property
	def connected_website(self) -> String:
		return self._d["connected_website"]
	# @var passport_data Optional. Telegram Passport data
	@property
	def passport_data(self) -> PassportData:
		return self._d["passport_data"]
	# @var proximity_alert_triggered Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
	@property
	def proximity_alert_triggered(self) -> ProximityAlertTriggered:
		return self._d["proximity_alert_triggered"]
	# @var video_chat_scheduled Optional. Service message: video chat scheduled
	@property
	def video_chat_scheduled(self) -> VideoChatScheduled:
		return self._d["video_chat_scheduled"]
	# @var video_chat_started Optional. Service message: video chat started
	@property
	def video_chat_started(self) -> VideoChatStarted:
		return self._d["video_chat_started"]
	# @var video_chat_ended Optional. Service message: video chat ended
	@property
	def video_chat_ended(self) -> VideoChatEnded:
		return self._d["video_chat_ended"]
	# @var video_chat_participants_invited Optional. Service message: new participants invited to a video chat
	@property
	def video_chat_participants_invited(self) -> VideoChatParticipantsInvited:
		return self._d["video_chat_participants_invited"]
	# @var web_app_data Optional. Service message: data sent by a Web App
	@property
	def web_app_data(self) -> WebAppData:
		return self._d["web_app_data"]
	# @var reply_markup Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]

