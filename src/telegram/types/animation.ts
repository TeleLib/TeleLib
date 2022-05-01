import * as type from '../types'
import Type from './type'


export declare type JsonAnimation = {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	file_size?: type.Number
	thumb?: type.JsonPhotoSize
	width: type.Number
	height: type.Number
	duration: type.Number
	file_name?: type.String
	mime_type?: type.String
}

export interface AnimationMessage {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	file_size?: type.Number
	thumb?: type.JsonPhotoSize
	width: type.Number
	height: type.Number
	duration: type.Number
	file_name?: type.String
	mime_type?: type.String
}

export default class Animation extends Type implements AnimationMessage {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	file_size?: type.Number
	thumb?: type.PhotoSize
	width: type.Number
	height: type.Number
	duration: type.Number
	file_name?: type.String
	mime_type?: type.String

	defaultObject!: JsonAnimation

	constructor(animation: JsonAnimation) {
		super()
		this.defaultObject = animation

		this.file_id = animation.file_id
		this.file_unique_id = animation.file_unique_id
		this.file_size = animation.file_size
		this.thumb = animation.thumb ? new type.PhotoSize(animation.thumb) : undefined
		this.width = animation.width
		this.height = animation.height
		this.duration = animation.duration
		this.file_name = animation.file_name
		this.mime_type = animation.mime_type
	}
}