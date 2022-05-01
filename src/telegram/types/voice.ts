import * as type from '../types'
import Type from './type'

export declare type JsonVoice = {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	duration: type.Number
	mime_type?: type.String
	file_size?: type.Number
}

export default class Voice extends Type {
	fileId: type.FileId
	fileUniqueId: type.UniqueFileId
	duration: type.Number
	mimeType?: type.String
	fileSize?: type.Number

	defaultObject!: JsonVoice

	constructor(params: JsonVoice) {
		super()
		this.defaultObject = params
		this.fileId = params.file_id
		this.fileUniqueId = params.file_unique_id
		this.duration = params.duration
		this.mimeType = params.mime_type|| undefined
		this.fileSize = params.file_size || undefined
	}
}
