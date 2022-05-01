
import { default as _Message, JsonMessage } from './types/message'
import { default as _Update, JsonUpdate } from './types/update'
import { default as _User, JsonUser } from './types/user'
import { default as _Chat, JsonChat } from './types/chat'
import { default as _CallbackQuery, JsonCallbackQuery } from './types/callback-query'
import { default as _ChatPhoto, JsonChatPhoto } from './types/chat-photo'
import { default as _ChatPermissions, JsonChatPermissions } from './types/chat-permissions'
import { default as _Location, JsonLocation } from './types/location'
import { default as _Venue, JsonVenue } from './types/venue'
import { default as _ChatLocation, JsonChatLocation } from './types/chat-location'
import { default as _MessageEntity, JsonMessageEntity } from './types/message-entity'
import { default as _Animation, JsonAnimation, AnimationMessage } from './types/animation'
import { default as _PhotoSize, JsonPhotoSize } from './types/photo-size'
import { default as _Audio, JsonAudio } from './types/audio'
import { default as _Document, JsonDocument } from './types/document'
import { default as _Sticker, JsonSticker } from './types/sticker'
import { default as _Video, JsonVideo } from './types/video'
import { default as _MaskPosition, JsonMaskPosition } from './types/mask-position'
import { default as _VideoNote, JsonVideoNote } from './types/video-note'
import { default as _Voice, JsonVoice } from './types/voice'
import { default as _Dice, JsonDice } from './types/dice'
import { default as _Contact, JsonContact } from './types/contact'
import { default as _Game, JsonGame } from './types/game'
import { default as _Poll, JsonPoll } from './types/poll'
import { default as _PollOption, JsonPollOption } from './types/poll-option'
import { default as _PollAnswer, JsonPollAnswer } from './types/poll-answer'
import { default as _Invoice, JsonInvoice } from './types/invoice'
import { default as _OrderInfo, JsonOrderInfo } from './types/order-info'
import { default as _MessageAutoDeleteTimerChanged, JsonMessageAutoDeleteTimerChanged } from './types/message-auto-delete-timer-changed'
import { default as _SuccessfulPayment, JsonSuccessfulPayment} from './types/successful-payment'
import { default as _ShippingAddress, JsonShippingAddress } from './types/shipping-address'
import { default as _PassportData, JsonPassportData } from './types/passport-data'
import { default as _EncryptedPassportElement, JsonEncryptedPassportElement } from './types/encrypted-passport-element'
import { default as _PassportFile, JsonPassportFile } from './types/passport-file'
import { default as _EncryptedCredentials, JsonEncryptedCredentials } from './types/encrypted-credentials'
import { default as _ProximityAlertTriggered, JsonProximityAlertTriggered } from './types/proximity-alert-triggered'
import { default as _VoiceChatScheduled, JsonVoiceChatScheduled } from './types/voice-chat-scheduled'
import { default as _VoiceChatStarted, JsonVoiceChatStarted } from './types/voice-chat-started'
import { default as _VoiceChatEnded, JsonVoiceChatEnded } from './types/voice-chat-ended'
import { default as _VoiceChatParticipantsInvited, JsonVoiceChatParticipantsInvited } from './types/voice-chat-participants-invited'
import { default as _InlineKeyboardMarkup, JsonInlineKeyboardMarkup } from './types/inline-keyboard-markup'
import { default as _InlineKeyboardButton, JsonInlineKeyboardButton } from './types/inline-keyboard-button'
import { default as _LoginUrl, JsonLoginUrl } from './types/login-url'
import { default as _CallbackGame, JsonCallbackGame } from './types/callback-game'
import { default as _KeyboardButton, JsonKeyboardButton } from './types/keyboard-button'
import {
	default as _ChatMember, JsonChatMember,
	JsonChatMemberAdministrator,
	JsonChatMemberBanned,
	JsonChatMemberLeft,
	JsonChatMemberMember,
	JsonChatMemberOwner,
	JsonChatMemberRestricted
} from './types/chat-member'

