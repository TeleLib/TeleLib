from typing import List, Union, Optional, Any


class Types:
    class DefaultType:
        def __init__(self, d):
            self._d = d

        def __repr__(self) -> str:
            string = f"{self.__class__.__name__}("
            for k, v in self._d.items():
                string += f"{k}={repr(v)}, "
            return string+")"

        def __iter__(self):
            return iter(self._d)

        def __getattr__(self, __name: str) -> Any:
            return self._d.get(__name, None)

        def __getitem__(self, name):
            return self._d.get(name, None)

    class DefaultMethod:
        def __init__(self, *args, **kwargs):
            self._called = False
            self._method: str = ""
            self._args = {}
            self._res: Any = None

        def _call(self):
            return (self._method, self._args)

    @staticmethod
    def Typify(data, type_, recursive=True) -> Any:
        if recursive:
            if isinstance(data, list):
                return [Types.Typify(d, type_) for d in data]

        if data is not None:
            return type_(data)

        return None


class Integer(int):
    ...


class String(str):
    ...


class Float(float):
    ...


Boolean = bool


class Update(Types.DefaultType):

    @property
    def update_id(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("update_id", None),
            Integer
        )

    @property
    def message(
        self
    ) -> Optional["Message"]:
        return Types.Typify(
            self._d.get("message", None),
            Message
        )

    @property
    def edited_message(
        self
    ) -> Optional["Message"]:
        return Types.Typify(
            self._d.get("edited_message", None),
            Message
        )

    @property
    def channel_post(
        self
    ) -> Optional["Message"]:
        return Types.Typify(
            self._d.get("channel_post", None),
            Message
        )

    @property
    def edited_channel_post(
        self
    ) -> Optional["Message"]:
        return Types.Typify(
            self._d.get("edited_channel_post", None),
            Message
        )

    @property
    def inline_query(
        self
    ) -> Optional["InlineQuery"]:
        return Types.Typify(
            self._d.get("inline_query", None),
            InlineQuery
        )

    @property
    def chosen_inline_result(
        self
    ) -> Optional["ChosenInlineResult"]:
        return Types.Typify(
            self._d.get("chosen_inline_result", None),
            ChosenInlineResult
        )

    @property
    def callback_query(
        self
    ) -> Optional["CallbackQuery"]:
        return Types.Typify(
            self._d.get("callback_query", None),
            CallbackQuery
        )

    @property
    def shipping_query(
        self
    ) -> Optional["ShippingQuery"]:
        return Types.Typify(
            self._d.get("shipping_query", None),
            ShippingQuery
        )

    @property
    def pre_checkout_query(
        self
    ) -> Optional["PreCheckoutQuery"]:
        return Types.Typify(
            self._d.get("pre_checkout_query", None),
            PreCheckoutQuery
        )

    @property
    def poll(
        self
    ) -> Optional["Poll"]:
        return Types.Typify(
            self._d.get("poll", None),
            Poll
        )

    @property
    def poll_answer(
        self
    ) -> Optional["PollAnswer"]:
        return Types.Typify(
            self._d.get("poll_answer", None),
            PollAnswer
        )

    @property
    def my_chat_member(
        self
    ) -> Optional["ChatMemberUpdated"]:
        return Types.Typify(
            self._d.get("my_chat_member", None),
            ChatMemberUpdated
        )

    @property
    def chat_member(
        self
    ) -> Optional["ChatMemberUpdated"]:
        return Types.Typify(
            self._d.get("chat_member", None),
            ChatMemberUpdated
        )

    @property
    def chat_join_request(
        self
    ) -> Optional["ChatJoinRequest"]:
        return Types.Typify(
            self._d.get("chat_join_request", None),
            ChatJoinRequest
        )


class WebhookInfo(Types.DefaultType):

    @property
    def url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("url", None),
            String
        )

    @property
    def has_custom_certificate(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("has_custom_certificate", None),
            Boolean
        )

    @property
    def pending_update_count(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("pending_update_count", None),
            Integer
        )

    @property
    def ip_address(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("ip_address", None),
            String
        )

    @property
    def last_error_date(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("last_error_date", None),
            Integer
        )

    @property
    def last_error_message(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("last_error_message", None),
            String
        )

    @property
    def last_synchronization_error_date(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("last_synchronization_error_date", None),
            Integer
        )

    @property
    def max_connections(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("max_connections", None),
            Integer
        )

    @property
    def allowed_updates(
        self
    ) -> Optional["List[String]"]:
        return Types.Typify(
            self._d.get("allowed_updates", None),
            String
        )


class User(Types.DefaultType):

    @property
    def id(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("id", None),
            Integer
        )

    @property
    def is_bot(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_bot", None),
            Boolean
        )

    @property
    def first_name(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("first_name", None),
            String
        )

    @property
    def last_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("last_name", None),
            String
        )

    @property
    def username(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("username", None),
            String
        )

    @property
    def language_code(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("language_code", None),
            String
        )

    @property
    def is_premium(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("is_premium", None),
            Boolean
        )

    @property
    def added_to_attachment_menu(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("added_to_attachment_menu", None),
            Boolean
        )

    @property
    def can_join_groups(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_join_groups", None),
            Boolean
        )

    @property
    def can_read_all_group_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_read_all_group_messages", None),
            Boolean
        )

    @property
    def supports_inline_queries(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("supports_inline_queries", None),
            Boolean
        )


class Chat(Types.DefaultType):

    @property
    def id(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("id", None),
            Integer
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def username(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("username", None),
            String
        )

    @property
    def first_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("first_name", None),
            String
        )

    @property
    def last_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("last_name", None),
            String
        )

    @property
    def photo(
        self
    ) -> Optional["ChatPhoto"]:
        return Types.Typify(
            self._d.get("photo", None),
            ChatPhoto
        )

    @property
    def bio(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("bio", None),
            String
        )

    @property
    def has_private_forwards(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("has_private_forwards", None),
            Boolean
        )

    @property
    def join_to_send_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("join_to_send_messages", None),
            Boolean
        )

    @property
    def join_by_request(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("join_by_request", None),
            Boolean
        )

    @property
    def description(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def invite_link(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("invite_link", None),
            String
        )

    @property
    def pinned_message(
        self
    ) -> Optional["Message"]:
        return Types.Typify(
            self._d.get("pinned_message", None),
            Message
        )

    @property
    def permissions(
        self
    ) -> Optional["ChatPermissions"]:
        return Types.Typify(
            self._d.get("permissions", None),
            ChatPermissions
        )

    @property
    def slow_mode_delay(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("slow_mode_delay", None),
            Integer
        )

    @property
    def message_auto_delete_time(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("message_auto_delete_time", None),
            Integer
        )

    @property
    def has_protected_content(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("has_protected_content", None),
            Boolean
        )

    @property
    def sticker_set_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("sticker_set_name", None),
            String
        )

    @property
    def can_set_sticker_set(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_set_sticker_set", None),
            Boolean
        )

    @property
    def linked_chat_id(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("linked_chat_id", None),
            Integer
        )

    @property
    def location(
        self
    ) -> Optional["ChatLocation"]:
        return Types.Typify(
            self._d.get("location", None),
            ChatLocation
        )


class Message(Types.DefaultType):

    @property
    def message_id(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("message_id", None),
            Integer
        )

    @property
    def from_(
        self
    ) -> Optional["User"]:
        return Types.Typify(
            self._d.get("from", None),
            User
        )

    @property
    def sender_chat(
        self
    ) -> Optional["Chat"]:
        return Types.Typify(
            self._d.get("sender_chat", None),
            Chat
        )

    @property
    def date(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("date", None),
            Integer
        )

    @property
    def chat(
        self
    ) -> "Chat":
        return Types.Typify(
            self._d.get("chat", None),
            Chat
        )

    @property
    def forward_from_(
        self
    ) -> Optional["User"]:
        return Types.Typify(
            self._d.get("forward_from", None),
            User
        )

    @property
    def forward_from__chat(
        self
    ) -> Optional["Chat"]:
        return Types.Typify(
            self._d.get("forward_from_chat", None),
            Chat
        )

    @property
    def forward_from__message_id(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("forward_from_message_id", None),
            Integer
        )

    @property
    def forward_signature(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("forward_signature", None),
            String
        )

    @property
    def forward_sender_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("forward_sender_name", None),
            String
        )

    @property
    def forward_date(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("forward_date", None),
            Integer
        )

    @property
    def is_automatic_forward(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("is_automatic_forward", None),
            Boolean
        )

    @property
    def reply_to_message(
        self
    ) -> Optional["Message"]:
        return Types.Typify(
            self._d.get("reply_to_message", None),
            Message
        )

    @property
    def via_bot(
        self
    ) -> Optional["User"]:
        return Types.Typify(
            self._d.get("via_bot", None),
            User
        )

    @property
    def edit_date(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("edit_date", None),
            Integer
        )

    @property
    def has_protected_content(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("has_protected_content", None),
            Boolean
        )

    @property
    def media_group_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("media_group_id", None),
            String
        )

    @property
    def author_signature(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("author_signature", None),
            String
        )

    @property
    def text(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("text", None),
            String
        )

    @property
    def entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("entities", None),
            MessageEntity
        )

    @property
    def animation(
        self
    ) -> Optional["Animation"]:
        return Types.Typify(
            self._d.get("animation", None),
            Animation
        )

    @property
    def audio(
        self
    ) -> Optional["Audio"]:
        return Types.Typify(
            self._d.get("audio", None),
            Audio
        )

    @property
    def document(
        self
    ) -> Optional["Document"]:
        return Types.Typify(
            self._d.get("document", None),
            Document
        )

    @property
    def photo(
        self
    ) -> Optional["List[PhotoSize]"]:
        return Types.Typify(
            self._d.get("photo", None),
            PhotoSize
        )

    @property
    def sticker(
        self
    ) -> Optional["Sticker"]:
        return Types.Typify(
            self._d.get("sticker", None),
            Sticker
        )

    @property
    def video(
        self
    ) -> Optional["Video"]:
        return Types.Typify(
            self._d.get("video", None),
            Video
        )

    @property
    def video_note(
        self
    ) -> Optional["VideoNote"]:
        return Types.Typify(
            self._d.get("video_note", None),
            VideoNote
        )

    @property
    def voice(
        self
    ) -> Optional["Voice"]:
        return Types.Typify(
            self._d.get("voice", None),
            Voice
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def contact(
        self
    ) -> Optional["Contact"]:
        return Types.Typify(
            self._d.get("contact", None),
            Contact
        )

    @property
    def dice(
        self
    ) -> Optional["Dice"]:
        return Types.Typify(
            self._d.get("dice", None),
            Dice
        )

    @property
    def game(
        self
    ) -> Optional["Game"]:
        return Types.Typify(
            self._d.get("game", None),
            Game
        )

    @property
    def poll(
        self
    ) -> Optional["Poll"]:
        return Types.Typify(
            self._d.get("poll", None),
            Poll
        )

    @property
    def venue(
        self
    ) -> Optional["Venue"]:
        return Types.Typify(
            self._d.get("venue", None),
            Venue
        )

    @property
    def location(
        self
    ) -> Optional["Location"]:
        return Types.Typify(
            self._d.get("location", None),
            Location
        )

    @property
    def new_chat_members(
        self
    ) -> Optional["List[User]"]:
        return Types.Typify(
            self._d.get("new_chat_members", None),
            User
        )

    @property
    def left_chat_member(
        self
    ) -> Optional["User"]:
        return Types.Typify(
            self._d.get("left_chat_member", None),
            User
        )

    @property
    def new_chat_title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("new_chat_title", None),
            String
        )

    @property
    def new_chat_photo(
        self
    ) -> Optional["List[PhotoSize]"]:
        return Types.Typify(
            self._d.get("new_chat_photo", None),
            PhotoSize
        )

    @property
    def delete_chat_photo(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("delete_chat_photo", None),
            Boolean
        )

    @property
    def group_chat_created(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("group_chat_created", None),
            Boolean
        )

    @property
    def supergroup_chat_created(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("supergroup_chat_created", None),
            Boolean
        )

    @property
    def channel_chat_created(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("channel_chat_created", None),
            Boolean
        )

    @property
    def message_auto_delete_timer_changed(
        self
    ) -> Optional["MessageAutoDeleteTimerChanged"]:
        return Types.Typify(
            self._d.get("message_auto_delete_timer_changed", None),
            MessageAutoDeleteTimerChanged
        )

    @property
    def migrate_to_chat_id(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("migrate_to_chat_id", None),
            Integer
        )

    @property
    def migrate_from__chat_id(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("migrate_from_chat_id", None),
            Integer
        )

    @property
    def pinned_message(
        self
    ) -> Optional["Message"]:
        return Types.Typify(
            self._d.get("pinned_message", None),
            Message
        )

    @property
    def invoice(
        self
    ) -> Optional["Invoice"]:
        return Types.Typify(
            self._d.get("invoice", None),
            Invoice
        )

    @property
    def successful_payment(
        self
    ) -> Optional["SuccessfulPayment"]:
        return Types.Typify(
            self._d.get("successful_payment", None),
            SuccessfulPayment
        )

    @property
    def connected_website(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("connected_website", None),
            String
        )

    @property
    def passport_data(
        self
    ) -> Optional["PassportData"]:
        return Types.Typify(
            self._d.get("passport_data", None),
            PassportData
        )

    @property
    def proximity_alert_triggered(
        self
    ) -> Optional["ProximityAlertTriggered"]:
        return Types.Typify(
            self._d.get("proximity_alert_triggered", None),
            ProximityAlertTriggered
        )

    @property
    def video_chat_scheduled(
        self
    ) -> Optional["VideoChatScheduled"]:
        return Types.Typify(
            self._d.get("video_chat_scheduled", None),
            VideoChatScheduled
        )

    @property
    def video_chat_started(
        self
    ) -> Optional["VideoChatStarted"]:
        return Types.Typify(
            self._d.get("video_chat_started", None),
            VideoChatStarted
        )

    @property
    def video_chat_ended(
        self
    ) -> Optional["VideoChatEnded"]:
        return Types.Typify(
            self._d.get("video_chat_ended", None),
            VideoChatEnded
        )

    @property
    def video_chat_participants_invited(
        self
    ) -> Optional["VideoChatParticipantsInvited"]:
        return Types.Typify(
            self._d.get("video_chat_participants_invited", None),
            VideoChatParticipantsInvited
        )

    @property
    def web_app_data(
        self
    ) -> Optional["WebAppData"]:
        return Types.Typify(
            self._d.get("web_app_data", None),
            WebAppData
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )


