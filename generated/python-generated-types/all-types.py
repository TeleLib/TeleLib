from telelib.bot import DefaultType

class Integer(int):
	...

class String(str):
	...

class Float(float):
	...

Boolean = bool


# @url https://core.telegram.org/bots/api#update
# This object represents an incoming update., At most one of the optional parameters can be present in any given update.
class Update(DefaultType):

    


	# The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
	@property
	def update_id(self) -> "Integer":
		return self._d["update_id"]


	# Optional. New incoming message of any kind - text, photo, sticker, etc.
	@property
	def message(self) -> "Message":
		return self._d["message"]


	# Optional. New version of a message that is known to the bot and was edited
	@property
	def edited_message(self) -> "Message":
		return self._d["edited_message"]


	# Optional. New incoming channel post of any kind - text, photo, sticker, etc.
	@property
	def channel_post(self) -> "Message":
		return self._d["channel_post"]


	# Optional. New version of a channel post that is known to the bot and was edited
	@property
	def edited_channel_post(self) -> "Message":
		return self._d["edited_channel_post"]


	# Optional. New incoming inline query
	@property
	def inline_query(self) -> "InlineQuery":
		return self._d["inline_query"]


	# Optional. The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
	@property
	def chosen_inline_result(self) -> "ChosenInlineResult":
		return self._d["chosen_inline_result"]


	# Optional. New incoming callback query
	@property
	def callback_query(self) -> "CallbackQuery":
		return self._d["callback_query"]


	# Optional. New incoming shipping query. Only for invoices with flexible price
	@property
	def shipping_query(self) -> "ShippingQuery":
		return self._d["shipping_query"]


	# Optional. New incoming pre-checkout query. Contains full information about checkout
	@property
	def pre_checkout_query(self) -> "PreCheckoutQuery":
		return self._d["pre_checkout_query"]


	# Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
	@property
	def poll(self) -> "Poll":
		return self._d["poll"]


	# Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
	@property
	def poll_answer(self) -> "PollAnswer":
		return self._d["poll_answer"]


	# Optional. The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.
	@property
	def my_chat_member(self) -> "ChatMemberUpdated":
		return self._d["my_chat_member"]


	# Optional. A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify "chat_member" in the list of allowed_updates to receive these updates.
	@property
	def chat_member(self) -> "ChatMemberUpdated":
		return self._d["chat_member"]


	# Optional. A request to join the chat has been sent. The bot must have the can_invite_users administrator right in the chat to receive these updates.
	@property
	def chat_join_request(self) -> "ChatJoinRequest":
		return self._d["chat_join_request"]




# @url https://core.telegram.org/bots/api#webhookinfo
# Describes the current status of a webhook.
class WebhookInfo(DefaultType):

    


	# Webhook URL, may be empty if webhook is not set up
	@property
	def url(self) -> "String":
		return self._d["url"]


	# True, if a custom certificate was provided for webhook certificate checks
	@property
	def has_custom_certificate(self) -> "Boolean":
		return self._d["has_custom_certificate"]


	# Number of updates awaiting delivery
	@property
	def pending_update_count(self) -> "Integer":
		return self._d["pending_update_count"]


	# Optional. Currently used webhook IP address
	@property
	def ip_address(self) -> "String":
		return self._d["ip_address"]


	# Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
	@property
	def last_error_date(self) -> "Integer":
		return self._d["last_error_date"]


	# Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
	@property
	def last_error_message(self) -> "String":
		return self._d["last_error_message"]


	# Optional. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters
	@property
	def last_synchronization_error_date(self) -> "Integer":
		return self._d["last_synchronization_error_date"]


	# Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
	@property
	def max_connections(self) -> "Integer":
		return self._d["max_connections"]


	# Optional. A list of update types the bot is subscribed to. Defaults to all update types except chat_member
	@property
	def allowed_updates(self) -> "Array of String":
		return self._d["allowed_updates"]




# @url https://core.telegram.org/bots/api#user
# This object represents a Telegram user or bot.
class User(DefaultType):

    


	# Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def id(self) -> "Integer":
		return self._d["id"]


	# True, if this user is a bot
	@property
	def is_bot(self) -> "Boolean":
		return self._d["is_bot"]


	# User's or bot's first name
	@property
	def first_name(self) -> "String":
		return self._d["first_name"]


	# Optional. User's or bot's last name
	@property
	def last_name(self) -> "String":
		return self._d["last_name"]


	# Optional. User's or bot's username
	@property
	def username(self) -> "String":
		return self._d["username"]


	# Optional. IETF language tag of the user's language
	@property
	def language_code(self) -> "String":
		return self._d["language_code"]


	# Optional. True, if this user is a Telegram Premium user
	@property
	def is_premium(self) -> "Boolean":
		return self._d["is_premium"]


	# Optional. True, if this user added the bot to the attachment menu
	@property
	def added_to_attachment_menu(self) -> "Boolean":
		return self._d["added_to_attachment_menu"]


	# Optional. True, if the bot can be invited to groups. Returned only in getMe.
	@property
	def can_join_groups(self) -> "Boolean":
		return self._d["can_join_groups"]


	# Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
	@property
	def can_read_all_group_messages(self) -> "Boolean":
		return self._d["can_read_all_group_messages"]


	# Optional. True, if the bot supports inline queries. Returned only in getMe.
	@property
	def supports_inline_queries(self) -> "Boolean":
		return self._d["supports_inline_queries"]




# @url https://core.telegram.org/bots/api#chat
# This object represents a chat.
class Chat(DefaultType):

    


	# Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def id(self) -> "Integer":
		return self._d["id"]


	# Type of chat, can be either "private", "group", "supergroup" or "channel"
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Optional. Title, for supergroups, channels and group chats
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Username, for private chats, supergroups and channels if available
	@property
	def username(self) -> "String":
		return self._d["username"]


	# Optional. First name of the other party in a private chat
	@property
	def first_name(self) -> "String":
		return self._d["first_name"]


	# Optional. Last name of the other party in a private chat
	@property
	def last_name(self) -> "String":
		return self._d["last_name"]


	# Optional. Chat photo. Returned only in getChat.
	@property
	def photo(self) -> "ChatPhoto":
		return self._d["photo"]


	# Optional. Bio of the other party in a private chat. Returned only in getChat.
	@property
	def bio(self) -> "String":
		return self._d["bio"]


	# Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat.
	@property
	def has_private_forwards(self) -> "Boolean":
		return self._d["has_private_forwards"]


	# Optional. True, if users need to join the supergroup before they can send messages. Returned only in getChat.
	@property
	def join_to_send_messages(self) -> "Boolean":
		return self._d["join_to_send_messages"]


	# Optional. True, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat.
	@property
	def join_by_request(self) -> "Boolean":
		return self._d["join_by_request"]


	# Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.
	@property
	def invite_link(self) -> "String":
		return self._d["invite_link"]


	# Optional. The most recent pinned message (by sending date). Returned only in getChat.
	@property
	def pinned_message(self) -> "Message":
		return self._d["pinned_message"]


	# Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
	@property
	def permissions(self) -> "ChatPermissions":
		return self._d["permissions"]


	# Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat.
	@property
	def slow_mode_delay(self) -> "Integer":
		return self._d["slow_mode_delay"]


	# Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.
	@property
	def message_auto_delete_time(self) -> "Integer":
		return self._d["message_auto_delete_time"]


	# Optional. True, if messages from the chat can't be forwarded to other chats. Returned only in getChat.
	@property
	def has_protected_content(self) -> "Boolean":
		return self._d["has_protected_content"]


	# Optional. For supergroups, name of group sticker set. Returned only in getChat.
	@property
	def sticker_set_name(self) -> "String":
		return self._d["sticker_set_name"]


	# Optional. True, if the bot can change the group sticker set. Returned only in getChat.
	@property
	def can_set_sticker_set(self) -> "Boolean":
		return self._d["can_set_sticker_set"]


	# Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.
	@property
	def linked_chat_id(self) -> "Integer":
		return self._d["linked_chat_id"]


	# Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat.
	@property
	def location(self) -> "ChatLocation":
		return self._d["location"]




# @url https://core.telegram.org/bots/api#message
# This object represents a message.
class Message(DefaultType):

    


	# Unique message identifier inside this chat
	@property
	def message_id(self) -> "Integer":
		return self._d["message_id"]


	# Optional. Sender of the message; empty for messages sent to channels. For backward compatibility, the field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
	@property
	def from_(self) -> "User":
		return self._d["from"]


	# Optional. Sender of the message, sent on behalf of a chat. For example, the channel itself for channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
	@property
	def sender_chat(self) -> "Chat":
		return self._d["sender_chat"]


	# Date the message was sent in Unix time
	@property
	def date(self) -> "Integer":
		return self._d["date"]


	# Conversation the message belongs to
	@property
	def chat(self) -> "Chat":
		return self._d["chat"]


	# Optional. For forwarded messages, sender of the original message
	@property
	def forward_from_(self) -> "User":
		return self._d["forward_from"]


	# Optional. For messages forwarded from channels or from anonymous administrators, information about the original sender chat
	@property
	def forward_from__chat(self) -> "Chat":
		return self._d["forward_from_chat"]


	# Optional. For messages forwarded from channels, identifier of the original message in the channel
	@property
	def forward_from__message_id(self) -> "Integer":
		return self._d["forward_from_message_id"]


	# Optional. For forwarded messages that were originally sent in channels or by an anonymous chat administrator, signature of the message sender if present
	@property
	def forward_signature(self) -> "String":
		return self._d["forward_signature"]


	# Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
	@property
	def forward_sender_name(self) -> "String":
		return self._d["forward_sender_name"]


	# Optional. For forwarded messages, date the original message was sent in Unix time
	@property
	def forward_date(self) -> "Integer":
		return self._d["forward_date"]


	# Optional. True, if the message is a channel post that was automatically forwarded to the connected discussion group
	@property
	def is_automatic_forward(self) -> "Boolean":
		return self._d["is_automatic_forward"]


	# Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
	@property
	def reply_to_message(self) -> "Message":
		return self._d["reply_to_message"]


	# Optional. Bot through which the message was sent
	@property
	def via_bot(self) -> "User":
		return self._d["via_bot"]


	# Optional. Date the message was last edited in Unix time
	@property
	def edit_date(self) -> "Integer":
		return self._d["edit_date"]


	# Optional. True, if the message can't be forwarded
	@property
	def has_protected_content(self) -> "Boolean":
		return self._d["has_protected_content"]


	# Optional. The unique identifier of a media message group this message belongs to
	@property
	def media_group_id(self) -> "String":
		return self._d["media_group_id"]


	# Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
	@property
	def author_signature(self) -> "String":
		return self._d["author_signature"]


	# Optional. For text messages, the actual UTF-8 text of the message
	@property
	def text(self) -> "String":
		return self._d["text"]


	# Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
	@property
	def entities(self) -> "Array of MessageEntity":
		return self._d["entities"]


	# Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
	@property
	def animation(self) -> "Animation":
		return self._d["animation"]


	# Optional. Message is an audio file, information about the file
	@property
	def audio(self) -> "Audio":
		return self._d["audio"]


	# Optional. Message is a general file, information about the file
	@property
	def document(self) -> "Document":
		return self._d["document"]


	# Optional. Message is a photo, available sizes of the photo
	@property
	def photo(self) -> "Array of PhotoSize":
		return self._d["photo"]


	# Optional. Message is a sticker, information about the sticker
	@property
	def sticker(self) -> "Sticker":
		return self._d["sticker"]


	# Optional. Message is a video, information about the video
	@property
	def video(self) -> "Video":
		return self._d["video"]


	# Optional. Message is a video note, information about the video message
	@property
	def video_note(self) -> "VideoNote":
		return self._d["video_note"]


	# Optional. Message is a voice message, information about the file
	@property
	def voice(self) -> "Voice":
		return self._d["voice"]


	# Optional. Caption for the animation, audio, document, photo, video or voice
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Message is a shared contact, information about the contact
	@property
	def contact(self) -> "Contact":
		return self._d["contact"]


	# Optional. Message is a dice with random value
	@property
	def dice(self) -> "Dice":
		return self._d["dice"]


	# Optional. Message is a game, information about the game. More about games: https://core.telegram.org/bots/api#games
	@property
	def game(self) -> "Game":
		return self._d["game"]


	# Optional. Message is a native poll, information about the poll
	@property
	def poll(self) -> "Poll":
		return self._d["poll"]


	# Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
	@property
	def venue(self) -> "Venue":
		return self._d["venue"]


	# Optional. Message is a shared location, information about the location
	@property
	def location(self) -> "Location":
		return self._d["location"]


	# Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
	@property
	def new_chat_members(self) -> "Array of User":
		return self._d["new_chat_members"]


	# Optional. A member was removed from the group, information about them (this member may be the bot itself)
	@property
	def left_chat_member(self) -> "User":
		return self._d["left_chat_member"]


	# Optional. A chat title was changed to this value
	@property
	def new_chat_title(self) -> "String":
		return self._d["new_chat_title"]


	# Optional. A chat photo was change to this value
	@property
	def new_chat_photo(self) -> "Array of PhotoSize":
		return self._d["new_chat_photo"]


	# Optional. Service message: the chat photo was deleted
	@property
	def delete_chat_photo(self) -> "Boolean":
		return self._d["delete_chat_photo"]


	# Optional. Service message: the group has been created
	@property
	def group_chat_created(self) -> "Boolean":
		return self._d["group_chat_created"]


	# Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
	@property
	def supergroup_chat_created(self) -> "Boolean":
		return self._d["supergroup_chat_created"]


	# Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
	@property
	def channel_chat_created(self) -> "Boolean":
		return self._d["channel_chat_created"]


	# Optional. Service message: auto-delete timer settings changed in the chat
	@property
	def message_auto_delete_timer_changed(self) -> "MessageAutoDeleteTimerChanged":
		return self._d["message_auto_delete_timer_changed"]


	# Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def migrate_to_chat_id(self) -> "Integer":
		return self._d["migrate_to_chat_id"]


	# Optional. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def migrate_from__chat_id(self) -> "Integer":
		return self._d["migrate_from_chat_id"]


	# Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
	@property
	def pinned_message(self) -> "Message":
		return self._d["pinned_message"]


	# Optional. Message is an invoice for a payment, information about the invoice. More about payments: https://core.telegram.org/bots/api#payments
	@property
	def invoice(self) -> "Invoice":
		return self._d["invoice"]


	# Optional. Message is a service message about a successful payment, information about the payment. More about payments: https://core.telegram.org/bots/api#payments
	@property
	def successful_payment(self) -> "SuccessfulPayment":
		return self._d["successful_payment"]


	# Optional. The domain name of the website on which the user has logged in. More about Telegram Login: https://core.telegram.org/bots/api/widgets/login
	@property
	def connected_website(self) -> "String":
		return self._d["connected_website"]


	# Optional. Telegram Passport data
	@property
	def passport_data(self) -> "PassportData":
		return self._d["passport_data"]


	# Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
	@property
	def proximity_alert_triggered(self) -> "ProximityAlertTriggered":
		return self._d["proximity_alert_triggered"]


	# Optional. Service message: video chat scheduled
	@property
	def video_chat_scheduled(self) -> "VideoChatScheduled":
		return self._d["video_chat_scheduled"]


	# Optional. Service message: video chat started
	@property
	def video_chat_started(self) -> "VideoChatStarted":
		return self._d["video_chat_started"]


	# Optional. Service message: video chat ended
	@property
	def video_chat_ended(self) -> "VideoChatEnded":
		return self._d["video_chat_ended"]


	# Optional. Service message: new participants invited to a video chat
	@property
	def video_chat_participants_invited(self) -> "VideoChatParticipantsInvited":
		return self._d["video_chat_participants_invited"]


	# Optional. Service message: data sent by a Web App
	@property
	def web_app_data(self) -> "WebAppData":
		return self._d["web_app_data"]


	# Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]