import { default as _InlineQuery, JsonInlineQuery } from './types/inline-query'
import { default as _ChosenInlineResult, JsonChosenInlineResult } from './types/chosen-inline-result'
import { default as _ShippingQuery, JsonShippingQuery } from './types/shipping-query'
import { default as _PreCheckoutQuery, JsonPreCheckoutQuery } from './types/pre-checkout-query'
import { default as _ChatMemberUpdated, JsonChatMemberUpdated } from './types/chat-member-updated'
import { default as _ChatJoinRequest, JsonChatJoinRequest } from './types/chat-join-request'
import { default as _ChatInviteLink, JsonChatInviteLink } from './types/chat-invite-link'

import { default as _ReplyKeyboardMarkup, JsonReplyKeyboardMarkup } from './types/reply-keyboard-markup'
import { default as _ReplyKeyboardRemove, JsonReplyKeyboardRemove } from './types/reply-keyboard-remove'
import { default as _ForceReply, JsonForceReply } from './types/force-reply'
import { default as _KeyboardButtonPollType, JsonKeyboardButtonPollType } from './types/keyboard-button-poll-type'
import { default as _WebAppInfo, JsonWebAppInfo } from './types/web-app-info'
import { default as _WebAppData, JsonWebAppData } from './types/webapp-data'

import {
	InlineQueryResult,
	InlineQueryResultArticle,
	InlineQueryResultPhoto,
	InlineQueryResultGif,
	InlineQueryResultMpeg4Gif,
	InlineQueryResultVideo,
	InlineQueryResultAudio,
	InlineQueryResultVenue,
	InlineQueryResultLocation,
	InlineQueryResultVoice,
	InlineQueryResultDocument,
	InlineQueryResultContact,
	InlineQueryResultGame,
	InlineQueryResultCachedPhoto,
	InlineQueryResultCachedMpeg4Gif,
	InlineQueryResultCachedGif,
	InlineQueryResultCachedSticker,
	InlineQueryResultCachedDocument,
	InlineQueryResultCachedVideo,
	InlineQueryResultCachedVoice,
	InlineQueryResultCachedAudio,
} from './types/inline-query-result'




import Type from './types/type'
export class InputFile {
	constructor(
		public file_path: Str,
		public file_name: Str
	) { }
}

export const CURRENT_UPDATE_TYPES: AllowedUpdates[] = [
	'message',
	'edited_message',
	'channel_post',
	'edited_channel_post',
	'inline_query',
	'chosen_inline_result',
	'callback_query',
	'shipping_query',
	'pre_checkout_query',
	'poll',
	'poll_answer',
	'my_chat_member',
	'chat_member',
	'chat_join_request',
]
export const TELEGRAM_API_VERSION = 6.0

export declare type Bool = boolean | 0 | 1
export declare type Num = number
export declare type BigNum = bigint
export declare type Str = string

export declare type Number = Num
export declare type String = Str
export declare type FileId = Str
export declare type UniqueFileId = Str
export declare type Boolean = Bool
export declare type UpdateId = Num
export declare type MessageId = Num
export declare type _ChatId = Str | Num | `-100${Num}` | `-${Num}` | `@${Str}`
export declare type _UserId = Num
export declare type UserId = Num | BigNum | _UserId
export declare type ChatId = Num | BigNum | _ChatId
// todo: add all language codes.
export declare type LanguageCode = Str
export declare type ParseMode =  'MarkDown' | 'MarkDownV2' | 'HTML'
export declare type ChatType = 'private' | 'group' | 'supergroup' | 'channel'
// subjected to be changed since Telegram is adding new Entity types with each update.
export declare type MessageEntityType = 'mention' | 'hashtag' | 'cashtag' | 'bot_command' | 'url' | 'email' | 'phone_number' | 'bold' | 'italic' | 'underline' | 'strikethrough' | 'spoiler' | 'code' | 'pre' | 'text_link' | 'text_mention'
// subjected to be changed since Telegram is adding new UpdateType types with each update.
export declare type AllowedUpdates = 'message' | 'edited_message' | 'channel_post' | 'edited_channel_post' | 'inline_query' | 'chosen_inline_result' | 'callback_query' | 'shipping_query' | 'pre_checkout_query' | 'poll' | 'poll_answer' | 'my_chat_member' | 'chat_member' | 'chat_join_request'
// subjected to be changed since Telegram is adding new DiceType with each update.
export declare type DiceType = '🎲' | '🎯' | '🎳' | '🏀' | '⚽' | '🎰'
export declare type PollType = 'regular' | 'quiz'
export declare type HttpsUrl = `https://${Str}`
export declare type HttpUrl = `http://${Str}`
export declare type Url = HttpUrl | HttpsUrl