class MessageId(Types.DefaultType):

    @property
    def message_id(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("message_id", None),
            Integer
        )


class MessageEntity(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def offset(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("offset", None),
            Integer
        )

    @property
    def length(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("length", None),
            Integer
        )

    @property
    def url(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("url", None),
            String
        )

    @property
    def user(
        self
    ) -> Optional["User"]:
        return Types.Typify(
            self._d.get("user", None),
            User
        )

    @property
    def language(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("language", None),
            String
        )


class PhotoSize(Types.DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_id", None),
            String
        )

    @property
    def file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_unique_id", None),
            String
        )

    @property
    def width(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("width", None),
            Integer
        )

    @property
    def height(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("height", None),
            Integer
        )

    @property
    def file_size(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("file_size", None),
            Integer
        )


class Animation(Types.DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_id", None),
            String
        )

    @property
    def file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_unique_id", None),
            String
        )

    @property
    def width(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("width", None),
            Integer
        )

    @property
    def height(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("height", None),
            Integer
        )

    @property
    def duration(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("duration", None),
            Integer
        )

    @property
    def thumb(
        self
    ) -> Optional["PhotoSize"]:
        return Types.Typify(
            self._d.get("thumb", None),
            PhotoSize
        )

    @property
    def file_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("file_name", None),
            String
        )

    @property
    def mime_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("mime_type", None),
            String
        )

    @property
    def file_size(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("file_size", None),
            Integer
        )


class Audio(Types.DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_id", None),
            String
        )

    @property
    def file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_unique_id", None),
            String
        )

    @property
    def duration(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("duration", None),
            Integer
        )

    @property
    def performer(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("performer", None),
            String
        )

    @property
    def title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def file_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("file_name", None),
            String
        )

    @property
    def mime_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("mime_type", None),
            String
        )

    @property
    def file_size(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("file_size", None),
            Integer
        )

    @property
    def thumb(
        self
    ) -> Optional["PhotoSize"]:
        return Types.Typify(
            self._d.get("thumb", None),
            PhotoSize
        )


class Document(Types.DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_id", None),
            String
        )

    @property
    def file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_unique_id", None),
            String
        )

    @property
    def thumb(
        self
    ) -> Optional["PhotoSize"]:
        return Types.Typify(
            self._d.get("thumb", None),
            PhotoSize
        )

    @property
    def file_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("file_name", None),
            String
        )

    @property
    def mime_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("mime_type", None),
            String
        )

    @property
    def file_size(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("file_size", None),
            Integer
        )


class Video(Types.DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_id", None),
            String
        )

    @property
    def file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_unique_id", None),
            String
        )

    @property
    def width(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("width", None),
            Integer
        )

    @property
    def height(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("height", None),
            Integer
        )

    @property
    def duration(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("duration", None),
            Integer
        )

    @property
    def thumb(
        self
    ) -> Optional["PhotoSize"]:
        return Types.Typify(
            self._d.get("thumb", None),
            PhotoSize
        )

    @property
    def file_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("file_name", None),
            String
        )

    @property
    def mime_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("mime_type", None),
            String
        )

    @property
    def file_size(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("file_size", None),
            Integer
        )


class VideoNote(Types.DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_id", None),
            String
        )

    @property
    def file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_unique_id", None),
            String
        )

    @property
    def length(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("length", None),
            Integer
        )

    @property
    def duration(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("duration", None),
            Integer
        )

    @property
    def thumb(
        self
    ) -> Optional["PhotoSize"]:
        return Types.Typify(
            self._d.get("thumb", None),
            PhotoSize
        )

    @property
    def file_size(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("file_size", None),
            Integer
        )


class Voice(Types.DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_id", None),
            String
        )

    @property
    def file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_unique_id", None),
            String
        )

    @property
    def duration(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("duration", None),
            Integer
        )

    @property
    def mime_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("mime_type", None),
            String
        )

    @property
    def file_size(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("file_size", None),
            Integer
        )


class Contact(Types.DefaultType):

    @property
    def phone_number(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("phone_number", None),
            String
        )

    @property
    def first_name(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("first_name", None),
            String
        )

    @property
    def last_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("last_name", None),
            String
        )

    @property
    def user_id(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("user_id", None),
            Integer
        )

    @property
    def vcard(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("vcard", None),
            String
        )


class Dice(Types.DefaultType):

    @property
    def emoji(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("emoji", None),
            String
        )

    @property
    def value(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("value", None),
            Integer
        )


class PollOption(Types.DefaultType):

    @property
    def text(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("text", None),
            String
        )

    @property
    def voter_count(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("voter_count", None),
            Integer
        )


class PollAnswer(Types.DefaultType):

    @property
    def poll_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("poll_id", None),
            String
        )

    @property
    def user(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("user", None),
            User
        )

    @property
    def option_ids(
        self
    ) -> "List[Integer]":
        return Types.Typify(
            self._d.get("option_ids", None),
            Integer
        )


class Poll(Types.DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def question(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("question", None),
            String
        )

    @property
    def options(
        self
    ) -> "List[PollOption]":
        return Types.Typify(
            self._d.get("options", None),
            PollOption
        )

    @property
    def total_voter_count(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("total_voter_count", None),
            Integer
        )

    @property
    def is_closed(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_closed", None),
            Boolean
        )

    @property
    def is_anonymous(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_anonymous", None),
            Boolean
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def allows_multiple_answers(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("allows_multiple_answers", None),
            Boolean
        )

    @property
    def correct_option_id(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("correct_option_id", None),
            Integer
        )

    @property
    def explanation(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("explanation", None),
            String
        )

    @property
    def explanation_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("explanation_entities", None),
            MessageEntity
        )

    @property
    def open_period(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("open_period", None),
            Integer
        )

    @property
    def close_date(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("close_date", None),
            Integer
        )


class Location(Types.DefaultType):

    @property
    def longitude(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("longitude", None),
            Float
        )

    @property
    def latitude(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("latitude", None),
            Float
        )

    @property
    def horizontal_accuracy(
        self
    ) -> Optional["Float"]:
        return Types.Typify(
            self._d.get("horizontal_accuracy", None),
            Float
        )

    @property
    def live_period(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("live_period", None),
            Integer
        )

    @property
    def heading(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("heading", None),
            Integer
        )

    @property
    def proximity_alert_radius(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("proximity_alert_radius", None),
            Integer
        )


class Venue(Types.DefaultType):

    @property
    def location(
        self
    ) -> "Location":
        return Types.Typify(
            self._d.get("location", None),
            Location
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def address(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("address", None),
            String
        )

    @property
    def foursquare_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("foursquare_id", None),
            String
        )

    @property
    def foursquare_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("foursquare_type", None),
            String
        )

    @property
    def google_place_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("google_place_id", None),
            String
        )

    @property
    def google_place_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("google_place_type", None),
            String
        )


class WebAppData(Types.DefaultType):

    @property
    def data(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("data", None),
            String
        )

    @property
    def button_text(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("button_text", None),
            String
        )


class ProximityAlertTriggered(Types.DefaultType):

    @property
    def traveler(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("traveler", None),
            User
        )

    @property
    def watcher(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("watcher", None),
            User
        )

    @property
    def distance(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("distance", None),
            Integer
        )


class MessageAutoDeleteTimerChanged(Types.DefaultType):

    @property
    def message_auto_delete_time(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("message_auto_delete_time", None),
            Integer
        )


class VideoChatScheduled(Types.DefaultType):

    @property
    def start_date(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("start_date", None),
            Integer
        )


class VideoChatStarted(Types.DefaultType):
    ...


class VideoChatEnded(Types.DefaultType):

    @property
    def duration(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("duration", None),
            Integer
        )


class VideoChatParticipantsInvited(Types.DefaultType):

    @property
    def users(
        self
    ) -> "List[User]":
        return Types.Typify(
            self._d.get("users", None),
            User
        )


class UserProfilePhotos(Types.DefaultType):

    @property
    def total_count(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("total_count", None),
            Integer
        )

    @property
    def photos(
        self
    ) -> "List[List[PhotoSize]]":
        return Types.Typify(
            self._d.get("photos", None),
            PhotoSize
        )


class File(Types.DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_id", None),
            String
        )

    @property
    def file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_unique_id", None),
            String
        )

    @property
    def file_size(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("file_size", None),
            Integer
        )

    @property
    def file_path(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("file_path", None),
            String
        )


class WebAppInfo(Types.DefaultType):

    @property
    def url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("url", None),
            String
        )


class ReplyKeyboardMarkup(Types.DefaultType):

    @property
    def keyboard(
        self
    ) -> "List[List[KeyboardButton]]":
        return Types.Typify(
            self._d.get("keyboard", None),
            KeyboardButton
        )

    @property
    def resize_keyboard(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("resize_keyboard", None),
            Boolean
        )

    @property
    def one_time_keyboard(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("one_time_keyboard", None),
            Boolean
        )

    @property
    def input_field_placeholder(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("input_field_placeholder", None),
            String
        )

    @property
    def selective(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("selective", None),
            Boolean
        )


class KeyboardButton(Types.DefaultType):

    @property
    def text(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("text", None),
            String
        )

    @property
    def request_contact(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("request_contact", None),
            Boolean
        )

    @property
    def request_location(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("request_location", None),
            Boolean
        )

    @property
    def request_poll(
        self
    ) -> Optional["KeyboardButtonPollType"]:
        return Types.Typify(
            self._d.get("request_poll", None),
            KeyboardButtonPollType
        )

    @property
    def web_app(
        self
    ) -> Optional["WebAppInfo"]:
        return Types.Typify(
            self._d.get("web_app", None),
            WebAppInfo
        )


class KeyboardButtonPollType(Types.DefaultType):

    @property
    def type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("type", None),
            String
        )


class ReplyKeyboardRemove(Types.DefaultType):

    @property
    def remove_keyboard(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("remove_keyboard", None),
            Boolean
        )

    @property
    def selective(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("selective", None),
            Boolean
        )


class InlineKeyboardMarkup(Types.DefaultType):

    @property
    def inline_keyboard(
        self
    ) -> "List[List[InlineKeyboardButton]]":
        return Types.Typify(
            self._d.get("inline_keyboard", None),
            InlineKeyboardButton
        )


class InlineKeyboardButton(Types.DefaultType):

    @property
    def text(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("text", None),
            String
        )

    @property
    def url(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("url", None),
            String
        )

    @property
    def callback_data(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("callback_data", None),
            String
        )

    @property
    def web_app(
        self
    ) -> Optional["WebAppInfo"]:
        return Types.Typify(
            self._d.get("web_app", None),
            WebAppInfo
        )

    @property
    def login_url(
        self
    ) -> Optional["LoginUrl"]:
        return Types.Typify(
            self._d.get("login_url", None),
            LoginUrl
        )

    @property
    def switch_inline_query(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("switch_inline_query", None),
            String
        )

    @property
    def switch_inline_query_current_chat(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("switch_inline_query_current_chat", None),
            String
        )

    @property
    def callback_game(
        self
    ) -> Optional["CallbackGame"]:
        return Types.Typify(
            self._d.get("callback_game", None),
            CallbackGame
        )

    @property
    def pay(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("pay", None),
            Boolean
        )


