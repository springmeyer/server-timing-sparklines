## Server Sparklines

Visualize [ttfb](https://en.wikipedia.org/wiki/Time_to_first_byte) + [server-timing headers](https://w3c.github.io/server-timing/#introduction) as [sparklines](https://en.wikipedia.org/wiki/Sparkline)


## Depends

 - Curl
 - Python 2 or 3
 - Termgraph (pip install termgraph)
 - A server that provides server timing headers in the http response

## Install

```
git clone git@github.com:springmeyer/server-timing-sparklines.git
cd server-timing-sparklines
./viz -h
```

## Usage

The `viz` command accepts a single argument of a URL to download

The `viz` command outputs:

 - The curl client timing for DNS lookup, TLS handshake, and Time To First Byte.
 - The Server-Timing headers provided by the backend
 - The overall time it took to initiate the request and download the response

Optionally pass `viz --loop [url]` to repeat the request in a loop indefinetly (ctrl-c to exit). This can be valuable to watch how the timing results change as you might put load on the backend load testing.

Example:

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
- https://developers.google.com/web/fundamentals/performance/navigation-and-resource-timing/