import Bot from './bot'
import Telegram from './telegram'
import * as types from './telegram/types'
import Logger from './logger'

const TeleLib = { Bot, Logger, Telegram, types }

export default TeleLib

export { Bot, Logger, Telegram, types }