# @url https://core.telegram.org/bots/api#messageid
# This object represents a unique message identifier.
class MessageId(DefaultType):

    


	# Unique message identifier
	@property
	def message_id(self) -> "Integer":
		return self._d["message_id"]




# @url https://core.telegram.org/bots/api#messageentity
# This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.
class MessageEntity(DefaultType):

    


	# Type of the entity. Currently, can be "mention" (@username), "hashtag" (#hashtag), "cashtag" ($USD), "bot_command" (/start@jobs_bot), "url" (https://telegram.org), "email" (do-not-reply@telegram.org), "phone_number" (+1-212-555-0123), "bold" (bold text), "italic" (italic text), "underline" (underlined text), "strikethrough" (strikethrough text), "spoiler" (spoiler message), "code" (monowidth string), "pre" (monowidth block), "text_link" (for clickable text URLs), "text_mention" (for users without usernames)
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Offset in UTF-16 code units to the start of the entity
	@property
	def offset(self) -> "Integer":
		return self._d["offset"]


	# Length of the entity in UTF-16 code units
	@property
	def length(self) -> "Integer":
		return self._d["length"]


	# Optional. For "text_link" only, URL that will be opened after user taps on the text
	@property
	def url(self) -> "String":
		return self._d["url"]


	# Optional. For "text_mention" only, the mentioned user
	@property
	def user(self) -> "User":
		return self._d["user"]


	# Optional. For "pre" only, the programming language of the entity text
	@property
	def language(self) -> "String":
		return self._d["language"]




# @url https://core.telegram.org/bots/api#photosize
# This object represents one size of a photo or a file / sticker thumbnail.
class PhotoSize(DefaultType):

    


	# Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> "String":
		return self._d["file_id"]


	# Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> "String":
		return self._d["file_unique_id"]


	# Photo width
	@property
	def width(self) -> "Integer":
		return self._d["width"]


	# Photo height
	@property
	def height(self) -> "Integer":
		return self._d["height"]


	# Optional. File size in bytes
	@property
	def file_size(self) -> "Integer":
		return self._d["file_size"]




# @url https://core.telegram.org/bots/api#animation
# This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).
class Animation(DefaultType):

    


	# Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> "String":
		return self._d["file_id"]


	# Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> "String":
		return self._d["file_unique_id"]


	# Video width as defined by sender
	@property
	def width(self) -> "Integer":
		return self._d["width"]


	# Video height as defined by sender
	@property
	def height(self) -> "Integer":
		return self._d["height"]


	# Duration of the video in seconds as defined by sender
	@property
	def duration(self) -> "Integer":
		return self._d["duration"]


	# Optional. Animation thumbnail as defined by sender
	@property
	def thumb(self) -> "PhotoSize":
		return self._d["thumb"]


	# Optional. Original animation filename as defined by sender
	@property
	def file_name(self) -> "String":
		return self._d["file_name"]


	# Optional. MIME type of the file as defined by sender
	@property
	def mime_type(self) -> "String":
		return self._d["mime_type"]


	# Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
	@property
	def file_size(self) -> "Integer":
		return self._d["file_size"]




# @url https://core.telegram.org/bots/api#audio
# This object represents an audio file to be treated as music by the Telegram clients.
class Audio(DefaultType):

    


	# Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> "String":
		return self._d["file_id"]


	# Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> "String":
		return self._d["file_unique_id"]


	# Duration of the audio in seconds as defined by sender
	@property
	def duration(self) -> "Integer":
		return self._d["duration"]


	# Optional. Performer of the audio as defined by sender or by audio tags
	@property
	def performer(self) -> "String":
		return self._d["performer"]


	# Optional. Title of the audio as defined by sender or by audio tags
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Original filename as defined by sender
	@property
	def file_name(self) -> "String":
		return self._d["file_name"]


	# Optional. MIME type of the file as defined by sender
	@property
	def mime_type(self) -> "String":
		return self._d["mime_type"]


	# Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
	@property
	def file_size(self) -> "Integer":
		return self._d["file_size"]


	# Optional. Thumbnail of the album cover to which the music file belongs
	@property
	def thumb(self) -> "PhotoSize":
		return self._d["thumb"]




# @url https://core.telegram.org/bots/api#document
# This object represents a general file (as opposed to photos, voice messages and audio files).
class Document(DefaultType):

    


	# Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> "String":
		return self._d["file_id"]


	# Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> "String":
		return self._d["file_unique_id"]


	# Optional. Document thumbnail as defined by sender
	@property
	def thumb(self) -> "PhotoSize":
		return self._d["thumb"]


	# Optional. Original filename as defined by sender
	@property
	def file_name(self) -> "String":
		return self._d["file_name"]


	# Optional. MIME type of the file as defined by sender
	@property
	def mime_type(self) -> "String":
		return self._d["mime_type"]


	# Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
	@property
	def file_size(self) -> "Integer":
		return self._d["file_size"]




# @url https://core.telegram.org/bots/api#video
# This object represents a video file.
class Video(DefaultType):

    


	# Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> "String":
		return self._d["file_id"]


	# Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> "String":
		return self._d["file_unique_id"]


	# Video width as defined by sender
	@property
	def width(self) -> "Integer":
		return self._d["width"]


	# Video height as defined by sender
	@property
	def height(self) -> "Integer":
		return self._d["height"]


	# Duration of the video in seconds as defined by sender
	@property
	def duration(self) -> "Integer":
		return self._d["duration"]


	# Optional. Video thumbnail
	@property
	def thumb(self) -> "PhotoSize":
		return self._d["thumb"]


	# Optional. Original filename as defined by sender
	@property
	def file_name(self) -> "String":
		return self._d["file_name"]


	# Optional. MIME type of the file as defined by sender
	@property
	def mime_type(self) -> "String":
		return self._d["mime_type"]


	# Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
	@property
	def file_size(self) -> "Integer":
		return self._d["file_size"]




# @url https://core.telegram.org/bots/api#videonote
# This object represents a video message (available in Telegram apps as of v.4.0).
class VideoNote(DefaultType):

    


	# Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> "String":
		return self._d["file_id"]


	# Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> "String":
		return self._d["file_unique_id"]


	# Video width and height (diameter of the video message) as defined by sender
	@property
	def length(self) -> "Integer":
		return self._d["length"]


	# Duration of the video in seconds as defined by sender
	@property
	def duration(self) -> "Integer":
		return self._d["duration"]


	# Optional. Video thumbnail
	@property
	def thumb(self) -> "PhotoSize":
		return self._d["thumb"]


	# Optional. File size in bytes
	@property
	def file_size(self) -> "Integer":
		return self._d["file_size"]




# @url https://core.telegram.org/bots/api#voice
# This object represents a voice note.
class Voice(DefaultType):

    


	# Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> "String":
		return self._d["file_id"]


	# Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> "String":
		return self._d["file_unique_id"]


	# Duration of the audio in seconds as defined by sender
	@property
	def duration(self) -> "Integer":
		return self._d["duration"]


	# Optional. MIME type of the file as defined by sender
	@property
	def mime_type(self) -> "String":
		return self._d["mime_type"]


	# Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
	@property
	def file_size(self) -> "Integer":
		return self._d["file_size"]




# @url https://core.telegram.org/bots/api#contact
# This object represents a phone contact.
class Contact(DefaultType):

    


	# Contact's phone number
	@property
	def phone_number(self) -> "String":
		return self._d["phone_number"]


	# Contact's first name
	@property
	def first_name(self) -> "String":
		return self._d["first_name"]


	# Optional. Contact's last name
	@property
	def last_name(self) -> "String":
		return self._d["last_name"]


	# Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def user_id(self) -> "Integer":
		return self._d["user_id"]


	# Optional. Additional data about the contact in the form of a vCard
	@property
	def vcard(self) -> "String":
		return self._d["vcard"]




# @url https://core.telegram.org/bots/api#dice
# This object represents an animated emoji that displays a random value.
class Dice(DefaultType):

    


	# Emoji on which the dice throw animation is based
	@property
	def emoji(self) -> "String":
		return self._d["emoji"]


	# Value of the dice, 1-6 for "🎲", "🎯" and "🎳" base emoji, 1-5 for "🏀" and "⚽" base emoji, 1-64 for "🎰" base emoji
	@property
	def value(self) -> "Integer":
		return self._d["value"]




# @url https://core.telegram.org/bots/api#polloption
# This object contains information about one answer option in a poll.
class PollOption(DefaultType):

    


	# Option text, 1-100 characters
	@property
	def text(self) -> "String":
		return self._d["text"]


	# Number of users that voted for this option
	@property
	def voter_count(self) -> "Integer":
		return self._d["voter_count"]




