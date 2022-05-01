
import * as type from '../types'
import Type from './type'


export declare type JsonAudio = {
	file_id: type.String
	file_unique_id: type.String
	file_size?: type.Number
	thumb?: type.JsonPhotoSize
	duration: type.String
	file_name?: type.String
	mime_type?: type.String
	performer?: type.String
	title?: type.String
}

export default class Audio extends Type {
	file_id: type.String
	file_unique_id: type.String
	file_size?: type.Number
	thumb?: type.PhotoSize
	duration: type.String
	file_name?: type.String
	mime_type?: type.String
	performer?: type.String
	title?: type.String

	defaultObject!: JsonAudio

	constructor(audio: JsonAudio) {
		super()

		this.defaultObject = audio

		this.file_id = audio.file_id
		this.file_unique_id = audio.file_unique_id
		this.file_size = audio.file_size
		this.thumb = audio.thumb ? new type.PhotoSize(audio.thumb) : undefined
		this.duration = audio.duration
		this.file_name = audio.file_name
		this.mime_type = audio.mime_type
		this.performer = audio.performer
		this.title = audio.title
	}
}