import { AxiosInstance, AxiosResponse } from 'axios'
import * as type from './types'
import Logger from '../logger'
import { serialize } from './object-to-form-data'
import Type from './types/type'


class Methods {
	private http_client: AxiosInstance
	constructor(AxiosClient: AxiosInstance) {
		this.http_client = AxiosClient
	}

	ready_data = (data: type.data = {}) => {
		let has_file = false

		for (const key in data) {
			if (data[key] instanceof type.InputFile) {
				has_file = true
			} else {
				if (data[key] !== undefined && data[key] !== null) {
					if (!has_file) {
						data[key] = data[key] instanceof Type ? data[key].toObject() : data[key]
					}
				} else {
					delete data[key]
				}
			}
		}

		return {data, has_file}
	}

	sync_call = (method: type.MethodNames, _data: type.data = {}): Promise<AxiosResponse<type.response<any>>> => {
		const { data, has_file } = this.ready_data(_data)

		let result
		if (has_file) {
			const form_data = serialize(data)
			result = this
				.http_client
				.post(
					method,
					form_data,
					{
						headers: {
							...form_data.getHeaders(),
							'Content-Type': 'application/x-www-form-urlencoded'
						},
					}
				)
		}

		if (!has_file) {
			result = this
				.http_client
				.post(
					method,
					data,
					{
						headers: {
							'Content-Type': 'application/json'
						},
					}
				)
		}

		if (!result) {
			throw Error(
				'Can\'t call method, no result from request which is not expected since has_file can either be true or false.'
				+ '\nThe only way you can get to this error is living in the feature! =)'
			)
		}

		Logger.tag(['[Telegram]', `${method}`, '[Sent]']).debug(`${method}`, data, 'Async call is sent.')
		return result
	}

	async_call = async (method: type.MethodNames, _data: type.data = {}): Promise<type.response<any>> => {
		const result = await this.sync_call(method, _data)

		if (!result) {
			throw Error(
				'Can\'t call method, no result from request which is not expected since has_file can either be true or false.'
				+ '\nThe only way you can get to this error is living in the feature! =)'
			)
		}

		Logger.tag(['[Telegram]', `${method}`, '[Received]']).debug(`${method}`, result.data)
		return result.data
	}

	/** default call method
	 *
	 * @param method {type.MethodNames}
	 * @param _data {type.data} - data for the method
	 * @returns {Promise<type.response<any>>}
	 */
	call = async (method: type.MethodNames, _data: type.data = {}): Promise<type.response<any>> => {
		if (globalThis.config.error_handle) {
			try {
				return await this.async_call(method, _data)
			} catch (e) {
				Logger.tag(['[Telegram]', `${method}`]).debug(`${e}`, _data)
			}

			return { ok: false, result: { error_code: -1, description: 'Unknown error' } }
		}

		return await this.async_call(method, _data)
	}

	/** GetUpdates
	 *
	 * Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.
	 *
	 * @param offset {type.Number} - Identifier of the first update to be returned.
	 * @param timeout {type.Number} - Timeout in seconds for long polling.
	 * @param limit {type.Number} - Limits the number of updates to be retrieved.
	 * @param allowed_updates {type.AllowedUpdates[]} - List the types of updates you want your bot to receive.
	 * @returns {Promise<type.response<type.JsonUpdate[]>>}
	 * @see https://core.telegram.org/bots/api#getupdates
	 * @see https://core.telegram.org/bots/api#update
	 * @see https://core.telegram.org/bots/api#allowed-updates
	 */
	getUpdates = (
		offset: type.Number = 0,
		timeout: type.Number = 120,
		limit: type.Number = 100,
		allowed_updates: type.AllowedUpdates[] = type.CURRENT_UPDATE_TYPES,
	): Promise<type.response<type.JsonUpdate[]>> => this.call('getUpdates', { offset, timeout, limit, allowed_updates })

	/**
	 *
	 * Use this method to specify a url and receive incoming updates via an outgoing webhook.
	 * Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url,
	 * containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts.
	 * Returns True on success. If you'd like to make sure that the Webhook request comes from Telegram,
	 * we recommend using a secret path in the URL, e.g. https://www.example.com/<token>.
	 * Since nobody else knows your bot's token, you can be pretty sure it's us.
	 *
	 * @param url {type.String} - HTTPS url to send updates to. Use an empty string to remove webhook integration
	 * @param certificate? {@file} - Upload your public key certificate so that the root certificate in use can be checked.
	 * @param ip_address {type.String} - The fixed IP address which will be used to send webhook requests instead of the IP address
	 * @param max_connections {type.Number} - Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100.
	 * @param allowed_updates {type.AllowedUpdates[]} - List the types of updates you want your bot to receive.
	 * @param drop_pending_updates {type.Boolean} - Pass True, if the current webhook status should be dropped and the old one dropped.
	 * @returns {Promise<type.Response<any>>}
	 * @see https://core.telegram.org/bots/api#setwebhook
	 * @see https://core.telegram.org/bots/api#update
	 * @see https://core.telegram.org/bots/api#allowed-updates
	 * @see https://core.telegram.org/bots/api#certificate
	 * @see https://core.telegram.org/bots/api#ip-address
	 * @see https://core.telegram.org/bots/api#max-connections
	 * @see https://core.telegram.org/bots/api#drop-pending-updates
	 * @see https://core.telegram.org/bots/api#webhook-info
	 */
	setWebhook = (
		url: type.String,
		ip_address: type.String,
		max_connections: type.Number,
		allowed_updates: type.AllowedUpdates[],
		drop_pending_updates: type.Boolean,
		certificate?: type.InputFile,
	): Promise<type.response<any>> => this.call('setWebhook', { url, certificate, ip_address, max_connections, allowed_updates, drop_pending_updates })

	/** Delete Web Hook
	 * Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success.
	 *
	 * @param drop_pending_updates {type.Boolean} - Pass True to drop all pending updates.
	 * @returns {Promise<type.Response<any>>}
	 * @see https://core.telegram.org/bots/api#deletewebhook
	 * @see https://core.telegram.org/bots/api#webhook-info
	 */
	deleteWebhook = (
		drop_pending_updates: type.Boolean,
	): Promise<type.response<any>> => this.call('deleteWebhook', { drop_pending_updates })

	/** Web Hook Info
	 * Use this method to get current webhook status.
	 * Requires no parameters.
	 * On success, returns a WebhookInfo object.
	 * If the bot is using getUpdates,
	 * will return an object with the url field empty.
	 *
	 * @returns {Promise<type.response<type.WebhookInfo>>}
	 * @see https://core.telegram.org/bots/api#getwebhookinfo
	 */
	getWebhookInfo = (): Promise<type.response<type.WebhookInfo>> => this.call('getWebhookInfo')


	/** Get Me
	 * A simple method for testing your bot's authentication token.
	 * Requires no parameters.
	 * Returns basic information about the bot in form of a User object.
	 *
	 * @returns {Promise<type.User>}
	 * @see https://core.telegram.org/bots/api#getme
	 * @see https://core.telegram.org/bots/api#user
	 */
	getMe = (): Promise<type.User> => this.call('getMe').then(r => new type.User(r.result))

	/** Logout
	 * Use this method to log out from the cloud Bot API server before launching the bot locally.
	 * You must log out the bot before running it locally,
	 * otherwise there is no guarantee that the bot will receive updates.
	 * After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes.
	 * Returns True on success. Requires no parameters.
	 *
	 * @returns {Promise<type.response<any>>}
	 * @see https://core.telegram.org/bots/api#logout
	 */
	logout = (): Promise<type.response<any>> => this.call('logout')

	/** Close
	 * Use this method to close the bot instance before moving it from one local server to another.
	 * You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart.
	 * The method will return error 429 in the first 10 minutes after the bot is launched.
	 * Returns True on success.
	 * Requires no parameters.
	 *
	 * @returns {Promise<type.response<any>>}
	 * @see https://core.telegram.org/bots/api#close
	 */
	close = (): Promise<type.response<any>> => this.call('close')

