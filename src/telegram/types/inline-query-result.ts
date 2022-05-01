import { InlineKeyboardMarkup, InputMessageContent, MessageEntity, Num, ParseMode, Str, Url } from '../types'


export declare type InlineQueryResultArticle = {
	type: 'article'
	id: Str
	title: Str
	input_message_content: InputMessageContent
	reply_markup?: InlineKeyboardMarkup
	url?: Str
	hide_url?: Url
	description	?: Str
	thumb_url?: Str
	thumb_width?: Num
	thumb_height?: Num
}

export declare type InlineQueryResultPhoto = {
	type: 'photo'
	id: Str
	photo_url: Url
	thumb_url: Url
	photo_width?: Num
	photo_height?: Num
	title: Str
	description?: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	input_message_content: InputMessageContent
	reply_markup?: InlineKeyboardMarkup
}

export declare type InlineQueryResultGif = {
	type: 'gif'
	id: Str
	gif_url	: Url
	gif_width?: Num
	gif_height?: Num
	gif_duration?: Num
	thumb_url?: Url
	thumb_mime_type?: 'image/jpeg'| 'image/gif' | 'video/mp4'
	title: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	input_message_content: InputMessageContent
	reply_markup?: InlineKeyboardMarkup
}

export declare type InlineQueryResultMpeg4Gif = {
	type: 'mpeg4_gif'
	id: Str
	mpeg4_url: Url
	mpeg4_width?: Num
	mpeg4_height?: Num
	mpeg4_duration?: Num
	thumb_url?: Url
	thumb_mime_type?: 'image/jpeg'| 'image/gif' | 'video/mp4'
	title: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	input_message_content: InputMessageContent
	reply_markup?: InlineKeyboardMarkup
}

export declare type InlineQueryResultVideo = {
	type: 'video'
	id: Str
	video_url: Url
	mime_type: 'text/html' | 'video/mp4'
	thumb_url: Url
	title: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	video_width?: Num
	video_height?: Num
	video_duration?: Num
	description?: Str
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
}

export declare type InlineQueryResultAudio = {
	type: 'audio'
	id: Str
	audio_url: Url
	title: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	performer?: Str
	audio_duration?: Num
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
}

export declare type InlineQueryResultVoice = {
	type: 'voice'
	id: Str
	voice_url: Url
	title: Str
	caption?:  Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	voice_duration?: Num
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
}

export declare type InlineQueryResultDocument = {
	type: 'document'
	id: Str
	title: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	document_url: Url
	mime_type: 'application/pdf' | 'application/zip'
	description?: Str
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
	thumb_url?: Str
	thumb_width?: Num
	thumb_height?: Num
}

export declare type InlineQueryResultLocation = {
	type: 'location'
	id: Str
	latitude: Num
	longitude: Num
	title: Str
	horizontal_accuracy?: Num
	live_period?: Num
	heading?: Num
	proximity_alert_radius?: Num
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
	thumb_url?: Url
	thumb_width?: Num
	thumb_height?: Num
}

export declare type InlineQueryResultVenue = {
	type: 'venue'
	id: Str
	latitude: Num
	longitude: Num
	title: Str
	address: Str
	foursquare_id?: Str
	foursquare_type?: Str
	google_place_id	?: Str
	google_place_type?: Str
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
	thumb_url?: Url
	thumb_width?: Num
	thumb_height?: Num
}

export declare type InlineQueryResultContact = {
	type: 'contact'
	id: Str
	phone_number: Str
	first_name: Str
	last_name?: Str
	vcard?: Str
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
	thumb_url?: Url
	thumb_width?: Num
	thumb_height?: Num
}

export declare type InlineQueryResultGame = {
	type: 'game'
	id: Str
	game_short_name: Str
	reply_markup?: InlineKeyboardMarkup
}

export declare type InlineQueryResultCachedPhoto = {
	type: 'photo'
	id: Str
	photo_file_id: Str
	title?: Str
	description?: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
}


export declare type InlineQueryResultCachedGif = {
	type: 'gif'
	id: Str
	gif_file_id: Str
	title?: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
}

export declare type InlineQueryResultCachedMpeg4Gif = {
	type: 'mpeg4_gif'
	id: Str
	mpeg4_file_id: Str
	title?: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
}


export declare type InlineQueryResultCachedSticker = {
	type: 'sticker'
	id: Str
	sticker_file_id: Str
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
}


export declare type InlineQueryResultCachedDocument = {
	type: 'document'
	id: Str
	document_file_id: Str
	title?: Str
	description?: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
	thumb_url?: Url
	thumb_width?: Num
	thumb_height?: Num
}

export declare type InlineQueryResultCachedVideo = {
	type: 'video'
	id: Str
	video_file_id: Str
	title?: Str
	description?: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
	thumb_url?: Url
	thumb_width?: Num
	thumb_height?: Num
}


export declare type InlineQueryResultCachedVoice = {
	type: 'voice'
	id: Str
	voice_file_id: Str
	title?: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
}


export declare type InlineQueryResultCachedAudio = {
	type: 'audio'
	id: Str
	audio_file_id: Str
	title?: Str
	caption?: Str
	parse_mode?: ParseMode
	caption_entities?: MessageEntity[]
	reply_markup?: InlineKeyboardMarkup
	input_message_content?: InputMessageContent
}



export declare type InlineQueryResult = InlineQueryResultArticle
	| InlineQueryResultPhoto
	| InlineQueryResultGif
	| InlineQueryResultMpeg4Gif
	| InlineQueryResultVideo
	| InlineQueryResultAudio
	| InlineQueryResultVenue
	| InlineQueryResultLocation
	| InlineQueryResultVoice
	| InlineQueryResultDocument
	| InlineQueryResultContact
	| InlineQueryResultGame
	| InlineQueryResultCachedPhoto
	| InlineQueryResultCachedGif
	| InlineQueryResultCachedMpeg4Gif
	| InlineQueryResultCachedSticker
	| InlineQueryResultCachedDocument
	| InlineQueryResultCachedVideo
	| InlineQueryResultCachedVoice
	| InlineQueryResultCachedAudio