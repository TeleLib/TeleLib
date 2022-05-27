# TeleLib

A Telegram Wrapper.

## NodeJS

### installation

```bash
yarn add @telelib/telelib
```

or

```bash
npm i --save @telelib/telelib
```

### how to use

create a .js or a .ts file
install the package using npm or yarn

import the package:

```typescript
import { Bot } from '@telelib/telelib'
```

create an instance:

```typescript
const TelegramBot = new Bot({
 telegram: {
  token: '[TOKEN]',
 },
 debug: true
})
```

since it's typescript, import Types as well

```typescript
import { types } from '@telelib/telelib'
```

- replace `[TOKEN]` with your telegram bot token

create a listener on 'Message' Type:

```typescript
TelegramBot.client.on(
 'message',
 (msg: types.Message) => {
  if (msg.text) {
   return msg.reply(`your message was:\n${msg.text}`)
  }
  msg.reply('i only understand text messages')
 }
)
```

then start the loop to fetch updates from telegram.

```typescript
TelegramBot.start()
```

- for more examples visit [examples](/examples)
- for better and more detailed documentation visit [docs](/docs)

## more info

## issues / bugs / suggestions ?

there's no template for now, just open an issue or fix it and do a Pull request, your name will be here as a contributor. :)

## contributors

[Mohammad Mahdi Afshar](https://github.com/reloadlife) - [me@mamad.dev](mailto:me@mamad.dev) - [Telegram](tg://resolve?domain=TheyCallMeMamad) - Maintainer

## todo list

- [ ] Write Full Documentation
- [ ] add Helper methods
- [ ] Add More examples
- [ ] Write Interfaces for all Message types, classes, methods.
- [ ] Add Support for Webhooks
- [ ] Implement TelegramPassport related methods
- [ ] Add MTProto and TDLib Wrapper.
- [ ] Clean up and optimize the code.

## Supported Languages

- [x] TypeScript
- [ ] Python
- [ ] PHP
- [ ] Lua
- [ ] Ruby
- [ ] Go
- [ ] Perl
- [ ] Julia