class LoginUrl(Types.DefaultType):

    @property
    def url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("url", None),
            String
        )

    @property
    def forward_text(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("forward_text", None),
            String
        )

    @property
    def bot_username(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("bot_username", None),
            String
        )

    @property
    def request_write_access(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("request_write_access", None),
            Boolean
        )


class CallbackQuery(Types.DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def from_(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("from", None),
            User
        )

    @property
    def message(
        self
    ) -> Optional["Message"]:
        return Types.Typify(
            self._d.get("message", None),
            Message
        )

    @property
    def inline_message_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("inline_message_id", None),
            String
        )

    @property
    def chat_instance(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("chat_instance", None),
            String
        )

    @property
    def data(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("data", None),
            String
        )

    @property
    def game_short_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("game_short_name", None),
            String
        )


class ForceReply(Types.DefaultType):

    @property
    def force_reply(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("force_reply", None),
            Boolean
        )

    @property
    def input_field_placeholder(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("input_field_placeholder", None),
            String
        )

    @property
    def selective(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("selective", None),
            Boolean
        )


class ChatPhoto(Types.DefaultType):

    @property
    def small_file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("small_file_id", None),
            String
        )

    @property
    def small_file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("small_file_unique_id", None),
            String
        )

    @property
    def big_file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("big_file_id", None),
            String
        )

    @property
    def big_file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("big_file_unique_id", None),
            String
        )


class ChatInviteLink(Types.DefaultType):

    @property
    def invite_link(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("invite_link", None),
            String
        )

    @property
    def creator(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("creator", None),
            User
        )

    @property
    def creates_join_request(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("creates_join_request", None),
            Boolean
        )

    @property
    def is_primary(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_primary", None),
            Boolean
        )

    @property
    def is_revoked(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_revoked", None),
            Boolean
        )

    @property
    def name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("name", None),
            String
        )

    @property
    def expire_date(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("expire_date", None),
            Integer
        )

    @property
    def member_limit(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("member_limit", None),
            Integer
        )

    @property
    def pending_join_request_count(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("pending_join_request_count", None),
            Integer
        )


class ChatAdministratorRights(Types.DefaultType):

    @property
    def is_anonymous(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_anonymous", None),
            Boolean
        )

    @property
    def can_manage_chat(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_manage_chat", None),
            Boolean
        )

    @property
    def can_delete_messages(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_delete_messages", None),
            Boolean
        )

    @property
    def can_manage_video_chats(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_manage_video_chats", None),
            Boolean
        )

    @property
    def can_restrict_members(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_restrict_members", None),
            Boolean
        )

    @property
    def can_promote_members(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_promote_members", None),
            Boolean
        )

    @property
    def can_change_info(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_change_info", None),
            Boolean
        )

    @property
    def can_invite_users(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_invite_users", None),
            Boolean
        )

    @property
    def can_post_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_post_messages", None),
            Boolean
        )

    @property
    def can_edit_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_edit_messages", None),
            Boolean
        )

    @property
    def can_pin_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_pin_messages", None),
            Boolean
        )


class ChatMember(Types.DefaultType):
    ...


class ChatMemberOwner(Types.DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("status", None),
            String
        )

    @property
    def user(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("user", None),
            User
        )

    @property
    def is_anonymous(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_anonymous", None),
            Boolean
        )

    @property
    def custom_title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("custom_title", None),
            String
        )


class ChatMemberAdministrator(Types.DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("status", None),
            String
        )

    @property
    def user(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("user", None),
            User
        )

    @property
    def can_be_edited(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_be_edited", None),
            Boolean
        )

    @property
    def is_anonymous(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_anonymous", None),
            Boolean
        )

    @property
    def can_manage_chat(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_manage_chat", None),
            Boolean
        )

    @property
    def can_delete_messages(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_delete_messages", None),
            Boolean
        )

    @property
    def can_manage_video_chats(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_manage_video_chats", None),
            Boolean
        )

    @property
    def can_restrict_members(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_restrict_members", None),
            Boolean
        )

    @property
    def can_promote_members(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_promote_members", None),
            Boolean
        )

    @property
    def can_change_info(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_change_info", None),
            Boolean
        )

    @property
    def can_invite_users(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_invite_users", None),
            Boolean
        )

    @property
    def can_post_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_post_messages", None),
            Boolean
        )

    @property
    def can_edit_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_edit_messages", None),
            Boolean
        )

    @property
    def can_pin_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_pin_messages", None),
            Boolean
        )

    @property
    def custom_title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("custom_title", None),
            String
        )


class ChatMemberMember(Types.DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("status", None),
            String
        )

    @property
    def user(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("user", None),
            User
        )


class ChatMemberRestricted(Types.DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("status", None),
            String
        )

    @property
    def user(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("user", None),
            User
        )

    @property
    def is_member(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_member", None),
            Boolean
        )

    @property
    def can_change_info(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_change_info", None),
            Boolean
        )

    @property
    def can_invite_users(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_invite_users", None),
            Boolean
        )

    @property
    def can_pin_messages(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_pin_messages", None),
            Boolean
        )

    @property
    def can_send_messages(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_send_messages", None),
            Boolean
        )

    @property
    def can_send_media_messages(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_send_media_messages", None),
            Boolean
        )

    @property
    def can_send_polls(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_send_polls", None),
            Boolean
        )

    @property
    def can_send_other_messages(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_send_other_messages", None),
            Boolean
        )

    @property
    def can_add_web_page_previews(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("can_add_web_page_previews", None),
            Boolean
        )

    @property
    def until_date(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("until_date", None),
            Integer
        )


class ChatMemberLeft(Types.DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("status", None),
            String
        )

    @property
    def user(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("user", None),
            User
        )


class ChatMemberBanned(Types.DefaultType):

    @property
    def status(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("status", None),
            String
        )

    @property
    def user(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("user", None),
            User
        )

    @property
    def until_date(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("until_date", None),
            Integer
        )


class ChatMemberUpdated(Types.DefaultType):

    @property
    def chat(
        self
    ) -> "Chat":
        return Types.Typify(
            self._d.get("chat", None),
            Chat
        )

    @property
    def from_(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("from", None),
            User
        )

    @property
    def date(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("date", None),
            Integer
        )

    @property
    def old_chat_member(
        self
    ) -> "ChatMember":
        return Types.Typify(
            self._d.get("old_chat_member", None),
            ChatMember
        )

    @property
    def new_chat_member(
        self
    ) -> "ChatMember":
        return Types.Typify(
            self._d.get("new_chat_member", None),
            ChatMember
        )

    @property
    def invite_link(
        self
    ) -> Optional["ChatInviteLink"]:
        return Types.Typify(
            self._d.get("invite_link", None),
            ChatInviteLink
        )


class ChatJoinRequest(Types.DefaultType):

    @property
    def chat(
        self
    ) -> "Chat":
        return Types.Typify(
            self._d.get("chat", None),
            Chat
        )

    @property
    def from_(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("from", None),
            User
        )

    @property
    def date(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("date", None),
            Integer
        )

    @property
    def bio(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("bio", None),
            String
        )

    @property
    def invite_link(
        self
    ) -> Optional["ChatInviteLink"]:
        return Types.Typify(
            self._d.get("invite_link", None),
            ChatInviteLink
        )


class ChatPermissions(Types.DefaultType):

    @property
    def can_send_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_send_messages", None),
            Boolean
        )

    @property
    def can_send_media_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_send_media_messages", None),
            Boolean
        )

    @property
    def can_send_polls(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_send_polls", None),
            Boolean
        )

    @property
    def can_send_other_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_send_other_messages", None),
            Boolean
        )

    @property
    def can_add_web_page_previews(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_add_web_page_previews", None),
            Boolean
        )

    @property
    def can_change_info(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_change_info", None),
            Boolean
        )

    @property
    def can_invite_users(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_invite_users", None),
            Boolean
        )

    @property
    def can_pin_messages(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("can_pin_messages", None),
            Boolean
        )


class ChatLocation(Types.DefaultType):

    @property
    def location(
        self
    ) -> "Location":
        return Types.Typify(
            self._d.get("location", None),
            Location
        )

    @property
    def address(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("address", None),
            String
        )


class BotCommand(Types.DefaultType):

    @property
    def command(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("command", None),
            String
        )

    @property
    def description(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("description", None),
            String
        )


class BotCommandScope(Types.DefaultType):
    ...


class BotCommandScopeDefault(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )


class BotCommandScopeAllPrivateChats(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )


class BotCommandScopeAllGroupChats(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )


class BotCommandScopeAllChatAdministrators(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )


