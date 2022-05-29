# General Code Structure of TeleLib

## last things first

- TeleLib package should export an Object named `TeleLib` in the end, <br/> TeleLib should Contain Telegram API methods, TeleLib `Bot` class and `Types` for Type strict languages and while developing TeleLib with a non-type strict language like Python, you have to export Types as abstract classes or Interfaces as well so it'd be easier for our users to create awesome projects using TeleLib :).

- exporting a `Logger` object is optional, but highly recommended in order to have a better logging experience for the users.

## TeleLib package

- it should contain a `TeleLib` object

```
├── [entry file] (Bot, Types and Logger should be exported here as TeleLib object) #[entry file] can vary depending on the language, (e.g. __init__.py in python or index.js in Javascript or index.ts in Typescript)
├── Bot (Bot Package)
├── Logger (Logger Package)
├── telegram (directory for telegram API methods)
│   ├── Methods (Package containing all Telegram API methods)
│   ├── Types (Package containing all Telegram API types + some additional types for TeleLib)
│   ├── types (directory containing all Telegram API types)
├── [test directory] (directory for tests)
├── [examples directory] (to write examples for the users [you can also write examples in the root `examples` directory])
```

## User Experience

- it is recommended to support both long pooling and webhooks in your code, but it's not required.
- for long pooling try writing non-blocking code on each update, use async functions and Threads to manage new updates, and use a queue to store new updates, and then process them in a separate thread. but keep in mind that your code should at least be able to handle +1,000 updates per second.
- for webhooks, use a built-in web server to handle requests, or use Nginx as an external web-server, you're required to write instructions to how to configure it, and use it properly.
- for multi threaded code, you have to provide users with the option to set their MAX_THREAD_COUNT, and you can use a Thread pool to manage thread count.
- to initiate an instance of TeleLib, users should be able to pass a Token, Telegram API Url, allowed_update_type, update_pull_limit, debug_mode.
- it's optional to get a default_exception_handler from users, to either just log exceptions or stop the process on exceptions.

## Linter

- you need to config a linter for your language, and it should be able to lint the code with the given configuration.
- you can use any linter that you want as long as it works perfectly.

## Prettier

- you need to configure Prettier for your language, and it should be able to format the code with the given configuration.

- Your code SHOULD use `Tabs` as indentation and `4 spaces` as tab width.
- Max line Width should be `100` in your codes.

