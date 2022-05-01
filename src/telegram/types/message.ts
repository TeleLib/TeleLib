import * as type from '../types'
import Type from './type'

export declare type JsonMessage = {
	message_id: type.MessageId
	from?: type.JsonUser
	sender_chat?: type.JsonChat
	date: type.Number
	chat?: type.JsonChat
	forward_from?: type.JsonUser
	forward_from_chat?: type.JsonChat
	forward_from_message_id: type.Number
	forward_signature?: type.String
	forward_sender_name?: type.String
	forward_date?: type.Number
	is_automatic_forward?: type.Boolean
	reply_to_message?: type.JsonMessage
	via_bot?: type.JsonUser
	edit_date?: type.Number
	has_protected_content?: type.Boolean
	media_group_id?: type.String
	author_signature?: type.String
	text?: type.String
	caption?: type.String
	entities?: type.JsonMessageEntity[]
	caption_entities?: type.JsonMessageEntity[]
	animation?: type.JsonAnimation
	audio?: type.JsonAudio
	document?: type.JsonDocument
	photo?: type.JsonPhotoSize[]
	sticker?: type.JsonSticker
	video?: type.JsonVideo
	video_note?: type.JsonVideoNote
	voice?: type.JsonVoice
	contact?: type.JsonContact
	dice?: type.JsonDice
	game?: type.JsonGame
	poll?: type.JsonPoll
	venue?: type.JsonVenue
	location?: type.JsonLocation
	new_chat_members?: type.JsonUser[]
	left_chat_member?: type.JsonUser
	new_chat_title?: type.String
	new_chat_photo?: type.JsonPhotoSize[]
	delete_chat_photo?: type.Boolean
	group_chat_created?: type.Boolean
	supergroup_chat_created?: type.Boolean
	channel_chat_created?: type.Boolean
	message_auto_delete_timer_changed?: type.JsonMessageAutoDeleteTimerChanged
	migrate_to_chat_id?: type.Number
	migrate_from_chat_id?: type.Number
	pinned_message?: type.JsonMessage
	invoice?: type.JsonInvoice
	successful_payment?: type.JsonSuccessfulPayment
	connected_website?: type.String
	passport_data?: type.JsonPassportData
	proximity_alert_triggered?: type.JsonProximityAlertTriggered
	voice_chat_scheduled?: type.JsonVoiceChatScheduled
	voice_chat_started?: type.JsonVoiceChatStarted
	voice_chat_ended?: type.JsonVoiceChatEnded
	voice_chat_participants_invited?: type.JsonVoiceChatParticipantsInvited

	video_chat_scheduled?: type.JsonVoiceChatScheduled
	video_chat_started?: type.JsonVoiceChatStarted
	video_chat_ended?: type.JsonVoiceChatEnded
	video_chat_participants_invited?: type.JsonVoiceChatParticipantsInvited

	web_app_data?: type.JsonWebAppData

	reply_markup?: type.JsonInlineKeyboardMarkup
}

export default class Message extends Type {
	message_id: type.MessageId
	from?: type.User
	sender_chat?: type.Chat
	date: type.Number
	chat?: type.Chat
	forward_from?: type.User
	forward_from_chat?: type.Chat
	forward_from_message_id: type.Number
	forward_signature?: type.String
	forward_sender_name?: type.String
	forward_date?: type.Number
	is_automatic_forward?: type.Boolean
	reply_to_message?: Message
	via_bot?: type.User
	edit_date?: type.Number
	has_protected_content?: type.Boolean
	media_group_id?: type.String
	author_signature?: type.String
	text?: type.String
	caption?: type.String
	entities?: type.MessageEntity[]
	caption_entities?: type.MessageEntity[]
	animation?: type.Animation
	audio?: type.Audio
	document?: type.Document
	photo?: type.PhotoSize[]
	sticker?: type.Sticker
	video?: type.Video
	video_note?: type.VideoNote
	voice?: type.Voice
	contact?: type.Contact
	dice?: type.Dice
	game?: type.Game
	poll?: type.Poll
	venue?: type.Venue
	location?: type.Location
	new_chat_members?: type.User[]
	left_chat_member?: type.User
	new_chat_title?: type.String
	new_chat_photo?: type.PhotoSize[]
	delete_chat_photo?: type.Boolean
	group_chat_created?: type.Boolean
	supergroup_chat_created?: type.Boolean
	channel_chat_created?: type.Boolean
	message_auto_delete_timer_changed?: type.MessageAutoDeleteTimerChanged
	migrate_to_chat_id?: type.Number
	migrate_from_chat_id?: type.Number
	pinned_message?: type.Message
	invoice?: type.Invoice
	successful_payment?: type.SuccessfulPayment
	connected_website?: type.String
	passport_data?: type.PassportData
	proximity_alert_triggered?: type.ProximityAlertTriggered


	// todo: remove and rename "VoiceChat" to "VideoChat" later
	// Renamed the fields voice_chat_scheduled, voice_chat_started, voice_chat_ended,
	// and voice_chat_participants_invited to
	// video_chat_scheduled,  video_chat_started, video_chat_ended, and video_chat_participants_invited in the class Message.
	// The old fields will remain temporarily available.

	voice_chat_scheduled?: type.VoiceChatScheduled
	voice_chat_started?: type.VoiceChatStarted
	voice_chat_ended?: type.VoiceChatEnded
	voice_chat_participants_invited?: type.VoiceChatParticipantsInvited

	video_chat_scheduled?: type.VoiceChatScheduled
	video_chat_started?: type.VoiceChatStarted
	video_chat_ended?: type.VoiceChatEnded
	video_chat_participants_invited?: type.VoiceChatParticipantsInvited

