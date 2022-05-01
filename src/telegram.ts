import { AxiosInstance } from 'axios'
import EventEmitter from 'eventemitter3'
import Methods from './telegram/methods'
import * as type from './telegram/types'
import Logger from './logger'



class Telegram extends EventEmitter {
	http_client!: AxiosInstance
	update?: type.Update
	methods!: Methods
	me?: type.User

	constructor(bot: AxiosInstance, update?: type.Update) {
		super()
		this.http_client = bot
		this.methods = new Methods(bot)
		this.update = update
		globalThis.methods = this.methods

		this.bind_me()
		Logger.tag(['[Telegram EventEmitter]']).debug('bind_me')
	}

	bind_me = async () => globalThis.me = this.me = (await this.methods.getMe())

	handle = async (update: type.Update) => {
		Logger.tag(['[function]']).debug('Telegram extends EventEmitter handle')
		this.update = globalThis.update = update

		if (!globalThis.config.telegram.allowed_update_type) {
			throw Error('`allowed_update_type` is not defined in `config`.')
		}

		if (!this.update) {
			throw Error('`update` is not defined in `Telegram`.')
		}

		globalThis.config.telegram.allowed_update_type.forEach((update_type) => {
			if (update[update_type] !== undefined) { // if the update has a value
				Logger.tag(['[EventEmitter]']).debug(`EVENT: ${update_type}`)
				this.emit(update_type, update[update_type])
			}
		})
	}
}

export default Telegram
