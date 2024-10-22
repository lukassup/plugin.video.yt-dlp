# Copyright (C) 2024, Lukas Supienis
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

import xbmc
import xbmcgui
import xbmcplugin

# from xbmcaddon import Addon
# from xbmcvfs import translatePath

from resources.lib import yt_dlp

# Get the plugin url in plugin:// notation.
URL = sys.argv[0]

# Get a plugin handle as an integer number.
HANDLE = int(sys.argv[1])


def play_stream(url: str):
    """
    Play a video stream from the provided website URL.

    :param url: Fully-qualified website URL containing the video stream
    :type url: str
    """
    if not (len(url) > 0):
        xbmc.log(f"Invalid URL provided: {url}", level=xbmc.LOGERROR)
        return  # TODO: exception
    xbmc.log(f"Fetching manifest_url for URL: {url}", level=xbmc.LOGDEBUG)

    stream_info = None
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        stream_info = ydl.extract_info(url, download=False)

    if stream_info is None:
        xbmc.log("Expected stream_info not to be None", level=xbmc.LOGERROR)
        return  # TODO: exception

    manifest_url = stream_info.get("manifest_url", None)
    # .manifest_url can be None, try to find it in .formats[*].manifest_url
    if manifest_url is None:
        for stream_fmt in stream_info["formats"]:
            manifest_url = stream_fmt.get("manifest_url", None)
            if manifest_url is not None:
                break
        else:
            xbmc.log(f"No manifest_url found for: {url}", level=xbmc.LOGERROR)
            return  # TODO: exception

    xbmc.log(f"Fetched manifest_url: {manifest_url}", level=xbmc.LOGINFO)
    # Create a playable item with a path to play.
    # offscreen=True means that the list item is not meant for displaying,
    # only to pass info to the Kodi player
    xbmcplugin.setResolvedUrl(
        HANDLE, True, listitem=xbmcgui.ListItem(offscreen=True, path=manifest_url)
    )


if __name__ == "__main__":
    xbmc.log(f"plugin args: {sys.argv}", level=xbmc.LOGDEBUG)
    plugin_param = sys.argv[2].lstrip("?")
    play_stream(plugin_param)
