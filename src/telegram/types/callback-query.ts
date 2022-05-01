import * as type from '../types'
import Type from './type'


export declare type JsonCallbackQuery = {
	id: type.String
	from: type.JsonUser
	message?: type.JsonMessage
	inline_message_id?: type.String
	chat_instance: type.String
	data?: type.String
	game_short_name?: type.String
}


export default class CallbackQuery extends Type {
	id: type.String
	from: type.User
	message?: type.Message
	inline_message_id?: type.String
	chat_instance: type.String
	data?: type.String
	game_short_name?: type.String

	defaultObject!: JsonCallbackQuery

	constructor(query: JsonCallbackQuery) {
		super()
		this.defaultObject = query
		this.id = query.id
		this.from = new type.User(query.from)
		this.message = query.message ? new type.Message(query.message) : undefined
		this.inline_message_id = query.inline_message_id
		this.chat_instance = query.chat_instance
		this.data = query.data
		this.game_short_name = query.game_short_name
	}

}