import * as type from '../types'
import Type from './type'


export declare type JsonInlineKeyboardButton = {
	text: type.String
	url?: type.String
	login_url?: type.JsonLoginUrl
	callback_data?: type.String
	switch_inline_query?: type.String
	switch_inline_query_current_chat?: type.String
	callback_game?: type.JsonCallbackGame
	pay?: type.Boolean
	web_app?: type.JsonWebAppInfo
}


export default class InlineKeyboardButton extends Type {
	text: type.String
	url?: type.String
	login_url?: type.LoginUrl
	callback_data?: type.String
	switch_inline_query?: type.String
	switch_inline_query_current_chat?: type.String
	callback_game?: type.CallbackGame
	pay?: type.Boolean
	web_app?: type.WebAppInfo

	defaultObject!: JsonInlineKeyboardButton

	constructor(properties: JsonInlineKeyboardButton) {
		super()

		this.defaultObject = properties

		this.text = properties.text
		this.url = properties.url ? properties.url : undefined
		this.login_url = properties.login_url ? new type.LoginUrl(properties.login_url) : undefined
		this.callback_data = properties.callback_data ? properties.callback_data : undefined
		this.switch_inline_query = properties.switch_inline_query ? properties.switch_inline_query : undefined
		this.switch_inline_query_current_chat = properties.switch_inline_query_current_chat ? properties.switch_inline_query_current_chat : undefined
		this.callback_game = properties.callback_game ? new type.CallbackGame(properties.callback_game) : undefined
		this.pay = properties.pay ? properties.pay : undefined
		this.web_app = properties.web_app ? new type.WebAppInfo(properties.web_app) : undefined
	}
}