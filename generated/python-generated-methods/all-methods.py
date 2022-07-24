from telelib.bot import DefaultMethod


# @url https://core.telegram.org/bots/api#getupdates
# Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.
class getUpdates(DefaultMethod):

    def __init__(
        self,
        offset: "Integer" = None,
        limit: "Integer" = None,
        timeout: "Integer" = None,
        allowed_updates: "List[String]" = None,
    ):
        self._method = "getUpdates"
        self._res_type = "List[Update]"
        self._args = {}
        self._args['offset'] = offset
        self._args['limit'] = limit
        self._args['timeout'] = timeout
        self._args['allowed_updates'] = allowed_updates

    def result(self) -> "List[Update]":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setwebhook
# Use this method to specify a URL and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success., If you'd like to make sure that the webhook was set by you, you can specify secret data in the parameter secret_token. If specified, the request will contain a header "X-Telegram-Bot-Api-Secret-Token" with the secret token as content.
class setWebhook(DefaultMethod):

    def __init__(
        self,
        url: "String",
        certificate: "InputFile" = None,
        ip_address: "String" = None,
        max_connections: "Integer" = None,
        allowed_updates: "List[String]" = None,
        drop_pending_updates: "Boolean" = None,
        secret_token: "String" = None,
    ):
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

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#deletewebhook
# Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success.
class deleteWebhook(DefaultMethod):

    def __init__(
        self,
        drop_pending_updates: "Boolean" = None,
    ):
        self._method = "deleteWebhook"
        self._res_type = "Boolean"
        self._args = {}
        self._args['drop_pending_updates'] = drop_pending_updates

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getwebhookinfo
# Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.
class getWebhookInfo(DefaultMethod):

    def __init__(
        self,

    ):
        self._method = "getWebhookInfo"
        self._res_type = "WebhookInfo"
        self._args = {}

    def result(self) -> "WebhookInfo":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getme
# A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object.
class getMe(DefaultMethod):

    def __init__(
        self,

    ):
        self._method = "getMe"
        self._res_type = "User"
        self._args = {}

    def result(self) -> "User":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#logout
# Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters.
class logOut(DefaultMethod):

    def __init__(
        self,

    ):
        self._method = "logOut"
        self._res_type = "Boolean"
        self._args = {}

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#close
# Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters.
class close(DefaultMethod):

    def __init__(
        self,

    ):
        self._method = "close"
        self._res_type = "Boolean"
        self._args = {}

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendmessage
# Use this method to send text messages. On success, the sent Message is returned.
class sendMessage(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        text: "String",
        parse_mode: "String" = None,
        entities: "List[MessageEntity]" = None,
        disable_web_page_preview: "Boolean" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#forwardmessage
# Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned.
class forwardMessage(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        from__chat_id: "Integer" | "String",
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        message_id: "Integer",
    ):
        self._method = "forwardMessage"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['from_chat_id'] = from__chat_id
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['message_id'] = message_id

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#copymessage
# Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.
class copyMessage(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        from__chat_id: "Integer" | "String",
        message_id: "Integer",
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "MessageId":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendphoto
# Use this method to send photos. On success, the sent Message is returned.
class sendPhoto(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        photo: "InputFile" | "String",
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendaudio
# Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future., For sending voice messages, use the sendVoice method instead.
class sendAudio(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        audio: "InputFile" | "String",
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        duration: "Integer" = None,
        performer: "String" = None,
        title: "String" = None,
        thumb: "InputFile" | "String" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#senddocument
# Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.
class sendDocument(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        document: "InputFile" | "String",
        thumb: "InputFile" | "String" = None,
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        disable_content_type_detection: "Boolean" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendvideo
# Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.
class sendVideo(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        video: "InputFile" | "String",
        duration: "Integer" = None,
        width: "Integer" = None,
        height: "Integer" = None,
        thumb: "InputFile" | "String" = None,
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        supports_streaming: "Boolean" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendanimation
# Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.
class sendAnimation(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        animation: "InputFile" | "String",
        duration: "Integer" = None,
        width: "Integer" = None,
        height: "Integer" = None,
        thumb: "InputFile" | "String" = None,
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendvoice
# Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.
class sendVoice(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        voice: "InputFile" | "String",
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        duration: "Integer" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendvideonote
# As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.
class sendVideoNote(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        video_note: "InputFile" | "String",
        duration: "Integer" = None,
        length: "Integer" = None,
        thumb: "InputFile" | "String" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendmediagroup
# Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.
class sendMediaGroup(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        media: "List[InputMediaAudio]" | "List[InputMediaDocument]" | "List[InputMediaPhoto]" | "List[InputMediaVideo]",
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
    ):
        self._method = "sendMediaGroup"
        self._res_type = "List[Message]"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['media'] = media
        self._args['disable_notification'] = disable_notification
        self._args['protect_content'] = protect_content
        self._args['reply_to_message_id'] = reply_to_message_id
        self._args['allow_sending_without_reply'] = allow_sending_without_reply

    def result(self) -> "List[Message]":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendlocation
# Use this method to send point on the map. On success, the sent Message is returned.
class sendLocation(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        latitude: "Float",
        longitude: "Float",
        horizontal_accuracy: "Float" = None,
        live_period: "Integer" = None,
        heading: "Integer" = None,
        proximity_alert_radius: "Integer" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#editmessagelivelocation
# Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
class editMessageLiveLocation(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        latitude: "Float",
        longitude: "Float",
        horizontal_accuracy: "Float" = None,
        heading: "Integer" = None,
        proximity_alert_radius: "Integer" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#stopmessagelivelocation
# Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned.
class stopMessageLiveLocation(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "stopMessageLiveLocation"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendvenue
# Use this method to send information about a venue. On success, the sent Message is returned.
class sendVenue(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        latitude: "Float",
        longitude: "Float",
        title: "String",
        address: "String",
        foursquare_id: "String" = None,
        foursquare_type: "String" = None,
        google_place_id: "String" = None,
        google_place_type: "String" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendcontact
# Use this method to send phone contacts. On success, the sent Message is returned.
class sendContact(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        phone_number: "String",
        first_name: "String",
        last_name: "String" = None,
        vcard: "String" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendpoll
# Use this method to send a native poll. On success, the sent Message is returned.
class sendPoll(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        question: "String",
        options: "List[String]",
        is_anonymous: "Boolean" = None,
        type: "String" = None,
        allows_multiple_answers: "Boolean" = None,
        correct_option_id: "Integer" = None,
        explanation: "String" = None,
        explanation_parse_mode: "String" = None,
        explanation_entities: "List[MessageEntity]" = None,
        open_period: "Integer" = None,
        close_date: "Integer" = None,
        is_closed: "Boolean" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#senddice
# Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.
class sendDice(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        emoji: "String" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendchataction
# Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success., We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.
class sendChatAction(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        action: "String",
    ):
        self._method = "sendChatAction"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['action'] = action

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getuserprofilephotos
# Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.
class getUserProfilePhotos(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        offset: "Integer" = None,
        limit: "Integer" = None,
    ):
        self._method = "getUserProfilePhotos"
        self._res_type = "UserProfilePhotos"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['offset'] = offset
        self._args['limit'] = limit

    def result(self) -> "UserProfilePhotos":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getfile
# Use this method to get basic information about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again., Note: This function may not preserve the original file name and MIME type. You should save the file's MIME type and name (if available) when the File object is received.
class getFile(DefaultMethod):

    def __init__(
        self,
        file_id: "String",
    ):
        self._method = "getFile"
        self._res_type = "File"
        self._args = {}
        self._args['file_id'] = file_id

    def result(self) -> "File":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#banchatmember
# Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
class banChatMember(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        user_id: "Integer",
        until_date: "Integer" = None,
        revoke_messages: "Boolean" = None,
    ):
        self._method = "banChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['until_date'] = until_date
        self._args['revoke_messages'] = revoke_messages

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#unbanchatmember
# Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success.
class unbanChatMember(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        user_id: "Integer",
        only_if_banned: "Boolean" = None,
    ):
        self._method = "unbanChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['only_if_banned'] = only_if_banned

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#restrictchatmember
# Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success.
class restrictChatMember(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        user_id: "Integer",
        permissions: "ChatPermissions",
        until_date: "Integer" = None,
    ):
        self._method = "restrictChatMember"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['permissions'] = permissions
        self._args['until_date'] = until_date

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#promotechatmember
# Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success.
class promoteChatMember(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        user_id: "Integer",
        is_anonymous: "Boolean" = None,
        can_manage_chat: "Boolean" = None,
        can_post_messages: "Boolean" = None,
        can_edit_messages: "Boolean" = None,
        can_delete_messages: "Boolean" = None,
        can_manage_video_chats: "Boolean" = None,
        can_restrict_members: "Boolean" = None,
        can_promote_members: "Boolean" = None,
        can_change_info: "Boolean" = None,
        can_invite_users: "Boolean" = None,
        can_pin_messages: "Boolean" = None,
    ):
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

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setchatadministratorcustomtitle
# Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success.
class setChatAdministratorCustomTitle(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        user_id: "Integer",
        custom_title: "String",
    ):
        self._method = "setChatAdministratorCustomTitle"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id
        self._args['custom_title'] = custom_title

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#banchatsenderchat
# Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success.
class banChatSenderChat(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        sender_chat_id: "Integer",
    ):
        self._method = "banChatSenderChat"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sender_chat_id'] = sender_chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#unbanchatsenderchat
# Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success.
class unbanChatSenderChat(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        sender_chat_id: "Integer",
    ):
        self._method = "unbanChatSenderChat"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sender_chat_id'] = sender_chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setchatpermissions
# Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success.
class setChatPermissions(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        permissions: "ChatPermissions",
    ):
        self._method = "setChatPermissions"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['permissions'] = permissions

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#exportchatinvitelink
# Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success.
class exportChatInviteLink(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "exportChatInviteLink"
        self._res_type = "String"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "String":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#createchatinvitelink
# Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object.
class createChatInviteLink(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        name: "String" = None,
        expire_date: "Integer" = None,
        member_limit: "Integer" = None,
        creates_join_request: "Boolean" = None,
    ):
        self._method = "createChatInviteLink"
        self._res_type = "ChatInviteLink"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['name'] = name
        self._args['expire_date'] = expire_date
        self._args['member_limit'] = member_limit
        self._args['creates_join_request'] = creates_join_request

    def result(self) -> "ChatInviteLink":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#editchatinvitelink
# Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object.
class editChatInviteLink(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        invite_link: "String",
        name: "String" = None,
        expire_date: "Integer" = None,
        member_limit: "Integer" = None,
        creates_join_request: "Boolean" = None,
    ):
        self._method = "editChatInviteLink"
        self._res_type = "ChatInviteLink"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['invite_link'] = invite_link
        self._args['name'] = name
        self._args['expire_date'] = expire_date
        self._args['member_limit'] = member_limit
        self._args['creates_join_request'] = creates_join_request

    def result(self) -> "ChatInviteLink":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#revokechatinvitelink
# Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object.
class revokeChatInviteLink(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        invite_link: "String",
    ):
        self._method = "revokeChatInviteLink"
        self._res_type = "ChatInviteLink"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['invite_link'] = invite_link

    def result(self) -> "ChatInviteLink":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#approvechatjoinrequest
# Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.
class approveChatJoinRequest(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        user_id: "Integer",
    ):
        self._method = "approveChatJoinRequest"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#declinechatjoinrequest
# Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.
class declineChatJoinRequest(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        user_id: "Integer",
    ):
        self._method = "declineChatJoinRequest"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setchatphoto
# Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
class setChatPhoto(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        photo: "InputFile",
    ):
        self._method = "setChatPhoto"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['photo'] = photo

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#deletechatphoto
# Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
class deleteChatPhoto(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "deleteChatPhoto"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setchattitle
# Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
class setChatTitle(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        title: "String",
    ):
        self._method = "setChatTitle"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['title'] = title

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setchatdescription
# Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
class setChatDescription(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        description: "String" = None,
    ):
        self._method = "setChatDescription"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['description'] = description

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#pinchatmessage
# Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.
class pinChatMessage(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        message_id: "Integer",
        disable_notification: "Boolean" = None,
    ):
        self._method = "pinChatMessage"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['disable_notification'] = disable_notification

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#unpinchatmessage
# Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.
class unpinChatMessage(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        message_id: "Integer" = None,
    ):
        self._method = "unpinChatMessage"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#unpinallchatmessages
# Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.
class unpinAllChatMessages(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "unpinAllChatMessages"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#leavechat
# Use this method for your bot to leave a group, supergroup or channel. Returns True on success.
class leaveChat(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "leaveChat"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getchat
# Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.
class getChat(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "getChat"
        self._res_type = "Chat"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Chat":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getchatadministrators
# Use this method to get a list of administrators in a chat. On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.
class getChatAdministrators(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "getChatAdministrators"
        self._res_type = "List[ChatMember]"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "List[ChatMember]":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getchatmembercount
# Use this method to get the number of members in a chat. Returns Int on success.
class getChatMemberCount(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "getChatMemberCount"
        self._res_type = "Integer"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Integer":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getchatmember
# Use this method to get information about a member of a chat. Returns a ChatMember object on success.
class getChatMember(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        user_id: "Integer",
    ):
        self._method = "getChatMember"
        self._res_type = "ChatMember"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['user_id'] = user_id

    def result(self) -> "ChatMember":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setchatstickerset
# Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.
class setChatStickerSet(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        sticker_set_name: "String",
    ):
        self._method = "setChatStickerSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['sticker_set_name'] = sticker_set_name

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#deletechatstickerset
# Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.
class deleteChatStickerSet(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
    ):
        self._method = "deleteChatStickerSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#answercallbackquery
# Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.
class answerCallbackQuery(DefaultMethod):

    def __init__(
        self,
        callback_query_id: "String",
        text: "String" = None,
        show_alert: "Boolean" = None,
        url: "String" = None,
        cache_time: "Integer" = None,
    ):
        self._method = "answerCallbackQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['callback_query_id'] = callback_query_id
        self._args['text'] = text
        self._args['show_alert'] = show_alert
        self._args['url'] = url
        self._args['cache_time'] = cache_time

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setmycommands
# Use this method to change the list of the bot's commands. See https://core.telegram.org/bots#commands for more details about bot commands. Returns True on success.
class setMyCommands(DefaultMethod):

    def __init__(
        self,
        commands: "List[BotCommand]",
        scope: "BotCommandScope" = None,
        language_code: "String" = None,
    ):
        self._method = "setMyCommands"
        self._res_type = "Boolean"
        self._args = {}
        self._args['commands'] = commands
        self._args['scope'] = scope
        self._args['language_code'] = language_code

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#deletemycommands
# Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success.
class deleteMyCommands(DefaultMethod):

    def __init__(
        self,
        scope: "BotCommandScope" = None,
        language_code: "String" = None,
    ):
        self._method = "deleteMyCommands"
        self._res_type = "Boolean"
        self._args = {}
        self._args['scope'] = scope
        self._args['language_code'] = language_code

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getmycommands
# Use this method to get the current list of the bot's commands for the given scope and user language. Returns Array of BotCommand on success. If commands aren't set, an empty list is returned.
class getMyCommands(DefaultMethod):

    def __init__(
        self,
        scope: "BotCommandScope" = None,
        language_code: "String" = None,
    ):
        self._method = "getMyCommands"
        self._res_type = "List[BotCommand]"
        self._args = {}
        self._args['scope'] = scope
        self._args['language_code'] = language_code

    def result(self) -> "List[BotCommand]":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setchatmenubutton
# Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success.
class setChatMenuButton(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" = None,
        menu_button: "MenuButton" = None,
    ):
        self._method = "setChatMenuButton"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['menu_button'] = menu_button

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getchatmenubutton
# Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success.
class getChatMenuButton(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" = None,
    ):
        self._method = "getChatMenuButton"
        self._res_type = "MenuButton"
        self._args = {}
        self._args['chat_id'] = chat_id

    def result(self) -> "MenuButton":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setmydefaultadministratorrights
# Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are are free to modify the list before adding the bot. Returns True on success.
class setMyDefaultAdministratorRights(DefaultMethod):

    def __init__(
        self,
        rights: "ChatAdministratorRights" = None,
        for_channels: "Boolean" = None,
    ):
        self._method = "setMyDefaultAdministratorRights"
        self._res_type = "Boolean"
        self._args = {}
        self._args['rights'] = rights
        self._args['for_channels'] = for_channels

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getmydefaultadministratorrights
# Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success.
class getMyDefaultAdministratorRights(DefaultMethod):

    def __init__(
        self,
        for_channels: "Boolean" = None,
    ):
        self._method = "getMyDefaultAdministratorRights"
        self._res_type = "ChatAdministratorRights"
        self._args = {}
        self._args['for_channels'] = for_channels

    def result(self) -> "ChatAdministratorRights":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#editmessagetext
# Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
class editMessageText(DefaultMethod):

    def __init__(
        self,
        text: "String",
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        parse_mode: "String" = None,
        entities: "List[MessageEntity]" = None,
        disable_web_page_preview: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#editmessagecaption
# Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
class editMessageCaption(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        caption: "String" = None,
        parse_mode: "String" = None,
        caption_entities: "List[MessageEntity]" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#editmessagemedia
# Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
class editMessageMedia(DefaultMethod):

    def __init__(
        self,
        media: "InputMedia",
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "editMessageMedia"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['media'] = media
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#editmessagereplymarkup
# Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
class editMessageReplyMarkup(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "editMessageReplyMarkup"
        self._res_type = "Message"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#stoppoll
# Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.
class stopPoll(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        message_id: "Integer",
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
        self._method = "stopPoll"
        self._res_type = "Poll"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['reply_markup'] = reply_markup

    def result(self) -> "Poll":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#deletemessage
# Use this method to delete a message, including service messages, with the following limitations:, - A message can only be deleted if it was sent less than 48 hours ago., - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago., - Bots can delete outgoing messages in private chats, groups, and supergroups., - Bots can delete incoming messages in private chats., - Bots granted can_post_messages permissions can delete outgoing messages in channels., - If the bot is an administrator of a group, it can delete any message there., - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there., Returns True on success.
class deleteMessage(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        message_id: "Integer",
    ):
        self._method = "deleteMessage"
        self._res_type = "Boolean"
        self._args = {}
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendsticker
# Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned.
class sendSticker(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        sticker: "InputFile" | "String",
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" | "ReplyKeyboardMarkup" | "ReplyKeyboardRemove" | "ForceReply" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getstickerset
# Use this method to get a sticker set. On success, a StickerSet object is returned.
class getStickerSet(DefaultMethod):

    def __init__(
        self,
        name: "String",
    ):
        self._method = "getStickerSet"
        self._res_type = "StickerSet"
        self._args = {}
        self._args['name'] = name

    def result(self) -> "StickerSet":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#uploadstickerfile
# Use this method to upload a .PNG file with a sticker for later use in createNewStickerSet and addStickerToSet methods (can be used multiple times). Returns the uploaded File on success.
class uploadStickerFile(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        png_sticker: "InputFile",
    ):
        self._method = "uploadStickerFile"
        self._res_type = "File"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['png_sticker'] = png_sticker

    def result(self) -> "File":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#createnewstickerset
# Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Returns True on success.
class createNewStickerSet(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        name: "String",
        title: "String",
        png_sticker: "InputFile" | "String" = None,
        tgs_sticker: "InputFile" = None,
        webm_sticker: "InputFile" = None,
        emojis: "String",
        contains_masks: "Boolean" = None,
        mask_position: "MaskPosition" = None,
    ):
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

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#addstickertoset
# Use this method to add a new sticker to a set created by the bot. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Animated stickers can be added to animated sticker sets and only to them. Animated sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success.
class addStickerToSet(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        name: "String",
        emojis: "String",
        png_sticker: "InputFile" | "String" = None,
        tgs_sticker: "InputFile" = None,
        webm_sticker: "InputFile" = None,
        mask_position: "MaskPosition" = None,
    ):
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

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setstickerpositioninset
# Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success.
class setStickerPositionInSet(DefaultMethod):

    def __init__(
        self,
        sticker: "String",
        position: "Integer",
    ):
        self._method = "setStickerPositionInSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['sticker'] = sticker
        self._args['position'] = position

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#deletestickerfromset
# Use this method to delete a sticker from a set created by the bot. Returns True on success.
class deleteStickerFromSet(DefaultMethod):

    def __init__(
        self,
        sticker: "String",
    ):
        self._method = "deleteStickerFromSet"
        self._res_type = "Boolean"
        self._args = {}
        self._args['sticker'] = sticker

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setstickersetthumb
# Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Video thumbnails can be set only for video sticker sets only. Returns True on success.
class setStickerSetThumb(DefaultMethod):

    def __init__(
        self,
        name: "String",
        user_id: "Integer",
        thumb: "InputFile" | "String" = None,
    ):
        self._method = "setStickerSetThumb"
        self._res_type = "Boolean"
        self._args = {}
        self._args['name'] = name
        self._args['user_id'] = user_id
        self._args['thumb'] = thumb

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#answerinlinequery
# Use this method to send answers to an inline query. On success, True is returned., No more than 50 results per query are allowed.
class answerInlineQuery(DefaultMethod):

    def __init__(
        self,
        inline_query_id: "String",
        results: "List[InlineQueryResult]",
        cache_time: "Integer" = None,
        is_personal: "Boolean" = None,
        next_offset: "String" = None,
        switch_pm_text: "String" = None,
        switch_pm_parameter: "String" = None,
    ):
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

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#answerwebappquery
# Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned.
class answerWebAppQuery(DefaultMethod):

    def __init__(
        self,
        web_app_query_id: "String",
        result: "InlineQueryResult",
    ):
        self._method = "answerWebAppQuery"
        self._res_type = "SentWebAppMessage"
        self._args = {}
        self._args['web_app_query_id'] = web_app_query_id
        self._args['result'] = result

    def result(self) -> "SentWebAppMessage":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendinvoice
# Use this method to send invoices. On success, the sent Message is returned.
class sendInvoice(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer" | "String",
        title: "String",
        description: "String",
        payload: "String",
        provider_token: "String",
        currency: "String",
        prices: "List[LabeledPrice]",
        max_tip_amount: "Integer" = None,
        suggested_tip_amounts: "List[Integer]" = None,
        start_parameter: "String" = None,
        provider_data: "String" = None,
        photo_url: "String" = None,
        photo_size: "Integer" = None,
        photo_width: "Integer" = None,
        photo_height: "Integer" = None,
        need_name: "Boolean" = None,
        need_phone_number: "Boolean" = None,
        need_email: "Boolean" = None,
        need_shipping_address: "Boolean" = None,
        send_phone_number_to_provider: "Boolean" = None,
        send_email_to_provider: "Boolean" = None,
        is_flexible: "Boolean" = None,
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#createinvoicelink
# Use this method to create a link for an invoice. Returns the created invoice link as String on success.
class createInvoiceLink(DefaultMethod):

    def __init__(
        self,
        title: "String",
        description: "String",
        payload: "String",
        provider_token: "String",
        currency: "String",
        prices: "List[LabeledPrice]",
        max_tip_amount: "Integer" = None,
        suggested_tip_amounts: "List[Integer]" = None,
        provider_data: "String" = None,
        photo_url: "String" = None,
        photo_size: "Integer" = None,
        photo_width: "Integer" = None,
        photo_height: "Integer" = None,
        need_name: "Boolean" = None,
        need_phone_number: "Boolean" = None,
        need_email: "Boolean" = None,
        need_shipping_address: "Boolean" = None,
        send_phone_number_to_provider: "Boolean" = None,
        send_email_to_provider: "Boolean" = None,
        is_flexible: "Boolean" = None,
    ):
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

    def result(self) -> "String":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#answershippingquery
# If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned.
class answerShippingQuery(DefaultMethod):

    def __init__(
        self,
        shipping_query_id: "String",
        ok: "Boolean",
        shipping_options: "List[ShippingOption]" = None,
        error_message: "String" = None,
    ):
        self._method = "answerShippingQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['shipping_query_id'] = shipping_query_id
        self._args['ok'] = ok
        self._args['shipping_options'] = shipping_options
        self._args['error_message'] = error_message

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#answerprecheckoutquery
# Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.
class answerPreCheckoutQuery(DefaultMethod):

    def __init__(
        self,
        pre_checkout_query_id: "String",
        ok: "Boolean",
        error_message: "String" = None,
    ):
        self._method = "answerPreCheckoutQuery"
        self._res_type = "Boolean"
        self._args = {}
        self._args['pre_checkout_query_id'] = pre_checkout_query_id
        self._args['ok'] = ok
        self._args['error_message'] = error_message

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setpassportdataerrors
# Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success., Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.
class setPassportDataErrors(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        errors: "List[PassportElementError]",
    ):
        self._method = "setPassportDataErrors"
        self._res_type = "Boolean"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['errors'] = errors

    def result(self) -> "Boolean":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#sendgame
# Use this method to send a game. On success, the sent Message is returned.
class sendGame(DefaultMethod):

    def __init__(
        self,
        chat_id: "Integer",
        game_short_name: "String",
        disable_notification: "Boolean" = None,
        protect_content: "Boolean" = None,
        reply_to_message_id: "Integer" = None,
        allow_sending_without_reply: "Boolean" = None,
        reply_markup: "InlineKeyboardMarkup" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#setgamescore
# Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False.
class setGameScore(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        score: "Integer",
        force: "Boolean" = None,
        disable_edit_message: "Boolean" = None,
        chat_id: "Integer" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
    ):
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

    def result(self) -> "Message":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res


# @url https://core.telegram.org/bots/api#getgamehighscores
# Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. On success, returns an Array of GameHighScore objects.
class getGameHighScores(DefaultMethod):

    def __init__(
        self,
        user_id: "Integer",
        chat_id: "Integer" = None,
        message_id: "Integer" = None,
        inline_message_id: "String" = None,
    ):
        self._method = "getGameHighScores"
        self._res_type = "List[GameHighScore]"
        self._args = {}
        self._args['user_id'] = user_id
        self._args['chat_id'] = chat_id
        self._args['message_id'] = message_id
        self._args['inline_message_id'] = inline_message_id

    def result(self) -> "List[GameHighScore]":
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res