# @url https://core.telegram.org/bots/api#pollanswer
# This object represents an answer of a user in a non-anonymous poll.
class PollAnswer(DefaultType):

    


	# Unique poll identifier
	@property
	def poll_id(self) -> "String":
		return self._d["poll_id"]


	# The user, who changed the answer to the poll
	@property
	def user(self) -> "User":
		return self._d["user"]


	# 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.
	@property
	def option_ids(self) -> "Array of Integer":
		return self._d["option_ids"]




# @url https://core.telegram.org/bots/api#poll
# This object contains information about a poll.
class Poll(DefaultType):

    


	# Unique poll identifier
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Poll question, 1-300 characters
	@property
	def question(self) -> "String":
		return self._d["question"]


	# List of poll options
	@property
	def options(self) -> "Array of PollOption":
		return self._d["options"]


	# Total number of users that voted in the poll
	@property
	def total_voter_count(self) -> "Integer":
		return self._d["total_voter_count"]


	# True, if the poll is closed
	@property
	def is_closed(self) -> "Boolean":
		return self._d["is_closed"]


	# True, if the poll is anonymous
	@property
	def is_anonymous(self) -> "Boolean":
		return self._d["is_anonymous"]


	# Poll type, currently can be "regular" or "quiz"
	@property
	def type(self) -> "String":
		return self._d["type"]


	# True, if the poll allows multiple answers
	@property
	def allows_multiple_answers(self) -> "Boolean":
		return self._d["allows_multiple_answers"]


	# Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
	@property
	def correct_option_id(self) -> "Integer":
		return self._d["correct_option_id"]


	# Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
	@property
	def explanation(self) -> "String":
		return self._d["explanation"]


	# Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
	@property
	def explanation_entities(self) -> "Array of MessageEntity":
		return self._d["explanation_entities"]


	# Optional. Amount of time in seconds the poll will be active after creation
	@property
	def open_period(self) -> "Integer":
		return self._d["open_period"]


	# Optional. Point in time (Unix timestamp) when the poll will be automatically closed
	@property
	def close_date(self) -> "Integer":
		return self._d["close_date"]




# @url https://core.telegram.org/bots/api#location
# This object represents a point on the map.
class Location(DefaultType):

    


	# Longitude as defined by sender
	@property
	def longitude(self) -> "Float":
		return self._d["longitude"]


	# Latitude as defined by sender
	@property
	def latitude(self) -> "Float":
		return self._d["latitude"]


	# Optional. The radius of uncertainty for the location, measured in meters; 0-1500
	@property
	def horizontal_accuracy(self) -> "Float":
		return self._d["horizontal_accuracy"]


	# Optional. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.
	@property
	def live_period(self) -> "Integer":
		return self._d["live_period"]


	# Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
	@property
	def heading(self) -> "Integer":
		return self._d["heading"]


	# Optional. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
	@property
	def proximity_alert_radius(self) -> "Integer":
		return self._d["proximity_alert_radius"]




# @url https://core.telegram.org/bots/api#venue
# This object represents a venue.
class Venue(DefaultType):

    


	# Venue location. Can't be a live location
	@property
	def location(self) -> "Location":
		return self._d["location"]


	# Name of the venue
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Address of the venue
	@property
	def address(self) -> "String":
		return self._d["address"]


	# Optional. Foursquare identifier of the venue
	@property
	def foursquare_id(self) -> "String":
		return self._d["foursquare_id"]


	# Optional. Foursquare type of the venue. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
	@property
	def foursquare_type(self) -> "String":
		return self._d["foursquare_type"]


	# Optional. Google Places identifier of the venue
	@property
	def google_place_id(self) -> "String":
		return self._d["google_place_id"]


	# Optional. Google Places type of the venue. (See supported types.)
	@property
	def google_place_type(self) -> "String":
		return self._d["google_place_type"]




# @url https://core.telegram.org/bots/api#webappdata
# Describes data sent from a Web App to the bot.
class WebAppData(DefaultType):

    


	# The data. Be aware that a bad client can send arbitrary data in this field.
	@property
	def data(self) -> "String":
		return self._d["data"]


	# Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field.
	@property
	def button_text(self) -> "String":
		return self._d["button_text"]




# @url https://core.telegram.org/bots/api#proximityalerttriggered
# This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.
class ProximityAlertTriggered(DefaultType):

    


	# User that triggered the alert
	@property
	def traveler(self) -> "User":
		return self._d["traveler"]


	# User that set the alert
	@property
	def watcher(self) -> "User":
		return self._d["watcher"]


	# The distance between the users
	@property
	def distance(self) -> "Integer":
		return self._d["distance"]




# @url https://core.telegram.org/bots/api#messageautodeletetimerchanged
# This object represents a service message about a change in auto-delete timer settings.
class MessageAutoDeleteTimerChanged(DefaultType):

    


	# New auto-delete time for messages in the chat; in seconds
	@property
	def message_auto_delete_time(self) -> "Integer":
		return self._d["message_auto_delete_time"]




# @url https://core.telegram.org/bots/api#videochatscheduled
# This object represents a service message about a video chat scheduled in the chat.
class VideoChatScheduled(DefaultType):

    


	# Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator
	@property
	def start_date(self) -> "Integer":
		return self._d["start_date"]




# @url https://core.telegram.org/bots/api#videochatstarted
# This object represents a service message about a video chat started in the chat. Currently holds no information.
class VideoChatStarted(DefaultType):

    ...




# @url https://core.telegram.org/bots/api#videochatended
# This object represents a service message about a video chat ended in the chat.
class VideoChatEnded(DefaultType):

    


	# Video chat duration in seconds
	@property
	def duration(self) -> "Integer":
		return self._d["duration"]




# @url https://core.telegram.org/bots/api#videochatparticipantsinvited
# This object represents a service message about new members invited to a video chat.
class VideoChatParticipantsInvited(DefaultType):

    


	# New members that were invited to the video chat
	@property
	def users(self) -> "Array of User":
		return self._d["users"]




# @url https://core.telegram.org/bots/api#userprofilephotos
# This object represent a user's profile pictures.
class UserProfilePhotos(DefaultType):

    


	# Total number of profile pictures the target user has
	@property
	def total_count(self) -> "Integer":
		return self._d["total_count"]


	# Requested profile pictures (in up to 4 sizes each)
	@property
	def photos(self) -> "Array of Array of PhotoSize":
		return self._d["photos"]




# @url https://core.telegram.org/bots/api#file
# This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.
class File(DefaultType):

    


	# Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> "String":
		return self._d["file_id"]


	# Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> "String":
		return self._d["file_unique_id"]


	# Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
	@property
	def file_size(self) -> "Integer":
		return self._d["file_size"]


	# Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
	@property
	def file_path(self) -> "String":
		return self._d["file_path"]




# @url https://core.telegram.org/bots/api#webappinfo
# Describes a Web App.
class WebAppInfo(DefaultType):

    


	# An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps
	@property
	def url(self) -> "String":
		return self._d["url"]




# @url https://core.telegram.org/bots/api#replykeyboardmarkup
# This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).
class ReplyKeyboardMarkup(DefaultType):

    


	# Array of button rows, each represented by an Array of KeyboardButton objects
	@property
	def keyboard(self) -> "Array of Array of KeyboardButton":
		return self._d["keyboard"]


	# Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
	@property
	def resize_keyboard(self) -> "Boolean":
		return self._d["resize_keyboard"]


	# Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
	@property
	def one_time_keyboard(self) -> "Boolean":
		return self._d["one_time_keyboard"]


	# Optional. The placeholder to be shown in the input field when the keyboard is active; 1-64 characters
	@property
	def input_field_placeholder(self) -> "String":
		return self._d["input_field_placeholder"]


	# Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message. Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.
	@property
	def selective(self) -> "Boolean":
		return self._d["selective"]




# @url https://core.telegram.org/bots/api#keyboardbutton
# This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields web_app, request_contact, request_location, and request_poll are mutually exclusive., Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message., Note: request_poll option will only work in Telegram versions released after 23 January, 2020. Older clients will display unsupported message., Note: web_app option will only work in Telegram versions released after 16 April, 2022. Older clients will display unsupported message.
class KeyboardButton(DefaultType):

    


	# Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
	@property
	def text(self) -> "String":
		return self._d["text"]


	# Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only.
	@property
	def request_contact(self) -> "Boolean":
		return self._d["request_contact"]


	# Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only.
	@property
	def request_location(self) -> "Boolean":
		return self._d["request_location"]


	# Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only.
	@property
	def request_poll(self) -> "KeyboardButtonPollType":
		return self._d["request_poll"]


	# Optional. If specified, the described Web App will be launched when the button is pressed. The Web App will be able to send a "web_app_data" service message. Available in private chats only.
	@property
	def web_app(self) -> "WebAppInfo":
		return self._d["web_app"]




# @url https://core.telegram.org/bots/api#keyboardbuttonpolltype
# This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.
class KeyboardButtonPollType(DefaultType):

    


	# Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
	@property
	def type(self) -> "String":
		return self._d["type"]




# @url https://core.telegram.org/bots/api#replykeyboardremove
# Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).
class ReplyKeyboardRemove(DefaultType):

    


	# Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)
	@property
	def remove_keyboard(self) -> "Boolean":
		return self._d["remove_keyboard"]


	# Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message. Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
	@property
	def selective(self) -> "Boolean":
		return self._d["selective"]




# @url https://core.telegram.org/bots/api#inlinekeyboardmarkup
# This object represents an inline keyboard that appears right next to the message it belongs to., Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.
class InlineKeyboardMarkup(DefaultType):

    


	# Array of button rows, each represented by an Array of InlineKeyboardButton objects
	@property
	def inline_keyboard(self) -> "Array of Array of InlineKeyboardButton":
		return self._d["inline_keyboard"]




# @url https://core.telegram.org/bots/api#inlinekeyboardbutton
# This object represents one button of an inline keyboard. You must use exactly one of the optional fields.
class InlineKeyboardButton(DefaultType):

    


	# Label text on the button
	@property
	def text(self) -> "String":
		return self._d["text"]


	# Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings.
	@property
	def url(self) -> "String":
		return self._d["url"]


	# Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
	@property
	def callback_data(self) -> "String":
		return self._d["callback_data"]


	# Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only in private chats between a user and the bot.
	@property
	def web_app(self) -> "WebAppInfo":
		return self._d["web_app"]


	# Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
	@property
	def login_url(self) -> "LoginUrl":
		return self._d["login_url"]


	# Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm... actions - in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
	@property
	def switch_inline_query(self) -> "String":
		return self._d["switch_inline_query"]


	# Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options.
	@property
	def switch_inline_query_current_chat(self) -> "String":
		return self._d["switch_inline_query_current_chat"]


	# Optional. Description of the game that will be launched when the user presses the button. NOTE: This type of button must always be the first button in the first row.
	@property
	def callback_game(self) -> "CallbackGame":
		return self._d["callback_game"]


	# Optional. Specify True, to send a Pay button. NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages.
	@property
	def pay(self) -> "Boolean":
		return self._d["pay"]




# @url https://core.telegram.org/bots/api#loginurl
# This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:, Telegram apps support these buttons as of version 5.7.
class LoginUrl(DefaultType):

    


	# An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data. NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.
	@property
	def url(self) -> "String":
		return self._d["url"]


	# Optional. New text of the button in forwarded messages.
	@property
	def forward_text(self) -> "String":
		return self._d["forward_text"]


	# Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.
	@property
	def bot_username(self) -> "String":
		return self._d["bot_username"]


	# Optional. Pass True to request the permission for your bot to send messages to the user.
	@property
	def request_write_access(self) -> "Boolean":
		return self._d["request_write_access"]




# @url https://core.telegram.org/bots/api#callbackquery
# This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.
class CallbackQuery(DefaultType):

    


	# Unique identifier for this query
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Sender
	@property
	def from_(self) -> "User":
		return self._d["from"]


	# Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
	@property
	def message(self) -> "Message":
		return self._d["message"]


	# Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
	@property
	def inline_message_id(self) -> "String":
		return self._d["inline_message_id"]


	# Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
	@property
	def chat_instance(self) -> "String":
		return self._d["chat_instance"]


	# Optional. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data.
	@property
	def data(self) -> "String":
		return self._d["data"]


	# Optional. Short name of a Game to be returned, serves as the unique identifier for the game
	@property
	def game_short_name(self) -> "String":
		return self._d["game_short_name"]