// Type of action to broadcast.
// Choose one, depending on what the user is about to receive:
// typing for text messages, upload_photo for photos,
// record_video or upload_video for videos, record_voice or upload_voice for voice notes,
// upload_document for general files, choose_sticker for stickers, find_location for location data,
// record_video_note or upload_video_note for video notes.
export declare type ChatAction = 'typing' | 'upload_photo' | 'record_video' | 'upload_video' | 'record_voice' | 'upload_voice' | 'upload_document' | 'choose_sticker' | 'find_location' | 'record_video_note' | 'upload_video_note'


export class Update extends _Update { }

export class Message extends _Message {
	type() {
		if (this.text) return 'text'
		if (this.photo) return 'photo'
		if (this.video) return 'video'
		if (this.animation) return 'animation'
		if (this.audio) return 'audio'
		if (this.document) return 'document'
		if (this.sticker) return 'sticker'
		if (this.video) return 'video'
		if (this.video_note) return 'video_note'
		if (this.voice) return 'voice'
		if (this.contact) return 'contact'
		if (this.dice) return 'dice'
		if (this.game) return 'game'
		if (this.poll) return 'poll'
		if (this.venue) return 'venue'
		if (this.location) return 'location'
		if (this.invoice) return 'invoice'
		if (this.successful_payment) return 'successful_payment'
		if (this.connected_website) return 'connected_website'
		if (this.pinned_message) return 'service_message'
		if (this.passport_data) return 'passport_data'
		if (this.proximity_alert_triggered) return 'proximity_alert_triggered'

		if (this.new_chat_members) return 'service_message'
		if (this.left_chat_member) return 'service_message'
		if (this.new_chat_title) return 'service_message'
		if (this.new_chat_photo) return 'service_message'
		if (this.delete_chat_photo) return 'service_message'
		if (this.supergroup_chat_created) return 'service_message'
		if (this.channel_chat_created) return 'service_message'
		if (this.message_auto_delete_timer_changed) return 'service_message'
		if (this.migrate_to_chat_id) return 'service_message'
		if (this.migrate_from_chat_id) return 'service_message'
		if (this.pinned_message) return 'service_message'
		if (this.web_app_data) return 'web_app_data'

		return 'unknown'
	}

	reply(text: string, reply_markup?: ReplyMarkup, parse_mode?: ParseMode) : never | Promise<Message> {
		if (!this.chat) {
			throw Error('Can\'t reply on a message while there\'s not message.')
		}

		return this.methods.sendMessage(this.chat.id, text, this.message_id, parse_mode, reply_markup)
	}

	onMatch(match: RegExp, next: (matcher?: any | any[]) => Bool): Bool {
		let text!: string

		if (this.text) {
			text = this.text
		}

		if (this.caption) {
			text = `$$<${this.type()}$$type>:type{${this.caption}}`
		}

		if (typeof text === 'undefined') {
			text = `$$<${this.type()}$$type>`
		}

		const matcher = text.match(match)

		if (matcher) {
			return next(matcher)
		}

		return false
	}

}

