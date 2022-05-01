import * as type from '../types'
import Type from './type'


export declare type JsonChatPhoto = {
	small_file_id: type.String
	small_file_unique_id: type.String
	big_file_id: type.String
	big_file_unique_id: type.String
}


export default class ChatPhoto extends Type {
	small_file_id: type.String
	small_file_unique_id: type.String
	big_file_id: type.String
	big_file_unique_id: type.String

	defaultObject!: JsonChatPhoto

	constructor(chatPhoto: JsonChatPhoto) {
		super()
		this.defaultObject = chatPhoto

		this.small_file_id = chatPhoto.small_file_id
		this.small_file_unique_id = chatPhoto.small_file_unique_id
		this.big_file_id = chatPhoto.big_file_id
		this.big_file_unique_id = chatPhoto.big_file_unique_id
	}
}