# @url https://core.telegram.org/bots/api#forcereply
# Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.
class ForceReply(DefaultType):

    


	# Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
	@property
	def force_reply(self) -> "Boolean":
		return self._d["force_reply"]


	# Optional. The placeholder to be shown in the input field when the reply is active; 1-64 characters
	@property
	def input_field_placeholder(self) -> "String":
		return self._d["input_field_placeholder"]


	# Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
	@property
	def selective(self) -> "Boolean":
		return self._d["selective"]




# @url https://core.telegram.org/bots/api#chatphoto
# This object represents a chat photo.
class ChatPhoto(DefaultType):

    


	# File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
	@property
	def small_file_id(self) -> "String":
		return self._d["small_file_id"]


	# Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def small_file_unique_id(self) -> "String":
		return self._d["small_file_unique_id"]


	# File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
	@property
	def big_file_id(self) -> "String":
		return self._d["big_file_id"]


	# Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def big_file_unique_id(self) -> "String":
		return self._d["big_file_unique_id"]




# @url https://core.telegram.org/bots/api#chatinvitelink
# Represents an invite link for a chat.
class ChatInviteLink(DefaultType):

    


	# The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with "...".
	@property
	def invite_link(self) -> "String":
		return self._d["invite_link"]


	# Creator of the link
	@property
	def creator(self) -> "User":
		return self._d["creator"]


	# True, if users joining the chat via the link need to be approved by chat administrators
	@property
	def creates_join_request(self) -> "Boolean":
		return self._d["creates_join_request"]


	# True, if the link is primary
	@property
	def is_primary(self) -> "Boolean":
		return self._d["is_primary"]


	# True, if the link is revoked
	@property
	def is_revoked(self) -> "Boolean":
		return self._d["is_revoked"]


	# Optional. Invite link name
	@property
	def name(self) -> "String":
		return self._d["name"]


	# Optional. Point in time (Unix timestamp) when the link will expire or has been expired
	@property
	def expire_date(self) -> "Integer":
		return self._d["expire_date"]


	# Optional. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
	@property
	def member_limit(self) -> "Integer":
		return self._d["member_limit"]


	# Optional. Number of pending join requests created using this link
	@property
	def pending_join_request_count(self) -> "Integer":
		return self._d["pending_join_request_count"]




# @url https://core.telegram.org/bots/api#chatadministratorrights
# Represents the rights of an administrator in a chat.
class ChatAdministratorRights(DefaultType):

    


	# True, if the user's presence in the chat is hidden
	@property
	def is_anonymous(self) -> "Boolean":
		return self._d["is_anonymous"]


	# True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
	@property
	def can_manage_chat(self) -> "Boolean":
		return self._d["can_manage_chat"]


	# True, if the administrator can delete messages of other users
	@property
	def can_delete_messages(self) -> "Boolean":
		return self._d["can_delete_messages"]


	# True, if the administrator can manage video chats
	@property
	def can_manage_video_chats(self) -> "Boolean":
		return self._d["can_manage_video_chats"]


	# True, if the administrator can restrict, ban or unban chat members
	@property
	def can_restrict_members(self) -> "Boolean":
		return self._d["can_restrict_members"]


	# True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
	@property
	def can_promote_members(self) -> "Boolean":
		return self._d["can_promote_members"]


	# True, if the user is allowed to change the chat title, photo and other settings
	@property
	def can_change_info(self) -> "Boolean":
		return self._d["can_change_info"]


	# True, if the user is allowed to invite new users to the chat
	@property
	def can_invite_users(self) -> "Boolean":
		return self._d["can_invite_users"]


	# Optional. True, if the administrator can post in the channel; channels only
	@property
	def can_post_messages(self) -> "Boolean":
		return self._d["can_post_messages"]


	# Optional. True, if the administrator can edit messages of other users and can pin messages; channels only
	@property
	def can_edit_messages(self) -> "Boolean":
		return self._d["can_edit_messages"]


	# Optional. True, if the user is allowed to pin messages; groups and supergroups only
	@property
	def can_pin_messages(self) -> "Boolean":
		return self._d["can_pin_messages"]




# @url https://core.telegram.org/bots/api#chatmember
# This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:, - ChatMemberOwner, - ChatMemberAdministrator, - ChatMemberMember, - ChatMemberRestricted, - ChatMemberLeft, - ChatMemberBanned
class ChatMember(DefaultType):

    ...




# @url https://core.telegram.org/bots/api#chatmemberowner
# Represents a chat member that owns the chat and has all administrator privileges.
class ChatMemberOwner(DefaultType):

    


	# The member's status in the chat, always "creator"
	@property
	def status(self) -> "String":
		return self._d["status"]


	# Information about the user
	@property
	def user(self) -> "User":
		return self._d["user"]


	# True, if the user's presence in the chat is hidden
	@property
	def is_anonymous(self) -> "Boolean":
		return self._d["is_anonymous"]


	# Optional. Custom title for this user
	@property
	def custom_title(self) -> "String":
		return self._d["custom_title"]




# @url https://core.telegram.org/bots/api#chatmemberadministrator
# Represents a chat member that has some additional privileges.
class ChatMemberAdministrator(DefaultType):

    


	# The member's status in the chat, always "administrator"
	@property
	def status(self) -> "String":
		return self._d["status"]


	# Information about the user
	@property
	def user(self) -> "User":
		return self._d["user"]


	# True, if the bot is allowed to edit administrator privileges of that user
	@property
	def can_be_edited(self) -> "Boolean":
		return self._d["can_be_edited"]


	# True, if the user's presence in the chat is hidden
	@property
	def is_anonymous(self) -> "Boolean":
		return self._d["is_anonymous"]


	# True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
	@property
	def can_manage_chat(self) -> "Boolean":
		return self._d["can_manage_chat"]


	# True, if the administrator can delete messages of other users
	@property
	def can_delete_messages(self) -> "Boolean":
		return self._d["can_delete_messages"]


	# True, if the administrator can manage video chats
	@property
	def can_manage_video_chats(self) -> "Boolean":
		return self._d["can_manage_video_chats"]


	# True, if the administrator can restrict, ban or unban chat members
	@property
	def can_restrict_members(self) -> "Boolean":
		return self._d["can_restrict_members"]


	# True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
	@property
	def can_promote_members(self) -> "Boolean":
		return self._d["can_promote_members"]


	# True, if the user is allowed to change the chat title, photo and other settings
	@property
	def can_change_info(self) -> "Boolean":
		return self._d["can_change_info"]


	# True, if the user is allowed to invite new users to the chat
	@property
	def can_invite_users(self) -> "Boolean":
		return self._d["can_invite_users"]


	# Optional. True, if the administrator can post in the channel; channels only
	@property
	def can_post_messages(self) -> "Boolean":
		return self._d["can_post_messages"]


	# Optional. True, if the administrator can edit messages of other users and can pin messages; channels only
	@property
	def can_edit_messages(self) -> "Boolean":
		return self._d["can_edit_messages"]


	# Optional. True, if the user is allowed to pin messages; groups and supergroups only
	@property
	def can_pin_messages(self) -> "Boolean":
		return self._d["can_pin_messages"]


	# Optional. Custom title for this user
	@property
	def custom_title(self) -> "String":
		return self._d["custom_title"]




# @url https://core.telegram.org/bots/api#chatmembermember
# Represents a chat member that has no additional privileges or restrictions.
class ChatMemberMember(DefaultType):

    


	# The member's status in the chat, always "member"
	@property
	def status(self) -> "String":
		return self._d["status"]


	# Information about the user
	@property
	def user(self) -> "User":
		return self._d["user"]




# @url https://core.telegram.org/bots/api#chatmemberrestricted
# Represents a chat member that is under certain restrictions in the chat. Supergroups only.
class ChatMemberRestricted(DefaultType):

    


	# The member's status in the chat, always "restricted"
	@property
	def status(self) -> "String":
		return self._d["status"]


	# Information about the user
	@property
	def user(self) -> "User":
		return self._d["user"]


	# True, if the user is a member of the chat at the moment of the request
	@property
	def is_member(self) -> "Boolean":
		return self._d["is_member"]


	# True, if the user is allowed to change the chat title, photo and other settings
	@property
	def can_change_info(self) -> "Boolean":
		return self._d["can_change_info"]


	# True, if the user is allowed to invite new users to the chat
	@property
	def can_invite_users(self) -> "Boolean":
		return self._d["can_invite_users"]


	# True, if the user is allowed to pin messages
	@property
	def can_pin_messages(self) -> "Boolean":
		return self._d["can_pin_messages"]


	# True, if the user is allowed to send text messages, contacts, locations and venues
	@property
	def can_send_messages(self) -> "Boolean":
		return self._d["can_send_messages"]


	# True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
	@property
	def can_send_media_messages(self) -> "Boolean":
		return self._d["can_send_media_messages"]


	# True, if the user is allowed to send polls
	@property
	def can_send_polls(self) -> "Boolean":
		return self._d["can_send_polls"]


	# True, if the user is allowed to send animations, games, stickers and use inline bots
	@property
	def can_send_other_messages(self) -> "Boolean":
		return self._d["can_send_other_messages"]


	# True, if the user is allowed to add web page previews to their messages
	@property
	def can_add_web_page_previews(self) -> "Boolean":
		return self._d["can_add_web_page_previews"]


	# Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted forever
	@property
	def until_date(self) -> "Integer":
		return self._d["until_date"]




# @url https://core.telegram.org/bots/api#chatmemberleft
# Represents a chat member that isn't currently a member of the chat, but may join it themselves.
class ChatMemberLeft(DefaultType):

    


	# The member's status in the chat, always "left"
	@property
	def status(self) -> "String":
		return self._d["status"]


	# Information about the user
	@property
	def user(self) -> "User":
		return self._d["user"]




# @url https://core.telegram.org/bots/api#chatmemberbanned
# Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.
class ChatMemberBanned(DefaultType):

    


	# The member's status in the chat, always "kicked"
	@property
	def status(self) -> "String":
		return self._d["status"]


	# Information about the user
	@property
	def user(self) -> "User":
		return self._d["user"]


	# Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned forever
	@property
	def until_date(self) -> "Integer":
		return self._d["until_date"]




# @url https://core.telegram.org/bots/api#chatmemberupdated
# This object represents changes in the status of a chat member.
class ChatMemberUpdated(DefaultType):

    


	# Chat the user belongs to
	@property
	def chat(self) -> "Chat":
		return self._d["chat"]


	# Performer of the action, which resulted in the change
	@property
	def from_(self) -> "User":
		return self._d["from"]


	# Date the change was done in Unix time
	@property
	def date(self) -> "Integer":
		return self._d["date"]


	# Previous information about the chat member
	@property
	def old_chat_member(self) -> "ChatMember":
		return self._d["old_chat_member"]


	# New information about the chat member
	@property
	def new_chat_member(self) -> "ChatMember":
		return self._d["new_chat_member"]


	# Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
	@property
	def invite_link(self) -> "ChatInviteLink":
		return self._d["invite_link"]




# @url https://core.telegram.org/bots/api#chatjoinrequest
# Represents a join request sent to a chat.
class ChatJoinRequest(DefaultType):

    


	# Chat to which the request was sent
	@property
	def chat(self) -> "Chat":
		return self._d["chat"]


	# User that sent the join request
	@property
	def from_(self) -> "User":
		return self._d["from"]


	# Date the request was sent in Unix time
	@property
	def date(self) -> "Integer":
		return self._d["date"]


	# Optional. Bio of the user.
	@property
	def bio(self) -> "String":
		return self._d["bio"]


	# Optional. Chat invite link that was used by the user to send the join request
	@property
	def invite_link(self) -> "ChatInviteLink":
		return self._d["invite_link"]




