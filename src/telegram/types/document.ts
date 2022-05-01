import * as type from '../types'
import Type from './type'



export declare type JsonDocument = {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	thumb?: type.JsonPhotoSize
	file_name?: type.String
	mime_type?: type.String
	file_size?: type.Number
}


export default class Document extends Type {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	thumb?: type.PhotoSize
	file_name?: type.String
	mime_type?: type.String
	file_size?: type.Number

	defaultObject!: JsonDocument
	constructor(options: JsonDocument) {
		super()

		this.defaultObject = options

		this.file_id = options.file_id
		this.file_unique_id = options.file_unique_id
		this.thumb = options.thumb && new type.PhotoSize(options.thumb) || undefined
		this.file_name = options.file_name || undefined
		this.mime_type = options.mime_type || undefined
		this.file_size = options.file_size || undefined
	}
}