
import * as type from '../types'
import Type from './type'


export declare type JsonCallbackGame = {
	chat_id?: type.ChatId
	user_id?: type.UserId
	score?: type.Number
}


export default class CallbackGame extends Type {
	chat_id?: type.ChatId
	user_id?: type.UserId
	score?: type.Number

	defaultObject!: JsonCallbackGame

	constructor(callbackGame: JsonCallbackGame) {
		super()
		this.defaultObject = callbackGame

		this.chat_id = callbackGame.chat_id
		this.user_id = callbackGame.user_id
		this.score = callbackGame.score
	}

}