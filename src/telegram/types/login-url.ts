import * as type from '../types'
import Type from './type'


export declare type JsonLoginUrl = {
	url: type.String
	forward_text?: type.String
	bot_username?: type.String
	request_write_access?: type.Boolean
}


export default class LoginUrl extends Type {
	url: type.String
	forward_text?: type.String
	bot_username?: type.String
	request_write_access?: type.Boolean

	defaultObject!: JsonLoginUrl

	constructor(properties: JsonLoginUrl) {
		super()

		this.defaultObject = properties

		this.url = properties.url
		this.forward_text = properties.forward_text ? properties.forward_text : undefined
		this.bot_username = properties.bot_username ? properties.bot_username : undefined
		this.request_write_access = properties.request_write_access ? properties.request_write_access : undefined
	}
}