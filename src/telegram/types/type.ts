import Methods from '../methods'
export default class Type {
	constructor() {
		this.methods = globalThis.methods
	}
	defaultObject!: object

	methods!: Methods

	setMethods(methods: Methods) {
		this.methods = methods
	}

	toObject(): any {

		if (this.defaultObject instanceof Type) {
			return this.defaultObject.toObject()
		}

		return this.defaultObject
	}

	toJSON() {
		return JSON.stringify(this.toObject())
	}
}
