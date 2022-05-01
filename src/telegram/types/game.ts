import * as type from '../types'
import Type from './type'


export declare type JsonGame = {
	title: type.String
	description: type.String
	photo: type.JsonPhotoSize[]
	text?: type.String
	text_entities?: type.JsonMessageEntity[]
	animation?: type.JsonAnimation
}

export default class Game extends Type {
	title: type.String
	description: type.String
	photo: type.PhotoSize[]
	text?: type.String
	text_entities?: type.MessageEntity[]
	animation?: type.Animation

	defaultObject!: JsonGame

	constructor(options: JsonGame) {
		super()

		this.defaultObject = options

		this.title = options.title
		this.description = options.description
		this.photo = options.photo.map(p => new type.PhotoSize(p))
		this.text = options.text || undefined
		this.text_entities = options.text_entities && options.text_entities.map(e => new type.MessageEntity(e)) || undefined
		this.animation = options.animation && new type.Animation(options.animation) || undefined
	}
}