	/**
	 * Use this method to send text messages. On success, the sent Message is returned.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param text {type.String} - Text of the message to be sent
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param parse_mode? {type.ParseMode} - Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param entities? {type.MessageEntity[]|type.ArrayObject} - List of special entities that appear in message text,
	 * @param disable_web_page_preview? {type.Boolean} - Disables link previews for links in this message
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @returns {Promise<type.Message>}
	 */
	sendMessage = (
		chat_id: type.ChatId,
		text: type.Str,
		reply_to_message_id?: type.MessageId,
		parse_mode?: type.ParseMode,
		reply_markup?: type.ReplyMarkup,
		entities?: type.MessageEntity[]|type.ArrayObject,
		disable_web_page_preview?: type.Bool,
		disable_notification?: type.Bool,
		protect_content?: type.Bool,
		allow_sending_without_reply?: type.Bool,
	): Promise<type.Message> => this.call('sendMessage', {
		chat_id,
		text,
		reply_to_message_id,
		parse_mode,
		entities,
		disable_web_page_preview,
		disable_notification,
		protect_content,
		reply_markup,
		allow_sending_without_reply
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to forward messages of any kind.
	 * Service messages can't be forwarded.
	 * On success,
	 * the sent Message is returned.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param from_chat_id {type.ChatId} - Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
	 * @param message_id {type.MessageId} - Unique message identifier
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @returns {Promise<type.Message>}
	 */
	forwardMessage = (
		chat_id: type.ChatId,
		from_chat_id: type.ChatId,
		message_id:  type.MessageId,
		protect_content?: type.Bool,
		disable_notification?: type.Bool,
	): Promise<type.Message> => this.call('forwardMessage', {
		chat_id,
		from_chat_id,
		message_id,
		disable_notification,
		protect_content,
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to copy messages of any kind.
	 * Service messages and invoice messages can't be copied.
	 * The method is analogous to the method forwardMessage,
	 * but the copied message doesn't have a link to the original message.
	 * Returns the MessageId of the sent message on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param from_chat_id {type.ChatId} - Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
	 * @param message_id {type.MessageId} - Unique message identifier
	 * @param caption? {type.String} - Caption of the message to be sent, 0-1024 characters
	 * @param parse_mode? {type.ParseMode} - Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param caption_entities? {type.MessageEntity[]|type.ArrayObject} - List of special entities that appear in message text,
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @returns {Promise<{message_id: type.MessageId}>}
	 */
	copyMessage = (
		chat_id: type.ChatId,
		from_chat_id: type.ChatId,
		message_id: type.MessageId,
		reply_to_message_id?: type.MessageId,
		allow_sending_without_reply?: type.Bool,
		caption?: type.String,
		parse_mode?: type.ParseMode,
		caption_entities?: type.MessageEntity[]|type.ArrayObject,
		protect_content?: type.Bool,
		disable_notification?: type.Bool,
		reply_markup?: type.ReplyMarkup,
	): Promise<{message_id: type.MessageId}> => this.call('copyMessage', {
		chat_id,
		from_chat_id,
		message_id,
		disable_notification,
		protect_content,
		caption_entities,
		parse_mode,
		caption,
		reply_markup,
		allow_sending_without_reply,
		reply_to_message_id,
	}).then(r => r.result)


	/**
	 * Use this method to send photos.
	 * On success,
	 * the sent Message is returned.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param photo {type.FileId | type.InputFile | type.Str} - Photo to send.
	 * @param caption? {type.String} - Caption of the message to be sent, 0-1024 characters
	 * @param parse_mode? {type.ParseMode} - Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param caption_entities? {type.MessageEntity[]|type.ArrayObject} - List of special entities that appear in message text,
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @returns {Promise<{type.Message}>}
	 */
	sendPhoto = (
		chat_id: type.ChatId,
		photo: type.FileId | type.InputFile | type.Str,
		caption?: type.Str,
		reply_to_message_id?: type.MessageId,
		parse_mode?: type.ParseMode,
		disable_notification?: type.Bool,
		reply_markup?: type.ReplyMarkup,
		allow_sending_without_reply?: type.Bool,
		caption_entities?: type.MessageEntity[]|type.ArrayObject,
		protect_content?: type.Bool,
	): Promise<type.Message> => this.call('sendPhoto', {
		chat_id,
		photo,
		caption,
		parse_mode,
		disable_notification,
		reply_to_message_id,
		reply_markup,
		allow_sending_without_reply,
		caption_entities,
		protect_content,
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to send audio files,
	 * if you want Telegram clients to display them in the music player.
	 * Your audio must be in the .MP3 or .M4A format. On success,
	 * the sent Message is returned.
	 * Bots can currently send audio files of up to 50 MB in size,
	 * this limit may be changed in the future.
	 * For sending voice messages, use the sendVoice method instead.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param audio {type.FileId | type.InputFile | type.Str} - Audio file to send.
	 * @param caption? {type.String} - Caption of the message to be sent, 0-1024 characters
	 * @param parse_mode? {type.ParseMode} - Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param caption_entities? {type.MessageEntity[]|type.ArrayObject} - List of special entities that appear in message text,
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @param duration? {type.Num} - Duration of the audio in seconds
	 * @param performer? {type.Str} - Performer
	 * @param title? {type.Str} - Track name
	 * @param thumb? {type.FileId | type.InputFile | type.Str} - Thumbnail of the file sent.
	 * @returns {Promise<{type.Message}>}
	 */
	sendAudio = (
		chat_id: type.ChatId,
		audio: type.FileId | type.InputFile | type.Str,
		caption?: type.Str,
		reply_to_message_id?: type.MessageId,
		duration?: type.Num,
		performer?: type.Str,
		title?: type.Str,
		thumb?: type.FileId | type.InputFile | type.Str,
		parse_mode?: type.ParseMode,
		disable_notification?: type.Bool,
		reply_markup?: type.ReplyMarkup,
		allow_sending_without_reply?: type.Bool,
		caption_entities?: type.MessageEntity[]|type.ArrayObject,
		protect_content?: type.Bool,
	): Promise<type.Message> => this.call('sendAudio', {
		chat_id,
		audio,
		caption,
		parse_mode,
		disable_notification,
		reply_to_message_id,
		reply_markup,
		allow_sending_without_reply,
		caption_entities,
		protect_content,
		duration,
		performer,
		title,
		thumb,
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to send general files.
	 * On success, the sent Message is returned.
	 * Bots can currently send files of any type of up to 50 MB in size,
	 * this limit may be changed in the future.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param document {type.FileId | type.InputFile | type.Str} - Document to send.
	 * @param caption? {type.String} - Caption of the message to be sent, 0-1024 characters
	 * @param parse_mode? {type.ParseMode} - Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param caption_entities? {type.MessageEntity[]|type.ArrayObject} - List of special entities that appear in message text,
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @param thumb? {type.FileId | type.InputFile | type.Str} - Thumbnail of the file sent.
	 * @returns {Promise<{type.Message}>}
	 */
	sendDocument = (
		chat_id: type.ChatId,
		document: type.FileId | type.InputFile | type.Str,
		caption?: type.Str,
		reply_to_message_id?: type.MessageId,
		parse_mode?: type.ParseMode,
		disable_notification?: type.Bool,
		reply_markup?: type.ReplyMarkup,
		allow_sending_without_reply?: type.Bool,
		caption_entities?: type.MessageEntity[]|type.ArrayObject,
		protect_content?: type.Bool,
		disable_content_type_detection?: type.Bool,
		thumb?: type.FileId | type.InputFile | type.Str,
	): Promise<type.Message> => this.call('sendDocument', {
		chat_id,
		document,
		caption,
		parse_mode,
		disable_notification,
		reply_to_message_id,
		reply_markup,
		allow_sending_without_reply,
		caption_entities,
		protect_content,
		disable_content_type_detection,
		thumb
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to send video files,
	 * Telegram clients support mp4 videos (other formats may be sent as Document).
	 * On success, the sent Message is returned.
	 * Bots can currently send video files of up to 50 MB in size,
	 * this limit may be changed in the future.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param video {type.FileId | type.InputFile | type.Str} - Video to send.
	 * @param caption? {type.String} - Caption of the video to be sent, 0-1024 characters
	 * @param parse_mode? {type.ParseMode} - Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param duration? {type.Num} - Duration of sent video in seconds
	 * @param width? {type.Num} - Video width
	 * @param height? {type.Num} - Video height
	 * @param thumb? {type.FileId | type.InputFile | type.Str} - Thumbnail of the file sent.
	 * @param caption_entities? {type.MessageEntity[]|type.ArrayObject} - List of special entities that appear in message text,
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @param supports_streaming? {type.Boolean} - Pass True, if the uploaded video is suitable for streaming
	 * @returns {Promise<{type.Message}>}
	 */
	sendVideo = (
		chat_id: type.ChatId,
		video: type.FileId | type.InputFile | type.Str,
		caption?: type.Str,
		reply_to_message_id?: type.MessageId,
		parse_mode?: type.ParseMode,
		disable_notification?: type.Bool,
		reply_markup?: type.ReplyMarkup,
		allow_sending_without_reply?: type.Bool,
		caption_entities?: type.MessageEntity[]|type.ArrayObject,
		protect_content?: type.Bool,
		supports_streaming?: type.Bool,
		thumb?: type.FileId | type.InputFile | type.Str,
		duration?: type.Num,
		width?: type.Num,
		height?: type.Num,
	): Promise<type.Message> => this.call('sendVideo', {
		chat_id,
		video,
		caption,
		parse_mode,
		disable_notification,
		reply_to_message_id,
		reply_markup,
		allow_sending_without_reply,
		caption_entities,
		protect_content,
		supports_streaming,
		duration,
		width,
		height,
		thumb
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound).
	 * On success, the sent Message is returned.
	 * Bots can currently send animation files of up to 50 MB in size,
	 * this limit may be changed in the future.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param animation {type.FileId | type.InputFile | type.Str} - Animation to send.
	 * @param caption? {type.String} - Caption of the animation to be sent, 0-1024 characters
	 * @param parse_mode? {type.ParseMode} - Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param duration? {type.Num} - Duration of sent Animation in seconds
	 * @param width? {type.Num} - Animation width
	 * @param height? {type.Num} - Animation height
	 * @param thumb? {type.FileId | type.InputFile | type.Str} - Thumbnail of the file sent.
	 * @param caption_entities? {type.MessageEntity[]|type.ArrayObject} - List of special entities that appear in message text,
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @returns {Promise<{type.Message}>}
	 */
	sendAnimation = (
		chat_id: type.ChatId,
		animation: type.FileId | type.InputFile | type.Str,
		caption?: type.Str,
		reply_to_message_id?: type.MessageId,
		parse_mode?: type.ParseMode,
		disable_notification?: type.Bool,
		reply_markup?: type.ReplyMarkup,
		allow_sending_without_reply?: type.Bool,
		caption_entities?: type.MessageEntity[]|type.ArrayObject,
		protect_content?: type.Bool,
		thumb?: type.FileId | type.InputFile | type.Str,
		duration?: type.Num,
		width?: type.Num,
		height?: type.Num,
	): Promise<type.Message> => this.call('sendAnimation', {
		chat_id,
		animation,
		caption,
		parse_mode,
		disable_notification,
		reply_to_message_id,
		reply_markup,
		allow_sending_without_reply,
		caption_entities,
		protect_content,
		duration,
		width,
		height,
		thumb
	}).then(r => new type.Message(r.result))

	/**
	 * Use this method to send audio files,
	 * if you want Telegram clients to display the file as a playable voice message.
	 * For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document).
	 * On success,
	 * the sent Message is returned.
	 * Bots can currently send voice messages of up to 50 MB in size,
	 * this limit may be changed in the future.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param voice {type.FileId | type.InputFile | type.Str} - Voice to send.
	 * @param caption? {type.String} - Caption of the Voice to be sent, 0-1024 characters
	 * @param parse_mode? {type.ParseMode} - Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param caption_entities? {type.MessageEntity[]|type.ArrayObject} - List of special entities that appear in message text,
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @returns {Promise<{type.Message}>}
	 */
	sendVoice = (
		chat_id: type.ChatId,
		voice: type.FileId | type.InputFile | type.Str,
		caption?: type.Str,
		reply_to_message_id?: type.MessageId,
		parse_mode?: type.ParseMode,
		disable_notification?: type.Bool,
		reply_markup?: type.ReplyMarkup,
		allow_sending_without_reply?: type.Bool,
		caption_entities?: type.MessageEntity[]|type.ArrayObject,
		protect_content?: type.Bool,
	): Promise<type.Message> => this.call('sendVoice', {
		chat_id,
		voice,
		caption,
		parse_mode,
		disable_notification,
		reply_to_message_id,
		reply_markup,
		allow_sending_without_reply,
		caption_entities,
		protect_content,
	}).then(r => new type.Message(r.result))


	/**
	 * As of v.4.0,
	 * Telegram clients support rounded square mp4 videos of up to 1 minute long.
	 * Use this method to send video messages.
	 * On success, the sent Message is returned.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param video_note {type.FileId | type.InputFile | type.Str} - Video note to send
	 * @param caption? {type.String} - Caption of the Video note to be sent, 0-1024 characters
	 * @param parse_mode? {type.ParseMode} - Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param caption_entities? {type.MessageEntity[]|type.ArrayObject} - List of special entities that appear in message text,
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @param thumb? {type.FileId | type.InputFile | type.Str} - Thumbnail of the file sent;
	 * @param duration? {type.Num} - Duration of sent video in seconds
	 * @param length? {type.Num} - Video width and height,
	 * @returns {Promise<{type.Message}>}
	 */
	sendVideoNote = (
		chat_id: type.ChatId,
		video_note: type.FileId | type.InputFile | type.Str,
		caption?: type.Str,
		duration?: type.Num,
		length?: type.Num,
		thumb?: type.FileId | type.InputFile | type.Str,
		reply_to_message_id?: type.MessageId,
		parse_mode?: type.ParseMode,
		disable_notification?: type.Bool,
		reply_markup?: type.ReplyMarkup,
		allow_sending_without_reply?: type.Bool,
		caption_entities?: type.MessageEntity[]|type.ArrayObject,
		protect_content?: type.Bool,
	): Promise<type.Message> => this.call('sendVideoNote', {
		chat_id,
		video_note,
		caption,
		parse_mode,
		disable_notification,
		reply_to_message_id,
		reply_markup,
		allow_sending_without_reply,
		caption_entities,
		protect_content,
		duration,
		length,
		thumb
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to send a group of photos, videos,
	 * documents or audios as an album.
	 * Documents and audio files can be only grouped in an album with messages of the same type.
	 * On success,
	 * an array of Messages that were sent is returned.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param media {[type.InputMedia, type.InputMedia, type.InputMedia?, type.InputMedia?, type.InputMedia?, type.InputMedia?, type.InputMedia?, type.InputMedia?, type.InputMedia?, type.InputMedia?]} - A JSON-serialized array describing messages to be sent, must include 2-10 items
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @returns {Promise<{type.Message[]}>}
	 */
	sendMediaGroup = (
		chat_id: type.ChatId,
		media: [type.InputMedia, type.InputMedia, type.InputMedia?, type.InputMedia?, type.InputMedia?, type.InputMedia?, type.InputMedia?, type.InputMedia?, type.InputMedia?, type.InputMedia?],
		disable_notification?: type.Bool,
		allow_sending_without_reply?: type.Bool,
		reply_to_message_id?: type.MessageId,
		protect_content?: type.Bool,
	): Promise<type.Message[]> => this.call('sendMediaGroup', {
		chat_id,
		media,
		disable_notification,
		allow_sending_without_reply,
		reply_to_message_id,
		protect_content,
	}).then(r => r.result.map( (v: type.JsonMessage ) => new type.Message(v)))

	/**
	 * Use this method to send point on the map.
	 * On success, the sent Message is returned.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param latitude {type.Num} - Latitude of the location
	 * @param longitude {type.Num} - Longitude of the location
	 * @param horizontal_accuracy? {type.Num} - The radius of uncertainty for the location, measured in meters; 0-1500
	 * @param live_period? {type.Num} - Period in seconds for which the location will be updated
	 * @param heading? {type.Num} - For live locations, a direction in which the user is moving, in degrees.
	 * @param proximity_alert_radius? {type.Num} - For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters.
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param protect_content? {type.Boolean} - If set to True, the message will be sent even if the specified replied-to message is not found
	 * @param disable_notification? {type.Boolean} - Sends the message silently. Users will receive a notification with no sound.
	 * @param allow_sending_without_reply? {type.Boolean} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @returns {Promise<{type.Message}>}
	 */
	sendLocation = (
		chat_id: type.ChatId,
		latitude: type.Num,
		longitude: type.Num,
		horizontal_accuracy?: type.Num,
		live_period?: type.Num,
		heading?: type.Num,
		proximity_alert_radius?: type.Num,
		disable_notification?: type.Bool,
		allow_sending_without_reply?: type.Bool,
		reply_to_message_id?: type.MessageId,
		protect_content?: type.Bool,
		reply_markup?: type.ReplyMarkup
	): Promise<type.Message> => this.call('sendLocation', {
		chat_id,
		latitude,
		longitude,
		horizontal_accuracy,
		live_period,
		heading,
		proximity_alert_radius,
		disable_notification,
		allow_sending_without_reply,
		reply_to_message_id,
		protect_content,
		reply_markup,
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to edit live location messages.
	 * A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation.
	 * On success, if the edited message is not an inline message,
	 * the edited Message is returned,
	 * otherwise True is returned.
	 *
	 * @param latitude {type.Num} - Latitude of the location
	 * @param longitude {type.Num} - Longitude of the location
	 * @param horizontal_accuracy? {type.Num} - The radius of uncertainty for the location, measured in meters; 0-1500
	 * @param heading {type.Num} - For live locations, a direction in which the user is moving, in degrees.
	 * @param proximity_alert_radius? {type.Num} - For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters.
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @param message_id? {type.MessageId} - Required if inline_message_id is not specified. Identifier of the sent message
	 * @param inline_message_id? {type.String} - Required if chat_id and message_id are not specified. Identifier of the inline message
	 * @param chat_id? {type.ChatId} - Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @returns {Promise<{type.Message|type.Bool}>}
	 */
	editMessageLiveLocation = (
		latitude: type.Num,
		longitude: type.Num,
		chat_id?: type.ChatId,
		message_id?: type.MessageId,
		inline_message_id?: type.Str,
		horizontal_accuracy?: type.Num,
		proximity_alert_radius?: type.Num,
		heading?: type.Num,
		reply_markup?: type.ReplyMarkup
	): Promise<type.Message|type.Bool> => this.call('editMessageLiveLocation', {
		chat_id,
		message_id,
		inline_message_id,
		latitude,
		longitude,
		horizontal_accuracy,
		heading,
		proximity_alert_radius,
		reply_markup,
	}).then(r => typeof r.result == 'boolean' ? r.result : new type.Message(r.result))


	/**
	 * Use this method to edit live location messages.
	 * A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation.
	 * On success, if the edited message is not an inline message,
	 * the edited Message is returned,
	 * otherwise True is returned.
	 *
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @param message_id? {type.MessageId} - Required if inline_message_id is not specified. Identifier of the sent message
	 * @param inline_message_id? {type.String} - Required if chat_id and message_id are not specified. Identifier of the inline message
	 * @param chat_id? {type.ChatId} - Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @returns {Promise<{type.Message|type.Bool}>}
	 */
	stopMessageLiveLocation = (
		chat_id?: type.ChatId,
		message_id?: type.MessageId,
		inline_message_id?: type.Str,
		reply_markup?: type.ReplyMarkup
	): Promise<type.Message|type.Bool> => this.call('stopMessageLiveLocation', {
		chat_id,
		message_id,
		inline_message_id,
		reply_markup,
	}).then(r => typeof r.result == 'boolean' ?  r.result : new type.Message(r.result))


	/**
	 * Use this method to send information about a venue.
	 * On success, the sent Message is returned.
	 * =
	 * @param chat_id {type.ChatId} - Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param latitude {type.Num} - Latitude of the venue
	 * @param longitude {type.Num} - Longitude of the venue
	 * @param title {type.String} - Name of the venue
	 * @param address {type.String} - Address of the venue
	 * @param foursquare_id {type.String} - Foursquare identifier of the venue
	 * @param foursquare_type {type.String} - Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
	 * @param google_place_id {type.String} - Google Place identifier of the venue
	 * @param google_place_type {type.String} - Google Place type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
	 * @param disable_notification? {type.Bool} - Sends the message silently. Users will receive a notification with no sound.
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param allow_sending_without_reply? {type.Bool} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @param protect_content? {type.Bool} - Pass True, if the message content should be protected from replay
	 * @returns {Promise<{type.Message}>}
	 */
	sendVenue = (
		chat_id: type.ChatId,
		latitude: type.Num,
		longitude: type.Num,
		title: type.String,
		address: type.String,
		foursquare_id?: type.String,
		foursquare_type?: type.String,
		google_place_id?: type.String,
		google_place_type?: type.String,
		reply_to_message_id?: type.MessageId,
		reply_markup?: type.ReplyMarkup,
		disable_notification?: type.Bool,
		protect_content?: type.Bool,
		allow_sending_without_reply?: type.Bool,
	): Promise<type.Message> => this.call('sendVenue', {
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
		allow_sending_without_reply,
		reply_to_message_id,
		reply_markup,
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to send phone contacts.
	 * On success, the sent Message is returned.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel in the format channelusername
	 * @param phone_number {type.String} - Contact's phone number
	 * @param first_name {type.String} - Contact's first name
	 * @param last_name {type.String} - Contact's last name
	 * @param vcard {type.String} - Additional data about the contact in the form of a vCard, 0-2048 bytes
	 * @param disable_notification? {type.Bool} - Sends the message silently. Users will receive a notification with no sound.
	 * @param protect_content? {type.Bool} - Pass True, if the message content should be protected from replay
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param allow_sending_without_reply? {type.Bool} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @returns {Promise<{type.Message}>}
	 */
	sendContact = (
		chat_id: type.ChatId,
		phone_number: type.String,
		first_name: type.String,
		last_name: type.String,
		vcard?: type.String,
		disable_notification?: type.Bool,
		protect_content?: type.Bool,
		reply_to_message_id?: type.MessageId,
		allow_sending_without_reply?: type.Bool,
		reply_markup?: type.ReplyMarkup,
	): Promise<type.Message> => this.call('sendContact', {
		chat_id,
		phone_number,
		first_name,
		last_name,
		vcard,
		disable_notification,
		protect_content,
		reply_to_message_id,
		allow_sending_without_reply,
		reply_markup,
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to send a native poll.
	 * On success, the sent Message is returned.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel in the format channelusername
	 * @param question {type.String} - Poll question, 1-255 characters
	 * @param options {[type.String, type.String, type.String?, type.String?, type.String?, type.String?, type.String?, type.String?, type.String?, type.String?,]} - A JSON-serialized list of answer options, 2-10 strings 1-100 characters each
	 * @param is_anonymous {type.Bool} - True, if the poll needs to be anonymous, defaults to True
	 * @param _type? {type.PollType} - Poll type, “quiz” or “regular”, defaults to “regular”
	 * @param allows_multiple_answers? {type.Bool} - True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False
	 * @param correct_option_id? {type.Num} - 0-based identifier of the correct answer option, required for polls in quiz mode
	 * @param explanation? {type.String} - Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
	 * @param explanation_parse_mode? {type.ParseMode} - Mode for parsing entities in the explanation. See formatting options for more details.
	 * @param explanation_entities? {type.MessageEntity[]|type.ArrayObject} - List of special entities that appear in the explanation, which can be specified instead of parse_mode
	 * @param open_period? {type.Num} - Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.
	 * @param close_date? {type.Num} - Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period.
	 * @param is_closed? {type.Bool} - Pass True, if the poll needs to be immediately closed
	 * @param disable_notification? {type.Bool} - Sends the message silently. Users will receive a notification with no sound.
	 * @param protect_content? {type.Bool} - Pass True, if the message content should be protected from replay
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param allow_sending_without_reply? {type.Bool} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @returns {Promise<{type.Message}>}
	 * @see https://core.telegram.org/bots/api#sendpoll
	 */
	sendPoll = (
		chat_id: type.ChatId,
		question: type.String,
		options: [type.String, type.String, type.String?, type.String?, type.String?, type.String?, type.String?, type.String?, type.String?, type.String?,],
		is_anonymous?: type.Bool,
		_type?: type.PollType,
		allows_multiple_answers?: type.Bool,
		correct_option_id?: type.Num,
		explanation?: type.String,
		explanation_parse_mode?: type.ParseMode,
		explanation_entities?: type.MessageEntity[]|type.ArrayObject,
		open_period?: type.Num,
		close_date?: type.Num,
		is_closed?: type.Bool,
		protect_content?: type.Bool,
		reply_to_message_id?: type.MessageId,
		allow_sending_without_reply?: type.Bool,
		disable_notification?: type.Bool,
		reply_markup?: type.ReplyMarkup,
	): Promise<type.Message> => this.call('sendPoll', {
		chat_id,
		question,
		options,
		is_anonymous,
		type: _type,
		allows_multiple_answers,
		disable_notification,
		correct_option_id,
		explanation,
		explanation_parse_mode,
		explanation_entities,
		open_period,
		close_date,
		is_closed,
		protect_content,
		reply_to_message_id,
		allow_sending_without_reply,
		reply_markup,
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method to send a dice, which will have a random value from 1 to 6.
	 * On success, the sent Message is returned.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel in the format channelusername
	 * @param emoji? {type.DiceType} - Emoji on which the dice throw animation is based. Currently, must be one of “🎲”, “🎯”, “🏀”, “🪂”. Dice can have values 1-6 for “🎲” and “🎯”, values 1-5 for “🏀” and “🪂”. Defaults to “🎲”
	 * @param disable_notification? {type.Bool} - Sends the message silently. Users will receive a notification with no sound.
	 * @param protect_content? {type.Bool} - Pass True, if the message content should be protected from replay
	 * @param reply_to_message_id? {type.MessageId} - If the message is a reply, ID of the original message
	 * @param allow_sending_without_reply? {type.Bool} - Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup? {type.ReplyMarkup} - Additional interface options.
	 * @returns {Promise<{type.Message}>}
	 * @see https://core.telegram.org/bots/api#senddice
	 * @see https://core.telegram.org/bots/api#message
	 * @see https://core.telegram.org/bots/api#diceemoji
	 */
	sendDice = (
		chat_id: type.ChatId,
		emoji?: type.DiceType,
		disable_notification?: type.Bool,
		protect_content?: type.Bool,
		reply_to_message_id?: type.MessageId,
		allow_sending_without_reply?: type.Bool,
		reply_markup?: type.ReplyMarkup,
	): Promise<type.Message> => this.call('sendDice', {
		chat_id,
		emoji,
		disable_notification,
		protect_content,
		reply_to_message_id,
		allow_sending_without_reply,
		reply_markup,
	}).then(r => new type.Message(r.result))


	/**
	 * Use this method when you need to tell the user that something is happening on the bot's side.
	 * The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status).
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param action {type.ChatAction} - Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_audio or upload_audio for audio files, upload_document for general files, find_location for location data, record_video_note or upload_video_note for video notes.
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#sendchataction
	 * @see https://core.telegram.org/bots/api#available-chat-actions
	 */

	sendChatAction = (
		chat_id: type.ChatId,
		action: type.ChatAction,
	): Promise<type.Bool> => this.call('sendChatAction', {
		chat_id,
		action,
	}).then(r => r.result)


	/**
	 * Use this method to get a list of profile pictures for a user.
	 *
	 * @param user_id {type.UserId} - Unique identifier of the target user
	 * @param offset? {type.Num} - Sequential number of the first photo to be returned. By default, all photos are returned.
	 * @param limit? {type.Num} - Limits the number of photos to be retrieved. Values between 1—100 are accepted. Defaults to 100.
	 * @returns {Promise<{type.UserProfilePhotos}>}
	 * @see https://core.telegram.org/bots/api#getuserprofilephotos
	 * @see https://core.telegram.org/bots/api#userprofilephotos
	 * @see https://core.telegram.org/bots/api#user
	 * @see https://core.telegram.org/bots/api#file
	 */

	getUserProfilePhotos = (
		user_id: type.UserId,
		offset?: type.Num,
		limit?: type.Num,
	): Promise<type.UserProfilePhotos> => this.call('getUserProfilePhotos', {
		user_id,
		offset,
		limit,
	}).then(r => new type.UserProfilePhotos(r.result))


	/**
	 * Use this method to get basic info about a file and prepare it for downloading.
	 * For the moment, bots can download files of up to 20MB in size.
	 * On success, a File object is returned.
	 * The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>,
	 * where <file_path> is taken from the response.
	 * It is guaranteed that the link will be valid for at least 1 hour.
	 * When the link expires, a new one can be requested by calling getFile again.
	 * Maximum file size to download is 20 MB
	 * @param file_id {type.FileId} - File identifier to get info about
	 * @returns {Promise<{type.File}>}
	 * @see https://core.telegram.org/bots/api#getfile
	 * @see https://core.telegram.org/bots/api#file
	 */

	getFile = (
		file_id: type.FileId,
	): Promise<type.File> => this.call('getFile', {
		file_id,
	}).then(r => new type.File(r.result))

	/**
	 * Use this method to kick a user from a group, a supergroup or a channel.
	 * In the case of supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
	 * Returns True on success.
	 * Note: In regular groups (non-supergroups), this method will only work if the ‘All Members Are Admins’ setting is off in the target group.
	 * Otherwise members may only be removed by the group's creator or by the member that added them.
	 * @param chat_id {type.ChatId} - Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
	 * @param user_id {type.UserId} - Unique identifier of the target user
	 * @param until_date? {type.Num} - Date when the user will be unbanned, unix time.
	 * @param revoke_messages {type.Bool} - Pass True, if the user's messages should also be deleted. DEFAULTS TO TRUE
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#kickchatmember
	 */

	kickChatMember = (
		chat_id: type.ChatId,
		user_id: type.UserId,
		until_date?: type.Num,
		revoke_messages: type.Bool = true,
	): Promise<type.Bool> => this.call('kickChatMember', {
		chat_id,
		user_id,
		until_date,
		revoke_messages,
	}).then(r => r.result)

	/**
	 * Use this method to unban a previously kicked user in a supergroup or channel.
	 * The user will not return to the group or channel automatically, but will be able to join via link, etc.
	 * The bot must be an administrator for this to work.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target group or username of the target supergroup or channel (in the format @username)
	 * @param user_id {type.UserId} - Unique identifier of the target user
	 * @param only_if_banned?: type.Bool - Pass True, if the user is previously banned and should be unbanned.
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#unbanchatmember
	 */

	unbanChatMember = (
		chat_id: type.ChatId,
		user_id: type.UserId,
		only_if_banned: type.Bool = true,
	): Promise<type.Bool> => this.call('unbanChatMember', {
		chat_id,
		user_id,
		only_if_banned,
	}).then(r => r.result)


	/**
	 * Use this method to restrict a user in a supergroup.
	 * The bot must be an administrator in the supergroup for this to work and must have the appropriate admin rights.
	 * Pass True for all boolean parameters to lift restrictions from a user.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	 * @param user_id {type.UserId} - Unique identifier of the target user
	 * @param permissions {type.ChatPermissions} - New user permissions
	 * @param until_date?: type.Num - Date when restrictions will be lifted for the user, unix time.
	 * If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#restrictchatmember
	 */

	restrictChatMember = (
		chat_id: type.ChatId,
		user_id: type.UserId,
		permissions: type.ChatPermissions,
		until_date?: type.Num,
	): Promise<type.Bool> => this.call('restrictChatMember', {
		chat_id,
		user_id,
		permissions,
		until_date,
	}).then(r => r.result)


	/**
	 * Use this method to promote or demote a user in a supergroup or a channel.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
	 * Pass False for all boolean parameters to demote a user.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param user_id {type.UserId} - Unique identifier of the target user
	 * @param is_anonymous {type.Bool} - Pass True, if the administrator's presence in the chat is hidden
	 * @param can_manage_chat {type.Bool} - Pass True, if the administrator can change chat title, photo and other settings
	 * @param can_post_messages {type.Bool} - Pass True, if the administrator can create channel posts, channels only
	 * @param can_edit_messages {type.Bool} - Pass True, if the administrator can edit messages of other users, channels only
	 * @param can_delete_messages {type.Bool} - Pass True, if the administrator can delete messages of other users
	 * @param can_manage_video_chats {type.Bool} - Pass True, if the administrator can change the chat information(title, photo, description, etc.)
	 * @param can_restrict_members {type.Bool} - Pass True, if the administrator can restrict, ban or unban chat members
	 * @param can_promote_members {type.Bool} - Pass True, if the administrator can add new administrators with a subset of his own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by him)
	 * @param can_pin_messages {type.Bool} - Pass True, if the administrator can pin messages, supergroups only
	 * @param can_invite_users {type.Bool} - Pass True, if the administrator can invite new users to the chat
	 * @param can_change_info {type.Bool} - Pass True, if the administrator can change chat title, photo and other settings
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#promotechatmember
	 */
	promoteChatMember = (
		chat_id: type.ChatId,
		user_id: type.UserId,
		is_anonymous: type.Bool = false,
		can_manage_chat: type.Bool = false,
		can_post_messages: type.Bool = false,
		can_edit_messages: type.Bool = false,
		can_delete_messages: type.Bool = false,
		can_manage_video_chats: type.Bool = false,
		can_restrict_members: type.Bool = false,
		can_promote_members: type.Bool = false,
		can_pin_messages: type.Bool = false,
		can_invite_users: type.Bool = false,
		can_change_info: type.Bool = false,
	): Promise<type.Bool> => this.call('promoteChatMember', {
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
		can_pin_messages,
		can_invite_users,
		can_change_info,
	}).then(r => r.result)

	/**
	 * Use this method to set a custom title for an administrator in a supergroup promoted by the bot.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	 * @param user_id {type.UserId} - Unique identifier of the target user
	 * @param custom_title {type.String} - New custom title for the administrator; 0-16 characters, emoji are not allowed
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#setchatadministratorcustomtitle
	 */
	setChatAdministratorCustomTitle = (
		chat_id: type.ChatId,
		user_id: type.UserId,
		custom_title: type.String,
	): Promise<type.Bool> => this.call('setChatAdministratorCustomTitle', {
		chat_id,
		user_id,
		custom_title,
	}).then(r => r.result)

	/**
	 * Use this method to ban a channel chat in a supergroup or a channel.
	 * Until the chat is unbanned,
	 * the owner of the banned chat won't be able to send messages on behalf of any of their channels.
	 * The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights.
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	 * @param sender_user_id {type.UserId} - Unique identifier of the target user
	 * @returns {Promise<type.Bool>} 
	 */
	banChatSenderChat = (
		chat_id: type.ChatId,
		sender_user_id: type.UserId,
	): Promise<type.Bool> => this.call('banChatSenderChat', {
		chat_id,
		sender_user_id,
	}).then(r => r.result)


	/**
	 * Use this method to unban a previously banned channel chat in a supergroup or channel.
	 * The bot must be an administrator for this to work and must have the appropriate administrator rights.
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	 * @param sender_user_id {type.UserId} - Unique identifier of the target user
	 * @returns {Promise<type.Bool>} 
	 */
	unbanChatSenderChat = (
		chat_id: type.ChatId,
		sender_user_id: type.UserId,
	): Promise<type.Bool> => this.call('unbanChatSenderChat', {
		chat_id,
		sender_user_id,
	}).then(r => r.result)


	/**
	 * Use this method to set default chat permissions for all members.
	 * The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members admin rights.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	 * @param permissions {type.ChatPermissions} - New default chat permissions
	 * @returns {Promise<type.Bool>}
	 */
	setChatPermissions = (
		chat_id: type.ChatId,
		permissions: type.ChatPermissions,
	): Promise<type.Bool> => this.call('setChatPermissions', {
		chat_id,
		permissions,
	}).then(r => r.result)

	/**
	 * Use this method to generate a new invite link for a chat; any previously generated link is revoked.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
	 * Returns the new invite link as String on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @returns {Promise<type.String>}
	 * @see https://core.telegram.org/bots/api#exportchatinvitelink
	 */

	exportChatInviteLink = (
		chat_id: type.ChatId,
	): Promise<type.String> => this.call('exportChatInviteLink', {
		chat_id,
	}).then(r => r.result)


	/**
	 * Use this method to create an additional invite link for a chat.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
	 * The link can be revoked using the method revokeChatInviteLink.
	 * Returns the new invite link as ChatInviteLink object.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param name {type.String} - New name of the invite link, 1-255 characters.
	 * @param expire_date {type.Num} - Point in time (Unix timestamp) when the invite link will be disabled.
	 * @param member_limit {type.Num} - Number of users who can join the chat using the invite link; 0 means no limit
	 * @param creates_join_request {type.Bool} - True, if the chat is created by the current user
	 * @returns {Promise<type.ChatInviteLink>}
	 */
	createChatInviteLink = (
		chat_id: type.ChatId,
		name: type.String,
		expire_date: type.Num,
		member_limit: type.Num,
		creates_join_request: type.Bool,
	): Promise<type.ChatInviteLink> => this.call('createChatInviteLink', {
		chat_id,
		name,
		expire_date,
		member_limit,
		creates_join_request,
	}).then(r => new type.ChatInviteLink(r.result))

	/**
	 * Use this method to edit a non-primary invite link created by the bot.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
	 * Returns the edited invite link as a ChatInviteLink object.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param invite_link {type.String} - The invite link to edit
	 * @param name {type.String} - New name of the invite link, 1-255 characters.
	 * @param expire_date {type.Num} - Point in time (Unix timestamp) when the invite link will be disabled.
	 * @param member_limit {type.Num} - Number of users who can join the chat using the invite link; 0 means no limit
	 * @param creates_join_request {type.Bool} - True, if the chat is created by the current user
	 * @returns {Promise<type.ChatInviteLink>}
	 */

	editChatInviteLink = (
		chat_id: type.ChatId,
		invite_link: type.String,
		name: type.String,
		expire_date: type.Num,
		member_limit: type.Num,
		creates_join_request: type.Bool,
	): Promise<type.ChatInviteLink> => this.call('editChatInviteLink', {
		chat_id,
		invite_link,
		name,
		expire_date,
		member_limit,
		creates_join_request,
	}).then(r => new type.ChatInviteLink(r.result))


	/**
	 * Use this method to revoke a link previously generated by the bot.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param invite_link {type.String} - The invite link to revoke
	 * @returns {Promise<type.Bool>}
	 */

	revokeChatInviteLink = (
		chat_id: type.ChatId,
		invite_link: type.String,
	): Promise<type.Bool> => this.call('revokeChatInviteLink', {
		chat_id,
		invite_link,
	}).then(r => r.result)

	/**
	 * Use this method to approve a chat join request.
	 * The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right.
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param user_id {type.UserId} - Unique identifier of the target user
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#answerchatinvitedrequest
	 */
	approveChatJoinRequest = (
		chat_id: type.ChatId,
		user_id: type.UserId,
	): Promise<type.Bool> => this.call('approveChatJoinRequest', {
		chat_id,
		user_id,
	}).then(r => r.result)

	/**
	 * Use this method to decline a chat join request.
	 * The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right.
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param user_id {type.UserId} - Unique identifier of the target user
	 * @returns {Promise<type.Bool>}
	 */
	declineChatJoinRequest = (
		chat_id: type.ChatId,
		user_id: type.UserId,
	): Promise<type.Bool> => this.call('declineChatJoinRequest', {
		chat_id,
		user_id,
	}).then(r => r.result)


	/**
	 * Use this method to set a new profile photo for the chat.
	 * Photos can't be changed for private chats.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param photo {type.InputFile} - New chat photo, uploaded using multipart/form-data
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#setchatphoto
	 */

	setChatPhoto = (
		chat_id: type.ChatId,
		photo: type.InputFile,
	): Promise<type.Bool> => this.call('setChatPhoto', {
		chat_id,
		photo,
	}).then(r => r.result)

	/**
	 * Use this method to delete a chat photo.
	 * Photos can't be changed for private chats.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#deletechatphoto
	 */
	deleteChatPhoto = (
		chat_id: type.ChatId,
	): Promise<type.Bool> => this.call('deleteChatPhoto', {
		chat_id,
	}).then(r => r.result)

	/**
	 * Use this method to change the title of a chat.
	 * Titles can't be changed for private chats.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param title {type.String} - New chat title, 1-255 characters
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#setchattitle
	 */
	setChatTitle = (
		chat_id: type.ChatId,
		title: type.String,
	): Promise<type.Bool> => this.call('setChatTitle', {
		chat_id,
		title,
	}).then(r => r.result)

	/**
	 * Use this method to change the description of a group, a supergroup or a channel.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param description {type.String} - New chat description, 0-255 characters
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#setchatdescription
	 */
	setChatDescription = (
		chat_id: type.ChatId,
		description: type.String,
	): Promise<type.Bool> => this.call('setChatDescription', {
		chat_id,
		description,
	}).then(r => r.result)

	/**
	 * Use this method to pin a message in a supergroup.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param message_id {type.MessageId} - Identifier of a message to pin
	 * @param disable_notification? {type.Bool} - Pass True, if it is not necessary to send a notification to all group members about the new pinned message.
	 * @returns {Promise<type.Bool>}
	 */
	pinChatMessage = (
		chat_id: type.ChatId,
		message_id: type.MessageId,
		disable_notification?: type.Bool,
	): Promise<type.Bool> => this.call('pinChatMessage', {
		chat_id,
		message_id,
		disable_notification,
	}).then(r => r.result)

	/**
	 * Use this method to unpin a message in a supergroup.
	 * The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param message_id {type.MessageId} - Identifier of a message to unpin
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#unpinchatmessage
	 */
	unpinChatMessage = (
		chat_id: type.ChatId,
		message_id: type.MessageId,
	): Promise<type.Bool> => this.call('unpinChatMessage', {
		chat_id,
		message_id,
	}).then(r => r.result)

	/**
	 * Use this method to clear the list of pinned messages in a chat.
	 * If the chat is not a private chat,
	 * the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages'
	 * administrator right in a supergroup or 'can_edit_messages' administrator right in a channel.
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#unpinchatmessage
	 */
	unpinAllChatMessages = (
		chat_id: type.ChatId,
	): Promise<type.Bool> => this.call('unpinAllChatMessages', {
		chat_id,
	}).then(r => r.result)

	/**
	 * Use this method for your bot to leave a group, supergroup or channel.
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#leavechat
	 */
	leaveChat = (
		chat_id: type.ChatId,
	): Promise<type.Bool> => this.call('leaveChat', {
		chat_id,
	}).then(r => r.result)


	/**
	 * Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.).
	 * Returns a Chat object on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
	 * @returns {Promise<type.Chat>}
	 * @see https://core.telegram.org/bots/api#getchat
	 */

	getChat = (
		chat_id: type.ChatId,
	): Promise<type.Chat> => this.call('getChat', {
		chat_id,
	}).then(r => new type.Chat(r.result))

	/**
	 * Use this method to get a list of administrators in a chat.
	 * On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots.
	 * If the chat is a group or a supergroup, only members of the chat itself (members) are returned.
	 * If the chat is a channel (stream), information about the channel itself will be returned as a ChatMember object.
	 * If a chat is a private chat, no information is returned.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
	 * @returns {Promise<type.ChatMember[]>}
	 * @see https://core.telegram.org/bots/api#getchatmemberscount
	 */
	getChatAdministrators = (
		chat_id: type.ChatId,
	): Promise<type.ChatMember[]> => this.call('getChatAdministrators', {
		chat_id,
	}).then(r => r.result.map((i: type.JsonChatMember) => new type.ChatMember(i)))

	/**
	 * Use this method to get the number of members in a chat.
	 * Returns Int on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
	 * @returns {Promise<type.Num>}
	 * @see https://core.telegram.org/bots/api#getchatmemberscount
	 */
	getChatMembersCount = (
		chat_id: type.ChatId,
	): Promise<type.Num> => this.call('getChatMembersCount', {
		chat_id,
	}).then(r => r.result)


	/**
	 * Use this method to get information about a member of a chat.
	 * Returns a ChatMember object on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
	 * @param user_id {type.UserId} - Unique identifier of the target user
	 * @returns {Promise<type.ChatMember>}
	 * @see https://core.telegram.org/bots/api#getchatmember
	 */
	getChatMember = (
		chat_id: type.ChatId,
		user_id: type.UserId,
	): Promise<type.ChatMember> => this.call('getChatMember', {
		chat_id,
		user_id,
	}).then(r => new type.ChatMember(r.result))


	/**
	 * Use this method to set a new group sticker set for a supergroup.
	 * Returns True on success.
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	 * @param sticker_set_name {type.Str} - Name of the sticker set to be set as the group sticker set
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#setchatstickerset
	 */
	setChatStickerSet = (
		chat_id: type.ChatId,
		sticker_set_name: type.Str,
	): Promise<type.Bool> => this.call('setChatStickerSet', {
		chat_id,
		sticker_set_name,
	}).then(r => r.result)

	/**
	 * Use this method to delete a group sticker set from a supergroup.
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	 * @returns {Promise<type.Bool>}
	 * @see https://core.telegram.org/bots/api#deletechatstickerset
	 */
	deleteChatStickerSet = (
		chat_id: type.ChatId,
	): Promise<type.Bool> => this.call('deleteChatStickerSet', {
		chat_id,
	}).then(r => r.result)

	/**
	 * Use this method to send answers to callback queries sent from inline keyboards.
	 * The answer will be displayed to the user as a notification at the top of the chat screen or as an alert.
	 * On success, True is returned.
	 * Alternatively, the user can be redirected to the specified URL.
	 * @param callback_query_id {type.Str} - Unique identifier for the query to be answered
	 * @param text {type.Str} - Text of the notification. If not specified, nothing will be shown to the user
	 * @param show_alert {type.Bool} - If true, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.
	 * @param url {type.Str} - URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @Botfather, specify the URL that opens your game.
	 * @param cache_time {type.Num} - The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.
	 * @returns {Promise<type.Bool>}
	 */
	answerCallbackQuery = (
		callback_query_id: type.Str,
		text?: type.Str,
		show_alert?: type.Bool,
		url?: type.Str,
		cache_time?: type.Num,
	): Promise<type.Bool> => this.call('answerCallbackQuery', {
		callback_query_id,
		text,
		show_alert,
		url,
		cache_time,
	}).then(r => r.result)

	/**
	 * Use this method to change the list of the bot's commands.
	 * See https://core.telegram.org/bots#commands for more details about bot commands.
	 * Returns True on success.
	 *
	 * @param commands {type.BotCommand[]|type.ArrayObject} - A JSON-serialized list of bot commands to be set as the list of the bot's commands.
	 * @param scope {type.BotCommandScope} - Optional. A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.
	 * @param language_code {type.Str} - Optional. If specified, commands will be available only for users of that language. Otherwise, commands will be available for all users.
	 * @returns {Promise<type.Bool>}
	 */
	setMyCommands = (
		commands: type.BotCommand[]|type.ArrayObject,
		scope?: type.BotCommandScope,
		language_code?: type.Str,
	): Promise<type.Bool> => this.call('setMyCommands', {
		commands,
		scope,
		language_code,
	}).then(r => r.result)

	/**
	 * Use this method to get the current list of the bot's commands.
	 *
	 * @param scope {type.BotCommandScope} - Optional. A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.
	 * @param language_code {type.Str} - Optional. If specified, commands will be available only for users of that language. Otherwise, commands will be available for all users.
	 * Returns Array of BotCommand on success.
	 * @returns {Promise<type.BotCommand[]>}
	 */
	getMyCommands = (
		scope?: type.BotCommandScope,
		language_code?: type.Str,
	): Promise<type.BotCommand[]> => this.call('getMyCommands', {
		scope,
		language_code,
	}).then(r => r.result.map((cmd:type.JsonBotCommand) => new type.BotCommand(cmd)))


	/**
	 * Use this method to delete the list of the bot's commands for the given scope and user language.
	 * After deletion, higher level commands will be shown to affected users.
	 * Returns True on success.
	 *
	 * @param scope {type.BotCommandScope} - Optional. A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.
	 * @param language_code {type.Str} - Optional. If specified, commands will be deleted only for users of that language. Otherwise, commands will be deleted for all users.
	 * @returns {Promise<type.Bool>}
	 */
	deleteMyCommands = (
		scope?: type.BotCommandScope,
		language_code?: type.Str,
	): Promise<type.Bool> => this.call('deleteMyCommands', {
		scope,
		language_code,
	}).then(r => r.result)


	/**
	 * Use this method to change the bot's menu button in a private chat, or the default menu button.
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target private chat. If not specified, default bot's menu button will be changed
	 * @param menu_button {type.MenuButton} - A JSON-serialized object for the bot's new menu button. Defaults to MenuButtonDefault
	 * @returns {Promise<type.Bool>}
	 */
	setChatMenuButton = (
		chat_id: type.ChatId,
		menu_button: type.JsonMenuButton,
	): Promise<type.Bool> => this.call('setChatMenuButton', {
		chat_id,
		menu_button,
	}).then(r => r.result)


	/**
	 * Use this method to get the current value of the bot's menu button in a private chat
	 *  or the default menu button.
	 * Returns MenuButton on success.
	 *
	 * @param chat_id {type.ChatId} - Unique identifier for the target private chat. If not specified, default bot's menu button will be returned
	 * @returns {Promise<type.MenuButton>}
	 */
	getChatMenuButton = (
		chat_id: type.ChatId,
	): Promise<type.MenuButton> => this.call('getChatMenuButton', {
		chat_id,
	}).then(r => new type.MenuButton(r.result))

	/**
	 * Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels.
	 * These rights will be suggested to users,
	 * but they are are free to modify the list before adding the bot.
	 * Returns True on success.
	 *
	 * @param rights {type.ChatAdministratorRights} - A JSON-serialized object for the new default administrator rights.
	 * @param for_channels?: {type.Bool} - Optional. Pass True, if the administrator rights are requested for a channel.
	 * @returns {Promise<type.Bool>}
	 */

	setDefaultChatAdministratorRights = (
		rights: type.JsonChatAdministratorRights,
		for_channels?: type.Bool,
	): Promise<type.Bool> => this.call('setDefaultChatAdministratorRights', {
		rights,
		for_channels,
	}).then(r => r.result)

	/**
	 * Use this method to get the default administrator rights for a chat.
	 * Returns ChatAdministratorRights on success.
	 *
	 * @param for_channels?: {type.Bool} - Optional. Pass True, if the administrator rights are requested for a channel.
	 * @returns {Promise<type.ChatAdministratorRights>}
	 */
	getDefaultChatAdministratorRights = (
		for_channels?: type.Bool,
	): Promise<type.ChatAdministratorRights> => this.call('getDefaultChatAdministratorRights', {
		for_channels,
	}).then(r => new type.ChatAdministratorRights(r.result))


	// edit messages InlineKeyboardMarkup

	/** Updating messages
	 * The following methods allow you to change an existing message in the message history instead of sending a new one with a result of an action.
	 * This is most useful for messages with inline keyboards using callback queries,
	 * but can also help reduce clutter in conversations with regular chat bots.
	 *
	 * Please note, that it is currently only possible to edit messages without reply_markup or with inline keyboards.
	 *
	 * Use this method to edit text and game messages.
	 * On success,
	 * if the edited message is not an inline message,
	 * the edited Message is returned,
	 * otherwise True is returned.
	 *
	 * @param chat_id {type.ChatId} - Required. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param message_id {type.MessageId} - Required. Identifier of the message to edit
	 * @param inline_message_id {type.Str} - Required. Identifier of the inline message
	 * @param text {type.Str} - Required. New text of the message
	 * @param parse_mode {type.Str} - Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param entities {type.MessageEntity[]|type.ArrayObject} - Optional. List of special entities that appear in the message,
	 * @param disable_web_page_preview?: {type.Bool} - Optional. Disables link previews for links in this message.
	 * @param reply_markup {type.InlineKeyboardMarkup} - Optional. A JSON-serialized object for an inline keyboard.
	 * @returns {Promise<type.Message|type.Bool>}
	 */
	editMessageText = (
		text: type.Str,
		chat_id?: type.ChatId,
		message_id?: type.MessageId,
		inline_message_id?: type.Str,
		parse_mode?: type.Str,
		entities?: type.MessageEntity[]|type.ArrayObject,
		disable_web_page_preview?: type.Bool,
		reply_markup?: type.InlineKeyboardMarkup,
	): Promise<type.Message | type.Bool> => this.call('editMessageText', {
		chat_id,
		message_id,
		inline_message_id,
		text,
		parse_mode,
		entities,
		disable_web_page_preview,
		reply_markup,
	}).then(r => typeof r.result == 'boolean' ?  r.result : new type.Message(r.result))


	/** editMessageCaption
	 * Use this method to edit captions of messages.
	 * On success,
	 * if the edited message is not an inline message,
	 * the edited Message is returned,
	 * otherwise True is returned.
	 *
	 * @param chat_id {type.ChatId} - Required. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param message_id {type.MessageId} - Required. Identifier of the message to edit
	 * @param inline_message_id {type.Str} - Required. Identifier of the inline message
	 * @param caption {type.Str} - Required. New caption of the message
	 * @param parse_mode {type.Str} - Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
	 * @param caption_entities {type.MessageEntity[]|type.ArrayObject} - Optional. List of special entities that appear in the message,
	 * @param reply_markup {type.InlineKeyboardMarkup} - Optional. A JSON-serialized object for an inline keyboard.
	 * @returns {Promise<type.Message|type.Bool>}
	 */
	editMessageCaption = (
		caption: type.Str,
		chat_id?: type.ChatId,
		message_id?: type.MessageId,
		inline_message_id?: type.Str,
		parse_mode?: type.Str,
		caption_entities?: type.MessageEntity[]|type.ArrayObject,
		reply_markup?: type.InlineKeyboardMarkup,
	): Promise<type.Message | type.Bool> => this.call('editMessageCaption', {
		chat_id,
		message_id,
		inline_message_id,
		caption,
		parse_mode,
		caption_entities,
		reply_markup,
	}).then(r => typeof r.result == 'boolean' ?  r.result : new type.Message(r.result))

	/** editMessageMedia
	 * Use this method to edit animation, audio, document, photo, or video messages.
	 * If a message is part of a message album, then it can be edited only to an audio for audio albums,
	 * only to a document for document albums and to a photo or a video otherwise.
	 * When an inline message is edited,
	 * a new file can't be uploaded;
	 * use a previously uploaded file via its file_id or specify a URL.
	 * On success,
	 * if the edited message is not an inline message,
	 * the edited Message is returned,
	 * otherwise True is returned.
	 *
	 * @param chat_id {type.ChatId} - Required. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param message_id {type.MessageId} - Required. Identifier of the message to edit
	 * @param inline_message_id {type.Str} - Required. Identifier of the inline message
	 * @param media {type.InputMedia} - Required. New media of the message
	 * @param reply_markup {type.InlineKeyboardMarkup} - Optional. A JSON-serialized object for an inline keyboard.
	 * @returns {Promise<type.Message|type.Bool>}
	 * @see https://core.telegram.org/bots/api#inputmedia
	 */
	editMessageMedia = (
		media: type.InputMedia,
		chat_id?: type.ChatId,
		message_id?: type.MessageId,
		inline_message_id?: type.Str,
		reply_markup?: type.InlineKeyboardMarkup,
	): Promise<type.Message | type.Bool> => this.call('editMessageMedia', {
		chat_id,
		message_id,
		inline_message_id,
		media,
		reply_markup,
	}).then(r => typeof r.result == 'boolean' ? r.result : new type.Message(r.result))


	/** editMessageReplyMarkup
	 * Use this method to edit only the reply markup of messages.
	 * On success,
	 * if the edited message is not an inline message,
	 * the edited Message is returned,
	 * otherwise True is returned.
	 * @param chat_id {type.ChatId} - Required. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param message_id {type.MessageId} - Required. Identifier of the message to edit
	 * @param inline_message_id {type.Str} - Required. Identifier of the inline message
	 * @param reply_markup {type.InlineKeyboardMarkup} - Optional. A JSON-serialized object for an inline keyboard.
	 * @returns {Promise<type.Message|type.Bool>}
	 * @see {@link https://core.telegram.org/bots/api#editmessagereplymarkup}
	 * @see {@link https://core.telegram.org/bots/api#inlinekeyboardmarkup}
	 * @see {@link https://core.telegram.org/bots/api#replykeyboardmarkup}
	 */
	editMessageReplyMarkup = (
		chat_id?: type.ChatId,
		message_id?: type.MessageId,
		inline_message_id?: type.Str,
		reply_markup?: type.InlineKeyboardMarkup,
	): Promise<type.Message | type.Bool> => this.call('editMessageReplyMarkup', {
		chat_id,
		message_id,
		inline_message_id,
		reply_markup,
	}).then(r => typeof r.result == 'boolean' ?  r.result : new type.Message(r.result))


	/** StopPoll
	 * Use this method to stop a poll which was sent by the bot.
	 * On success,
	 * the stopped Poll is returned.
	 *
	 * @param chat_id {type.ChatId} - Required. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param message_id {type.MessageId} - Required. Identifier of the original message with the poll
	 * @param reply_markup {type.InlineKeyboardMarkup} - Optional. A JSON-serialized object for a new message inline keyboard.
	 */
	stopPoll = (
		chat_id: type.ChatId,
		message_id: type.MessageId,
		reply_markup?: type.InlineKeyboardMarkup,
	): Promise<type.Poll> => this.call('stopPoll', {
		chat_id,
		message_id,
		reply_markup,
	}).then(r => new type.Poll(r.result))

	/** deleteMessage
	 * Use this method to delete a message, including service messages, with the following limitations:
	 * - A message can only be deleted if it was sent less than 48 hours ago.
	 * - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
	 * - Bots can delete outgoing messages in private chats, groups, and supergroups.
	 * - Bots can delete incoming messages in private chats.
	 * - Bots granted can_post_messages permissions can delete outgoing messages in channels.
	 * - If the bot is an administrator of a group, it can delete any message there.
	 * - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
	 * Returns True on success.
	 *
	 * @param chat_id {type.ChatId} - Required. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param message_id {type.MessageId} - Required. Identifier of the message to delete
	 * @returns {Promise<type.Bool>}
	 * @see {@link https://core.telegram.org/bots/api#deletemessage}
	 */
	deleteMessage = (
		chat_id: type.ChatId,
		message_id: type.MessageId,
	): Promise<type.Bool> => this.call('deleteMessage', {
		chat_id,
		message_id,
	}).then(r => r.result)


	/**
	 * Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers.
	 * On success, the sent Message is returned.
	 *
	 * @param chat_id {type.ChatId} - Required. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
	 * @param sticker {type.InputFile|type.Str} - Required. Sticker to send.
	 * @param disable_notification {type.Bool} - Optional. Sends the message silently. Users will receive a notification with no sound.
	 * @param protect_content {type.Bool} - Optional. Protects the contents of the sent message from forwarding and saving
	 * @param reply_to_message_id {type.MessageId} - Optional. If the message is a reply, ID of the original message
	 * @param allow_sending_without_reply {type.Bool} - Optional. Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup {type.ReplyMarkup} - Optional. Additional interface options.
	 * @returns {Promise<type.Message>}
	 * @see {@link https://core.telegram.org/bots/api#sendsticker}
	 */
	sendSticker = (
		chat_id: type.ChatId,
		sticker: type.InputFile | type.Str,
		disable_notification?: type.Bool,
		protect_content?: type.Bool,
		reply_to_message_id?: type.MessageId,
		allow_sending_without_reply?: type.Bool,
		reply_markup?: type.ReplyMarkup
	): Promise<type.Message> => this.call('sendSticker', {
		chat_id,
		sticker,
		disable_notification,
		protect_content,
		reply_to_message_id,
		allow_sending_without_reply,
		reply_markup,
	}).then(r => new type.Message(r.result))

	/**
	 * Use this method to get a sticker set.
	 * On success, a StickerSet object is returned.
	 * =
	 * @param name {type.Str} - Required. Name of the sticker set
	 * @returns {Promise<type.StickerSet>}
	 * @see {@link https://core.telegram.org/bots/api#getstickerset}
	 */
	getStickerSet = (
		name: type.Str,
	): Promise<type.StickerSet> => this.call('getStickerSet', {
		name,
	}).then(r => new type.StickerSet(r.result))

	/**
	 * Use this method to upload a .PNG file with a sticker for later use in createNewStickerSet and addStickerToSet methods.
	 * Returns the uploaded File on success.
	 *
	 * @param user_id {type.UserId} - Required. User identifier of sticker file owner
	 * @param png_sticker {type.InputFile} - Required. PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px.
	 * @returns {Promise<type.File>}
	 * @see {@link https://core.telegram.org/bots/api#uploadstickerfile}
	 */
	uploadStickerFile = (
		user_id: type.UserId,
		png_sticker: type.InputFile,
	): Promise<type.File> => this.call('uploadStickerFile', {
		user_id,
		png_sticker,
	}).then(r => new type.File(r.result))

	/**
	 * Use this method to create a new sticker set owned by a user.
	 * The bot will be able to edit the created sticker set.
	 * Returns True on success.
	 * @param user_id {type.UserId} - Required. User identifier of created sticker set owner
	 * @param name {type.Str} - Required. Short name of sticker set, to be used in the title of the sticker set list
	 * @param png_sticker? {type.InputFile|type.Str} - Optional. Png image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px.
	 * @param tgs_sticker? {type.InputFile|type.Str} - Optional. Tgs animation with the sticker, must be up to 512 kilobytes in size, duration must not exceed 60 seconds.
	 * @param webm_sticker? {type.InputFile|type.Str} - Optional. Webp image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px.
	 * @param emojis {type.Str} - Required. One or more emoji corresponding to the sticker
	 * @param contains_masks {type.Bool} - Optional. Pass True, if a set of mask stickers should be created
	 * @param mask_position {type.MaskPosition} - Optional. Position where the mask should be placed on faces
	 * @returns {Promise<type.Bool>}
	 * @see {@link https://core.telegram.org/bots/api#createnewstickerset}
	 */
	createNewStickerSet = (
		user_id: type.UserId,
		name: type.Str,
		emojis: type.Str,
		png_sticker?: type.InputFile | type.Str,
		tgs_sticker?: type.InputFile | type.Str,
		webm_sticker?: type.InputFile | type.Str,
		contains_masks?: type.Bool,
		mask_position?: type.MaskPosition,
	): Promise<type.Bool> => this.call('createNewStickerSet', {
		user_id,
		name,
		png_sticker,
		tgs_sticker,
		webm_sticker,
		emojis,
		contains_masks,
		mask_position,
	}).then(r => r.result)

	/**
	 * Use this method to move a sticker in a set created by the bot to a specific position.
	 * Returns True on success.
	 *
	 * @param sticker {type.FileId} - Required. File identifier of the sticker
	 * @param position {type.Num} - Required. New position of the sticker in the set, zero-based
	 * @returns {Promise<type.Bool>}
	 * @see {@link https://core.telegram.org/bots/api#setstickerpositioninset}
	 */
	setStickerPositionInSet = (
		sticker: type.FileId,
		position: type.Num,
	): Promise<type.Bool> => this.call('setStickerPositionInSet', {
		sticker,
		position,
	}).then(r => r.result)

	/**
	 * Use this method to delete a sticker from a set created by the bot.
	 * Returns True on success.
	 *
	 * @param sticker {type.FileId} - Required. File identifier of the sticker
	 * @returns {Promise<type.Bool>}
	 * @see {@link https://core.telegram.org/bots/api#deletestickerfromset}
	 */
	deleteStickerFromSet = (
		sticker: type.FileId,
	): Promise<type.Bool> => this.call('deleteStickerFromSet', {
		sticker,
	}).then(r => r.result)

	/**
	 * Use this method to set the thumbnail of a sticker set.
	 * Animated thumbnails can be set for animated sticker sets only.
	 * Video thumbnails can be set only for video sticker sets only.
	 * Returns True on success.
	 *
	 * @param name {type.Str} - Required. Name of the sticker set
	 * @param user_id {type.UserId} - Required. User identifier of the sticker set owner
	 * @param thumbnail {type.InputFile} - Required. Sticker thumbnail to set
	 * @returns {Promise<type.Bool>}
	 * @see {@link https://core.telegram.org/bots/api#setstickersetthumbnail}
	 */
	setStickerSetThumbnail = (
		name: type.Str,
		user_id: type.UserId,
		thumbnail: type.InputFile,
	): Promise<type.Bool> => this.call('setStickerSetThumbnail', {
		name,
		user_id,
		thumbnail,
	}).then(r => r.result)

	/**
	 * Use this method to send answers to an inline query. On success, True is returned.
	 * No more than 50 results per query are allowed.
	 *
	 * @param inline_query_id {type.Str} - Required. Unique identifier for the answered query
	 * @param results {type.InlineQueryResult[]|type.ArrayObject} - Required. A JSON-serialized array of results for the inline query
	 * @param cache_time {type.Num} - Optional. The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.
	 * @param is_personal {type.Bool} - Optional. Pass True, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query
	 * @param next_offset {type.Str} - Optional. Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.
	 * @param switch_pm_text {type.Str} - Optional. If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with the parameter switch_pm_parameter
	 * @param switch_pm_parameter {type.Str} - Optional. Deep-linking parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed. Example: AnswerInlineQuery
	 * @returns {Promise<type.Bool>}
	 * @see {@link https://core.telegram.org/bots/api#answerinlinequery}
	 */

	answerInlineQuery = (
		inline_query_id: type.Str,
		results: type.InlineQueryResult[]|type.ArrayObject,
		cache_time?: type.Num,
		is_personal?: type.Bool,
		next_offset?: type.Str,
		switch_pm_text?: type.Str,
		switch_pm_parameter?: type.Str,
	): Promise<type.Bool> => this.call('answerInlineQuery', {
		inline_query_id,
		results,
		cache_time,
		is_personal,
		next_offset,
		switch_pm_text,
		switch_pm_parameter,
	}).then(r => r.result)


	/**
	 * Use this method to set the result of an interaction with a Web App and
	 * send a corresponding message on behalf of the user to the chat from which the query originated.
	 * On success,
	 * a SentWebAppMessage object is returned.
	 *
	 * @param web_app_query_id {type.Str} - Required. Unique identifier for the query to be answered
	 * @param result {type.InlineQueryResult[]|type.ArrayObject} - Required. A JSON-serialized array of results for the inline query
	 * @returns {Promise<type.SentWebAppMessage>}
	 * @see {@link https://core.telegram.org/bots/api#answerwebappquery}
	 */
	answerWebAppQuery = (
		web_app_query_id: type.Str,
		result: type.InlineQueryResult[]|type.ArrayObject,
	): Promise<type.SentWebAppMessage> => this.call('answerWebAppQuery', {
		web_app_query_id,
		result,
	}).then(r => new type.SentWebAppMessage(r.result))

	/**
	 * Use this method to send invoices.
	 * On success, the sent Message is returned.
	 *
	 * @param chat_id {type.ChatId} - Required. Unique identifier for the target private chat
	 * @param title {type.Str} - Required. Product name, 1-32 characters
	 * @param description {type.Str} - Required. Product description, 1-255 characters
	 * @param payload {type.Str} - Required. Product payload, 1-128 bytes
	 * @param provider_token {type.Str} - Required. Payments provider token, obtained via Botfather
	 * @param currency {type.Str} - Required. Three-letter ISO 4217 currency code
	 * @param prices {type.LabeledPrice[]|type.ArrayObject} - Required. Price breakdown, a list of components
	 * @param max_tip_amount {type.Num} - Optional. The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0
	 * @param suggested_tip_amounts {type.Num[]|type.ArrayObject} - Optional. A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
	 * @param start_parameter {type.Str} - Required. Unique deep-linking parameter that can be used to generate this invoice
	 * @param provider_data {type.Str} - Optional. JSON-encoded data about the invoice, which will be shared with the payment provider. A stringified JSON object with the following fields:
	 * @param photo_url {type.Str} - Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
	 * @param photo_size {type.Num} - Optional. Photo size
	 * @param photo_width {type.Num} - Optional. Photo width
	 * @param photo_height {type.Num} - Optional. Photo height
	 * @param need_name {type.Bool} - Optional. Pass True, if you require the user's full name to complete the order
	 * @param need_phone_number {type.Bool} - Optional. Pass True, if you require the user's phone number to complete the order
	 * @param need_email {type.Bool} - Optional. Pass True, if you require the user's email address to complete the order
	 * @param need_shipping_address {type.Bool} - Optional. Pass True, if you require the user's shipping address to complete the order
	 * @param send_phone_number_to_provider {type.Bool} - Optional. Pass True, if user's phone number should be sent to provider
	 * @param send_email_to_provider {type.Bool} - Optional. Pass True, if user's email address should be sent to provider
	 * @param is_flexible {type.Bool} - Optional. Pass True, if the final price depends on the shipping method
	 * @param disable_notification {type.Bool} - Optional. Sends the message silently. Users will receive a notification with no sound.
	 * @param protect_content {type.Bool} - Optional. Protects the contents of the sent message from forwarding and saving
	 * @param reply_to_message_id {type.Num} - Optional. If the message is a reply, ID of the original message
	 * @param allow_sending_without_reply {type.Bool} - Optional. Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup {type.InlineKeyboardMarkup} - Optional. A JSON-serialized object for an inline keyboard. If empty, one_time_keyboard and selective are ignored
	 * @returns {Promise<type.Message>}
	 * @see {@link https://core.telegram.org/bots/api#sendinvoice}
	 * @see {@link https://core.telegram.org/bots/api#message}
	 * @see {@link https://core.telegram.org/bots/payments/currencies.json}
	 */
	sendInvoice = (
		chat_id: type.ChatId,
		title: type.Str,
		description: type.Str,
		payload: type.Str,
		provider_token: type.Str,
		currency: type.Str,
		prices: type.LabeledPrice[]|type.ArrayObject,
		max_tip_amount?: type.Num,
		suggested_tip_amounts?: type.Num[]|type.ArrayObject,
		start_parameter?: type.Str,
		provider_data?: type.Str,
		photo_url?: type.Str,
		photo_size?: type.Num,
		photo_width?: type.Num,
		photo_height?: type.Num,
		need_name?: type.Bool,
		need_phone_number?: type.Bool,
		need_email?: type.Bool,
		need_shipping_address?: type.Bool,
		send_phone_number_to_provider?: type.Bool,
		send_email_to_provider?: type.Bool,
		is_flexible?: type.Bool,
		disable_notification?: type.Bool,
		protect_content?: type.Bool,
		reply_to_message_id?: type.Num,
		allow_sending_without_reply?: type.Bool,
		reply_markup?: type.InlineKeyboardMarkup,
	): Promise<type.Message> => this.call('sendInvoice', {
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
		reply_markup,
	}).then(res => new type.Message(res.result))


	/**
	 * If you sent an invoice requesting a shipping address and the parameter is_flexible was specified,
	 * the Bot API will send an Update with a shipping_query field to the bot.
	 * Use this method to reply to shipping queries.
	 * On success,
	 * True is returned.
	 *
	 * @param shipping_query_id {type.Str} - Required. Unique identifier for the query
	 * @param ok {type.Bool} - Required. Specify True if delivery to the specified address is possible and False if not
	 * @param shipping_options {type.ShippingOption[]|type.ArrayObject} - Optional. Required if ok is True. A JSON-serialized array of available shipping options.
	 * @param error_message {type.Str} - Optional. Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable').
	 * @returns {Promise<type.Bool>}
	 * @see {@link https://core.telegram.org/bots/api#answershippingquery}
	 */

	answerShippingQuery = (
		shipping_query_id: type.Str,
		ok: type.Bool,
		shipping_options: type.ShippingOption[]|type.ArrayObject,
		error_message: type.Str,
	): Promise<type.Bool> => this.call('answerShippingQuery', {
		shipping_query_id,
		ok,
		shipping_options,
		error_message,
	}).then(res => res.result)

	/**
	 * Once the user has confirmed their payment and shipping details,
	 * the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query.
	 * Use this method to respond to such pre-checkout queries.
	 * On success,
	 * True is returned.
	 *
	 * Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.
	 *
	 * @param pre_checkout_query_id {type.Str} - Required. Unique identifier for the query
	 * @param ok {type.Bool} - Required. Specify True if everything is ok (goods are available, etc.) and False if not.
	 * @param error_message {type.Str} - Optional. Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!").
	 * @returns {Promise<type.Bool>}
	 * @see {@link https://core.telegram.org/bots/api#answerprecheckoutquery}
	 */

	answerPreCheckoutQuery = (
		pre_checkout_query_id: type.Str,
		ok: type.Bool,
		error_message: type.Str,
	): Promise<type.Bool> => this.call('answerPreCheckoutQuery', {
		pre_checkout_query_id,
		ok,
		error_message,
	}).then(res => res.result)


	/**
	 * Use this method to send a game.
	 * On success,
	 * an Update with the message is returned.
	 * @param chat_id {type.ChatId} - Required. Unique identifier for the target chat
	 * @param game_short_name {type.Str} - Required. Short name of the game, serves as the unique identifier for the game.
	 * @param disable_notification {type.Bool} - Optional. Sends the message silently. Users will receive a notification with no sound.
	 * @param protect_content {type.Bool} - Optional. Protects the contents of the sent message from forwarding and saving
	 * @param reply_to_message_id {type.Num} - Optional. If the message is a reply, ID of the original message
	 * @param allow_sending_without_reply {type.Bool} - Optional. Pass True, if the message should be sent even if the specified replied-to message is not found
	 * @param reply_markup {type.InlineKeyboardMarkup} - Optional. A JSON-serialized object for an inline keyboard. If empty, one ‘Play game_title’ button will be shown. If not empty, the first button must launch the game.
	 * @returns {Promise<type.Message>}
	 * @see {@link https://core.telegram.org/bots/api#sendgame}
	 */
	sendGame = (
		chat_id: type.ChatId,
		game_short_name: type.Str,
		disable_notification?: type.Bool,
		protect_content?: type.Bool,
		reply_to_message_id?: type.Num,
		allow_sending_without_reply?: type.Bool,
		reply_markup?: type.InlineKeyboardMarkup,
	): Promise<type.Message> => this.call('sendGame', {
		chat_id,
		game_short_name,
		disable_notification,
		protect_content,
		reply_to_message_id,
		allow_sending_without_reply,
		reply_markup,
	}).then(res => new type.Message(res.result))

	/**
	 * Use this method to set the score of the specified user in a game message.
	 * On success, if the message is not an inline message,
	 * the Message is returned, otherwise True is returned.
	 * Returns an error,
	 * if the new score is not greater than the user's current score in the chat and force is False.
	 *
	 * @param user_id {type.Num} - Required. User identifier
	 * @param score {type.Num} - Required. New score, must be positive
	 * @param chat_id {type.ChatId} - Optional. Unique identifier for the target chat
	 * @param message_id {type.Num} - Optional. Identifier of the sent message
	 * @param inline_message_id {type.Str} - Optional. Identifier of the inline message
	 * @param disable_edit_message {type.Bool} - Optional. Pass True, if the game message should not be automatically edited to include the current score
	 * @param force {type.Bool} - Optional. Pass True, if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters
	 * @returns {Promise<type.Message|type.Bool>}
	 * @see {@link https://core.telegram.org/bots/api#setgamescore}
	 */
	setGameScore = (
		user_id: type.Num,
		score: type.Num,
		chat_id?: type.ChatId,
		message_id?: type.Num,
		inline_message_id?: type.Str,
		disable_edit_message?: type.Bool,
		force?: type.Bool,
	): Promise<type.Message | type.Bool> => this.call('setGameScore', {
		user_id,
		score,
		chat_id,
		message_id,
		inline_message_id,
		disable_edit_message,
		force,
	}).then(res => typeof res.result == 'boolean' ? res.result : new type.Message(res.result))

	/**
	 * Use this method to get data for high score tables.
	 * Will return the score of the specified user and several of their neighbors in a game.
	 * On success,
	 * returns an Array of GameHighScore objects.
	 *
	 * This method will currently return scores for the target user,
	 * plus two of their closest neighbors on each side.
	 * Will also return the top three users if the user and his neighbors are not among them.
	 * Please note that this behavior is subject to change.
	 *
	 * @param user_id {type.Num} - Required. Target user id
	 * @param chat_id {type.ChatId} - Optional. Required if inline_message_id is not specified. Unique identifier for the target chat
	 * @param message_id {type.Num} - Optional. Required if inline_message_id is not specified. Identifier of the sent message
	 * @param inline_message_id {type.Str} - Optional. Required if chat_id and message_id are not specified. Identifier of the inline message
	 * @returns {Promise<type.GameHighScore[]>}
	 * @see {@link https://core.telegram.org/bots/api#getgamehighscores}
	 */
	getGameHighScores = (
		user_id: type.Num,
		chat_id?: type.ChatId,
		message_id?: type.Num,
		inline_message_id?: type.Str,
	): Promise<type.GameHighScore[]> => this.call('getGameHighScores', {
		user_id,
		chat_id,
		message_id,
		inline_message_id,
	}).then(res => res.result.map((el: type.JsonGameHighScore) => new type.GameHighScore(el)))


}

export default Methods

/**
 * @see {@link https://core.telegram.org/bots/api}
 *
 * i used Github's Copilot to write most of this code, so I'm not 100% sure if i covered everything :)
 * if there's any problem just open an issue and explain it, i'll try to fix it ASAP
 * or if you can fix it your-self do it and make a pull request, it's highly appreciated :)
 */









// :)