# yt-dlp plugin for Kodi

Requires `inputstream.adaptive`.

## USAGE

Plugin is used together with IPTV Simple Client plugin and aids in extracting stream URLs from websites.

```
#EXTM3U

#EXTINF:-1 tvg-logo="https://i.imgur.com/FL2ZuGC.png", LRT HD
#KODIPROP:inputstream=inputstream.adaptive
plugin://plugin.video.streamlink?https://www.lrt.lt/mediateka/tiesiogiai/lrt-televizija
```

## License

[GPLv3](http://www.gnu.org/copyleft/gpl.html)