	web_app_data?: type.WebAppData

	reply_markup?: type.InlineKeyboardMarkup

	defaultObject!: JsonMessage

	constructor(data: JsonMessage) {
		super()
		this.defaultObject = data
		this.message_id = data.message_id
		this.from = data.from ? new type.User(data.from) : undefined
		this.sender_chat = data.sender_chat ? new type.Chat(data.sender_chat) : undefined
		this.date = data.date
		this.chat = data.chat ? new type.Chat(data.chat) : undefined
		this.forward_from = data.forward_from ? new type.User(data.forward_from) : undefined
		this.forward_from_chat = data.forward_from_chat
			? new type.Chat(data.forward_from_chat)
			: undefined
		this.forward_from_message_id = data.forward_from_message_id
		this.forward_signature = data.forward_signature
		this.forward_sender_name = data.forward_sender_name
		this.forward_date = data.forward_date
		this.is_automatic_forward = data.is_automatic_forward
		this.reply_to_message = data.reply_to_message
			? new type.Message(data.reply_to_message)
			: undefined
		this.via_bot = data.via_bot ? new type.User(data.via_bot) : undefined
		this.edit_date = data.edit_date
		this.has_protected_content = data.has_protected_content
		this.media_group_id = data.media_group_id
		this.author_signature = data.author_signature
		this.text = data.text
		this.caption = data.caption
		this.entities = data.entities ? data.entities.map((x) => new type.MessageEntity(x)) : undefined
		this.caption_entities = data.caption_entities
			? data.caption_entities.map((x) => new type.MessageEntity(x))
			: undefined
		this.animation = data.animation ? new type.Animation(data.animation) : undefined
		this.audio = data.audio ? new type.Audio(data.audio) : undefined
		this.document = data.document ? new type.Document(data.document) : undefined
		this.photo = data.photo ? data.photo.map((x) => new type.PhotoSize(x)) : undefined
		this.sticker = data.sticker ? new type.Sticker(data.sticker) : undefined
		this.video = data.video ? new type.Video(data.video) : undefined
		this.video_note = data.video_note ? new type.VideoNote(data.video_note) : undefined
		this.voice = data.voice ? new type.Voice(data.voice) : undefined
		this.contact = data.contact ? new type.Contact(data.contact) : undefined
		this.dice = data.dice ? new type.Dice(data.dice) : undefined
		this.game = data.game ? new type.Game(data.game) : undefined
		this.poll = data.poll ? new type.Poll(data.poll) : undefined
		this.venue = data.venue ? new type.Venue(data.venue) : undefined
		this.location = data.location ? new type.Location(data.location) : undefined
		this.new_chat_members = data.new_chat_members
			? data.new_chat_members.map((x) => new type.User(x))
			: undefined
		this.left_chat_member = data.left_chat_member ? new type.User(data.left_chat_member) : undefined
		this.new_chat_title = data.new_chat_title
		this.new_chat_photo = data.new_chat_photo
			? data.new_chat_photo.map((x) => new type.PhotoSize(x))
			: undefined
		this.delete_chat_photo = data.delete_chat_photo
		this.group_chat_created = data.group_chat_created
		this.supergroup_chat_created = data.supergroup_chat_created
		this.channel_chat_created = data.channel_chat_created
		this.message_auto_delete_timer_changed = data.message_auto_delete_timer_changed
			? new type.MessageAutoDeleteTimerChanged(data.message_auto_delete_timer_changed)
			: undefined
		this.migrate_to_chat_id = data.migrate_to_chat_id
		this.migrate_from_chat_id = data.migrate_from_chat_id
		this.pinned_message = data.pinned_message ? new type.Message(data.pinned_message) : undefined
		this.invoice = data.invoice ? new type.Invoice(data.invoice) : undefined
		this.successful_payment = data.successful_payment
			? new type.SuccessfulPayment(data.successful_payment)
			: undefined
		this.connected_website = data.connected_website
		this.passport_data = data.passport_data ? new type.PassportData(data.passport_data) : undefined
		this.proximity_alert_triggered = data.proximity_alert_triggered
			? new type.ProximityAlertTriggered(data.proximity_alert_triggered)
			: undefined
		this.voice_chat_scheduled = data.voice_chat_scheduled
			? new type.VoiceChatScheduled(data.voice_chat_scheduled)
			: undefined
		this.voice_chat_started = data.voice_chat_started
			? new type.VoiceChatStarted(data.voice_chat_started)
			: undefined
		this.voice_chat_ended = data.voice_chat_ended
			? new type.VoiceChatEnded(data.voice_chat_ended)
			: undefined
		this.voice_chat_participants_invited = data.voice_chat_participants_invited
			? new type.VoiceChatParticipantsInvited(data.voice_chat_participants_invited)
			: undefined

		this.video_chat_scheduled = data.video_chat_scheduled
			? new type.VoiceChatScheduled(data.video_chat_scheduled)
			: undefined
		this.video_chat_started = data.video_chat_started
			? new type.VoiceChatStarted(data.video_chat_started)
			: undefined
		this.video_chat_ended = data.video_chat_ended
			? new type.VoiceChatEnded(data.video_chat_ended)
			: undefined
		this.video_chat_participants_invited = data.video_chat_participants_invited
			? new type.VoiceChatParticipantsInvited(data.video_chat_participants_invited)
			: undefined

		this.reply_markup = data.reply_markup
			? new type.InlineKeyboardMarkup(data.reply_markup)
			: undefined
		
		this.web_app_data = data.web_app_data ? new type.WebAppData(data.web_app_data) : undefined
	}
}
