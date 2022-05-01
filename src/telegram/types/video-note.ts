import * as type from '../types'
import Type from './type'


export declare type JsonVideoNote = {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	length: type.Number
	duration: type.Number
	thumb?: type.JsonPhotoSize
	file_size?: type.Number
}


export default class VideoNote extends Type {
	fileId: type.FileId
	fileUniqueId: type.UniqueFileId
	length:  type.Number
	duration:  type.Number
	thumb?: type.PhotoSize
	fileSize?:  type.Number

	constructor(params: JsonVideoNote) {
		super()
		this.fileId = params.file_id
		this.fileUniqueId = params.file_unique_id
		this.length = params.length
		this.duration = params.duration
		this.thumb = params.thumb ? new type.PhotoSize(params.thumb) : undefined
		this.fileSize = params.file_size || undefined
	}
}
