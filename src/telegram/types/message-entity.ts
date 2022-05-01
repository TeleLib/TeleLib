import * as type from '../types'
import Type from './type'

export declare type JsonMessageEntity = {
	type: type.MessageEntityType
	offset: type.Number
	length: type.Number
	url?: type.String
	user?: type.JsonUser
	language?: type.String
}

export default class MessageEntity extends Type {
	type: type.MessageEntityType
	offset: type.Number
	length: type.Number
	url?: type.String
	user?: type.User
	language?: type.String

	defaultObject!: JsonMessageEntity

	constructor(messageEntity: JsonMessageEntity) {
		super()
		this.defaultObject = messageEntity

		this.type = messageEntity.type
		this.offset = messageEntity.offset
		this.length = messageEntity.length
		this.url = messageEntity.url
		this.user = messageEntity.user ? new type.User(messageEntity.user) : undefined
		this.language = messageEntity.language
	}
}