import * as type from '../types'
import Type from './type'




export declare type JsonInlineKeyboardMarkup = {
	inline_keyboard: type.JsonInlineKeyboardButton[][]
}


export default class InlineKeyboardMarkup extends Type {
	inline_keyboard: type.InlineKeyboardButton[][]

	defaultObject!: JsonInlineKeyboardMarkup

	constructor(properties: JsonInlineKeyboardMarkup) {
		super()

		this.defaultObject = properties

		this.inline_keyboard = properties.inline_keyboard.map(
			i => i.map(
				l => new type.InlineKeyboardButton(l)
			)
		)
	}

	toObject() {
		return {
			inline_keyboard: this.inline_keyboard.map(
				i => i.map(
					l => l.toObject()
				)
			)
		}
	}
}