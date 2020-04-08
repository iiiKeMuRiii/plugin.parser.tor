#import requests
#import lxml
#import re
#from bs4 import BeautifulSoup, SoupStrainer

# Imports
from future import standard_library
from xbmcplugin import addDirectoryItem
#from _pydevd_bundle.pydevd_cython import self
standard_library.install_aliases()
from builtins import str
from builtins import object
import re
import sys
import urllib.parse
import urllib
import datetime
import json
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmcvfs
import html.parser
from bs4 import BeautifulSoup, SoupStrainer
import requests
import requests_cache


# DEBUG
DEBUG = True

_addon = xbmcaddon.Addon()
_addonID = _addon.getAddonInfo('id')
_plugin = _addon.getAddonInfo('name')
_version = _addon.getAddonInfo('version')
_icon = _addon.getAddonInfo('icon')
_fanart = _addon.getAddonInfo('fanart')
_language = _addon.getLocalizedString
_settings = _addon.getSetting
_addonpath = 'special://profile/addon_data/{}/'.format(_addonID)
PY3 = sys.version_info[0] == 3

url_Main = 'http://37.1.201.32/categories/'
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
           }

addon_handle = int(sys.argv[1])
#session = requests.session()
#request = session.get(url, headers=headers)
args = urllib.parse.parse_qs(sys.argv[2][1:])

mode = args.get('mode', None)




def main_CAT():

        r = requests.get(url_Main, headers=headers)
        r.encoding = 'utf-8'
        xbmc.log('*************** Ссылка ' + str(r), xbmc.LOGDEBUG)
        soup = BeautifulSoup(r.text, 'html.parser', parse_only=SoupStrainer('div', id='content'))
        main_cat = soup.find_all('h2')[2:9]



        db_cat = []
        for i in range(0, 7):
            db_cat.append ({'title': main_cat[i].text})


        for l in db_cat:
            #listitem = xbmcgui.ListItem(i['title'])
            #li = xbmcgui.ListItem (i['title'], iconImage='DefaultVideo.png')
            #xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
            add_main_CAT(l['title'], url_Main, 0, 'DefaultVideo.png')
            #xbmcplugin.addDirectoryItem(handle=addon_handle, url=url_Main, listitem=li, isFolder=True)
        add_main_CAT('Next Page', url_Main, 1, 'DefaultVideo.png')
        xbmcplugin.endOfDirectory(addon_handle)

def sub_CAT():

        r = requests.get(url_Main, headers=headers)
        r.encoding = 'utf-8'
        xbmc.log('*************** Ссылка ' + str(r), xbmc.LOGDEBUG)
        soup = BeautifulSoup(r.text, 'html.parser', parse_only=SoupStrainer('div', id='content'))
        sub_menu = soup.find_all('h3')[2].text

        #xbmc.log('*************** Ссылка ' + str(main_cat), xbmc.LOGDEBUG)

        sub_CAT = []
        l = re.split('\s', sub_menu)[0:28]
        l = list(filter (None, l))
        for i in range(1, 27):
            sub_CAT.append ({'title': l[i]})
        #xbmc.log('*************** СПИСОК ' + str(sub_cat), xbmc.LOGDEBUG)
        #xbmc.log('*************** addon_handle ' + str(addon_handle), xbmc.LOGDEBUG)

        for l in sub_CAT:
            #listitem = xbmcgui.ListItem(i['title'])
            #li = xbmcgui.ListItem (i['title'], iconImage='DefaultVideo.png')
            #xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
            add_main_CAT(l['title'], url_Main, 0, 'DefaultVideo.png')
            #xbmcplugin.addDirectoryItem(handle=addon_handle, url=url_Main, listitem=li, isFolder=True)
        add_main_CAT('Next Page', url_Main, 1, 'DefaultVideo.png')
        xbmcplugin.endOfDirectory(addon_handle)


def add_main_CAT(title, url, mode, iconimage):
        u=sys.argv[0]+"?url="+urllib.parse.quote_plus(url)+"&mode="+str(mode)+"name="+urllib.parse.quote_plus(title)
        ok = True
        liz = xbmcgui.ListItem(title)
        ok = xbmcplugin.addDirectoryItem(addon_handle, url=u, listitem=liz, isFolder=True) #*****************????????????????? правильный адрес ?????знак ? и =
        #xbmcgui.Dialog().ok('Warning!', url)
        xbmc.log('******* ::::::::::::: MODE ::::::::::: ******* ' + str(mode), xbmc.LOGDEBUG)
        xbmc.log('******* ::::::::::::: addCatt ::::::::::: ******* ' + u, xbmc.LOGDEBUG)
        return ok



def log(self, description):
        xbmc.log("[ADD-ON] '{} v{}': {}".format(_plugin, _version, description), xbmc.LOGNOTICE)

if mode == '1name=Next PageEE':
        xbmc.log('******* ///////////////////// значение MODE ::::::::::: ******* ' + str(mode), xbmc.LOGDEBUG)


if mode == None:
        xbmcgui.Dialog().ok('Title: mode', 'NONE_NONE')
elif str(mode[0]).split('=')[1] == 'Next Page':
        xbmcgui.Dialog().ok('Title: mode', 'УРРРААА')
        sub_CAT()


if __name__ == '__main__':
    main_CAT()