export class CallbackQuery extends _CallbackQuery { }
export class InlineQuery extends _InlineQuery { }
export class ChosenInlineResult extends _ChosenInlineResult { }
export class ShippingQuery extends _ShippingQuery { }
export class PreCheckoutQuery extends _PreCheckoutQuery { }
export class ChatMemberUpdated extends _ChatMemberUpdated { }
export class ChatJoinRequest extends _ChatJoinRequest { }

export class User extends _User {  }


export class Chat extends _Chat {
	isPrivate = () => this.type === 'private'
}

export class ChatPhoto extends _ChatPhoto { }
export class ChatPermissions extends _ChatPermissions { }
export class Location extends _Location { }
export class Venue extends _Venue { }
export class ChatLocation extends _ChatLocation { }
export class MessageEntity extends _MessageEntity { }
export class Animation extends _Animation { }
export class PhotoSize extends _PhotoSize { }
export class Audio extends _Audio { }
export class Sticker extends _Sticker { }
export class MaskPosition extends _MaskPosition { }
export class Video extends _Video { }
export class Document extends _Document { }
export class VideoNote extends _VideoNote { }
export class Voice extends _Voice { }
export class Contact extends _Contact { }
export class Dice extends _Dice { }
export class Game extends _Game { }
export class Poll extends _Poll { }
export class PollOption extends _PollOption { }
export class PollAnswer extends _PollAnswer { }
export class Invoice extends _Invoice { }
export class MessageAutoDeleteTimerChanged extends _MessageAutoDeleteTimerChanged { }
export class SuccessfulPayment extends _SuccessfulPayment { }
export class OrderInfo extends _OrderInfo { }
export class ShippingAddress extends _ShippingAddress { }
export class PassportData extends _PassportData { }
export class EncryptedPassportElement extends _EncryptedPassportElement {}
export class PassportFile extends _PassportFile {}
export class EncryptedCredentials extends _EncryptedCredentials { }
export class ProximityAlertTriggered extends _ProximityAlertTriggered { }
export class VoiceChatScheduled extends _VoiceChatScheduled { }
export class VoiceChatStarted extends _VoiceChatStarted { }
export class VoiceChatEnded extends _VoiceChatEnded { }
export class VoiceChatParticipantsInvited extends _VoiceChatParticipantsInvited { }
export class InlineKeyboardMarkup extends _InlineKeyboardMarkup { }
export class InlineKeyboardButton extends _InlineKeyboardButton { }
export class LoginUrl extends _LoginUrl { }
export class CallbackGame extends _CallbackGame { }
export class KeyboardButton extends _KeyboardButton { }
export class ChatMember extends _ChatMember { }
export class ChatInviteLink extends _ChatInviteLink { }
export class ReplyKeyboardMarkup extends _ReplyKeyboardMarkup { }
export class ReplyKeyboardRemove extends _ReplyKeyboardRemove { }
export class ForceReply extends _ForceReply { }
export class KeyboardButtonPollType extends _KeyboardButtonPollType { }
export class WebAppInfo extends _WebAppInfo { }
export class WebAppData extends _WebAppData { }



export class ReplyMarkup extends Type {

	defaultObject!: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply

	constructor(keyboard: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply) {
		super()
		this.defaultObject = keyboard
	}
}









export declare type MethodNames = 'getUpdates'
	| 'setWebhook'
	| 'deleteWebhook'
	| 'getWebhookInfo'
	| 'getMe'
	| string


export declare type data = {
	offset: Num
	timeout: Num
	limit: Num
	allowed_updates: AllowedUpdates[]
}
	| {
		url:Str
		certificate:JsonFile
		ip_address: Str
		max_connections: Num
		allowed_updates: AllowedUpdates[]
		drop_pending_updates: Bool
	}
	| Record<string, never>
	| any

export declare type WebhookInfo = {
	url: Str,
	ip_address: Str,
	has_custom_certificate: Bool,
	pending_update_count: Num,
	last_synchronization_error_date?: Num,
	last_error_date?: Num,
	last_error_message?: Str,
	max_connections?: Num,
	allowed_updates: AllowedUpdates[],
}

export declare type InputMediaPhoto = {
	type: 'photo'
	media: FileId | InputFile | Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
}

