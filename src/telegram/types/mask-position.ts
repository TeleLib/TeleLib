import * as type from '../types'
import Type from './type'


export declare type JsonMaskPosition = {
	point: type.String
	x_shift: type.Number
	y_shift: type.Number
	scale:  type.Number
}

export default class MaskPosition extends Type {
	point: type.String
	x_shift: type.Number
	y_shift: type.Number
	scale:  type.Number

	defaultObject!: JsonMaskPosition

	constructor(maskPosition: JsonMaskPosition) {
		super()

		this.defaultObject = maskPosition

		this.point = maskPosition.point
		this.x_shift = maskPosition.x_shift
		this.y_shift = maskPosition.y_shift
		this.scale = maskPosition.scale
	}
}