import Bot from './src/bot'
import Logger from './src/logger'
import Telegram from './src/telegram'
import * as types from './src/telegram/types'

const TeleLib = {
	Bot,
	Logger,
	Telegram,
	types
}

export default TeleLib

export {
	Bot,
	Logger,
	Telegram,
	types
}