export declare type InputMediaVideo = {
	type: 'video'
	media: FileId | InputFile | Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	thumb?: FileId | InputFile | Str
	width?: Num
	height?: Num
	duration?: Num
	supports_streaming?: Bool
}

export declare type InputMediaAnimation = {
	type: 'animation'
	media: FileId | InputFile | Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	thumb?: FileId | InputFile | Str
	width?: Num
	height?: Num
	duration?: Num
}

export declare type InputMediaAudio = {
	type: 'audio'
	media: FileId | InputFile | Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	thumb?: FileId | InputFile | Str
	performer?: Str
	title?: Str
	duration?: Num
}

export declare type InputMediaDocument = {
	type: 'document'
	media: FileId | InputFile | Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	disable_content_type_detection?: Bool
}


export declare type InputMedia = InputMediaDocument | InputMediaAudio | InputMediaAnimation | InputMediaVideo | InputMediaPhoto




export declare type JsonUserProfilePhotos = {
	total_count: number
	photos: JsonPhotoSize[][]
}

export class UserProfilePhotos extends Type {
	photos: PhotoSize[][]
	total_count: number


	defaultObject!: JsonUserProfilePhotos

	constructor(res: JsonUserProfilePhotos) {
		super()

		this.defaultObject = res

		this.photos = res.photos.map(photo => photo.map(size => new PhotoSize(size)))
		this.total_count = res.total_count
	}
}

export declare type JsonFile = {
	file_id: FileId
	file_unique_id: UniqueFileId
	file_size: Num
	file_path?: Str
}

export class File extends Type {
	file_id: FileId
	file_unique_id: UniqueFileId
	file_size: Num
	file_path?: Str

	defaultObject!: JsonFile

	constructor(res: JsonFile) {
		super()

		this.defaultObject = res

		this.file_id = res.file_id
		this.file_unique_id = res.file_unique_id
		this.file_size = res.file_size
		this.file_path = res.file_path
	}
}

export declare type JsonBotCommand = {
	command: Str
	description: Str
}

export class BotCommand extends Type {
	command: Str
	description: Str

	defaultObject!:JsonBotCommand

	constructor(res: JsonBotCommand) {
		super()

		this.defaultObject = res

		this.command = res.command
		this.description = res.description
	}
}



export declare type BotCommandScope = BotCommandScopeDefault | BotCommandScopeAllPrivateChats | BotCommandScopeAllGroupChats | BotCommandScopeAllChatAdministrators | BotCommandScopeChat | BotCommandScopeChatMember | BotCommandScopeChatAdministrators


export declare type BotCommandScopeDefault = {
	type: 'default'
}

export declare type BotCommandScopeAllPrivateChats = {
	type: 'all_private_chats'
}

export declare type BotCommandScopeAllGroupChats = {
	type: 'all_group_chats'
}

export declare type BotCommandScopeAllChatAdministrators = {
	type: 'all_chat_administrators'
}

export declare type BotCommandScopeChat = {
	type: 'chat'
	chat_id: ChatId
}

export declare type BotCommandScopeChatAdministrators = {
	type: 'chat_administrators'
	chat_id: ChatId
}

export declare type BotCommandScopeChatMember = {
	type: 'chat_member'
	chat_id: ChatId
	user_id: UserId
}


export declare type JsonMenuButton = MenuButtonCommands | MenuButtonWebApp | MenuButtonDefault

export class MenuButton extends Type {
	type: 'commands' | 'web_app' | 'default'
	text?: Str
	web_app?: JsonWebAppInfo

	defaultObject!: JsonMenuButton

	constructor(res: JsonMenuButton) {
		super()

		this.defaultObject = res

		this.type = res.type

		if (res.type === 'web_app') {
			this.text = res.text
		}
	}
}

export declare type MenuButtonDefault = {
	type: 'default'
}

export declare type MenuButtonCommands = {
	type: 'commands'
}