class BotCommandScopeChat(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def chat_id(
        self
    ) -> Union["Integer", "String"]:
        return Types.Typify(
            Types.Typify(
                self._d.get("chat_id", None),
                Integer
            ),
            String
        )


class BotCommandScopeChatAdministrators(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def chat_id(
        self
    ) -> Union["Integer", "String"]:
        return Types.Typify(
            Types.Typify(
                self._d.get("chat_id", None),
                Integer
            ),
            String
        )


class BotCommandScopeChatMember(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def chat_id(
        self
    ) -> Union["Integer", "String"]:
        return Types.Typify(
            Types.Typify(
                self._d.get("chat_id", None),
                Integer
            ),
            String
        )

    @property
    def user_id(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("user_id", None),
            Integer
        )


class MenuButton(Types.DefaultType):
    ...


class MenuButtonCommands(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )


class MenuButtonWebApp(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def text(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("text", None),
            String
        )

    @property
    def web_app(
        self
    ) -> "WebAppInfo":
        return Types.Typify(
            self._d.get("web_app", None),
            WebAppInfo
        )


class MenuButtonDefault(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )


class ResponseParameters(Types.DefaultType):

    @property
    def migrate_to_chat_id(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("migrate_to_chat_id", None),
            Integer
        )

    @property
    def retry_after(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("retry_after", None),
            Integer
        )


class InputMedia(Types.DefaultType):
    ...


class InputMediaPhoto(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def media(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("media", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )


class InputMediaVideo(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def media(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("media", None),
            String
        )

    @property
    def thumb(
        self
    ) -> Optional[Union["InputFile", "String"]]:
        return Types.Typify(
            Types.Typify(
                self._d.get("thumb", None),
                InputFile
            ),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("width", None),
            Integer
        )

    @property
    def height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("height", None),
            Integer
        )

    @property
    def duration(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("duration", None),
            Integer
        )

    @property
    def supports_streaming(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("supports_streaming", None),
            Boolean
        )


class InputMediaAnimation(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def media(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("media", None),
            String
        )

    @property
    def thumb(
        self
    ) -> Optional[Union["InputFile", "String"]]:
        return Types.Typify(
            Types.Typify(
                self._d.get("thumb", None),
                InputFile
            ),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("width", None),
            Integer
        )

    @property
    def height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("height", None),
            Integer
        )

    @property
    def duration(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("duration", None),
            Integer
        )


class InputMediaAudio(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def media(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("media", None),
            String
        )

    @property
    def thumb(
        self
    ) -> Optional[Union["InputFile", "String"]]:
        return Types.Typify(
            Types.Typify(
                self._d.get("thumb", None),
                InputFile
            ),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def duration(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("duration", None),
            Integer
        )

    @property
    def performer(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("performer", None),
            String
        )

    @property
    def title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("title", None),
            String
        )


class InputMediaDocument(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def media(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("media", None),
            String
        )

    @property
    def thumb(
        self
    ) -> Optional[Union["InputFile", "String"]]:
        return Types.Typify(
            Types.Typify(
                self._d.get("thumb", None),
                InputFile
            ),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def disable_content_type_detection(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("disable_content_type_detection", None),
            Boolean
        )


class InputFile(Types.DefaultType):
    ...


class Sticker(Types.DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_id", None),
            String
        )

    @property
    def file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_unique_id", None),
            String
        )

    @property
    def width(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("width", None),
            Integer
        )

    @property
    def height(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("height", None),
            Integer
        )

    @property
    def is_animated(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_animated", None),
            Boolean
        )

    @property
    def is_video(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_video", None),
            Boolean
        )

    @property
    def thumb(
        self
    ) -> Optional["PhotoSize"]:
        return Types.Typify(
            self._d.get("thumb", None),
            PhotoSize
        )

    @property
    def emoji(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("emoji", None),
            String
        )

    @property
    def set_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("set_name", None),
            String
        )

    @property
    def premium_animation(
        self
    ) -> Optional["File"]:
        return Types.Typify(
            self._d.get("premium_animation", None),
            File
        )

    @property
    def mask_position(
        self
    ) -> Optional["MaskPosition"]:
        return Types.Typify(
            self._d.get("mask_position", None),
            MaskPosition
        )

    @property
    def file_size(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("file_size", None),
            Integer
        )


class StickerSet(Types.DefaultType):

    @property
    def name(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("name", None),
            String
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def is_animated(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_animated", None),
            Boolean
        )

    @property
    def is_video(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("is_video", None),
            Boolean
        )

    @property
    def contains_masks(
        self
    ) -> "Boolean":
        return Types.Typify(
            self._d.get("contains_masks", None),
            Boolean
        )

    @property
    def stickers(
        self
    ) -> "List[Sticker]":
        return Types.Typify(
            self._d.get("stickers", None),
            Sticker
        )

    @property
    def thumb(
        self
    ) -> Optional["PhotoSize"]:
        return Types.Typify(
            self._d.get("thumb", None),
            PhotoSize
        )


class MaskPosition(Types.DefaultType):

    @property
    def point(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("point", None),
            String
        )

    @property
    def x_shift(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("x_shift", None),
            Float
        )

    @property
    def y_shift(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("y_shift", None),
            Float
        )

    @property
    def scale(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("scale", None),
            Float
        )


class InlineQuery(Types.DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def from_(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("from", None),
            User
        )

    @property
    def query(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("query", None),
            String
        )

    @property
    def offset(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("offset", None),
            String
        )

    @property
    def chat_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("chat_type", None),
            String
        )

    @property
    def location(
        self
    ) -> Optional["Location"]:
        return Types.Typify(
            self._d.get("location", None),
            Location
        )


class InlineQueryResult(Types.DefaultType):
    ...


class InlineQueryResultArticle(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def input_message_content(
        self
    ) -> "InputMessageContent":
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def url(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("url", None),
            String
        )

    @property
    def hide_url(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("hide_url", None),
            Boolean
        )

    @property
    def description(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def thumb_url(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("thumb_url", None),
            String
        )

    @property
    def thumb_width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("thumb_width", None),
            Integer
        )

    @property
    def thumb_height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("thumb_height", None),
            Integer
        )


class InlineQueryResultPhoto(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def photo_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("photo_url", None),
            String
        )

    @property
    def thumb_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("thumb_url", None),
            String
        )

    @property
    def photo_width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("photo_width", None),
            Integer
        )

    @property
    def photo_height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("photo_height", None),
            Integer
        )

    @property
    def title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def description(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultGif(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def gif_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("gif_url", None),
            String
        )

    @property
    def gif_width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("gif_width", None),
            Integer
        )

    @property
    def gif_height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("gif_height", None),
            Integer
        )

    @property
    def gif_duration(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("gif_duration", None),
            Integer
        )

    @property
    def thumb_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("thumb_url", None),
            String
        )

    @property
    def thumb_mime_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("thumb_mime_type", None),
            String
        )

    @property
    def title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultMpeg4Gif(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def mpeg4_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("mpeg4_url", None),
            String
        )

    @property
    def mpeg4_width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("mpeg4_width", None),
            Integer
        )

    @property
    def mpeg4_height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("mpeg4_height", None),
            Integer
        )

    @property
    def mpeg4_duration(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("mpeg4_duration", None),
            Integer
        )

    @property
    def thumb_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("thumb_url", None),
            String
        )

    @property
    def thumb_mime_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("thumb_mime_type", None),
            String
        )

    @property
    def title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultVideo(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def video_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("video_url", None),
            String
        )

    @property
    def mime_type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("mime_type", None),
            String
        )

    @property
    def thumb_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("thumb_url", None),
            String
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def video_width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("video_width", None),
            Integer
        )

    @property
    def video_height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("video_height", None),
            Integer
        )

    @property
    def video_duration(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("video_duration", None),
            Integer
        )

    @property
    def description(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultAudio(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def audio_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("audio_url", None),
            String
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def performer(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("performer", None),
            String
        )

    @property
    def audio_duration(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("audio_duration", None),
            Integer
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultVoice(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def voice_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("voice_url", None),
            String
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def voice_duration(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("voice_duration", None),
            Integer
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultDocument(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def document_url(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("document_url", None),
            String
        )

    @property
    def mime_type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("mime_type", None),
            String
        )

    @property
    def description(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )

    @property
    def thumb_url(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("thumb_url", None),
            String
        )

    @property
    def thumb_width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("thumb_width", None),
            Integer
        )

    @property
    def thumb_height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("thumb_height", None),
            Integer
        )


class InlineQueryResultLocation(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def latitude(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("latitude", None),
            Float
        )

    @property
    def longitude(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("longitude", None),
            Float
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def horizontal_accuracy(
        self
    ) -> Optional["Float"]:
        return Types.Typify(
            self._d.get("horizontal_accuracy", None),
            Float
        )

    @property
    def live_period(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("live_period", None),
            Integer
        )

    @property
    def heading(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("heading", None),
            Integer
        )

    @property
    def proximity_alert_radius(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("proximity_alert_radius", None),
            Integer
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )

    @property
    def thumb_url(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("thumb_url", None),
            String
        )

    @property
    def thumb_width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("thumb_width", None),
            Integer
        )

    @property
    def thumb_height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("thumb_height", None),
            Integer
        )


class InlineQueryResultVenue(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def latitude(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("latitude", None),
            Float
        )

    @property
    def longitude(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("longitude", None),
            Float
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def address(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("address", None),
            String
        )

    @property
    def foursquare_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("foursquare_id", None),
            String
        )

    @property
    def foursquare_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("foursquare_type", None),
            String
        )

    @property
    def google_place_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("google_place_id", None),
            String
        )

    @property
    def google_place_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("google_place_type", None),
            String
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )

    @property
    def thumb_url(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("thumb_url", None),
            String
        )

    @property
    def thumb_width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("thumb_width", None),
            Integer
        )

    @property
    def thumb_height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("thumb_height", None),
            Integer
        )


class InlineQueryResultContact(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def phone_number(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("phone_number", None),
            String
        )

    @property
    def first_name(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("first_name", None),
            String
        )

    @property
    def last_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("last_name", None),
            String
        )

    @property
    def vcard(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("vcard", None),
            String
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )

    @property
    def thumb_url(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("thumb_url", None),
            String
        )

    @property
    def thumb_width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("thumb_width", None),
            Integer
        )

    @property
    def thumb_height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("thumb_height", None),
            Integer
        )


