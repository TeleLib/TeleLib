import colors from 'colors-cli'

export default class Logger {
	static tags: any[] = []
	static tag(tags: any[] = []) {
		this.tags = tags
		return this
	}
	static debug(message?: any, ...optionalParams: any[]): void {
		if (globalThis.debug) {
			return console.log(
				colors.yellow('[DEBUG]'),
				colors.yellow(this.tags.join(' ')),
				colors.yellow_bt(message),
				...optionalParams
			)
		}
	}
}