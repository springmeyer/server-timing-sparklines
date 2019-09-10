## Server Sparklines

Visualize server-timing headers as sparklines.


## Depends

 - Curl
 - Python 2 or 3
 - Termgraph (pip install termgraph)
 - A server that provides server timing headers in the http response


## Usage


```
$ ./viz https://www.bbc.co.uk/iplayer

data  : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 59.28
markup: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 73.60
total : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 142.84
```

## See also

- https://w3c.github.io/server-timing/#introduction
- https://medium.com/bbc-design-engineering/server-timing-in-the-wild-bfb34816322e
- https://calendar.perfplanet.com/2018/server-timing
- https://github.com/benbria/node-servertime