import * as type from '../types'
import Type from './type'

export declare type JsonDice = {
	emoji: type.DiceType
	value: type.Number
}

export default class Dice extends Type {
	public emoji: type.DiceType
	public value: type.Number

	defaultObject!: JsonDice

	constructor(params: JsonDice) {
		super()
		this.defaultObject = params
		this.emoji = params.emoji
		this.value = params.value
	}
}
