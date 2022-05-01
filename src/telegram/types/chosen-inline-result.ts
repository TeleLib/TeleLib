import * as type from '../types'
import Type from './type'


export declare type JsonChosenInlineResult = {
	result_id: type.String
	from: type.JsonUser
	location?: type.JsonLocation
	inline_message_id?: type.String
	query: type.String
}


export default class ChosenInlineResult extends Type {
	result_id: type.String
	from: type.User
	location?: type.Location
	inline_message_id?: type.String
	query: type.String

	defaultObject!: JsonChosenInlineResult

	constructor(inlineQuery: JsonChosenInlineResult) {
		super()

		this.defaultObject = inlineQuery

		this.result_id = inlineQuery.result_id
		this.from = new type.User(inlineQuery.from)
		this.location = inlineQuery.location ? new type.Location(inlineQuery.location) : undefined
		this.inline_message_id = inlineQuery.inline_message_id
		this.query = inlineQuery.query
	}
}