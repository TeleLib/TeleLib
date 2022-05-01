import * as type from '../types'
import Type from './type'

export declare type JsonLocation = {
	longitude: type.Number
	latitude: type.Number
	horizontal_accuracy?: type.Number
	live_period?: type.Number
	heading?: type.Number
	proximity_alert_radius?: type.Number
}

export default class Location extends Type {
	longitude: type.Number
	latitude: type.Number
	horizontal_accuracy?: type.Number
	live_period?: type.Number
	heading?: type.Number
	proximity_alert_radius?: type.Number

	defaultObject!: JsonLocation

	constructor(location: JsonLocation) {
		super()
		this.defaultObject = location

		this.longitude = location.longitude
		this.latitude = location.latitude
		this.horizontal_accuracy = location.horizontal_accuracy
		this.live_period = location.live_period
		this.heading = location.heading
		this.proximity_alert_radius = location.proximity_alert_radius
	}
}