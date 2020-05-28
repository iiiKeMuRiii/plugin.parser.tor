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

url_Main = 'http://222njbta.ihg.xrutor.org'
cat = '/categories/'
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
           }

addon_handle = int(sys.argv[1])
args = urllib.parse.parse_qs(sys.argv[2][1:])
tags = urllib.parse.parse_qs(sys.argv[3][1:])
mode = args.get('mode', None)
page = args.get('page', None)
part_url = args.get('part_url', None)
tag_part = args.get('tag_part', None)


def request(link):
    r = requests.get(url_Main + link, headers=headers)
    r.encoding = 'utf-8'
    return r.text

def get_total_page(pages):
    r = requests.get(pages, headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser', parse_only=SoupStrainer('div', id='index'))
    m = soup.find_all('a')[-1]
    return m.text

def main_CAT():
    if DEBUG:
        log('*+*+*+*+*+*+*+*+*+*+*+*+*+*+* main_cat() ')
    xbmc.log('*************** Ссылка ' + str(mode), xbmc.LOGDEBUG)
    soup = BeautifulSoup(request(cat), 'html.parser', parse_only=SoupStrainer('div', id='content'))
    main_cat = soup.find_all('h2')[2:9]
    db_main_cat = []
    for i in range(0, 7):
        db_main_cat.append ({'title': main_cat[i].text,
                             'index': i})
    xbmc.log('*************** TEST ' + str(db_main_cat), xbmc.LOGDEBUG)
    for l in db_main_cat:
        add_CAT(l['title'], url_Main + cat, 0, 'tag', 'DefaultVideo.png')
    xbmcplugin.endOfDirectory(addon_handle)


def sub_CAT(indx_1, tag_link):
    if DEBUG:
        log('*+*+*+*+*+*+*+*+*+*+*+*+*+*+* sub_CAT() ===== ')
    soup = BeautifulSoup(request(cat), 'html.parser', parse_only=SoupStrainer('div', id='content'))
    sub_cat = soup.find_all('h3')[indx_1]('a') ## выборка категории - фильмы, сериалы, мультики...
    if indx_1 == 2 or indx_1 == 3 or indx_1 == 8:
        db_sub_cat = []
        for i in sub_cat[0:len(sub_cat)-48]:
            db_sub_cat.append ({'title': i.text})
        for i in db_sub_cat:
            add_CAT(i['title'], url_Main + cat, indx_1, tag_link, 'DefaultVideo.png')

    if indx_1 == 4 or indx_1 == 5 or indx_1 == 6  or indx_1 == 7:
        db_ser = []
        for i in sub_cat:
            s = re.split('/', i.text.capitalize())
            db_ser.append ({'title': s[0]})
        for i in db_ser:
            add_CAT(i['title'], url_Main + cat, indx_1, tag_link, 'DefaultVideo.png')
    xbmcplugin.endOfDirectory(addon_handle)
    xbmcgui.Dialog().ok('sub_CAT!', str(mode))
    #video_link()


def video_link():
    if DEBUG:
        log('*+*+*+*+*+*+*+*+*+*+*+*+*+*+* video_link() ===== ')
    #r = requests.get(url_Main + link, headers=headers)
    #r.encoding = 'utf-8'
    #xbmc.log('*************** СВЯЗЬ ' + str(r), xbmc.LOGDEBUG)
    #xbmcgui.Dialog().ok('TEST_CAT!!!!!!', 'ЗНАЧЕНИЕ ' + str(test_cat))
    #xbmcgui.Dialog().ok('Warning!', import_films + str(mode[0]).split('=')[1] + '/')
    #tagg = tag
    page = 0
    total_pages = get_total_page(url_Main + '/search/' + str(page) + part_url[0] + str(mode[0]).split('=')[1] + '/')
    xbmcgui.Dialog().ok('video_link MODE!', str(page))
                                #'search/0/1/010/0/'

    #if indx_1 == 2 or indx_1 == 3 or indx_1 == 8:
    soup = BeautifulSoup(request('/search/' + str(page) + part_url[0] + str(mode[0]).split('=')[1] + '/'), 'html.parser', parse_only=SoupStrainer('div', id='index'))
    db_mov_lnk = []
    #xbmcgui.Dialog().ok('Warning!', str(mode[0]).split('=')[1])
    #xbmc.log('******* ::::::::::::: addCatt ::::::::::: ******* ' + str(soup), xbmc.LOGDEBUG)


    for i in range(1, len(soup.find_all('tr'))):
        pars_list = soup.find_all('tr')[i]
        list_mov = pars_list.findAll('a')
        if len(list_mov) == 1:
            db_mov_lnk.append ({'title': list_mov[0].text})
        elif len(list_mov) == 2:
            db_mov_lnk.append ({'title': list_mov[1].text})

    for i in db_mov_lnk:
        add_CAT(i['title'], url_Main + '/search/' + str(page) + part_url[0] + str(mode[0]).split('=')[1] + '/', 1, 'tag', 'DefaultVideo.png')
                                      # search/ + page/ + /1/010/0/
    #xbmcgui.Dialog().ok('Warning!', str(sys.argv[0]) + str(sys.argv[1]) + str(sys.argv[2]))
    #add_CAT('Next Page', url_Main.replace(url_Main, 'http://37.1.201.32/tag/1/Арт-хаус/2'), 1, 'DefaultVideo.png')
    #xbmcgui.Dialog().ok('Warning!', url_Main)
    #xbmcplugin.endOfDirectory(addon_handle)
    #xbmcgui.Dialog().ok('video_link!', str(mode))

    #for i in range(1, int(total_pages)):
    z = soup.find('b').find('a')['href']
    xbmcgui.Dialog().ok('video_link!', url_Main + z)
    add_CAT('Next Page', 'http://222njbta.ihg.xrutor.org/search/1/1/010/0/Арт-хаус', 1, 'tag', 'DefaultVideo.png')
    video_link()
    xbmcplugin.endOfDirectory(addon_handle)




def file_torrent():
    if DEBUG:
        log('*+*+*+*+*+*+*+*+*+*+*+*+*+*+* file_torrent() ===== ')
    #r = requests.get(url_Main + link, headers=headers)
    #r.encoding = 'utf-8'
    #xbmc.log('*************** СВЯЗЬ ' + str(r), xbmc.LOGDEBUG)
    #xbmcgui.Dialog().ok('TEST_CAT!!!!!!', 'ЗНАЧЕНИЕ ' + str(test_cat))
    #xbmcgui.Dialog().ok('Warning!', import_films + str(mode[0]).split('=')[1] + '/')
    #tagg = tag

    xbmcgui.Dialog().ok('video_link MODE!', str(part_url[0]))
                                #'search/0/1/010/0/'
    page = 0
    #if indx_1 == 2 or indx_1 == 3 or indx_1 == 8:
    soup = BeautifulSoup(request('search/' + str(page) + part_url[0] + str(mode[0]).split('=')[1] + '/'), 'html.parser', parse_only=SoupStrainer('div', id='index'))
    db_mov_lnk = []
    #xbmcgui.Dialog().ok('Warning!', str(mode[0]).split('=')[1])
    #xbmc.log('******* ::::::::::::: addCatt ::::::::::: ******* ' + str(soup), xbmc.LOGDEBUG)


    for i in range(1, len(soup.find_all('tr'))):
        pars_list = soup.find_all('tr')[i]
        list_mov = pars_list.findAll('a')
        if len(list_mov) == 1:
            db_mov_lnk.append ({'title': list_mov[0].text})
        elif len(list_mov) == 2:
            db_mov_lnk.append ({'title': list_mov[1].text})

    for i in db_mov_lnk:
        add_CAT(i['title'], url_Main + 'search/' + str(page) + part_url[0] + str(mode[0]).split('=')[1] + '/', 1, 'tag', 'DefaultVideo.png')
                                      # search/ + page/ + /1/010/0/
    #xbmcgui.Dialog().ok('Warning!', str(sys.argv[0]) + str(sys.argv[1]) + str(sys.argv[2]))
    #add_CAT('Next Page', url_Main.replace(url_Main, 'http://37.1.201.32/tag/1/Арт-хаус/2'), 1, 'DefaultVideo.png')
    #xbmcgui.Dialog().ok('Warning!', url_Main)

    xbmcplugin.endOfDirectory(addon_handle)
    xbmcgui.Dialog().ok('video_link!', str(mode))

def add_CAT(title, url, mode, part_url, iconimage):
    u=sys.argv[0]+"?url="+urllib.parse.quote_plus(url)+"&part_url="+str(part_url)+"&mode="+str(mode)+"name="+urllib.parse.quote_plus(title)
    ok = True
    liz = xbmcgui.ListItem(title)
    ok = xbmcplugin.addDirectoryItem(addon_handle, url=u, listitem=liz, isFolder=True) #*****************????????????????? правильный адрес ?????знак ? и =

    #liz.setArt ({ 'iconimage': 'http://c.radikal.ru/c20/2003/79/d0f12ddef3e1.jpg' })

    #xbmcgui.Dialog().ok('Warning!', url)
    #xbmc.log('******* ::::::::::::: MODE ::::::::::: ******* ' + str(mode), xbmc.LOGDEBUG)
    xbmc.log('******* ::::::::::::: addCatt ::::::::::: ******* ' + u, xbmc.LOGDEBUG)
    return ok

######## plugin://plugin.parser.tor/?url=http%3A%2F%2F37.1.201.32%2Fcategories%2F&mode=1name=%D0%AD%D1%80%D0%BE%D1%82%D0%B8%D0%BA%D0%B0
def add_CAT2(title, url, mode, iconimage):
    u=sys.argv[0]+"?url="+urllib.parse.quote_plus(url)+"&mode="+str(mode)+"name="+urllib.parse.quote_plus(title)
    ok = True
    liz = xbmcgui.ListItem(title)
    ok = xbmcplugin.addDirectoryItem(addon_handle, url=u, listitem=liz, isFolder=True) #*****************????????????????? правильный адрес ?????знак ? и =

    #liz.setArt ({ 'iconimage': 'http://c.radikal.ru/c20/2003/79/d0f12ddef3e1.jpg' })

    #xbmcgui.Dialog().ok('Warning!', url)
    #xbmc.log('******* ::::::::::::: MODE ::::::::::: ******* ' + str(mode), xbmc.LOGDEBUG)
    xbmc.log('******* ::::::::::::: addCatt ::::::::::: ******* ' + u, xbmc.LOGDEBUG)
    return ok

def log(description):
    xbmc.log("[ADD-ON] '{} v{}': {}".format(_plugin, _version, description), xbmc.LOGNOTICE)

if mode == '1name=Next PageEE':
    xbmc.log('******* ///////////////////// значение MODE ::::::::::: ******* ' + str(mode), xbmc.LOGDEBUG)


if mode == None:
    pass
elif str(mode[0]).split('=')[1] == 'Зарубежные фильмы':     # tag = search/0/1/010/0/:      search/  +  page/ +  1/010/0/
    sub_CAT(2, '/1/010/0/')
elif str(mode[0]).split('=')[1] == 'Наши фильмы':           # tag = search/ 0 /5/010/0/
    sub_CAT(3, '/5/010/0/')
elif str(mode[0]).split('=')[1] == 'Зарубежные сериалы':    # tag = search/ 0/ 4/0/0/
    sub_CAT(4, '/4/0/0/')
elif str(mode[0]).split('=')[1] == 'Наши сериалы':          # tag = search/ 0/ 16/0/0/
    tag_link = 'search/0/16/0/0/'
    sub_CAT(5, '/16/010/0/')
elif str(mode[0]).split('=')[1] == 'Телевизор':             # tag = search/ 0/ 6/0/0/
    tag_link = 'search/0/6/0/0/'
    sub_CAT(6)
elif str(mode[0]).split('=')[1] == 'Мультипликация':        # tag = tag/7/
    tag_link = 'tag/7/'
    sub_CAT(7)
elif str(mode[0]).split('=')[1] == 'Аниме':                 # tag = search/ 0/ 10/010/0/
    sub_CAT(8, '/10/010/0/')
elif int(mode[0].split('=')[0][-5]) == 2:
    tag_part = 'tag/1/'
    video_link()
elif int(mode[0].split('=')[0][-5]) == 3:
    video_link()
elif int(mode[0].split('=')[0][-5]) == 4:
    video_link()
elif int(mode[0].split('=')[0][-5]) == 5:
    video_link()
elif int(mode[0].split('=')[0][-5]) == 6:
    video_link()
elif int(mode[0].split('=')[0][-5]) == 7:
    video_link()
elif int(mode[0].split('=')[0][-5]) == 8:
    video_link()


if __name__ == '__main__':
    main_CAT()
