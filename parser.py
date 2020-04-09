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
    if DEBUG:
        log('*+*+*+*+*+*+*+*+*+*+*+*+*+*+* main_cat()')
    r = requests.get(url_Main, headers=headers)
    r.encoding = 'utf-8'
    xbmc.log('*************** Ссылка ' + str(r), xbmc.LOGDEBUG)
    soup = BeautifulSoup(r.text, 'html.parser', parse_only=SoupStrainer('div', id='content'))
    main_cat = soup.find_all('h2')[2:9]

    xbmc.log('*************** Ссылка ' + str(main_cat), xbmc.LOGDEBUG)

    db_main_cat = []
    for i in range(0, 7):
        db_main_cat.append ({'title': main_cat[i].text})
    xbmc.log('*************** СПИСОК ' + str(db_main_cat), xbmc.LOGDEBUG)
    xbmc.log('*************** addon_handle ' + str(addon_handle), xbmc.LOGDEBUG)

    for l in db_main_cat:
        #listitem = xbmcgui.ListItem(i['title'])
        #li = xbmcgui.ListItem (i['title'], iconImage='DefaultVideo.png')
        #xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
        add_main_CAT(l['title'], url_Main, 0, 'DefaultVideo.png')
        #xbmcplugin.addDirectoryItem(handle=addon_handle, url=url_Main, listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)

def sub_CAT(indx_1):
    if DEBUG:
        log('*+*+*+*+*+*+*+*+*+*+*+*+*+*+* sub_CAT() ===== ' + str(indx_1))
    r = requests.get(url_Main, headers=headers)
    r.encoding = 'utf-8'
    xbmc.log('*************** СВЯЗЬ ' + str(r), xbmc.LOGDEBUG)
    soup = BeautifulSoup(r.text, 'html.parser', parse_only=SoupStrainer('div', id='content'))
    sub_cat = soup.find_all('h3')[indx_1]('a')

    if indx_1 == 2 or indx_1 == 3:
        db_sub_cat = []
        #l = re.split('\s', sub_cat[0:len(sub_cat)-48])
        #l = list(filter (None, l))
        #xbmc.log('*********//////////////// ЗНАЧЕНИЕ L ' + str(len(l)), xbmc.LOGDEBUG)
        for i in sub_cat[0:len(sub_cat)-48]:
            db_sub_cat.append ({'title': i.text})
        for i in db_sub_cat:
            add_main_CAT(i['title'], url_Main, 0, 'DefaultVideo.png')
    xbmcplugin.endOfDirectory(addon_handle)


def video_SER(indx_5):
    #if DEBUG:
    #    log('*+*+*+*+*+*+*+*+*+*+*+*+*+*+* sub_CAT() ===== ' + str(indx_1))
    r = requests.get(url_Main, headers=headers)
    r.encoding = 'utf-8'
    xbmc.log('*************** СВЯЗЬ ' + str(r), xbmc.LOGDEBUG)
    soup = BeautifulSoup(r.text, 'html.parser', parse_only=SoupStrainer('div', id='content'))
    video_ser = soup.find_all('h3')[indx_5]('a')
    xbmc.log('*************** СВЯЗЬ ' + str(video_ser), xbmc.LOGDEBUG)

    if indx_5 == 4 or indx_5 == 6 or indx_5 == 7:
        db_ser = []
        #xbmc.log('*********//////////////// ЗНАЧЕНИЕ L ' + str(len(l)), xbmc.LOGDEBUG)
        for i in video_ser:
            s = re.split('/', i.text.capitalize())
            db_ser.append ({'title': s[0]})
            xbmc.log('*********//////////////// ЗНАЧЕНИЕ СПИСКА ' + str(db_ser), xbmc.LOGDEBUG)
        for i in db_ser:
            add_main_CAT(i['title'], url_Main, 0, 'DefaultVideo.png')
    elif indx_5 == 5:
        db_ser = []
        for i in video_ser[0:len(video_ser)-37]:
            s = re.split('/', i.text)
            db_ser.append ({'title': s[0]})
            xbmc.log('*********//////////////// ЗНАЧЕНИЕ СПИСКА ' + str(db_ser), xbmc.LOGDEBUG)
        for i in db_ser:
            add_main_CAT(i['title'], url_Main, 0, 'DefaultVideo.png')
    elif indx_5 == 8:
        db_ser = []
        for i in video_ser:
            s = i.text.title()
            db_ser.append ({'title': s})
        for i in db_ser:
            add_main_CAT(i['title'], url_Main, 0, 'DefaultVideo.png')

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



def log(description):
    xbmc.log("[ADD-ON] '{} v{}': {}".format(_plugin, _version, description), xbmc.LOGNOTICE)

if mode == '1name=Next PageEE':
    xbmc.log('******* ///////////////////// значение MODE ::::::::::: ******* ' + str(mode), xbmc.LOGDEBUG)


if mode == None:
    pass
elif str(mode[0]).split('=')[1] == 'Зарубежные фильмы':
    sub_CAT(2)
elif str(mode[0]).split('=')[1] == 'Наши фильмы':
    sub_CAT(3, 30, 29)
elif str(mode[0]).split('=')[1] == 'Зарубежные сериалы':
    video_SER(4)
elif str(mode[0]).split('=')[1] == 'Наши сериалы':
    video_SER(5)
elif str(mode[0]).split('=')[1] == 'Телевизор':
    video_SER(6)
elif str(mode[0]).split('=')[1] == 'Мультипликация':
    video_SER(7)
elif str(mode[0]).split('=')[1] == 'Аниме':
    video_SER(8)


if __name__ == '__main__':
    main_CAT()
