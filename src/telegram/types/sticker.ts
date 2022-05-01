import * as type from '../types'
import Type from './type'


export declare type JsonSticker = {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	width: type.Number
	height: type.Number
	is_animated:  type.Boolean
	is_video:  type.Boolean
	thumb?: type.JsonPhotoSize
	emoji?: type.String
	set_name?: type.String
	mask_position?: type.JsonMaskPosition
	file_size?: type.Number
}

export default class Sticker extends Type {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	width: type.Number
	height: type.Number
	is_animated: type.Boolean
	is_video: type.Boolean
	thumb?: type.PhotoSize
	emoji?: type.String
	set_name?: type.String
	mask_position?: type.MaskPosition
	file_size?: type.Number

	defaultObject!: JsonSticker

	constructor(sticker: JsonSticker) {
		super()

		this.defaultObject = sticker

		this.file_id = sticker.file_id
		this.file_unique_id = sticker.file_unique_id
		this.width = sticker.width
		this.height = sticker.height
		this.is_animated = sticker.is_animated
		this.is_video = sticker.is_video
		this.thumb = sticker.thumb ? new type.PhotoSize(sticker.thumb) : undefined
		this.emoji = sticker.emoji
		this.set_name = sticker.set_name
		this.mask_position = sticker.mask_position ? new type.MaskPosition(sticker.mask_position) : undefined
		this.file_size = sticker.file_size
	}
}