# @url https://core.telegram.org/bots/api#chatpermissions
# Describes actions that a non-administrator user is allowed to take in a chat.
class ChatPermissions(DefaultType):

    


	# Optional. True, if the user is allowed to send text messages, contacts, locations and venues
	@property
	def can_send_messages(self) -> "Boolean":
		return self._d["can_send_messages"]


	# Optional. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
	@property
	def can_send_media_messages(self) -> "Boolean":
		return self._d["can_send_media_messages"]


	# Optional. True, if the user is allowed to send polls, implies can_send_messages
	@property
	def can_send_polls(self) -> "Boolean":
		return self._d["can_send_polls"]


	# Optional. True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages
	@property
	def can_send_other_messages(self) -> "Boolean":
		return self._d["can_send_other_messages"]


	# Optional. True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages
	@property
	def can_add_web_page_previews(self) -> "Boolean":
		return self._d["can_add_web_page_previews"]


	# Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
	@property
	def can_change_info(self) -> "Boolean":
		return self._d["can_change_info"]


	# Optional. True, if the user is allowed to invite new users to the chat
	@property
	def can_invite_users(self) -> "Boolean":
		return self._d["can_invite_users"]


	# Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
	@property
	def can_pin_messages(self) -> "Boolean":
		return self._d["can_pin_messages"]




# @url https://core.telegram.org/bots/api#chatlocation
# Represents a location to which a chat is connected.
class ChatLocation(DefaultType):

    


	# The location to which the supergroup is connected. Can't be a live location.
	@property
	def location(self) -> "Location":
		return self._d["location"]


	# Location address; 1-64 characters, as defined by the chat owner
	@property
	def address(self) -> "String":
		return self._d["address"]




# @url https://core.telegram.org/bots/api#botcommand
# This object represents a bot command.
class BotCommand(DefaultType):

    


	# Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores.
	@property
	def command(self) -> "String":
		return self._d["command"]


	# Description of the command; 1-256 characters.
	@property
	def description(self) -> "String":
		return self._d["description"]




# @url https://core.telegram.org/bots/api#botcommandscope
# This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:, - BotCommandScopeDefault, - BotCommandScopeAllPrivateChats, - BotCommandScopeAllGroupChats, - BotCommandScopeAllChatAdministrators, - BotCommandScopeChat, - BotCommandScopeChatAdministrators, - BotCommandScopeChatMember
class BotCommandScope(DefaultType):

    ...




# @url https://core.telegram.org/bots/api#botcommandscopedefault
# Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.
class BotCommandScopeDefault(DefaultType):

    


	# Scope type, must be default
	@property
	def type(self) -> "String":
		return self._d["type"]




# @url https://core.telegram.org/bots/api#botcommandscopeallprivatechats
# Represents the scope of bot commands, covering all private chats.
class BotCommandScopeAllPrivateChats(DefaultType):

    


	# Scope type, must be all_private_chats
	@property
	def type(self) -> "String":
		return self._d["type"]




# @url https://core.telegram.org/bots/api#botcommandscopeallgroupchats
# Represents the scope of bot commands, covering all group and supergroup chats.
class BotCommandScopeAllGroupChats(DefaultType):

    


	# Scope type, must be all_group_chats
	@property
	def type(self) -> "String":
		return self._d["type"]




# @url https://core.telegram.org/bots/api#botcommandscopeallchatadministrators
# Represents the scope of bot commands, covering all group and supergroup chat administrators.
class BotCommandScopeAllChatAdministrators(DefaultType):

    


	# Scope type, must be all_chat_administrators
	@property
	def type(self) -> "String":
		return self._d["type"]




# @url https://core.telegram.org/bots/api#botcommandscopechat
# Represents the scope of bot commands, covering a specific chat.
class BotCommandScopeChat(DefaultType):

    


	# Scope type, must be chat
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	@property
	def chat_id(self) -> "Integer"|"String":
		return self._d["chat_id"]




# @url https://core.telegram.org/bots/api#botcommandscopechatadministrators
# Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.
class BotCommandScopeChatAdministrators(DefaultType):

    


	# Scope type, must be chat_administrators
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	@property
	def chat_id(self) -> "Integer"|"String":
		return self._d["chat_id"]




# @url https://core.telegram.org/bots/api#botcommandscopechatmember
# Represents the scope of bot commands, covering a specific member of a group or supergroup chat.
class BotCommandScopeChatMember(DefaultType):

    


	# Scope type, must be chat_member
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	@property
	def chat_id(self) -> "Integer"|"String":
		return self._d["chat_id"]


	# Unique identifier of the target user
	@property
	def user_id(self) -> "Integer":
		return self._d["user_id"]




# @url https://core.telegram.org/bots/api#menubutton
# This object describes the bot's menu button in a private chat. It should be one of, - MenuButtonCommands, - MenuButtonWebApp, - MenuButtonDefault, If a menu button other than MenuButtonDefault is set for a private chat, then it is applied in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands.
class MenuButton(DefaultType):

    ...




# @url https://core.telegram.org/bots/api#menubuttoncommands
# Represents a menu button, which opens the bot's list of commands.
class MenuButtonCommands(DefaultType):

    


	# Type of the button, must be commands
	@property
	def type(self) -> "String":
		return self._d["type"]




# @url https://core.telegram.org/bots/api#menubuttonwebapp
# Represents a menu button, which launches a Web App.
class MenuButtonWebApp(DefaultType):

    


	# Type of the button, must be web_app
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Text on the button
	@property
	def text(self) -> "String":
		return self._d["text"]


	# Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery.
	@property
	def web_app(self) -> "WebAppInfo":
		return self._d["web_app"]




# @url https://core.telegram.org/bots/api#menubuttondefault
# Describes that no specific value for the menu button was set.
class MenuButtonDefault(DefaultType):

    


	# Type of the button, must be default
	@property
	def type(self) -> "String":
		return self._d["type"]




# @url https://core.telegram.org/bots/api#responseparameters
# Describes why a request was unsuccessful.
class ResponseParameters(DefaultType):

    


	# Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
	@property
	def migrate_to_chat_id(self) -> "Integer":
		return self._d["migrate_to_chat_id"]


	# Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
	@property
	def retry_after(self) -> "Integer":
		return self._d["retry_after"]




# @url https://core.telegram.org/bots/api#inputmedia
# This object represents the content of a media message to be sent. It should be one of, - InputMediaAnimation, - InputMediaDocument, - InputMediaAudio, - InputMediaPhoto, - InputMediaVideo
class InputMedia(DefaultType):

    ...




# @url https://core.telegram.org/bots/api#inputmediaphoto
# Represents a photo to be sent.
class InputMediaPhoto(DefaultType):

    


	# Type of the result, must be photo
	@property
	def type(self) -> "String":
		return self._d["type"]


	# File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def media(self) -> "String":
		return self._d["media"]


	# Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]




# @url https://core.telegram.org/bots/api#inputmediavideo
# Represents a video to be sent.
class InputMediaVideo(DefaultType):

    


	# Type of the result, must be video
	@property
	def type(self) -> "String":
		return self._d["type"]


	# File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def media(self) -> "String":
		return self._d["media"]


	# Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def thumb(self) -> "InputFile"|"String":
		return self._d["thumb"]


	# Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the video caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Video width
	@property
	def width(self) -> "Integer":
		return self._d["width"]


	# Optional. Video height
	@property
	def height(self) -> "Integer":
		return self._d["height"]


	# Optional. Video duration in seconds
	@property
	def duration(self) -> "Integer":
		return self._d["duration"]


	# Optional. Pass True, if the uploaded video is suitable for streaming
	@property
	def supports_streaming(self) -> "Boolean":
		return self._d["supports_streaming"]




# @url https://core.telegram.org/bots/api#inputmediaanimation
# Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.
class InputMediaAnimation(DefaultType):

    


	# Type of the result, must be animation
	@property
	def type(self) -> "String":
		return self._d["type"]


	# File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def media(self) -> "String":
		return self._d["media"]


	# Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def thumb(self) -> "InputFile"|"String":
		return self._d["thumb"]


	# Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the animation caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Animation width
	@property
	def width(self) -> "Integer":
		return self._d["width"]


	# Optional. Animation height
	@property
	def height(self) -> "Integer":
		return self._d["height"]


	# Optional. Animation duration in seconds
	@property
	def duration(self) -> "Integer":
		return self._d["duration"]




# @url https://core.telegram.org/bots/api#inputmediaaudio
# Represents an audio file to be treated as music to be sent.
class InputMediaAudio(DefaultType):

    


	# Type of the result, must be audio
	@property
	def type(self) -> "String":
		return self._d["type"]


	# File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def media(self) -> "String":
		return self._d["media"]


	# Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def thumb(self) -> "InputFile"|"String":
		return self._d["thumb"]


	# Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Duration of the audio in seconds
	@property
	def duration(self) -> "Integer":
		return self._d["duration"]


	# Optional. Performer of the audio
	@property
	def performer(self) -> "String":
		return self._d["performer"]


	# Optional. Title of the audio
	@property
	def title(self) -> "String":
		return self._d["title"]




# @url https://core.telegram.org/bots/api#inputmediadocument
# Represents a general file to be sent.
class InputMediaDocument(DefaultType):

    


	# Type of the result, must be document
	@property
	def type(self) -> "String":
		return self._d["type"]


	# File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def media(self) -> "String":
		return self._d["media"]


	# Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def thumb(self) -> "InputFile"|"String":
		return self._d["thumb"]


	# Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the document caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True, if the document is sent as part of an album.
	@property
	def disable_content_type_detection(self) -> "Boolean":
		return self._d["disable_content_type_detection"]




# @url https://core.telegram.org/bots/api#inputfile
# This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.
class InputFile(DefaultType):

    ...




# @url https://core.telegram.org/bots/api#sticker
# This object represents a sticker.
class Sticker(DefaultType):

    


	# Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> "String":
		return self._d["file_id"]


	# Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> "String":
		return self._d["file_unique_id"]


	# Sticker width
	@property
	def width(self) -> "Integer":
		return self._d["width"]


	# Sticker height
	@property
	def height(self) -> "Integer":
		return self._d["height"]


	# True, if the sticker is animated
	@property
	def is_animated(self) -> "Boolean":
		return self._d["is_animated"]


	# True, if the sticker is a video sticker
	@property
	def is_video(self) -> "Boolean":
		return self._d["is_video"]


	# Optional. Sticker thumbnail in the .WEBP or .JPG format
	@property
	def thumb(self) -> "PhotoSize":
		return self._d["thumb"]


	# Optional. Emoji associated with the sticker
	@property
	def emoji(self) -> "String":
		return self._d["emoji"]


	# Optional. Name of the sticker set to which the sticker belongs
	@property
	def set_name(self) -> "String":
		return self._d["set_name"]


	# Optional. Premium animation for the sticker, if the sticker is premium
	@property
	def premium_animation(self) -> "File":
		return self._d["premium_animation"]


	# Optional. For mask stickers, the position where the mask should be placed
	@property
	def mask_position(self) -> "MaskPosition":
		return self._d["mask_position"]


	# Optional. File size in bytes
	@property
	def file_size(self) -> "Integer":
		return self._d["file_size"]




# @url https://core.telegram.org/bots/api#stickerset
# This object represents a sticker set.
class StickerSet(DefaultType):

    


	# Sticker set name
	@property
	def name(self) -> "String":
		return self._d["name"]


	# Sticker set title
	@property
	def title(self) -> "String":
		return self._d["title"]


	# True, if the sticker set contains animated stickers
	@property
	def is_animated(self) -> "Boolean":
		return self._d["is_animated"]


	# True, if the sticker set contains video stickers
	@property
	def is_video(self) -> "Boolean":
		return self._d["is_video"]


	# True, if the sticker set contains masks
	@property
	def contains_masks(self) -> "Boolean":
		return self._d["contains_masks"]


	# List of all set stickers
	@property
	def stickers(self) -> "Array of Sticker":
		return self._d["stickers"]


	# Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format
	@property
	def thumb(self) -> "PhotoSize":
		return self._d["thumb"]




