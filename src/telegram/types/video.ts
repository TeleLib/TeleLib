
import * as type from '../types'
import Type from './type'


export declare type JsonVideo = {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	width: type.Number
	height: type.Number
	duration: type.Number
	thumb?: type.JsonPhotoSize
	file_name?: type.String
	mime_type?: type.String
	file_size?: type.Number
}


export default class Video extends Type {
	file_id!: type.FileId
	file_unique_id!: type.UniqueFileId
	width: type.Number
	height: type.Number
	duration: type.Number
	thumb?: type.PhotoSize
	fileName?: type.String
	mimeType?: type.String
	fileSize?: type.Number

	defaultObject!: JsonVideo

	constructor(video: JsonVideo) {
		super()

		this.defaultObject = video

		this.file_id = video.file_id
		this.file_unique_id = video.file_unique_id
		this.width = video.width
		this.height = video.height
		this.duration = video.duration
		this.thumb = video.thumb ? new type.PhotoSize(video.thumb) : undefined
		this.fileName = video.file_name
		this.mimeType = video.mime_type
		this.fileSize = video.file_size
	}
}