import * as type from '../types'
import Type from './type'


export declare type JsonInlineQuery = {
	id: type.String
	from: type.JsonUser
	query: type.String
	offset: type.Number
	chat_type?: 'sender' | type.ChatType
	location?: type.JsonLocation
}


export default class InlineQuery extends Type {
	id: type.String
	from: type.User
	query: type.String
	offset: type.Number
	chat_type?: 'sender' | type.ChatType
	location?: type.Location

	defaultObject!: JsonInlineQuery

	constructor(inlineQuery: JsonInlineQuery) {
		super()

		this.defaultObject = inlineQuery

		this.id = inlineQuery.id
		this.from = new type.User(inlineQuery.from)
		this.query = inlineQuery.query
		this.offset = inlineQuery.offset
		this.chat_type = inlineQuery.chat_type
		this.location = inlineQuery.location ? new type.Location(inlineQuery.location) : undefined
	}
}