# @url https://core.telegram.org/bots/api#maskposition
# This object describes the position on faces where a mask should be placed by default.
class MaskPosition(DefaultType):

    


	# The part of the face relative to which the mask should be placed. One of "forehead", "eyes", "mouth", or "chin".
	@property
	def point(self) -> "String":
		return self._d["point"]


	# Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
	@property
	def x_shift(self) -> "Float":
		return self._d["x_shift"]


	# Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
	@property
	def y_shift(self) -> "Float":
		return self._d["y_shift"]


	# Mask scaling coefficient. For example, 2.0 means double size.
	@property
	def scale(self) -> "Float":
		return self._d["scale"]




# @url https://core.telegram.org/bots/api#inlinequery
# This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.
class InlineQuery(DefaultType):

    


	# Unique identifier for this query
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Sender
	@property
	def from_(self) -> "User":
		return self._d["from"]


	# Text of the query (up to 256 characters)
	@property
	def query(self) -> "String":
		return self._d["query"]


	# Offset of the results to be returned, can be controlled by the bot
	@property
	def offset(self) -> "String":
		return self._d["offset"]


	# Optional. Type of the chat from which the inline query was sent. Can be either "sender" for a private chat with the inline query sender, "private", "group", "supergroup", or "channel". The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat
	@property
	def chat_type(self) -> "String":
		return self._d["chat_type"]


	# Optional. Sender location, only for bots that request user location
	@property
	def location(self) -> "Location":
		return self._d["location"]




# @url https://core.telegram.org/bots/api#inlinequeryresult
# This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:, - InlineQueryResultCachedAudio, - InlineQueryResultCachedDocument, - InlineQueryResultCachedGif, - InlineQueryResultCachedMpeg4Gif, - InlineQueryResultCachedPhoto, - InlineQueryResultCachedSticker, - InlineQueryResultCachedVideo, - InlineQueryResultCachedVoice, - InlineQueryResultArticle, - InlineQueryResultAudio, - InlineQueryResultContact, - InlineQueryResultGame, - InlineQueryResultDocument, - InlineQueryResultGif, - InlineQueryResultLocation, - InlineQueryResultMpeg4Gif, - InlineQueryResultPhoto, - InlineQueryResultVenue, - InlineQueryResultVideo, - InlineQueryResultVoice, Note: All URLs passed in inline query results will be available to end users and therefore must be assumed to be public.
class InlineQueryResult(DefaultType):

    ...




# @url https://core.telegram.org/bots/api#inlinequeryresultarticle
# Represents a link to an article or web page.
class InlineQueryResultArticle(DefaultType):

    


	# Type of the result, must be article
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 Bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Title of the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Content of the message to be sent
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. URL of the result
	@property
	def url(self) -> "String":
		return self._d["url"]


	# Optional. Pass True, if you don't want the URL to be shown in the message
	@property
	def hide_url(self) -> "Boolean":
		return self._d["hide_url"]


	# Optional. Short description of the result
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Optional. Url of the thumbnail for the result
	@property
	def thumb_url(self) -> "String":
		return self._d["thumb_url"]


	# Optional. Thumbnail width
	@property
	def thumb_width(self) -> "Integer":
		return self._d["thumb_width"]


	# Optional. Thumbnail height
	@property
	def thumb_height(self) -> "Integer":
		return self._d["thumb_height"]




