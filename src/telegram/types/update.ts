import * as type from '../types'
import Type from './type'

export declare type JsonUpdate = {
	update_id: type.UpdateId
	message?: type.JsonMessage
	edited_message?: type.JsonMessage
	channel_post?: type.JsonMessage
	edited_channel_post?: type.JsonMessage
	callback_query?: type.JsonCallbackQuery
	poll?: type.JsonPoll
	poll_answer?: type.JsonPollAnswer
	inline_query?: type.JsonInlineQuery
	chosen_inline_result?: type.JsonChosenInlineResult
	shipping_query?: type.JsonShippingQuery
	pre_checkout_query?: type.JsonPreCheckoutQuery
	my_chat_member?: type.JsonChatMemberUpdated
	chat_member?: type.JsonChatMemberUpdated
	chat_join_request?: type.JsonChatJoinRequest
}

export default class Update extends Type {
	update_id: type.UpdateId
	message?: type.Message
	edited_message?: type.Message
	channel_post?: type.Message
	edited_channel_post?: type.Message
	callback_query?: type.CallbackQuery
	poll?: type.Poll
	poll_answer?: type.PollAnswer
	inline_query?: type.InlineQuery
	chosen_inline_result?: type.ChosenInlineResult
	shipping_query?: type.ShippingQuery
	pre_checkout_query?: type.PreCheckoutQuery
	chat_member?: type.ChatMemberUpdated
	my_chat_member?: type.ChatMemberUpdated
	chat_join_request?: type.ChatJoinRequest

	defaultObject!: JsonUpdate

	constructor(update: JsonUpdate) {
		super()

		this.defaultObject = update

		this.update_id = update.update_id
		this.message = update.message ? new type.Message(update.message) : undefined
		this.edited_message = update.edited_message ? new type.Message(update.edited_message) : undefined
		this.channel_post = update.channel_post ? new type.Message(update.channel_post) : undefined
		this.edited_channel_post = update.edited_channel_post ? new type.Message(update.edited_channel_post) : undefined
		this.callback_query = update.callback_query ? new type.CallbackQuery(update.callback_query) : undefined
		this.inline_query = update.inline_query ? new type.InlineQuery(update.inline_query) : undefined
		this.chosen_inline_result = update.chosen_inline_result ? new type.ChosenInlineResult(update.chosen_inline_result) : undefined
		this.poll = update.poll ? new type.Poll(update.poll) : undefined
		this.poll_answer = update.poll_answer ? new type.PollAnswer(update.poll_answer) : undefined
		this.shipping_query = update.shipping_query ? new type.ShippingQuery(update.shipping_query) : undefined
		this.pre_checkout_query = update.pre_checkout_query ? new type.PreCheckoutQuery(update.pre_checkout_query) : undefined
		this.my_chat_member = update.my_chat_member ? new type.ChatMemberUpdated(update.my_chat_member) : undefined
		this.chat_member = update.chat_member ?  new type.ChatMemberUpdated(update.chat_member) : undefined
		this.chat_join_request = update.chat_join_request ? new type.ChatJoinRequest(update.chat_join_request) : undefined
	}
}
