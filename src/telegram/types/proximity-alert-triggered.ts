import * as type from '../types'
import Type from './type'


export declare type JsonProximityAlertTriggered = {
	distance: type.Number
}


export default class ProximityAlertTriggered extends Type {
	distance: type.Number

	defaultObject!: JsonProximityAlertTriggered

	constructor(proximityAlertTriggered: JsonProximityAlertTriggered) {
		super()
		this.defaultObject = proximityAlertTriggered

		this.distance = proximityAlertTriggered.distance
	}
}