export declare type MenuButtonWebApp = {
	type: 'web_app'
	text: Str
	web_app: JsonWebAppInfo
}

export declare type JsonChatAdministratorRights = {
	is_anonymous: Bool
	can_manage_chat: Bool
	can_delete_messages: Bool
	can_manage_video_chats: Bool
	can_restrict_members: Bool
	can_promote_members: Bool
	can_change_info: Bool
	can_invite_users: Bool
	can_post_messages: Bool
	can_edit_messages: Bool
	can_pin_messages: Bool
}

export class ChatAdministratorRights extends Type {
	is_anonymous: Bool
	can_manage_chat: Bool
	can_delete_messages: Bool
	can_manage_video_chats: Bool
	can_restrict_members: Bool
	can_promote_members: Bool
	can_change_info: Bool
	can_invite_users: Bool
	can_post_messages: Bool
	can_edit_messages: Bool
	can_pin_messages: Bool

	defaultObject!: JsonChatAdministratorRights

	constructor(res: JsonChatAdministratorRights) {
		super()

		this.defaultObject = res

		this.is_anonymous = res.is_anonymous
		this.can_manage_chat = res.can_manage_chat
		this.can_delete_messages = res.can_delete_messages
		this.can_manage_video_chats = res.can_manage_video_chats
		this.can_restrict_members = res.can_restrict_members
		this.can_promote_members = res.can_promote_members
		this.can_change_info = res.can_change_info
		this.can_invite_users = res.can_invite_users
		this.can_post_messages = res.can_post_messages
		this.can_edit_messages = res.can_edit_messages
		this.can_pin_messages = res.can_pin_messages
	}
}


export declare type JsonStickerSet = {
	name: Str
	title: Str
	is_animated: Bool
	is_video: Bool
	contains_masks: Bool
	stickers: Sticker[]
	thumb?: PhotoSize
}

export class StickerSet extends Type {
	name: Str
	title: Str
	is_animated: Bool
	is_video: Bool
	contains_masks: Bool
	stickers: Sticker[]
	thumb?: PhotoSize

	defaultObject!: JsonStickerSet

	constructor(res: JsonStickerSet) {
		super()

		this.defaultObject = res

		this.name = res.name
		this.title = res.title
		this.is_animated = res.is_animated
		this.is_video = res.is_video
		this.contains_masks = res.contains_masks
		this.stickers = res.stickers.map(s => new Sticker(s))
		this.thumb = res.thumb ? new PhotoSize(res.thumb) : undefined
	}
}

export declare type LabeledPrice = {
	label: Str
	amount: Num
}


export declare type InputTextMessageContent = {
	message_text: Str
	parse_mode?: ParseMode
	entities?: MessageEntity[]
	disable_web_page_preview?: Bool
}

export declare type InputLocationMessageContent = {
	latitude: Num
	longitude: Num
	horizontal_accuracy?: Num
	live_period?: Num
	heading?: Num
	proximity_alert_radius?: Num
}

export declare type InputVenueMessageContent = {
	latitude: Num
	longitude: Num
	title: Str
	address: Str
	foursquare_id?: Str
	foursquare_type?: Str
	google_place_id?: Str
	google_place_type?: Str
}

export declare type InputContactMessageContent = {
	phone_number: Str
	first_name: Str
	last_name?: Str
	vcard?: Str
}

export declare type InputInvoiceMessageContent = {
	title: Str
	description: Str
	payload: Str
	provider_token: Str
	currency: Str
	prices: LabeledPrice[]
	max_tip_amount?: Num
	suggested_tip_amounts?: Num[]
	provider_data?: Str
	photo_url?: Str
	photo_size?: Num
	photo_width?: Num
	photo_height?: Num
	need_name?: Bool
	need_phone_number?: Bool
	need_email?: Bool
	need_shipping_address?: Bool
	send_phone_number_to_provide?: Bool
	send_email_to_provide?: Bool
	is_flexible?: Bool
}

export declare type InputMessageContent = InputTextMessageContent | InputLocationMessageContent | InputVenueMessageContent | InputContactMessageContent | InputInvoiceMessageContent

