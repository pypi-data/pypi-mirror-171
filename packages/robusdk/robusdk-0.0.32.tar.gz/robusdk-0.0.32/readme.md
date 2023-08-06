```js
(async () => {
  const robsdk = require('robusdk')
  const {Coroutine, Sequence, Logger, Awaitable} = require('robusdk')

  const Client = robsdk({
    url: 'http://localhost/',
    username: 'username',
    password: 'password'
  })

  const rpc = new Client('rpc')
  const pipeline = new Client('pipeline')
  const ws = new Client('pipeline', true)

  Logger.info(await new Coroutine([
    new Sequence(() => rpc.methodA(...paramsA), Logger.debug, Logger.error),
    new Sequence(() => rpc.methodB(...paramsB), Logger.debug, Logger.error),
    new Sequence(() => pipeline.methodA(...paramsA), Logger.debug, Logger.error),
    new Sequence(() => pipeline.methodB(...*paramsB), Logger.debug, Logger.error),
    new Awaitable(() => ws.methodA(...paramsA), Logger.debug),
    new Awaitable(() => ws.methodB(...paramsB), Logger.debug),
  ]))
})()
```

```python
async def future():
  from robusdk import robusdk, Logger, Sequence, Coroutine, Awaitable
  Client = robsdk(
    url='http://localhost/',
    username='username',
    password='password',
  )
  rpc = Client('rpc')
  pipeline = Client('pipeline')
  ws = Client('pipeline', True)
  Logger.info(await Coroutine([
      Sequence(lambda: rpc.methodA(**paramsA), Logger.debug, Logger.error),
      Sequence(lambda: rpc.methodB(**paramsB), Logger.debug, Logger.error),
      Sequence(lambda: pipeline.methodA(**paramsA), Logger.debug, Logger.error),
      Sequence(lambda: pipeline.methodB(**paramsB), Logger.debug, Logger.error),
      Awaitable(lambda: ws.methodA(**paramsA), Logger.debug),
      Awaitable(lambda: ws.methodB(**paramsB), Logger.debug),
  ]))

from asyncio import run
run(future())
```