class InlineQueryResultGame(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def game_short_name(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("game_short_name", None),
            String
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )


class InlineQueryResultCachedPhoto(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def photo_file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("photo_file_id", None),
            String
        )

    @property
    def title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def description(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultCachedGif(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def gif_file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("gif_file_id", None),
            String
        )

    @property
    def title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultCachedMpeg4Gif(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def mpeg4_file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("mpeg4_file_id", None),
            String
        )

    @property
    def title(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultCachedSticker(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def sticker_file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("sticker_file_id", None),
            String
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultCachedDocument(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def document_file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("document_file_id", None),
            String
        )

    @property
    def description(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultCachedVideo(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def video_file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("video_file_id", None),
            String
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def description(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultCachedVoice(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def voice_file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("voice_file_id", None),
            String
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InlineQueryResultCachedAudio(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def audio_file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("audio_file_id", None),
            String
        )

    @property
    def caption(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("caption", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def caption_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("caption_entities", None),
            MessageEntity
        )

    @property
    def reply_markup(
        self
    ) -> Optional["InlineKeyboardMarkup"]:
        return Types.Typify(
            self._d.get("reply_markup", None),
            InlineKeyboardMarkup
        )

    @property
    def input_message_content(
        self
    ) -> Optional["InputMessageContent"]:
        return Types.Typify(
            self._d.get("input_message_content", None),
            InputMessageContent
        )


class InputMessageContent(Types.DefaultType):
    ...


class InputTextMessageContent(Types.DefaultType):

    @property
    def message_text(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("message_text", None),
            String
        )

    @property
    def parse_mode(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("parse_mode", None),
            String
        )

    @property
    def entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("entities", None),
            MessageEntity
        )

    @property
    def disable_web_page_preview(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("disable_web_page_preview", None),
            Boolean
        )


class InputLocationMessageContent(Types.DefaultType):

    @property
    def latitude(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("latitude", None),
            Float
        )

    @property
    def longitude(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("longitude", None),
            Float
        )

    @property
    def horizontal_accuracy(
        self
    ) -> Optional["Float"]:
        return Types.Typify(
            self._d.get("horizontal_accuracy", None),
            Float
        )

    @property
    def live_period(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("live_period", None),
            Integer
        )

    @property
    def heading(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("heading", None),
            Integer
        )

    @property
    def proximity_alert_radius(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("proximity_alert_radius", None),
            Integer
        )


class InputVenueMessageContent(Types.DefaultType):

    @property
    def latitude(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("latitude", None),
            Float
        )

    @property
    def longitude(
        self
    ) -> "Float":
        return Types.Typify(
            self._d.get("longitude", None),
            Float
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def address(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("address", None),
            String
        )

    @property
    def foursquare_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("foursquare_id", None),
            String
        )

    @property
    def foursquare_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("foursquare_type", None),
            String
        )

    @property
    def google_place_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("google_place_id", None),
            String
        )

    @property
    def google_place_type(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("google_place_type", None),
            String
        )


class InputContactMessageContent(Types.DefaultType):

    @property
    def phone_number(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("phone_number", None),
            String
        )

    @property
    def first_name(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("first_name", None),
            String
        )

    @property
    def last_name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("last_name", None),
            String
        )

    @property
    def vcard(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("vcard", None),
            String
        )


class InputInvoiceMessageContent(Types.DefaultType):

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def description(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def payload(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("payload", None),
            String
        )

    @property
    def provider_token(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("provider_token", None),
            String
        )

    @property
    def currency(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("currency", None),
            String
        )

    @property
    def prices(
        self
    ) -> "List[LabeledPrice]":
        return Types.Typify(
            self._d.get("prices", None),
            LabeledPrice
        )

    @property
    def max_tip_amount(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("max_tip_amount", None),
            Integer
        )

    @property
    def suggested_tip_amounts(
        self
    ) -> Optional["List[Integer]"]:
        return Types.Typify(
            self._d.get("suggested_tip_amounts", None),
            Integer
        )

    @property
    def provider_data(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("provider_data", None),
            String
        )

    @property
    def photo_url(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("photo_url", None),
            String
        )

    @property
    def photo_size(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("photo_size", None),
            Integer
        )

    @property
    def photo_width(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("photo_width", None),
            Integer
        )

    @property
    def photo_height(
        self
    ) -> Optional["Integer"]:
        return Types.Typify(
            self._d.get("photo_height", None),
            Integer
        )

    @property
    def need_name(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("need_name", None),
            Boolean
        )

    @property
    def need_phone_number(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("need_phone_number", None),
            Boolean
        )

    @property
    def need_email(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("need_email", None),
            Boolean
        )

    @property
    def need_shipping_address(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("need_shipping_address", None),
            Boolean
        )

    @property
    def send_phone_number_to_provider(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("send_phone_number_to_provider", None),
            Boolean
        )

    @property
    def send_email_to_provider(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("send_email_to_provider", None),
            Boolean
        )

    @property
    def is_flexible(
        self
    ) -> Optional["Boolean"]:
        return Types.Typify(
            self._d.get("is_flexible", None),
            Boolean
        )


class ChosenInlineResult(Types.DefaultType):

    @property
    def result_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("result_id", None),
            String
        )

    @property
    def from_(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("from", None),
            User
        )

    @property
    def location(
        self
    ) -> Optional["Location"]:
        return Types.Typify(
            self._d.get("location", None),
            Location
        )

    @property
    def inline_message_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("inline_message_id", None),
            String
        )

    @property
    def query(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("query", None),
            String
        )


class SentWebAppMessage(Types.DefaultType):

    @property
    def inline_message_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("inline_message_id", None),
            String
        )


class LabeledPrice(Types.DefaultType):

    @property
    def label(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("label", None),
            String
        )

    @property
    def amount(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("amount", None),
            Integer
        )


class Invoice(Types.DefaultType):

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def description(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def start_parameter(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("start_parameter", None),
            String
        )

    @property
    def currency(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("currency", None),
            String
        )

    @property
    def total_amount(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("total_amount", None),
            Integer
        )


class ShippingAddress(Types.DefaultType):

    @property
    def country_code(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("country_code", None),
            String
        )

    @property
    def state(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("state", None),
            String
        )

    @property
    def city(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("city", None),
            String
        )

    @property
    def street_line1(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("street_line1", None),
            String
        )

    @property
    def street_line2(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("street_line2", None),
            String
        )

    @property
    def post_code(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("post_code", None),
            String
        )


class OrderInfo(Types.DefaultType):

    @property
    def name(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("name", None),
            String
        )

    @property
    def phone_number(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("phone_number", None),
            String
        )

    @property
    def email(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("email", None),
            String
        )

    @property
    def shipping_address(
        self
    ) -> Optional["ShippingAddress"]:
        return Types.Typify(
            self._d.get("shipping_address", None),
            ShippingAddress
        )


class ShippingOption(Types.DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def prices(
        self
    ) -> "List[LabeledPrice]":
        return Types.Typify(
            self._d.get("prices", None),
            LabeledPrice
        )


class SuccessfulPayment(Types.DefaultType):

    @property
    def currency(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("currency", None),
            String
        )

    @property
    def total_amount(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("total_amount", None),
            Integer
        )

    @property
    def invoice_payload(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("invoice_payload", None),
            String
        )

    @property
    def shipping_option_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("shipping_option_id", None),
            String
        )

    @property
    def order_info(
        self
    ) -> Optional["OrderInfo"]:
        return Types.Typify(
            self._d.get("order_info", None),
            OrderInfo
        )

    @property
    def telegram_payment_charge_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("telegram_payment_charge_id", None),
            String
        )

    @property
    def provider_payment_charge_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("provider_payment_charge_id", None),
            String
        )


class ShippingQuery(Types.DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def from_(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("from", None),
            User
        )

    @property
    def invoice_payload(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("invoice_payload", None),
            String
        )

    @property
    def shipping_address(
        self
    ) -> "ShippingAddress":
        return Types.Typify(
            self._d.get("shipping_address", None),
            ShippingAddress
        )


class PreCheckoutQuery(Types.DefaultType):

    @property
    def id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("id", None),
            String
        )

    @property
    def from_(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("from", None),
            User
        )

    @property
    def currency(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("currency", None),
            String
        )

    @property
    def total_amount(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("total_amount", None),
            Integer
        )

    @property
    def invoice_payload(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("invoice_payload", None),
            String
        )

    @property
    def shipping_option_id(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("shipping_option_id", None),
            String
        )

    @property
    def order_info(
        self
    ) -> Optional["OrderInfo"]:
        return Types.Typify(
            self._d.get("order_info", None),
            OrderInfo
        )


class PassportData(Types.DefaultType):

    @property
    def data(
        self
    ) -> "List[EncryptedPassportElement]":
        return Types.Typify(
            self._d.get("data", None),
            EncryptedPassportElement
        )

    @property
    def credentials(
        self
    ) -> "EncryptedCredentials":
        return Types.Typify(
            self._d.get("credentials", None),
            EncryptedCredentials
        )


class PassportFile(Types.DefaultType):

    @property
    def file_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_id", None),
            String
        )

    @property
    def file_unique_id(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_unique_id", None),
            String
        )

    @property
    def file_size(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("file_size", None),
            Integer
        )

    @property
    def file_date(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("file_date", None),
            Integer
        )


class EncryptedPassportElement(Types.DefaultType):

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def data(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("data", None),
            String
        )

    @property
    def phone_number(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("phone_number", None),
            String
        )

    @property
    def email(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("email", None),
            String
        )

    @property
    def files(
        self
    ) -> Optional["List[PassportFile]"]:
        return Types.Typify(
            self._d.get("files", None),
            PassportFile
        )

    @property
    def front_side(
        self
    ) -> Optional["PassportFile"]:
        return Types.Typify(
            self._d.get("front_side", None),
            PassportFile
        )

    @property
    def reverse_side(
        self
    ) -> Optional["PassportFile"]:
        return Types.Typify(
            self._d.get("reverse_side", None),
            PassportFile
        )

    @property
    def selfie(
        self
    ) -> Optional["PassportFile"]:
        return Types.Typify(
            self._d.get("selfie", None),
            PassportFile
        )

    @property
    def translation(
        self
    ) -> Optional["List[PassportFile]"]:
        return Types.Typify(
            self._d.get("translation", None),
            PassportFile
        )

    @property
    def hash(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("hash", None),
            String
        )


class EncryptedCredentials(Types.DefaultType):

    @property
    def data(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("data", None),
            String
        )

    @property
    def hash(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("hash", None),
            String
        )

    @property
    def secret(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("secret", None),
            String
        )


class PassportElementError(Types.DefaultType):
    ...


class PassportElementErrorDataField(Types.DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("source", None),
            String
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def field_name(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("field_name", None),
            String
        )

    @property
    def data_hash(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("data_hash", None),
            String
        )

    @property
    def message(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("message", None),
            String
        )


class PassportElementErrorFrontSide(Types.DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("source", None),
            String
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def file_hash(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_hash", None),
            String
        )

    @property
    def message(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("message", None),
            String
        )


class PassportElementErrorReverseSide(Types.DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("source", None),
            String
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def file_hash(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_hash", None),
            String
        )

    @property
    def message(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("message", None),
            String
        )


class PassportElementErrorSelfie(Types.DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("source", None),
            String
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def file_hash(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_hash", None),
            String
        )

    @property
    def message(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("message", None),
            String
        )


class PassportElementErrorFile(Types.DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("source", None),
            String
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def file_hash(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_hash", None),
            String
        )

    @property
    def message(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("message", None),
            String
        )


class PassportElementErrorFiles(Types.DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("source", None),
            String
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def file_hashes(
        self
    ) -> "List[String]":
        return Types.Typify(
            self._d.get("file_hashes", None),
            String
        )

    @property
    def message(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("message", None),
            String
        )


class PassportElementErrorTranslationFile(Types.DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("source", None),
            String
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def file_hash(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("file_hash", None),
            String
        )

    @property
    def message(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("message", None),
            String
        )


class PassportElementErrorTranslationFiles(Types.DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("source", None),
            String
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def file_hashes(
        self
    ) -> "List[String]":
        return Types.Typify(
            self._d.get("file_hashes", None),
            String
        )

    @property
    def message(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("message", None),
            String
        )


class PassportElementErrorUnspecified(Types.DefaultType):

    @property
    def source(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("source", None),
            String
        )

    @property
    def type(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("type", None),
            String
        )

    @property
    def element_hash(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("element_hash", None),
            String
        )

    @property
    def message(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("message", None),
            String
        )


class Game(Types.DefaultType):

    @property
    def title(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("title", None),
            String
        )

    @property
    def description(
        self
    ) -> "String":
        return Types.Typify(
            self._d.get("description", None),
            String
        )

    @property
    def photo(
        self
    ) -> "List[PhotoSize]":
        return Types.Typify(
            self._d.get("photo", None),
            PhotoSize
        )

    @property
    def text(
        self
    ) -> Optional["String"]:
        return Types.Typify(
            self._d.get("text", None),
            String
        )

    @property
    def text_entities(
        self
    ) -> Optional["List[MessageEntity]"]:
        return Types.Typify(
            self._d.get("text_entities", None),
            MessageEntity
        )

    @property
    def animation(
        self
    ) -> Optional["Animation"]:
        return Types.Typify(
            self._d.get("animation", None),
            Animation
        )


class CallbackGame(Types.DefaultType):
    ...


class GameHighScore(Types.DefaultType):

    @property
    def position(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("position", None),
            Integer
        )

    @property
    def user(
        self
    ) -> "User":
        return Types.Typify(
            self._d.get("user", None),
            User
        )

    @property
    def score(
        self
    ) -> "Integer":
        return Types.Typify(
            self._d.get("score", None),
            Integer
        )


class getUpdates(Types.DefaultMethod):

    def __init__(
        self,
        offset: Optional["Integer"] = None,
        limit: Optional["Integer"] = None,
        timeout: Optional["Integer"] = None,
        allowed_updates: Optional["List[String]"] = None,
    ):
        super().__init__(
            offset,
            limit,
            timeout,
            allowed_updates
        )
        self._method = "getUpdates"
        self._res_type = "List[Update]"
        self._args = {}
        self._args['offset'] = offset
        self._args['limit'] = limit
        self._args['timeout'] = timeout
        self._args['allowed_updates'] = allowed_updates

    def result(self, update_type=Update) -> "List[Update]":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setWebhook(Types.DefaultMethod):

    def __init__(
        self,
        url: "String",
        certificate: Optional["InputFile"] = None,
        ip_address: Optional["String"] = None,
        max_connections: Optional["Integer"] = None,
        allowed_updates: Optional["List[String]"] = None,
        drop_pending_updates: Optional["Boolean"] = None,
        secret_token: Optional["String"] = None,
    ):
        super().__init__(
            url,
            certificate,
            ip_address,
            max_connections,
            allowed_updates,
            drop_pending_updates,
            secret_token
        )
        self._method = "setWebhook"
        self._res_type = "Boolean"
        self._args = {}
        self._args['url'] = url
        self._args['certificate'] = certificate
        self._args['ip_address'] = ip_address
        self._args['max_connections'] = max_connections
        self._args['allowed_updates'] = allowed_updates
        self._args['drop_pending_updates'] = drop_pending_updates
        self._args['secret_token'] = secret_token

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class deleteWebhook(Types.DefaultMethod):

    def __init__(
        self,
        drop_pending_updates: Optional["Boolean"] = None,
    ):
        super().__init__(
            drop_pending_updates
        )
        self._method = "deleteWebhook"
        self._res_type = "Boolean"
        self._args = {}
        self._args['drop_pending_updates'] = drop_pending_updates

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getWebhookInfo(Types.DefaultMethod):

    def __init__(
        self,

    ):
        super().__init__(
            INTSUPAR
        )
        self._method = "getWebhookInfo"
        self._res_type = "WebhookInfo"
        self._args = {}

    def result(self, update_type=WebhookInfo) -> "WebhookInfo":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getMe(Types.DefaultMethod):

    def __init__(
        self,

    ):
        super().__init__(
            INTSUPAR
        )
        self._method = "getMe"
        self._res_type = "User"
        self._args = {}

    def result(self, update_type=User) -> "User":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class logOut(Types.DefaultMethod):

    def __init__(
        self,

    ):
        super().__init__(
            INTSUPAR
        )
        self._method = "logOut"
        self._res_type = "Boolean"
        self._args = {}

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class close(Types.DefaultMethod):

    def __init__(
        self,

    ):
        super().__init__(
            INTSUPAR
        )
        self._method = "close"
        self._res_type = "Boolean"
        self._args = {}

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendMessage(Types.DefaultMethod):

    def __init__(
        self,
        text: "String",
        chat_id: Union["Integer", "String"],
        parse_mode: Optional["String"] = None,
        entities: Optional["List[MessageEntity]"] = None,
        disable_web_page_preview: Optional["Boolean"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            text,
            parse_mode,
            entities,
            disable_web_page_preview,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendMessage"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['text'] = text
        self._args['parse_mode'] = parse_mode
        self._args['entities'] = entities
        self._args['disable_web_page_preview'] = disable_web_page_preview
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class forwardMessage(Types.DefaultMethod):

    def __init__(
        self,
        message_id: "Integer",
        from__chat_id: Union["Integer", "String"],
        chat_id: Union["Integer", "String"],
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
    ):
        super().__init__(
            chat_id,
            from__chat_id,
            disable_notification,
            protect_content,
            message_id
        )
        self._method = "forwardMessage"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['from_chat_id'] = from__chat_id
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['message_id'] = message_id

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class copyMessage(Types.DefaultMethod):

    def __init__(
        self,
        message_id: "Integer",
        from__chat_id: Union["Integer", "String"],
        chat_id: Union["Integer", "String"],
        caption: Optional["String"] = None,
        parse_mode: Optional["String"] = None,
        caption_entities: Optional["List[MessageEntity]"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            from__chat_id,
            message_id,
            caption,
            parse_mode,
            caption_entities,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "copyMessage"
        self._res_type = "MessageId"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['from_chat_id'] = from__chat_id
        self._args['message_id'] = message_id
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=MessageId) -> "MessageId":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendPhoto(Types.DefaultMethod):

    def __init__(
        self,
        photo: Union["InputFile", "String"],
        chat_id: Union["Integer", "String"],
        caption: Optional["String"] = None,
        parse_mode: Optional["String"] = None,
        caption_entities: Optional["List[MessageEntity]"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            photo,
            caption,
            parse_mode,
            caption_entities,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendPhoto"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['photo'] = photo
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendAudio(Types.DefaultMethod):

    def __init__(
        self,
        audio: Union["InputFile", "String"],
        chat_id: Union["Integer", "String"],
        caption: Optional["String"] = None,
        parse_mode: Optional["String"] = None,
        caption_entities: Optional["List[MessageEntity]"] = None,
        duration: Optional["Integer"] = None,
        performer: Optional["String"] = None,
        title: Optional["String"] = None,
        thumb: Optional[Union["InputFile", "String"]] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            audio,
            caption,
            parse_mode,
            caption_entities,
            duration,
            performer,
            title,
            thumb,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendAudio"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['audio'] = audio
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['duration'] = duration
        self._args['performer'] = performer
        self._args['title'] = title
        self._args['thumb'] = thumb
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendDocument(Types.DefaultMethod):

    def __init__(
        self,
        document: Union["InputFile", "String"],
        chat_id: Union["Integer", "String"],
        thumb: Optional[Union["InputFile", "String"]] = None,
        caption: Optional["String"] = None,
        parse_mode: Optional["String"] = None,
        caption_entities: Optional["List[MessageEntity]"] = None,
        disable_content_type_detection: Optional["Boolean"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            document,
            thumb,
            caption,
            parse_mode,
            caption_entities,
            disable_content_type_detection,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendDocument"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['document'] = document
        self._args['thumb'] = thumb
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['disable_content_type_detection'] = disable_content_type_detection
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendVideo(Types.DefaultMethod):

    def __init__(
        self,
        video: Union["InputFile", "String"],
        chat_id: Union["Integer", "String"],
        duration: Optional["Integer"] = None,
        width: Optional["Integer"] = None,
        height: Optional["Integer"] = None,
        thumb: Optional[Union["InputFile", "String"]] = None,
        caption: Optional["String"] = None,
        parse_mode: Optional["String"] = None,
        caption_entities: Optional["List[MessageEntity]"] = None,
        supports_streaming: Optional["Boolean"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            video,
            duration,
            width,
            height,
            thumb,
            caption,
            parse_mode,
            caption_entities,
            supports_streaming,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendVideo"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['video'] = video
        self._args['duration'] = duration
        self._args['width'] = width
        self._args['height'] = height
        self._args['thumb'] = thumb
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['supports_streaming'] = supports_streaming
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendAnimation(Types.DefaultMethod):

    def __init__(
        self,
        animation: Union["InputFile", "String"],
        chat_id: Union["Integer", "String"],
        duration: Optional["Integer"] = None,
        width: Optional["Integer"] = None,
        height: Optional["Integer"] = None,
        thumb: Optional[Union["InputFile", "String"]] = None,
        caption: Optional["String"] = None,
        parse_mode: Optional["String"] = None,
        caption_entities: Optional["List[MessageEntity]"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            animation,
            duration,
            width,
            height,
            thumb,
            caption,
            parse_mode,
            caption_entities,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendAnimation"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['animation'] = animation
        self._args['duration'] = duration
        self._args['width'] = width
        self._args['height'] = height
        self._args['thumb'] = thumb
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendVoice(Types.DefaultMethod):

    def __init__(
        self,
        voice: Union["InputFile", "String"],
        chat_id: Union["Integer", "String"],
        caption: Optional["String"] = None,
        parse_mode: Optional["String"] = None,
        caption_entities: Optional["List[MessageEntity]"] = None,
        duration: Optional["Integer"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            voice,
            caption,
            parse_mode,
            caption_entities,
            duration,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendVoice"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['voice'] = voice
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['duration'] = duration
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendVideoNote(Types.DefaultMethod):

    def __init__(
        self,
        video_note: Union["InputFile", "String"],
        chat_id: Union["Integer", "String"],
        duration: Optional["Integer"] = None,
        length: Optional["Integer"] = None,
        thumb: Optional[Union["InputFile", "String"]] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            video_note,
            duration,
            length,
            thumb,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendVideoNote"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['video_note'] = video_note
        self._args['duration'] = duration
        self._args['length'] = length
        self._args['thumb'] = thumb
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendMediaGroup(Types.DefaultMethod):

    def __init__(
        self,
        media: Union["List[InputMediaAudio]", "List[InputMediaDocument]", "List[InputMediaPhoto]", "List[InputMediaVideo]"],
        chat_id: Union["Integer", "String"],
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
    ):
        super().__init__(
            chat_id,
            media,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply
        )
        self._method = "sendMediaGroup"
        self._res_type = "List[Message]"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['media'] = media
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply

    def result(self, update_type=Message) -> "List[Message]":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendLocation(Types.DefaultMethod):

    def __init__(
        self,
        longitude: "Float",
        latitude: "Float",
        chat_id: Union["Integer", "String"],
        horizontal_accuracy: Optional["Float"] = None,
        live_period: Optional["Integer"] = None,
        heading: Optional["Integer"] = None,
        proximity_alert_radius: Optional["Integer"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            latitude,
            longitude,
            horizontal_accuracy,
            live_period,
            heading,
            proximity_alert_radius,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendLocation"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['latitude'] = latitude
        self._args['longitude'] = longitude
        self._args['horizontal_accuracy'] = horizontal_accuracy
        self._args['live_period'] = live_period
        self._args['heading'] = heading
        self._args['proximity_alert_radius'] = proximity_alert_radius
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class editMessageLiveLocation(Types.DefaultMethod):

    def __init__(
        self,
        longitude: "Float",
        latitude: "Float",
        chat_id: Optional[Union["Integer", "String"]] = None,
        message_id: Optional["Integer"] = None,
        inline_message_id: Optional["String"] = None,
        horizontal_accuracy: Optional["Float"] = None,
        heading: Optional["Integer"] = None,
        proximity_alert_radius: Optional["Integer"] = None,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
    ):
        super().__init__(
            chat_id,
            message_id,
            inline_message_id,
            latitude,
            longitude,
            horizontal_accuracy,
            heading,
            proximity_alert_radius,
            reply_markup
        )
        self._method = "editMessageLiveLocation"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['latitude'] = latitude
        self._args['longitude'] = longitude
        self._args['horizontal_accuracy'] = horizontal_accuracy
        self._args['heading'] = heading
        self._args['proximity_alert_radius'] = proximity_alert_radius
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class stopMessageLiveLocation(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Optional[Union["Integer", "String"]] = None,
        message_id: Optional["Integer"] = None,
        inline_message_id: Optional["String"] = None,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
    ):
        super().__init__(
            chat_id,
            message_id,
            inline_message_id,
            reply_markup
        )
        self._method = "stopMessageLiveLocation"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendVenue(Types.DefaultMethod):

    def __init__(
        self,
        address: "String",
        title: "String",
        longitude: "Float",
        latitude: "Float",
        chat_id: Union["Integer", "String"],
        foursquare_id: Optional["String"] = None,
        foursquare_type: Optional["String"] = None,
        google_place_id: Optional["String"] = None,
        google_place_type: Optional["String"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            latitude,
            longitude,
            title,
            address,
            foursquare_id,
            foursquare_type,
            google_place_id,
            google_place_type,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendVenue"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['latitude'] = latitude
        self._args['longitude'] = longitude
        self._args['title'] = title
        self._args['address'] = address
        self._args['foursquare_id'] = foursquare_id
        self._args['foursquare_type'] = foursquare_type
        self._args['google_place_id'] = google_place_id
        self._args['google_place_type'] = google_place_type
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendContact(Types.DefaultMethod):

    def __init__(
        self,
        first_name: "String",
        phone_number: "String",
        chat_id: Union["Integer", "String"],
        last_name: Optional["String"] = None,
        vcard: Optional["String"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            phone_number,
            first_name,
            last_name,
            vcard,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendContact"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['phone_number'] = phone_number
        self._args['first_name'] = first_name
        self._args['last_name'] = last_name
        self._args['vcard'] = vcard
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendPoll(Types.DefaultMethod):

    def __init__(
        self,
        options: "List[String]",
        question: "String",
        chat_id: Union["Integer", "String"],
        is_anonymous: Optional["Boolean"] = None,
        type: Optional["String"] = None,
        allows_multiple_answers: Optional["Boolean"] = None,
        correct_option_id: Optional["Integer"] = None,
        explanation: Optional["String"] = None,
        explanation_parse_mode: Optional["String"] = None,
        explanation_entities: Optional["List[MessageEntity]"] = None,
        open_period: Optional["Integer"] = None,
        close_date: Optional["Integer"] = None,
        is_closed: Optional["Boolean"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            question,
            options,
            is_anonymous,
            type,
            allows_multiple_answers,
            correct_option_id,
            explanation,
            explanation_parse_mode,
            explanation_entities,
            open_period,
            close_date,
            is_closed,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendPoll"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['question'] = question
        self._args['options'] = options
        self._args['is_anonymous'] = is_anonymous
        self._args['type'] = type
        self._args['allows_multiple_answers'] = allows_multiple_answers
        self._args['correct_option_id'] = correct_option_id
        self._args['explanation'] = explanation
        self._args['explanation_parse_mode'] = explanation_parse_mode
        self._args['explanation_entities'] = explanation_entities
        self._args['open_period'] = open_period
        self._args['close_date'] = close_date
        self._args['is_closed'] = is_closed
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendDice(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
        emoji: Optional["String"] = None,
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            emoji,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendDice"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['emoji'] = emoji
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendChatAction(Types.DefaultMethod):

    def __init__(
        self,
        action: "String",
                chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            action
        )
        self._method = "sendChatAction"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['action'] = action

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getUserProfilePhotos(Types.DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        offset: Optional["Integer"] = None,
        limit: Optional["Integer"] = None,
    ):
        super().__init__(
            user_id,
            offset,
            limit
        )
        self._method = "getUserProfilePhotos"
        self._res_type = "UserProfilePhotos"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['offset'] = offset
        self._args['limit'] = limit

    def result(self, update_type=UserProfilePhotos) -> "UserProfilePhotos":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getFile(Types.DefaultMethod):

    def __init__(
        self,
        file_id: "String",
    ):
        super().__init__(
            file_id
        )
        self._method = "getFile"
        self._res_type = "File"
        self._args = {}
        self._args['file_id'] = file_id

    def result(self, update_type=File) -> "File":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class banChatMember(Types.DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: Union["Integer", "String"],
        until_date: Optional["Integer"] = None,
        revoke_messages: Optional["Boolean"] = None,
    ):
        super().__init__(
            chat_id,
            user_id,
            until_date,
            revoke_messages
        )
        self._method = "banChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['until_date'] = until_date
        self._args['revoke_messages'] = revoke_messages

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class unbanChatMember(Types.DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: Union["Integer", "String"],
        only_if_banned: Optional["Boolean"] = None,
    ):
        super().__init__(
            chat_id,
            user_id,
            only_if_banned
        )
        self._method = "unbanChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['only_if_banned'] = only_if_banned

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class restrictChatMember(Types.DefaultMethod):

    def __init__(
        self,
        permissions: "ChatPermissions",
        user_id: "Integer",
        chat_id: Union["Integer", "String"],
        until_date: Optional["Integer"] = None,
    ):
        super().__init__(
            chat_id,
            user_id,
            permissions,
            until_date
        )
        self._method = "restrictChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['permissions'] = permissions
        self._args['until_date'] = until_date

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class promoteChatMember(Types.DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: Union["Integer", "String"],
        is_anonymous: Optional["Boolean"] = None,
        can_manage_chat: Optional["Boolean"] = None,
        can_post_messages: Optional["Boolean"] = None,
        can_edit_messages: Optional["Boolean"] = None,
        can_delete_messages: Optional["Boolean"] = None,
        can_manage_video_chats: Optional["Boolean"] = None,
        can_restrict_members: Optional["Boolean"] = None,
        can_promote_members: Optional["Boolean"] = None,
        can_change_info: Optional["Boolean"] = None,
        can_invite_users: Optional["Boolean"] = None,
        can_pin_messages: Optional["Boolean"] = None,
    ):
        super().__init__(
            chat_id,
            user_id,
            is_anonymous,
            can_manage_chat,
            can_post_messages,
            can_edit_messages,
            can_delete_messages,
            can_manage_video_chats,
            can_restrict_members,
            can_promote_members,
            can_change_info,
            can_invite_users,
            can_pin_messages
        )
        self._method = "promoteChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['is_anonymous'] = is_anonymous
        self._args['can_manage_chat'] = can_manage_chat
        self._args['can_post_messages'] = can_post_messages
        self._args['can_edit_messages'] = can_edit_messages
        self._args['can_delete_messages'] = can_delete_messages
        self._args['can_manage_video_chats'] = can_manage_video_chats
        self._args['can_restrict_members'] = can_restrict_members
        self._args['can_promote_members'] = can_promote_members
        self._args['can_change_info'] = can_change_info
        self._args['can_invite_users'] = can_invite_users
        self._args['can_pin_messages'] = can_pin_messages

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setChatAdministratorCustomTitle(Types.DefaultMethod):

    def __init__(
        self,
        custom_title: "String",
        user_id: "Integer",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            user_id,
            custom_title
        )
        self._method = "setChatAdministratorCustomTitle"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['custom_title'] = custom_title

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class banChatSenderChat(Types.DefaultMethod):

    def __init__(
        self,
        sender_chat_id: "Integer",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            sender_chat_id
        )
        self._method = "banChatSenderChat"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sender_chat_id'] = sender_chat_id

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class unbanChatSenderChat(Types.DefaultMethod):

    def __init__(
        self,
        sender_chat_id: "Integer",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            sender_chat_id
        )
        self._method = "unbanChatSenderChat"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sender_chat_id'] = sender_chat_id

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setChatPermissions(Types.DefaultMethod):

    def __init__(
        self,
        permissions: "ChatPermissions",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            permissions
        )
        self._method = "setChatPermissions"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['permissions'] = permissions

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class exportChatInviteLink(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id
        )
        self._method = "exportChatInviteLink"
        self._res_type = "String"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self, update_type=String) -> "String":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class createChatInviteLink(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
        name: Optional["String"] = None,
        expire_date: Optional["Integer"] = None,
        member_limit: Optional["Integer"] = None,
        creates_join_request: Optional["Boolean"] = None,
    ):
        super().__init__(
            chat_id,
            name,
            expire_date,
            member_limit,
            creates_join_request
        )
        self._method = "createChatInviteLink"
        self._res_type = "ChatInviteLink"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['name'] = name
        self._args['expire_date'] = expire_date
        self._args['member_limit'] = member_limit
        self._args['creates_join_request'] = creates_join_request

    def result(self, update_type=ChatInviteLink) -> "ChatInviteLink":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class editChatInviteLink(Types.DefaultMethod):

    def __init__(
        self,
        invite_link: "String",
        chat_id: Union["Integer", "String"],
        name: Optional["String"] = None,
        expire_date: Optional["Integer"] = None,
        member_limit: Optional["Integer"] = None,
        creates_join_request: Optional["Boolean"] = None,
    ):
        super().__init__(
            chat_id,
            invite_link,
            name,
            expire_date,
            member_limit,
            creates_join_request
        )
        self._method = "editChatInviteLink"
        self._res_type = "ChatInviteLink"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['invite_link'] = invite_link
        self._args['name'] = name
        self._args['expire_date'] = expire_date
        self._args['member_limit'] = member_limit
        self._args['creates_join_request'] = creates_join_request

    def result(self, update_type=ChatInviteLink) -> "ChatInviteLink":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class revokeChatInviteLink(Types.DefaultMethod):

    def __init__(
        self,
        invite_link: "String",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            invite_link
        )
        self._method = "revokeChatInviteLink"
        self._res_type = "ChatInviteLink"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['invite_link'] = invite_link

    def result(self, update_type=ChatInviteLink) -> "ChatInviteLink":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class approveChatJoinRequest(Types.DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            user_id
        )
        self._method = "approveChatJoinRequest"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class declineChatJoinRequest(Types.DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            user_id
        )
        self._method = "declineChatJoinRequest"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setChatPhoto(Types.DefaultMethod):

    def __init__(
        self,
        photo: "InputFile",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            photo
        )
        self._method = "setChatPhoto"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['photo'] = photo

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class deleteChatPhoto(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id
        )
        self._method = "deleteChatPhoto"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setChatTitle(Types.DefaultMethod):

    def __init__(
        self,
        title: "String",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            title
        )
        self._method = "setChatTitle"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['title'] = title

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setChatDescription(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
        description: Optional["String"] = None,
    ):
        super().__init__(
            chat_id,
            description
        )
        self._method = "setChatDescription"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['description'] = description

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class pinChatMessage(Types.DefaultMethod):

    def __init__(
        self,
        message_id: "Integer",
        chat_id: Union["Integer", "String"],
        disable_notification: Optional["Boolean"] = None,
    ):
        super().__init__(
            chat_id,
            message_id,
            disable_notification
        )
        self._method = "pinChatMessage"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['disable_notification'] = disable_notification

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class unpinChatMessage(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
        message_id: Optional["Integer"] = None,
    ):
        super().__init__(
            chat_id,
            message_id
        )
        self._method = "unpinChatMessage"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class unpinAllChatMessages(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id
        )
        self._method = "unpinAllChatMessages"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class leaveChat(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id
        )
        self._method = "leaveChat"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getChat(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id
        )
        self._method = "getChat"
        self._res_type = "Chat"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self, update_type=Chat) -> "Chat":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getChatAdministrators(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id
        )
        self._method = "getChatAdministrators"
        self._res_type = "List[ChatMember]"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self, update_type=ChatMember) -> "List[ChatMember]":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getChatMemberCount(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id
        )
        self._method = "getChatMemberCount"
        self._res_type = "Integer"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self, update_type=Integer) -> "Integer":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getChatMember(Types.DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            user_id
        )
        self._method = "getChatMember"
        self._res_type = "ChatMember"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id

    def result(self, update_type=ChatMember) -> "ChatMember":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setChatStickerSet(Types.DefaultMethod):

    def __init__(
        self,
        sticker_set_name: "String",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            sticker_set_name
        )
        self._method = "setChatStickerSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sticker_set_name'] = sticker_set_name

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class deleteChatStickerSet(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id
        )
        self._method = "deleteChatStickerSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class answerCallbackQuery(Types.DefaultMethod):

    def __init__(
        self,
        callback_query_id: "String",
        text: Optional["String"] = None,
        show_alert: Optional["Boolean"] = None,
        url: Optional["String"] = None,
        cache_time: Optional["Integer"] = None,
    ):
        super().__init__(
            callback_query_id,
            text,
            show_alert,
            url,
            cache_time
        )
        self._method = "answerCallbackQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['callback_query_id'] = callback_query_id
        self._args['text'] = text
        self._args['show_alert'] = show_alert
        self._args['url'] = url
        self._args['cache_time'] = cache_time

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setMyCommands(Types.DefaultMethod):

    def __init__(
        self,
        commands: "List[BotCommand]",
        scope: Optional["BotCommandScope"] = None,
        language_code: Optional["String"] = None,
    ):
        super().__init__(
            commands,
            scope,
            language_code
        )
        self._method = "setMyCommands"
        self._res_type = "Boolean"
        self._args = {}
        self._args['commands'] = commands
        self._args['scope'] = scope
        self._args['language_code'] = language_code

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class deleteMyCommands(Types.DefaultMethod):

    def __init__(
        self,
        scope: Optional["BotCommandScope"] = None,
        language_code: Optional["String"] = None,
    ):
        super().__init__(
            scope,
            language_code
        )
        self._method = "deleteMyCommands"
        self._res_type = "Boolean"
        self._args = {}
        self._args['scope'] = scope
        self._args['language_code'] = language_code

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getMyCommands(Types.DefaultMethod):

    def __init__(
        self,
        scope: Optional["BotCommandScope"] = None,
        language_code: Optional["String"] = None,
    ):
        super().__init__(
            scope,
            language_code
        )
        self._method = "getMyCommands"
        self._res_type = "List[BotCommand]"
        self._args = {}
        self._args['scope'] = scope
        self._args['language_code'] = language_code

    def result(self, update_type=BotCommand) -> "List[BotCommand]":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setChatMenuButton(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Optional["Integer"] = None,
        menu_button: Optional["MenuButton"] = None,
    ):
        super().__init__(
            chat_id,
            menu_button
        )
        self._method = "setChatMenuButton"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['menu_button'] = menu_button

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getChatMenuButton(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Optional["Integer"] = None,
    ):
        super().__init__(
            chat_id
        )
        self._method = "getChatMenuButton"
        self._res_type = "MenuButton"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self, update_type=MenuButton) -> "MenuButton":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setMyDefaultAdministratorRights(Types.DefaultMethod):

    def __init__(
        self,
        rights: Optional["ChatAdministratorRights"] = None,
        for_channels: Optional["Boolean"] = None,
    ):
        super().__init__(
            rights,
            for_channels
        )
        self._method = "setMyDefaultAdministratorRights"
        self._res_type = "Boolean"
        self._args = {}
        self._args['rights'] = rights
        self._args['for_channels'] = for_channels

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getMyDefaultAdministratorRights(Types.DefaultMethod):

    def __init__(
        self,
        for_channels: Optional["Boolean"] = None,
    ):
        super().__init__(
            for_channels
        )
        self._method = "getMyDefaultAdministratorRights"
        self._res_type = "ChatAdministratorRights"
        self._args = {}
        self._args['for_channels'] = for_channels

    def result(self, update_type=ChatAdministratorRights) -> "ChatAdministratorRights":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class editMessageText(Types.DefaultMethod):

    def __init__(
        self,
        text: "String",
        chat_id: Optional[Union["Integer", "String"]] = None,
        message_id: Optional["Integer"] = None,
        inline_message_id: Optional["String"] = None,
        parse_mode: Optional["String"] = None,
        entities: Optional["List[MessageEntity]"] = None,
        disable_web_page_preview: Optional["Boolean"] = None,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
    ):
        super().__init__(
            chat_id,
            message_id,
            inline_message_id,
            text,
            parse_mode,
            entities,
            disable_web_page_preview,
            reply_markup
        )
        self._method = "editMessageText"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['text'] = text
        self._args['parse_mode'] = parse_mode
        self._args['entities'] = entities
        self._args['disable_web_page_preview'] = disable_web_page_preview
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class editMessageCaption(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Optional[Union["Integer", "String"]] = None,
        message_id: Optional["Integer"] = None,
        inline_message_id: Optional["String"] = None,
        caption: Optional["String"] = None,
        parse_mode: Optional["String"] = None,
        caption_entities: Optional["List[MessageEntity]"] = None,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
    ):
        super().__init__(
            chat_id,
            message_id,
            inline_message_id,
            caption,
            parse_mode,
            caption_entities,
            reply_markup
        )
        self._method = "editMessageCaption"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['caption'] = caption
        self._args['parse_mode'] = parse_mode
        self._args['caption_entities'] = caption_entities
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class editMessageMedia(Types.DefaultMethod):

    def __init__(
        self,
        media: "InputMedia",
        chat_id: Optional[Union["Integer", "String"]] = None,
        message_id: Optional["Integer"] = None,
        inline_message_id: Optional["String"] = None,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
    ):
        super().__init__(
            chat_id,
            message_id,
            inline_message_id,
            media,
            reply_markup
        )
        self._method = "editMessageMedia"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['media'] = media
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class editMessageReplyMarkup(Types.DefaultMethod):

    def __init__(
        self,
        chat_id: Optional[Union["Integer", "String"]] = None,
        message_id: Optional["Integer"] = None,
        inline_message_id: Optional["String"] = None,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
    ):
        super().__init__(
            chat_id,
            message_id,
            inline_message_id,
            reply_markup
        )
        self._method = "editMessageReplyMarkup"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class stopPoll(Types.DefaultMethod):

    def __init__(
        self,
        message_id: "Integer",
        chat_id: Union["Integer", "String"],
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
    ):
        super().__init__(
            chat_id,
            message_id,
            reply_markup
        )
        self._method = "stopPoll"
        self._res_type = "Poll"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Poll) -> "Poll":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class deleteMessage(Types.DefaultMethod):

    def __init__(
        self,
        message_id: "Integer",
        chat_id: Union["Integer", "String"],
    ):
        super().__init__(
            chat_id,
            message_id
        )
        self._method = "deleteMessage"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendSticker(Types.DefaultMethod):

    def __init__(
        self,
        sticker: Union["InputFile", "String"],
        chat_id: Union["Integer", "String"],
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional[Union["InlineKeyboardMarkup",
                                     "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]] = None,
    ):
        super().__init__(
            chat_id,
            sticker,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendSticker"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sticker'] = sticker
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getStickerSet(Types.DefaultMethod):

    def __init__(
        self,
        name: "String",
    ):
        super().__init__(
            name
        )
        self._method = "getStickerSet"
        self._res_type = "StickerSet"
        self._args = {}
        self._args['name'] = name

    def result(self, update_type=StickerSet) -> "StickerSet":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class uploadStickerFile(Types.DefaultMethod):

    def __init__(
        self,
        png_sticker: "InputFile",
        user_id: "Integer",
    ):
        super().__init__(
            user_id,
            png_sticker
        )
        self._method = "uploadStickerFile"
        self._res_type = "File"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['png_sticker'] = png_sticker

    def result(self, update_type=File) -> "File":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class createNewStickerSet(Types.DefaultMethod):

    def __init__(
        self,
        emojis: "String",
                title: "String",
                name: "String",
                user_id: "Integer",
                png_sticker: Optional[Union["InputFile", "String"]] = None,
                tgs_sticker: Optional["InputFile"] = None,
                webm_sticker: Optional["InputFile"] = None,
                contains_masks: Optional["Boolean"] = None,
                mask_position: Optional["MaskPosition"] = None,
    ):
        super().__init__(
            user_id,
            name,
            title,
            png_sticker,
            tgs_sticker,
            webm_sticker,
            emojis,
            contains_masks,
            mask_position
        )
        self._method = "createNewStickerSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['name'] = name
        self._args['title'] = title
        self._args['png_sticker'] = png_sticker
        self._args['tgs_sticker'] = tgs_sticker
        self._args['webm_sticker'] = webm_sticker
        self._args['emojis'] = emojis
        self._args['contains_masks'] = contains_masks
        self._args['mask_position'] = mask_position

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class addStickerToSet(Types.DefaultMethod):

    def __init__(
        self,
        emojis: "String",
                name: "String",
                user_id: "Integer",
                png_sticker: Optional[Union["InputFile", "String"]] = None,
                tgs_sticker: Optional["InputFile"] = None,
                webm_sticker: Optional["InputFile"] = None,
                mask_position: Optional["MaskPosition"] = None,
    ):
        super().__init__(
            user_id,
            name,
            png_sticker,
            tgs_sticker,
            webm_sticker,
            emojis,
            mask_position
        )
        self._method = "addStickerToSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['name'] = name
        self._args['png_sticker'] = png_sticker
        self._args['tgs_sticker'] = tgs_sticker
        self._args['webm_sticker'] = webm_sticker
        self._args['emojis'] = emojis
        self._args['mask_position'] = mask_position

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setStickerPositionInSet(Types.DefaultMethod):

    def __init__(
        self,
        position: "Integer",
        sticker: "String",
    ):
        super().__init__(
            sticker,
            position
        )
        self._method = "setStickerPositionInSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['sticker'] = sticker
        self._args['position'] = position

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class deleteStickerFromSet(Types.DefaultMethod):

    def __init__(
        self,
        sticker: "String",
    ):
        super().__init__(
            sticker
        )
        self._method = "deleteStickerFromSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['sticker'] = sticker

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setStickerSetThumb(Types.DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        name: "String",
        thumb: Optional[Union["InputFile", "String"]] = None,
    ):
        super().__init__(
            name,
            user_id,
            thumb
        )
        self._method = "setStickerSetThumb"
        self._res_type = "Boolean"
        self._args = {}
        self._args['name'] = name
        self._args['user_id'] = user_id
        self._args['thumb'] = thumb

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class answerInlineQuery(Types.DefaultMethod):

    def __init__(
        self,
        results: "List[InlineQueryResult]",
        inline_query_id: "String",
        cache_time: Optional["Integer"] = None,
        is_personal: Optional["Boolean"] = None,
        next_offset: Optional["String"] = None,
        switch_pm_text: Optional["String"] = None,
        switch_pm_parameter: Optional["String"] = None,
    ):
        super().__init__(
            inline_query_id,
            results,
            cache_time,
            is_personal,
            next_offset,
            switch_pm_text,
            switch_pm_parameter
        )
        self._method = "answerInlineQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['inline_query_id'] = inline_query_id
        self._args['results'] = results
        self._args['cache_time'] = cache_time
        self._args['is_personal'] = is_personal
        self._args['next_offset'] = next_offset
        self._args['switch_pm_text'] = switch_pm_text
        self._args['switch_pm_parameter'] = switch_pm_parameter

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class answerWebAppQuery(Types.DefaultMethod):

    def __init__(
        self,
        result: "InlineQueryResult",
                web_app_query_id: "String",
    ):
        super().__init__(
            web_app_query_id,
            result
        )
        self._method = "answerWebAppQuery"
        self._res_type = "SentWebAppMessage"
        self._args = {}
        self._args['web_app_query_id'] = web_app_query_id
        self._args['result'] = result

    def result(self, update_type=SentWebAppMessage) -> "SentWebAppMessage":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendInvoice(Types.DefaultMethod):

    def __init__(
        self,
        prices: "List[LabeledPrice]",
                currency: "String",
                provider_token: "String",
                payload: "String",
                description: "String",
                title: "String",
                chat_id: Union["Integer", "String"],
                max_tip_amount: Optional["Integer"] = None,
                suggested_tip_amounts: Optional["List[Integer]"] = None,
                start_parameter: Optional["String"] = None,
                provider_data: Optional["String"] = None,
                photo_url: Optional["String"] = None,
                photo_size: Optional["Integer"] = None,
                photo_width: Optional["Integer"] = None,
                photo_height: Optional["Integer"] = None,
                need_name: Optional["Boolean"] = None,
                need_phone_number: Optional["Boolean"] = None,
                need_email: Optional["Boolean"] = None,
                need_shipping_address: Optional["Boolean"] = None,
                send_phone_number_to_provider: Optional["Boolean"] = None,
                send_email_to_provider: Optional["Boolean"] = None,
                is_flexible: Optional["Boolean"] = None,
                disable_notification: Optional["Boolean"] = None,
                protect_content: Optional["Boolean"] = None,
                reply_to_message_id: Optional["Integer"] = None,
                allow_sending_without_reply: Optional["Boolean"] = None,
                reply_markup: Optional["InlineKeyboardMarkup"] = None,
    ):
        super().__init__(
            chat_id,
            title,
            description,
            payload,
            provider_token,
            currency,
            prices,
            max_tip_amount,
            suggested_tip_amounts,
            start_parameter,
            provider_data,
            photo_url,
            photo_size,
            photo_width,
            photo_height,
            need_name,
            need_phone_number,
            need_email,
            need_shipping_address,
            send_phone_number_to_provider,
            send_email_to_provider,
            is_flexible,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendInvoice"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['title'] = title
        self._args['description'] = description
        self._args['payload'] = payload
        self._args['provider_token'] = provider_token
        self._args['currency'] = currency
        self._args['prices'] = prices
        self._args['max_tip_amount'] = max_tip_amount
        self._args['suggested_tip_amounts'] = suggested_tip_amounts
        self._args['start_parameter'] = start_parameter
        self._args['provider_data'] = provider_data
        self._args['photo_url'] = photo_url
        self._args['photo_size'] = photo_size
        self._args['photo_width'] = photo_width
        self._args['photo_height'] = photo_height
        self._args['need_name'] = need_name
        self._args['need_phone_number'] = need_phone_number
        self._args['need_email'] = need_email
        self._args['need_shipping_address'] = need_shipping_address
        self._args['send_phone_number_to_provider'] = send_phone_number_to_provider
        self._args['send_email_to_provider'] = send_email_to_provider
        self._args['is_flexible'] = is_flexible
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class createInvoiceLink(Types.DefaultMethod):

    def __init__(
        self,
        prices: "List[LabeledPrice]",
                currency: "String",
                provider_token: "String",
                payload: "String",
                description: "String",
                title: "String",
                max_tip_amount: Optional["Integer"] = None,
                suggested_tip_amounts: Optional["List[Integer]"] = None,
                provider_data: Optional["String"] = None,
                photo_url: Optional["String"] = None,
                photo_size: Optional["Integer"] = None,
                photo_width: Optional["Integer"] = None,
                photo_height: Optional["Integer"] = None,
                need_name: Optional["Boolean"] = None,
                need_phone_number: Optional["Boolean"] = None,
                need_email: Optional["Boolean"] = None,
                need_shipping_address: Optional["Boolean"] = None,
                send_phone_number_to_provider: Optional["Boolean"] = None,
                send_email_to_provider: Optional["Boolean"] = None,
                is_flexible: Optional["Boolean"] = None,
    ):
        super().__init__(
            title,
            description,
            payload,
            provider_token,
            currency,
            prices,
            max_tip_amount,
            suggested_tip_amounts,
            provider_data,
            photo_url,
            photo_size,
            photo_width,
            photo_height,
            need_name,
            need_phone_number,
            need_email,
            need_shipping_address,
            send_phone_number_to_provider,
            send_email_to_provider,
            is_flexible
        )
        self._method = "createInvoiceLink"
        self._res_type = "String"
        self._args = {}
        self._args['title'] = title
        self._args['description'] = description
        self._args['payload'] = payload
        self._args['provider_token'] = provider_token
        self._args['currency'] = currency
        self._args['prices'] = prices
        self._args['max_tip_amount'] = max_tip_amount
        self._args['suggested_tip_amounts'] = suggested_tip_amounts
        self._args['provider_data'] = provider_data
        self._args['photo_url'] = photo_url
        self._args['photo_size'] = photo_size
        self._args['photo_width'] = photo_width
        self._args['photo_height'] = photo_height
        self._args['need_name'] = need_name
        self._args['need_phone_number'] = need_phone_number
        self._args['need_email'] = need_email
        self._args['need_shipping_address'] = need_shipping_address
        self._args['send_phone_number_to_provider'] = send_phone_number_to_provider
        self._args['send_email_to_provider'] = send_email_to_provider
        self._args['is_flexible'] = is_flexible

    def result(self, update_type=String) -> "String":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class answerShippingQuery(Types.DefaultMethod):

    def __init__(
        self,
        ok: "Boolean",
        shipping_query_id: "String",
        shipping_options: Optional["List[ShippingOption]"] = None,
        error_message: Optional["String"] = None,
    ):
        super().__init__(
            shipping_query_id,
            ok,
            shipping_options,
            error_message
        )
        self._method = "answerShippingQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['shipping_query_id'] = shipping_query_id
        self._args['ok'] = ok
        self._args['shipping_options'] = shipping_options
        self._args['error_message'] = error_message

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class answerPreCheckoutQuery(Types.DefaultMethod):

    def __init__(
        self,
        ok: "Boolean",
        pre_checkout_query_id: "String",
        error_message: Optional["String"] = None,
    ):
        super().__init__(
            pre_checkout_query_id,
            ok,
            error_message
        )
        self._method = "answerPreCheckoutQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['pre_checkout_query_id'] = pre_checkout_query_id
        self._args['ok'] = ok
        self._args['error_message'] = error_message

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setPassportDataErrors(Types.DefaultMethod):

    def __init__(
        self,
        errors: "List[PassportElementError]",
                user_id: "Integer",
    ):
        super().__init__(
            user_id,
            errors
        )
        self._method = "setPassportDataErrors"
        self._res_type = "Boolean"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['errors'] = errors

    def result(self, update_type=Boolean) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class sendGame(Types.DefaultMethod):

    def __init__(
        self,
        game_short_name: "String",
        chat_id: "Integer",
        disable_notification: Optional["Boolean"] = None,
        protect_content: Optional["Boolean"] = None,
        reply_to_message_id: Optional["Integer"] = None,
        allow_sending_without_reply: Optional["Boolean"] = None,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
    ):
        super().__init__(
            chat_id,
            game_short_name,
            disable_notification,
            protect_content,
            reply_to_message_id,
            allow_sending_without_reply,
            reply_markup
        )
        self._method = "sendGame"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['game_short_name'] = game_short_name
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply
        self._args['reply_markup'] = reply_markup

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class setGameScore(Types.DefaultMethod):

    def __init__(
        self,
        score: "Integer",
        user_id: "Integer",
        force: Optional["Boolean"] = None,
        disable_edit_message: Optional["Boolean"] = None,
        chat_id: Optional["Integer"] = None,
        message_id: Optional["Integer"] = None,
        inline_message_id: Optional["String"] = None,
    ):
        super().__init__(
            user_id,
            score,
            force,
            disable_edit_message,
            chat_id,
            message_id,
            inline_message_id
        )
        self._method = "setGameScore"
        self._res_type = "Message"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['score'] = score
        self._args['force'] = force
        self._args['disable_edit_message'] = disable_edit_message
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id

    def result(self, update_type=Message) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)


class getGameHighScores(Types.DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: Optional["Integer"] = None,
        message_id: Optional["Integer"] = None,
        inline_message_id: Optional["String"] = None,
    ):
        super().__init__(
            user_id,
            chat_id,
            message_id,
            inline_message_id
        )
        self._method = "getGameHighScores"
        self._res_type = "List[GameHighScore]"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id

    def result(self, update_type=GameHighScore) -> "List[GameHighScore]":
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)