export declare type ShippingOption = {
	id: Str
	title: Str
	prices: LabeledPrice[]
}


export class SentWebAppMessage extends Type {
	inline_message_id: Str

	defaultObject!: {
		inline_message_id: Str
	}

	constructor(res: { inline_message_id: Str }) {
		super()

		this.defaultObject = res

		this.inline_message_id = res.inline_message_id
	}
}

export declare type JsonGameHighScore =  {
	position: Num
	user: JsonUser
	score: Num
}

export class GameHighScore extends Type {
	position: Num
	user: User
	score: Num

	defaultObject!: JsonGameHighScore

	constructor(res: JsonGameHighScore) {
		super()

		this.defaultObject = res

		this.position = res.position
		this.user = new User(res.user)
		this.score = res.score
	}
}

export declare type response<T> = {
	ok: boolean
	result: T
}

export {
	JsonMessage,
	JsonUpdate,
	JsonUser,
	JsonChat,
	JsonCallbackQuery,
	JsonChatPhoto,
	JsonChatPermissions,
	JsonLocation,
	JsonOrderInfo,
	JsonMessageEntity,
	JsonChatLocation,
	JsonAnimation,
	JsonPhotoSize,
	JsonSticker,
	JsonMaskPosition,
	JsonVideo,
	JsonVideoNote,
	JsonVoice,
	JsonContact,
	JsonDice,
	JsonAudio,
	JsonPoll,
	JsonPollOption,
	JsonPollAnswer,
	JsonVenue,
	JsonDocument,
	JsonMessageAutoDeleteTimerChanged,
	JsonInvoice,
	JsonGame,
	JsonShippingAddress,
	JsonSuccessfulPayment,
	JsonPassportData,
	JsonEncryptedPassportElement,
	JsonPassportFile,
	JsonEncryptedCredentials,
	JsonProximityAlertTriggered,
	JsonVoiceChatScheduled,
	JsonVoiceChatStarted,
	JsonVoiceChatEnded,
	JsonVoiceChatParticipantsInvited,
	JsonInlineKeyboardButton,
	JsonInlineKeyboardMarkup,
	JsonLoginUrl,
	JsonCallbackGame,
	JsonKeyboardButton,
	JsonChatMember,
	JsonInlineQuery,
	JsonChosenInlineResult,
	JsonShippingQuery,
	JsonPreCheckoutQuery,
	JsonChatMemberUpdated,
	JsonChatJoinRequest,
	JsonChatInviteLink,
	JsonReplyKeyboardMarkup,
	JsonReplyKeyboardRemove,
	JsonForceReply,
	JsonKeyboardButtonPollType,
	JsonWebAppInfo,
	JsonChatMemberAdministrator,
	JsonChatMemberBanned,
	JsonChatMemberLeft,
	JsonChatMemberMember,
	JsonChatMemberOwner,
	JsonChatMemberRestricted,
	JsonWebAppData,
	InlineQueryResult,
	InlineQueryResultArticle,
	InlineQueryResultPhoto,
	InlineQueryResultGif,
	InlineQueryResultMpeg4Gif,
	InlineQueryResultVideo,
	InlineQueryResultAudio,
	InlineQueryResultVenue,
	InlineQueryResultLocation,
	InlineQueryResultVoice,
	InlineQueryResultDocument,
	InlineQueryResultContact,
	InlineQueryResultGame,
	InlineQueryResultCachedPhoto,
	InlineQueryResultCachedMpeg4Gif,
	InlineQueryResultCachedGif,
	InlineQueryResultCachedSticker,
	InlineQueryResultCachedDocument,
	InlineQueryResultCachedVideo,
	InlineQueryResultCachedVoice,
	InlineQueryResultCachedAudio,

	AnimationMessage,
}

export default {

}


// todo: Clean it up later.

// if you want to do it, look at other typings in /types directory
// and move types that are scattered in this file there and make a pull request
// i'd be happy to see one :)