# @url https://core.telegram.org/bots/api#inlinequeryresultphoto
# Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
class InlineQueryResultPhoto(DefaultType):

    


	# Type of the result, must be photo
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB
	@property
	def photo_url(self) -> "String":
		return self._d["photo_url"]


	# URL of the thumbnail for the photo
	@property
	def thumb_url(self) -> "String":
		return self._d["thumb_url"]


	# Optional. Width of the photo
	@property
	def photo_width(self) -> "Integer":
		return self._d["photo_width"]


	# Optional. Height of the photo
	@property
	def photo_height(self) -> "Integer":
		return self._d["photo_height"]


	# Optional. Title for the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Short description of the result
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the photo
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultgif
# Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
class InlineQueryResultGif(DefaultType):

    


	# Type of the result, must be gif
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid URL for the GIF file. File size must not exceed 1MB
	@property
	def gif_url(self) -> "String":
		return self._d["gif_url"]


	# Optional. Width of the GIF
	@property
	def gif_width(self) -> "Integer":
		return self._d["gif_width"]


	# Optional. Height of the GIF
	@property
	def gif_height(self) -> "Integer":
		return self._d["gif_height"]


	# Optional. Duration of the GIF in seconds
	@property
	def gif_duration(self) -> "Integer":
		return self._d["gif_duration"]


	# URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
	@property
	def thumb_url(self) -> "String":
		return self._d["thumb_url"]


	# Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg"
	@property
	def thumb_mime_type(self) -> "String":
		return self._d["thumb_mime_type"]


	# Optional. Title for the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the GIF animation
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
# Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
class InlineQueryResultMpeg4Gif(DefaultType):

    


	# Type of the result, must be mpeg4_gif
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid URL for the MPEG4 file. File size must not exceed 1MB
	@property
	def mpeg4_url(self) -> "String":
		return self._d["mpeg4_url"]


	# Optional. Video width
	@property
	def mpeg4_width(self) -> "Integer":
		return self._d["mpeg4_width"]


	# Optional. Video height
	@property
	def mpeg4_height(self) -> "Integer":
		return self._d["mpeg4_height"]


	# Optional. Video duration in seconds
	@property
	def mpeg4_duration(self) -> "Integer":
		return self._d["mpeg4_duration"]


	# URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
	@property
	def thumb_url(self) -> "String":
		return self._d["thumb_url"]


	# Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg"
	@property
	def thumb_mime_type(self) -> "String":
		return self._d["thumb_mime_type"]


	# Optional. Title for the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the video animation
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultvideo
# Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
class InlineQueryResultVideo(DefaultType):

    


	# Type of the result, must be video
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid URL for the embedded video player or video file
	@property
	def video_url(self) -> "String":
		return self._d["video_url"]


	# MIME type of the content of the video URL, "text/html" or "video/mp4"
	@property
	def mime_type(self) -> "String":
		return self._d["mime_type"]


	# URL of the thumbnail (JPEG only) for the video
	@property
	def thumb_url(self) -> "String":
		return self._d["thumb_url"]


	# Title for the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the video caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Video width
	@property
	def video_width(self) -> "Integer":
		return self._d["video_width"]


	# Optional. Video height
	@property
	def video_height(self) -> "Integer":
		return self._d["video_height"]


	# Optional. Video duration in seconds
	@property
	def video_duration(self) -> "Integer":
		return self._d["video_duration"]


	# Optional. Short description of the result
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultaudio
# Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio., Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
class InlineQueryResultAudio(DefaultType):

    


	# Type of the result, must be audio
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid URL for the audio file
	@property
	def audio_url(self) -> "String":
		return self._d["audio_url"]


	# Title
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Caption, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Performer
	@property
	def performer(self) -> "String":
		return self._d["performer"]


	# Optional. Audio duration in seconds
	@property
	def audio_duration(self) -> "Integer":
		return self._d["audio_duration"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the audio
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultvoice
# Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message., Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
class InlineQueryResultVoice(DefaultType):

    


	# Type of the result, must be voice
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid URL for the voice recording
	@property
	def voice_url(self) -> "String":
		return self._d["voice_url"]


	# Recording title
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Caption, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the voice message caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Recording duration in seconds
	@property
	def voice_duration(self) -> "Integer":
		return self._d["voice_duration"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the voice recording
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultdocument
# Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method., Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
class InlineQueryResultDocument(DefaultType):

    


	# Type of the result, must be document
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Title for the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the document caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# A valid URL for the file
	@property
	def document_url(self) -> "String":
		return self._d["document_url"]


	# MIME type of the content of the file, either "application/pdf" or "application/zip"
	@property
	def mime_type(self) -> "String":
		return self._d["mime_type"]


	# Optional. Short description of the result
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the file
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]


	# Optional. URL of the thumbnail (JPEG only) for the file
	@property
	def thumb_url(self) -> "String":
		return self._d["thumb_url"]


	# Optional. Thumbnail width
	@property
	def thumb_width(self) -> "Integer":
		return self._d["thumb_width"]


	# Optional. Thumbnail height
	@property
	def thumb_height(self) -> "Integer":
		return self._d["thumb_height"]




# @url https://core.telegram.org/bots/api#inlinequeryresultlocation
# Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location., Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
class InlineQueryResultLocation(DefaultType):

    


	# Type of the result, must be location
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 Bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Location latitude in degrees
	@property
	def latitude(self) -> "Float":
		return self._d["latitude"]


	# Location longitude in degrees
	@property
	def longitude(self) -> "Float":
		return self._d["longitude"]


	# Location title
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. The radius of uncertainty for the location, measured in meters; 0-1500
	@property
	def horizontal_accuracy(self) -> "Float":
		return self._d["horizontal_accuracy"]


	# Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
	@property
	def live_period(self) -> "Integer":
		return self._d["live_period"]


	# Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
	@property
	def heading(self) -> "Integer":
		return self._d["heading"]


	# Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
	@property
	def proximity_alert_radius(self) -> "Integer":
		return self._d["proximity_alert_radius"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the location
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]


	# Optional. Url of the thumbnail for the result
	@property
	def thumb_url(self) -> "String":
		return self._d["thumb_url"]


	# Optional. Thumbnail width
	@property
	def thumb_width(self) -> "Integer":
		return self._d["thumb_width"]


	# Optional. Thumbnail height
	@property
	def thumb_height(self) -> "Integer":
		return self._d["thumb_height"]




# @url https://core.telegram.org/bots/api#inlinequeryresultvenue
# Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue., Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
class InlineQueryResultVenue(DefaultType):

    


	# Type of the result, must be venue
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 Bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Latitude of the venue location in degrees
	@property
	def latitude(self) -> "Float":
		return self._d["latitude"]


	# Longitude of the venue location in degrees
	@property
	def longitude(self) -> "Float":
		return self._d["longitude"]


	# Title of the venue
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Address of the venue
	@property
	def address(self) -> "String":
		return self._d["address"]


	# Optional. Foursquare identifier of the venue if known
	@property
	def foursquare_id(self) -> "String":
		return self._d["foursquare_id"]


	# Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
	@property
	def foursquare_type(self) -> "String":
		return self._d["foursquare_type"]


	# Optional. Google Places identifier of the venue
	@property
	def google_place_id(self) -> "String":
		return self._d["google_place_id"]


	# Optional. Google Places type of the venue. (See supported types.)
	@property
	def google_place_type(self) -> "String":
		return self._d["google_place_type"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the venue
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]


	# Optional. Url of the thumbnail for the result
	@property
	def thumb_url(self) -> "String":
		return self._d["thumb_url"]


	# Optional. Thumbnail width
	@property
	def thumb_width(self) -> "Integer":
		return self._d["thumb_width"]


	# Optional. Thumbnail height
	@property
	def thumb_height(self) -> "Integer":
		return self._d["thumb_height"]




# @url https://core.telegram.org/bots/api#inlinequeryresultcontact
# Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact., Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
class InlineQueryResultContact(DefaultType):

    


	# Type of the result, must be contact
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 Bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Contact's phone number
	@property
	def phone_number(self) -> "String":
		return self._d["phone_number"]


	# Contact's first name
	@property
	def first_name(self) -> "String":
		return self._d["first_name"]


	# Optional. Contact's last name
	@property
	def last_name(self) -> "String":
		return self._d["last_name"]


	# Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
	@property
	def vcard(self) -> "String":
		return self._d["vcard"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the contact
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]


	# Optional. Url of the thumbnail for the result
	@property
	def thumb_url(self) -> "String":
		return self._d["thumb_url"]


	# Optional. Thumbnail width
	@property
	def thumb_width(self) -> "Integer":
		return self._d["thumb_width"]


	# Optional. Thumbnail height
	@property
	def thumb_height(self) -> "Integer":
		return self._d["thumb_height"]




# @url https://core.telegram.org/bots/api#inlinequeryresultgame
# Represents a Game., Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.
class InlineQueryResultGame(DefaultType):

    


	# Type of the result, must be game
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Short name of the game
	@property
	def game_short_name(self) -> "String":
		return self._d["game_short_name"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]




# @url https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
# Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
class InlineQueryResultCachedPhoto(DefaultType):

    


	# Type of the result, must be photo
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid file identifier of the photo
	@property
	def photo_file_id(self) -> "String":
		return self._d["photo_file_id"]


	# Optional. Title for the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Short description of the result
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the photo
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultcachedgif
# Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.
class InlineQueryResultCachedGif(DefaultType):

    


	# Type of the result, must be gif
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid file identifier for the GIF file
	@property
	def gif_file_id(self) -> "String":
		return self._d["gif_file_id"]


	# Optional. Title for the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the GIF animation
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif
# Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
class InlineQueryResultCachedMpeg4Gif(DefaultType):

    


	# Type of the result, must be mpeg4_gif
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid file identifier for the MPEG4 file
	@property
	def mpeg4_file_id(self) -> "String":
		return self._d["mpeg4_file_id"]


	# Optional. Title for the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the video animation
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
# Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker., Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.
class InlineQueryResultCachedSticker(DefaultType):

    


	# Type of the result, must be sticker
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid file identifier of the sticker
	@property
	def sticker_file_id(self) -> "String":
		return self._d["sticker_file_id"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the sticker
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultcacheddocument
# Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file., Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
class InlineQueryResultCachedDocument(DefaultType):

    


	# Type of the result, must be document
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Title for the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# A valid file identifier for the file
	@property
	def document_file_id(self) -> "String":
		return self._d["document_file_id"]


	# Optional. Short description of the result
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the document caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the file
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultcachedvideo
# Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
class InlineQueryResultCachedVideo(DefaultType):

    


	# Type of the result, must be video
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid file identifier for the video file
	@property
	def video_file_id(self) -> "String":
		return self._d["video_file_id"]


	# Title for the result
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Short description of the result
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the video caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the video
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultcachedvoice
# Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message., Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
class InlineQueryResultCachedVoice(DefaultType):

    


	# Type of the result, must be voice
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid file identifier for the voice message
	@property
	def voice_file_id(self) -> "String":
		return self._d["voice_file_id"]


	# Voice message title
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Optional. Caption, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the voice message caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the voice message
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
# Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio., Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
class InlineQueryResultCachedAudio(DefaultType):

    


	# Type of the result, must be audio
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> "String":
		return self._d["id"]


	# A valid file identifier for the audio file
	@property
	def audio_file_id(self) -> "String":
		return self._d["audio_file_id"]


	# Optional. Caption, 0-1024 characters after entities parsing
	@property
	def caption(self) -> "String":
		return self._d["caption"]


	# Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> "Array of MessageEntity":
		return self._d["caption_entities"]


	# Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> "InlineKeyboardMarkup":
		return self._d["reply_markup"]


	# Optional. Content of the message to be sent instead of the audio
	@property
	def input_message_content(self) -> "InputMessageContent":
		return self._d["input_message_content"]




# @url https://core.telegram.org/bots/api#inputmessagecontent
# This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:, - InputTextMessageContent, - InputLocationMessageContent, - InputVenueMessageContent, - InputContactMessageContent, - InputInvoiceMessageContent
class InputMessageContent(DefaultType):

    ...




# @url https://core.telegram.org/bots/api#inputtextmessagecontent
# Represents the content of a text message to be sent as the result of an inline query.
class InputTextMessageContent(DefaultType):

    


	# Text of the message to be sent, 1-4096 characters
	@property
	def message_text(self) -> "String":
		return self._d["message_text"]


	# Optional. Mode for parsing entities in the message text. See formatting options for more details.
	@property
	def parse_mode(self) -> "String":
		return self._d["parse_mode"]


	# Optional. List of special entities that appear in message text, which can be specified instead of parse_mode
	@property
	def entities(self) -> "Array of MessageEntity":
		return self._d["entities"]


	# Optional. Disables link previews for links in the sent message
	@property
	def disable_web_page_preview(self) -> "Boolean":
		return self._d["disable_web_page_preview"]




# @url https://core.telegram.org/bots/api#inputlocationmessagecontent
# Represents the content of a location message to be sent as the result of an inline query.
class InputLocationMessageContent(DefaultType):

    


	# Latitude of the location in degrees
	@property
	def latitude(self) -> "Float":
		return self._d["latitude"]


	# Longitude of the location in degrees
	@property
	def longitude(self) -> "Float":
		return self._d["longitude"]


	# Optional. The radius of uncertainty for the location, measured in meters; 0-1500
	@property
	def horizontal_accuracy(self) -> "Float":
		return self._d["horizontal_accuracy"]


	# Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
	@property
	def live_period(self) -> "Integer":
		return self._d["live_period"]


	# Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
	@property
	def heading(self) -> "Integer":
		return self._d["heading"]


	# Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
	@property
	def proximity_alert_radius(self) -> "Integer":
		return self._d["proximity_alert_radius"]




# @url https://core.telegram.org/bots/api#inputvenuemessagecontent
# Represents the content of a venue message to be sent as the result of an inline query.
class InputVenueMessageContent(DefaultType):

    


	# Latitude of the venue in degrees
	@property
	def latitude(self) -> "Float":
		return self._d["latitude"]


	# Longitude of the venue in degrees
	@property
	def longitude(self) -> "Float":
		return self._d["longitude"]


	# Name of the venue
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Address of the venue
	@property
	def address(self) -> "String":
		return self._d["address"]


	# Optional. Foursquare identifier of the venue, if known
	@property
	def foursquare_id(self) -> "String":
		return self._d["foursquare_id"]


	# Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
	@property
	def foursquare_type(self) -> "String":
		return self._d["foursquare_type"]


	# Optional. Google Places identifier of the venue
	@property
	def google_place_id(self) -> "String":
		return self._d["google_place_id"]


	# Optional. Google Places type of the venue. (See supported types.)
	@property
	def google_place_type(self) -> "String":
		return self._d["google_place_type"]




# @url https://core.telegram.org/bots/api#inputcontactmessagecontent
# Represents the content of a contact message to be sent as the result of an inline query.
class InputContactMessageContent(DefaultType):

    


	# Contact's phone number
	@property
	def phone_number(self) -> "String":
		return self._d["phone_number"]


	# Contact's first name
	@property
	def first_name(self) -> "String":
		return self._d["first_name"]


	# Optional. Contact's last name
	@property
	def last_name(self) -> "String":
		return self._d["last_name"]


	# Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
	@property
	def vcard(self) -> "String":
		return self._d["vcard"]




# @url https://core.telegram.org/bots/api#inputinvoicemessagecontent
# Represents the content of an invoice message to be sent as the result of an inline query.
class InputInvoiceMessageContent(DefaultType):

    


	# Product name, 1-32 characters
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Product description, 1-255 characters
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
	@property
	def payload(self) -> "String":
		return self._d["payload"]


	# Payment provider token, obtained via @BotFather
	@property
	def provider_token(self) -> "String":
		return self._d["provider_token"]


	# Three-letter ISO 4217 currency code, see more on currencies
	@property
	def currency(self) -> "String":
		return self._d["currency"]


	# Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
	@property
	def prices(self) -> "Array of LabeledPrice":
		return self._d["prices"]


	# Optional. The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0
	@property
	def max_tip_amount(self) -> "Integer":
		return self._d["max_tip_amount"]


	# Optional. A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
	@property
	def suggested_tip_amounts(self) -> "Array of Integer":
		return self._d["suggested_tip_amounts"]


	# Optional. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.
	@property
	def provider_data(self) -> "String":
		return self._d["provider_data"]


	# Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.
	@property
	def photo_url(self) -> "String":
		return self._d["photo_url"]


	# Optional. Photo size in bytes
	@property
	def photo_size(self) -> "Integer":
		return self._d["photo_size"]


	# Optional. Photo width
	@property
	def photo_width(self) -> "Integer":
		return self._d["photo_width"]


	# Optional. Photo height
	@property
	def photo_height(self) -> "Integer":
		return self._d["photo_height"]


	# Optional. Pass True, if you require the user's full name to complete the order
	@property
	def need_name(self) -> "Boolean":
		return self._d["need_name"]


	# Optional. Pass True, if you require the user's phone number to complete the order
	@property
	def need_phone_number(self) -> "Boolean":
		return self._d["need_phone_number"]


	# Optional. Pass True, if you require the user's email address to complete the order
	@property
	def need_email(self) -> "Boolean":
		return self._d["need_email"]


	# Optional. Pass True, if you require the user's shipping address to complete the order
	@property
	def need_shipping_address(self) -> "Boolean":
		return self._d["need_shipping_address"]


	# Optional. Pass True, if the user's phone number should be sent to provider
	@property
	def send_phone_number_to_provider(self) -> "Boolean":
		return self._d["send_phone_number_to_provider"]


	# Optional. Pass True, if the user's email address should be sent to provider
	@property
	def send_email_to_provider(self) -> "Boolean":
		return self._d["send_email_to_provider"]


	# Optional. Pass True, if the final price depends on the shipping method
	@property
	def is_flexible(self) -> "Boolean":
		return self._d["is_flexible"]




# @url https://core.telegram.org/bots/api#choseninlineresult
# Represents a result of an inline query that was chosen by the user and sent to their chat partner., Note: It is necessary to enable inline feedback via @BotFather in order to receive these objects in updates.
class ChosenInlineResult(DefaultType):

    


	# The unique identifier for the result that was chosen
	@property
	def result_id(self) -> "String":
		return self._d["result_id"]


	# The user that chose the result
	@property
	def from_(self) -> "User":
		return self._d["from"]


	# Optional. Sender location, only for bots that require user location
	@property
	def location(self) -> "Location":
		return self._d["location"]


	# Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
	@property
	def inline_message_id(self) -> "String":
		return self._d["inline_message_id"]


	# The query that was used to obtain the result
	@property
	def query(self) -> "String":
		return self._d["query"]




# @url https://core.telegram.org/bots/api#sentwebappmessage
# Describes an inline message sent by a Web App on behalf of a user.
class SentWebAppMessage(DefaultType):

    


	# Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message.
	@property
	def inline_message_id(self) -> "String":
		return self._d["inline_message_id"]




# @url https://core.telegram.org/bots/api#labeledprice
# This object represents a portion of the price for goods or services.
class LabeledPrice(DefaultType):

    


	# Portion label
	@property
	def label(self) -> "String":
		return self._d["label"]


	# Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
	@property
	def amount(self) -> "Integer":
		return self._d["amount"]




# @url https://core.telegram.org/bots/api#invoice
# This object contains basic information about an invoice.
class Invoice(DefaultType):

    


	# Product name
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Product description
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Unique bot deep-linking parameter that can be used to generate this invoice
	@property
	def start_parameter(self) -> "String":
		return self._d["start_parameter"]


	# Three-letter ISO 4217 currency code
	@property
	def currency(self) -> "String":
		return self._d["currency"]


	# Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
	@property
	def total_amount(self) -> "Integer":
		return self._d["total_amount"]




# @url https://core.telegram.org/bots/api#shippingaddress
# This object represents a shipping address.
class ShippingAddress(DefaultType):

    


	# Two-letter ISO 3166-1 alpha-2 country code
	@property
	def country_code(self) -> "String":
		return self._d["country_code"]


	# State, if applicable
	@property
	def state(self) -> "String":
		return self._d["state"]


	# City
	@property
	def city(self) -> "String":
		return self._d["city"]


	# First line for the address
	@property
	def street_line1(self) -> "String":
		return self._d["street_line1"]


	# Second line for the address
	@property
	def street_line2(self) -> "String":
		return self._d["street_line2"]


	# Address post code
	@property
	def post_code(self) -> "String":
		return self._d["post_code"]




# @url https://core.telegram.org/bots/api#orderinfo
# This object represents information about an order.
class OrderInfo(DefaultType):

    


	# Optional. User name
	@property
	def name(self) -> "String":
		return self._d["name"]


	# Optional. User's phone number
	@property
	def phone_number(self) -> "String":
		return self._d["phone_number"]


	# Optional. User email
	@property
	def email(self) -> "String":
		return self._d["email"]


	# Optional. User shipping address
	@property
	def shipping_address(self) -> "ShippingAddress":
		return self._d["shipping_address"]




# @url https://core.telegram.org/bots/api#shippingoption
# This object represents one shipping option.
class ShippingOption(DefaultType):

    


	# Shipping option identifier
	@property
	def id(self) -> "String":
		return self._d["id"]


	# Option title
	@property
	def title(self) -> "String":
		return self._d["title"]


	# List of price portions
	@property
	def prices(self) -> "Array of LabeledPrice":
		return self._d["prices"]




# @url https://core.telegram.org/bots/api#successfulpayment
# This object contains basic information about a successful payment.
class SuccessfulPayment(DefaultType):

    


	# Three-letter ISO 4217 currency code
	@property
	def currency(self) -> "String":
		return self._d["currency"]


	# Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
	@property
	def total_amount(self) -> "Integer":
		return self._d["total_amount"]


	# Bot specified invoice payload
	@property
	def invoice_payload(self) -> "String":
		return self._d["invoice_payload"]


	# Optional. Identifier of the shipping option chosen by the user
	@property
	def shipping_option_id(self) -> "String":
		return self._d["shipping_option_id"]


	# Optional. Order information provided by the user
	@property
	def order_info(self) -> "OrderInfo":
		return self._d["order_info"]


	# Telegram payment identifier
	@property
	def telegram_payment_charge_id(self) -> "String":
		return self._d["telegram_payment_charge_id"]


	# Provider payment identifier
	@property
	def provider_payment_charge_id(self) -> "String":
		return self._d["provider_payment_charge_id"]




# @url https://core.telegram.org/bots/api#shippingquery
# This object contains information about an incoming shipping query.
class ShippingQuery(DefaultType):

    


	# Unique query identifier
	@property
	def id(self) -> "String":
		return self._d["id"]


	# User who sent the query
	@property
	def from_(self) -> "User":
		return self._d["from"]


	# Bot specified invoice payload
	@property
	def invoice_payload(self) -> "String":
		return self._d["invoice_payload"]


	# User specified shipping address
	@property
	def shipping_address(self) -> "ShippingAddress":
		return self._d["shipping_address"]




# @url https://core.telegram.org/bots/api#precheckoutquery
# This object contains information about an incoming pre-checkout query.
class PreCheckoutQuery(DefaultType):

    


	# Unique query identifier
	@property
	def id(self) -> "String":
		return self._d["id"]


	# User who sent the query
	@property
	def from_(self) -> "User":
		return self._d["from"]


	# Three-letter ISO 4217 currency code
	@property
	def currency(self) -> "String":
		return self._d["currency"]


	# Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
	@property
	def total_amount(self) -> "Integer":
		return self._d["total_amount"]


	# Bot specified invoice payload
	@property
	def invoice_payload(self) -> "String":
		return self._d["invoice_payload"]


	# Optional. Identifier of the shipping option chosen by the user
	@property
	def shipping_option_id(self) -> "String":
		return self._d["shipping_option_id"]


	# Optional. Order information provided by the user
	@property
	def order_info(self) -> "OrderInfo":
		return self._d["order_info"]




# @url https://core.telegram.org/bots/api#passportdata
# Describes Telegram Passport data shared with the bot by the user.
class PassportData(DefaultType):

    


	# Array with information about documents and other Telegram Passport elements that was shared with the bot
	@property
	def data(self) -> "Array of EncryptedPassportElement":
		return self._d["data"]


	# Encrypted credentials required to decrypt the data
	@property
	def credentials(self) -> "EncryptedCredentials":
		return self._d["credentials"]




# @url https://core.telegram.org/bots/api#passportfile
# This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.
class PassportFile(DefaultType):

    


	# Identifier for this file, which can be used to download or reuse the file
	@property
	def file_id(self) -> "String":
		return self._d["file_id"]


	# Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
	@property
	def file_unique_id(self) -> "String":
		return self._d["file_unique_id"]


	# File size in bytes
	@property
	def file_size(self) -> "Integer":
		return self._d["file_size"]


	# Unix time when the file was uploaded
	@property
	def file_date(self) -> "Integer":
		return self._d["file_date"]




# @url https://core.telegram.org/bots/api#encryptedpassportelement
# Describes documents or other Telegram Passport elements shared with the bot by the user.
class EncryptedPassportElement(DefaultType):

    


	# Element type. One of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration", "phone_number", "email".
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for "personal_details", "passport", "driver_license", "identity_card", "internal_passport" and "address" types. Can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def data(self) -> "String":
		return self._d["data"]


	# Optional. User's verified phone number, available only for "phone_number" type
	@property
	def phone_number(self) -> "String":
		return self._d["phone_number"]


	# Optional. User's verified email address, available only for "email" type
	@property
	def email(self) -> "String":
		return self._d["email"]


	# Optional. Array of encrypted files with documents provided by the user, available for "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and "temporary_registration" types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def files(self) -> "Array of PassportFile":
		return self._d["files"]


	# Optional. Encrypted file with the front side of the document, provided by the user. Available for "passport", "driver_license", "identity_card" and "internal_passport". The file can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def front_side(self) -> "PassportFile":
		return self._d["front_side"]


	# Optional. Encrypted file with the reverse side of the document, provided by the user. Available for "driver_license" and "identity_card". The file can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def reverse_side(self) -> "PassportFile":
		return self._d["reverse_side"]


	# Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for "passport", "driver_license", "identity_card" and "internal_passport". The file can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def selfie(self) -> "PassportFile":
		return self._d["selfie"]


	# Optional. Array of encrypted files with translated versions of documents provided by the user. Available if requested for "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and "temporary_registration" types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
	@property
	def translation(self) -> "Array of PassportFile":
		return self._d["translation"]


	# Base64-encoded element hash for using in PassportElementErrorUnspecified
	@property
	def hash(self) -> "String":
		return self._d["hash"]




# @url https://core.telegram.org/bots/api#encryptedcredentials
# Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.
class EncryptedCredentials(DefaultType):

    


	# Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication
	@property
	def data(self) -> "String":
		return self._d["data"]


	# Base64-encoded data hash for data authentication
	@property
	def hash(self) -> "String":
		return self._d["hash"]


	# Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption
	@property
	def secret(self) -> "String":
		return self._d["secret"]




# @url https://core.telegram.org/bots/api#passportelementerror
# This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:, - PassportElementErrorDataField, - PassportElementErrorFrontSide, - PassportElementErrorReverseSide, - PassportElementErrorSelfie, - PassportElementErrorFile, - PassportElementErrorFiles, - PassportElementErrorTranslationFile, - PassportElementErrorTranslationFiles, - PassportElementErrorUnspecified
class PassportElementError(DefaultType):

    ...




# @url https://core.telegram.org/bots/api#passportelementerrordatafield
# Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.
class PassportElementErrorDataField(DefaultType):

    


	# Error source, must be data
	@property
	def source(self) -> "String":
		return self._d["source"]


	# The section of the user's Telegram Passport which has the error, one of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address"
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Name of the data field which has the error
	@property
	def field_name(self) -> "String":
		return self._d["field_name"]


	# Base64-encoded data hash
	@property
	def data_hash(self) -> "String":
		return self._d["data_hash"]


	# Error message
	@property
	def message(self) -> "String":
		return self._d["message"]




# @url https://core.telegram.org/bots/api#passportelementerrorfrontside
# Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.
class PassportElementErrorFrontSide(DefaultType):

    


	# Error source, must be front_side
	@property
	def source(self) -> "String":
		return self._d["source"]


	# The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport"
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Base64-encoded hash of the file with the front side of the document
	@property
	def file_hash(self) -> "String":
		return self._d["file_hash"]


	# Error message
	@property
	def message(self) -> "String":
		return self._d["message"]




# @url https://core.telegram.org/bots/api#passportelementerrorreverseside
# Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.
class PassportElementErrorReverseSide(DefaultType):

    


	# Error source, must be reverse_side
	@property
	def source(self) -> "String":
		return self._d["source"]


	# The section of the user's Telegram Passport which has the issue, one of "driver_license", "identity_card"
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Base64-encoded hash of the file with the reverse side of the document
	@property
	def file_hash(self) -> "String":
		return self._d["file_hash"]


	# Error message
	@property
	def message(self) -> "String":
		return self._d["message"]




# @url https://core.telegram.org/bots/api#passportelementerrorselfie
# Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.
class PassportElementErrorSelfie(DefaultType):

    


	# Error source, must be selfie
	@property
	def source(self) -> "String":
		return self._d["source"]


	# The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport"
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Base64-encoded hash of the file with the selfie
	@property
	def file_hash(self) -> "String":
		return self._d["file_hash"]


	# Error message
	@property
	def message(self) -> "String":
		return self._d["message"]




# @url https://core.telegram.org/bots/api#passportelementerrorfile
# Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.
class PassportElementErrorFile(DefaultType):

    


	# Error source, must be file
	@property
	def source(self) -> "String":
		return self._d["source"]


	# The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Base64-encoded file hash
	@property
	def file_hash(self) -> "String":
		return self._d["file_hash"]


	# Error message
	@property
	def message(self) -> "String":
		return self._d["message"]




# @url https://core.telegram.org/bots/api#passportelementerrorfiles
# Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.
class PassportElementErrorFiles(DefaultType):

    


	# Error source, must be files
	@property
	def source(self) -> "String":
		return self._d["source"]


	# The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
	@property
	def type(self) -> "String":
		return self._d["type"]


	# List of base64-encoded file hashes
	@property
	def file_hashes(self) -> "Array of String":
		return self._d["file_hashes"]


	# Error message
	@property
	def message(self) -> "String":
		return self._d["message"]




# @url https://core.telegram.org/bots/api#passportelementerrortranslationfile
# Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.
class PassportElementErrorTranslationFile(DefaultType):

    


	# Error source, must be translation_file
	@property
	def source(self) -> "String":
		return self._d["source"]


	# Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Base64-encoded file hash
	@property
	def file_hash(self) -> "String":
		return self._d["file_hash"]


	# Error message
	@property
	def message(self) -> "String":
		return self._d["message"]




# @url https://core.telegram.org/bots/api#passportelementerrortranslationfiles
# Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.
class PassportElementErrorTranslationFiles(DefaultType):

    


	# Error source, must be translation_files
	@property
	def source(self) -> "String":
		return self._d["source"]


	# Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
	@property
	def type(self) -> "String":
		return self._d["type"]


	# List of base64-encoded file hashes
	@property
	def file_hashes(self) -> "Array of String":
		return self._d["file_hashes"]


	# Error message
	@property
	def message(self) -> "String":
		return self._d["message"]




# @url https://core.telegram.org/bots/api#passportelementerrorunspecified
# Represents an issue in an unspecified place. The error is considered resolved when new data is added.
class PassportElementErrorUnspecified(DefaultType):

    


	# Error source, must be unspecified
	@property
	def source(self) -> "String":
		return self._d["source"]


	# Type of element of the user's Telegram Passport which has the issue
	@property
	def type(self) -> "String":
		return self._d["type"]


	# Base64-encoded element hash
	@property
	def element_hash(self) -> "String":
		return self._d["element_hash"]


	# Error message
	@property
	def message(self) -> "String":
		return self._d["message"]




# @url https://core.telegram.org/bots/api#game
# This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
class Game(DefaultType):

    


	# Title of the game
	@property
	def title(self) -> "String":
		return self._d["title"]


	# Description of the game
	@property
	def description(self) -> "String":
		return self._d["description"]


	# Photo that will be displayed in the game message in chats.
	@property
	def photo(self) -> "Array of PhotoSize":
		return self._d["photo"]


	# Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
	@property
	def text(self) -> "String":
		return self._d["text"]


	# Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
	@property
	def text_entities(self) -> "Array of MessageEntity":
		return self._d["text_entities"]


	# Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
	@property
	def animation(self) -> "Animation":
		return self._d["animation"]




# @url https://core.telegram.org/bots/api#callbackgame
# A placeholder, currently holds no information. Use BotFather to set up your game.
class CallbackGame(DefaultType):

    ...




# @url https://core.telegram.org/bots/api#gamehighscore
# This object represents one row of the high scores table for a game.
class GameHighScore(DefaultType):

    


	# Position in high score table for the game
	@property
	def position(self) -> "Integer":
		return self._d["position"]


	# User
	@property
	def user(self) -> "User":
		return self._d["user"]


	# Score
	@property
	def score(self) -> "Integer":
		return self._d["score"]

