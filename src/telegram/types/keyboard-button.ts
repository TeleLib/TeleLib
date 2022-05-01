
import * as type from '../types'
import Type from './type'



export declare type JsonKeyboardButton = {
	text: type.String
	request_contact?: type.Boolean
	request_location?: type.Boolean
	web_app?: type.JsonWebAppInfo
	request_poll?: type.JsonKeyboardButtonPollType
}


export default class KeyboardButton extends Type {
	text: type.String
	request_contact?: type.Boolean
	request_location?: type.Boolean
	web_app?: type.WebAppInfo
	request_poll?: type.KeyboardButtonPollType

	defaultObject!: JsonKeyboardButton

	constructor(properties: JsonKeyboardButton) {
		super()

		this.defaultObject = properties

		this.text = properties.text
		this.request_contact = properties.request_contact
		this.request_location = properties.request_location
		this.web_app = properties.web_app ? new type.WebAppInfo(properties.web_app) : undefined
		this.request_poll = properties.request_poll ? new type.KeyboardButtonPollType(properties.request_poll) : undefined
	}
}