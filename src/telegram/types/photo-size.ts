import * as type from '../types'
import Type from './type'


export declare type JsonPhotoSize = {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	file_size?: type.Number
	width: type.Number
	height: type.Number
}

export default class PhotoSize extends Type {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	file_size?: type.Number
	width: type.Number
	height: type.Number

	defaultObject!: JsonPhotoSize
	constructor(photoSize: JsonPhotoSize) {
		super()

		this.defaultObject = photoSize

		this.file_id = photoSize.file_id
		this.file_unique_id = photoSize.file_unique_id
		this.file_size = photoSize.file_size
		this.width = photoSize.width
		this.height = photoSize.height
	}
}