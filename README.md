## Server Sparklines

Visualize ttfb + server-timing headers as sparklines.


## Depends

 - Curl
 - Python 2 or 3
 - Termgraph (pip install termgraph)
 - A server that provides server timing headers in the http response


## Usage


```
$ ./viz https://www.bbc.co.uk/iplayer

client:dns-lookup   : ▇▇▇▇▇▇▇▇▇ 515.02
client:tls-handshake: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1249.60
client:ttfb         : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1786.07
data                : ▇ 99.34
markup              : ▇ 78.96
total               : ▇▇▇ 186.41
overall             : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2611.00

```

## See also

- https://w3c.github.io/server-timing/#introduction
- https://medium.com/bbc-design-engineering/server-timing-in-the-wild-bfb34816322e
- https://calendar.perfplanet.com/2018/server-timing
- https://github.com/benbria/node-servertime
- https://blog.cloudflare.com/a-question-of-timing