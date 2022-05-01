import * as type from '../types'
import Type from './type'

export declare type JsonChatLocation = {
	location: type.JsonLocation
	address: type.String
}

export default class ChatLocation extends Type {
	location: type.Location
	address: type.String

	defaultObject!: JsonChatLocation

	constructor(chatLocation: JsonChatLocation) {
		super()
		this.defaultObject = chatLocation

		this.location = new type.Location(chatLocation.location)
		this.address = chatLocation.address
	}
}