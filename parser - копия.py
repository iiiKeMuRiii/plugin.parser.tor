#import requests
#import lxml
#import re
#from bs4 import BeautifulSoup, SoupStrainer

# Imports
from future import standard_library
from xbmcplugin import addDirectoryItem
standard_library.install_aliases()
from builtins import str
from builtins import object
import re
import sys
import urllib.parse
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


CONTENT_URL = 'https://www.imdb.com/trailers/'
SHOWING_URL = 'https://www.imdb.com/movies-in-theaters/'
COMING_URL = 'https://www.imdb.com/movies-coming-soon/{}-{:02}'
DETAILS_PAGE = "https://m.imdb.com/videoplayer/{}"
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17'


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


url_Main = 'http://filmitorrent.biz/'
url_2 = 'http://filmitorrent.biz/triller/3499-neogranennye-almazy-2019.html'
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
           }

addon_handle = int(sys.argv[1])
#session = requests.session()
#request = session.get(url, headers=headers)


class Main(object):
    def __init__(self):
        if ('action=komedia' in sys.argv[2]) or ('action=boevik' in sys.argv[2]):
            self.films_test()
        elif ('action=fantastika' in sys.argv[2]) or ('action=melodrama' in sys.argv[2]):
            self.films_title()
        elif ('action=fantasy' in sys.argv[2]) or ('action=mult' in sys.argv[2]):
            self.films_title()
        elif ('action=triller' in sys.argv[2]):
            self.films_title()
        elif ('action=anime' in sys.argv[2]) or ('action=biografy' in sys.argv[2]):
            self.dis_cat()
        elif ('action=western' in sys.argv[2]) or ('action=military' in sys.argv[2]):
            self.dis_cat()
        elif ('action=detectiv' in sys.argv[2]) or ('action=documental' in sys.argv[2]):
            self.dis_cat()
        elif ('action=drama' in sys.argv[2]) or ('action=history' in sys.argv[2]):
            self.dis_cat()
        elif ('action=criminal' in sys.argv[2]) or ('action=melodramatic' in sys.argv[2]):
            self.dis_cat() 
        elif ('action=music' in sys.argv[2]) or ('action=musical' in sys.argv[2]):
            self.dis_cat()
        elif ('action=our' in sys.argv[2]) or ('action=adventure' in sys.argv[2]):
            self.dis_cat()
        elif ('action=family' in sys.argv[2]) or ('action=Series' in sys.argv[2]):
            self.dis_cat()
        elif ('action=horror' in sys.argv[2]):
            self.dis_cat()
        elif ('action=act1ion' in sys.argv[2]):
            self.play()
        elif ('action=wester2n' in sys.argv[2]):
            self.films_title()
        else:
            self.CATEGORY()

# Категории фильмов ***************************

    def CATEGORY(self):
        url = ''
        category = [{'title':'Аниме', 'key':'anime'},
                    {'title':'Биография', 'key':'biografy'},
                    {'title':'Боевик', 'key':'action'},
                    {'title':'Вестерн', 'key':'western'},
                    {'title':'Военный', 'key':'military'},
                    {'title':'Детектив', 'key':'detectiv'},
                    {'title':'Документальный', 'key':'documental'},
                    {'title':'Драма', 'key':'drama'},
                    {'title':'История', 'key':'history'},
                    {'title':'Комедия', 'key':'comedy'},
                    {'title':'Криминал', 'key':'criminal'},
                    {'title':'Мелодрама', 'key':'melodramatic'},
                    {'title':'Музыка', 'key':'music'},
                    {'title':'Мультфильм', 'key':'cartoon'},
                    {'title':'Мюзикл', 'key':'musical'},
                    {'title':'Наше кино', 'key':'our'},
                    {'title':'Приключения', 'key':'adventure'},
                    {'title':'Семейный', 'key':'family'},
                    {'title':'Сериалы', 'key':'Series'},
                    {'title':'Спорт', 'key':'sport'},
                    {'title':'Триллер', 'key':'thriller'},
                    {'title':'Ужасы', 'key':'horror'},
                    {'title':'Фантастика', 'key':'fantastic'},
                    {'title':'Фэнтези', 'key':'fantasy'}]
        
        
        for i in category:
            list = xbmcgui.ListItem(i['title'])
            if i['key'] == 'comedy':
                #l = ('komedia')
                url = sys.argv[0] + '?' + urllib.parse.urlencode({'action': 'komedia'})
            elif i['key'] == 'action':
                url = sys.argv[0] + '?' + urllib.parse.urlencode({'action': 'boevik'})
                xbmc.log('*************** КАТЕГОРИЯ::::::: *********************** ' + str(url), xbmc.LOGDEBUG)
                #url = sys.argv[0] + '?' + urllib.parse.urlencode({'action': 'list2', 'key': i['key']})
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list, isFolder=True)           
        xbmcplugin.setContent(int(sys.argv[1]), 'addons')
        xbmcplugin.endOfDirectory(addon_handle)
        return i
       

    def dis_cat(self):
        xbmcgui.Dialog().ok('Warning!', 'Категория отключена') 


    def test_url(self):
        #url = 'http://filmitorrent.biz/'
        #l = url
        #request = session.get(url)
        l = sys.argv[2]             # возвращает выбраную категорию (нужно порезать)
        #soup = BeautifulSoup(request.content, 'html.parser', parse_only=SoupStrainer('div', id='dle-content'))
        xbmcgui.Dialog().ok('Title', l + '/') 

# Кнопка "Далее"

    def test_2(self):
        x = 'Next Page'
        y = 'Page Next'
        l = sys.argv[2].split('=')[1] + '/'
        url = 'http://filmitorrent.biz/boevik/page/36/'
        request = session.get(url + l, headers=headers)
        #if i['key'] == 'comedy':
        #l = ('komedia')
        #    url = sys.argv[0] + '?' + urllib.parse.urlencode({'action': 'komedia'})
        #xbmcgui.Dialog().ok('Title', sys.argv[2])
        
        #soup = BeautifulSoup(request.content, 'html.parser', parse_only=SoupStrainer('div', id='dle-content'))
        #xbmcgui.Dialog().notification(_plugin, 'Test Function_2', _icon, 3000, False)
        return x, y


# Количество страниц в категории ******************

    def get_total_page(self):
        if DEBUG:
            self.log('get_total_page()')
        
        l = sys.argv[2].split('=')[1] + '/'
        request = session.get(url + l, headers=headers)
        soup = BeautifulSoup(request.content, 'html.parser', parse_only=SoupStrainer('div', class_='navigation'))
        pages = soup.find_all('a')[-2].text
        return int(pages)
    
    
# Заголовки фильмов ******************
    
    def films_title(self):
        url = 'http://filmitorrent.biz/boevik/page/1/'
        url_2 = 'http://filmitorrent.biz/boevik/page/2/'
        l = sys.argv[2].split('=')[1] + '/'

            

        request = session.get(url + l, headers=headers)
        #xbmcgui.Dialog().ok('Title', url + l)
        soup = BeautifulSoup(request.content, 'html.parser', parse_only=SoupStrainer('div', id='dle-content'))    ### Запрос с выборкой категории + страница категории!!! Переменная request!!!
        #desc = BeautifulSoup(request2.content, 'lxml', parse_only=SoupStrainer('div', id='dle-content'))


        dict_sample = {}
    

        db_films = []
        films_name = soup.find_all(class_='post')
        #addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'movies')
    
    #desc_films = desc.find_all(class_='post-story')
        for f_name in films_name:
            title = f_name.find('a').get_text().strip()                             # Название фильма
            href = f_name.find('a')['href']                                         # ссылка на страницу с описанием
            #year = int(f_name.find(class_='post-story').find_all('a')[-1].text)     # год выпуска
            genre = f_name.find(class_='post-data').find('a').text                  # жанр фильма
            country = f_name.find(class_='post-story').find('a').text               # страна
            #description = desc.find('table', class_='res85gtj').find('tbody').find('tr')
            db_films.append ({'title': title,
                              'year': 'year',
                              'plot': genre,
                              'country': country,
                              'url': href
                              })    
            
            for i in db_films:
                #listitem = xbmcgui.ListItem(i['title'])
                li = xbmcgui.ListItem (i['title'], iconImage='DefaultVideo.png')
                li.setInfo(type='video',
                                 infoLabels={'title': db_films[0]['title']})
                #xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
        next_x, next_y = self.test_2()
        #lil = xbmcgui.ListItem(next_x, iconImage='DefaultVideo.png')
        self.addDir('Next PageEE', url.replace(url, url_2), 'DefaultVideo.png')
        xbmc.log('*************** Ссылка ' + url, xbmc.LOGDEBUG)
        #xbmcgui.Dialog().ok('Title', label)
        #xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=lil, isFolder=True)
        xbmcplugin.endOfDirectory(addon_handle)
            
    
    
#***************************************///////////////////////////////////////////////////****************************************    
    
    def getUrl2(url):
        #if familyFilter == "1":
        #    ff = "on"
        #else:
        #    ff = "off"
        #xbmc.log('DAILYMOTION - The url is {}'.format(url), xbmc.LOGDEBUG)
        #headers = {'User-Agent': 'Android'}
        #cookie = {'lang': language,
        #          'ff': ff}
        rr = requests.get(url)
        #r = requests.get(url, headers=headers, cookies=cookie)
        return rr.text
    
    
    
    def test_test(self):
        url = 'http://filmitorrent.biz/boevik/page/'
        page = 1
        r = requests.get(url)
        
        currentPage = page
        nextPage = currentPage + 1
        self.addDir('Next Page' + ' (' + str(nextPage) + ')', url + str(nextPage) + '/', 'listVideos')

        
        
        
        
    
    
    def films_test(self):
        url_main = 'http://filmitorrent.biz/'
        l = sys.argv[2].split('=')[1] + '/'
        url = url_main + l
        u = re.compile('page')
        u2 = u.findall(url)
        xbmc.log('*************** COMPILE::::::::::: ****************** ' + str(u2), xbmc.LOGDEBUG)
                
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser', parse_only=SoupStrainer('div', id='dle-content'))    ### Запрос с выборкой категории + страница категории!!! Переменная request!!!

        db_films = []
        films_name = soup.find_all(class_='post')
        
        for f_name in films_name:
            title = f_name.find('a').get_text().strip()                             # Название фильма
            href = f_name.find('a')['href']                                         # ссылка на страницу с описанием
            
            db_films.append ({'title': title,
                              'url': href
                              })    
            
        for i in db_films:
            self.addDir(i['title'], i['url'], 'DefaultVideo.png')
        
        
        a = 3
        
        if a == 3:                                     # Next Page
            tt = 'plugin://plugin.parser.tor/?url=http://filmitorrent.biz/boevik/page/5/'
            self.addDir('NEXT Page', tt, 'DefaultVideo.png')

        #xbmc.log('*************** Переменная А *********************** ' + url1, xbmc.LOGDEBUG)
        xbmcplugin.endOfDirectory(addon_handle)
        xbmc.log('*************** addon_handle::::::::::: ****************** ' + str(addon_handle), xbmc.LOGDEBUG)
        

# Нужно сформировать каким-то образом адрес URL ************************************
    
    def addDir(self, name, url_main, iconimage):
        l = sys.argv[2].split('=')[1] + '/'
        url_main = url + l
        
        
        
        #urrl = urllib.parse.unquote(url)
        u = sys.argv[0] + urllib.parse.unquote("?url=")
        #xbmc.log('*************** addDir ****************** ' + u, xbmc.LOGDEBUG)
        ok = True
        liz = xbmcgui.ListItem(name)
        zzz = urllib.parse.quote_plus(u, safe='?,=')
        ok = xbmcplugin.addDirectoryItem(addon_handle, url_main, listitem=liz, isFolder=True) #*****************????????????????? правильный адрес ?????знак ? и =

        return ok
    
    
    
    
    
    def addLink(self, name, url):  #*******************/////////////////////////*********************
        u = sys.argv[0] + "?url=" + urllib.parse.quote_plus(url, safe=':,/')
        #xbmc.log('*************** Функция ADDLINK ****************** ' + u, xbmc.LOGDEBUG)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser', parse_only=SoupStrainer('tbody'))
        t = soup.find('b')
        ok = True
        liz = xbmcgui.ListItem(name)
        ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)
        return ok
    
    
    def test(self):
        if DEBUG:
            self.log('test()')
        xbmcgui.Dialog().ok('Title', url)       
        return url
    

            
    def log(self, description):
        xbmc.log("[ADD-ON] '{} v{}': {}".format(_plugin, _version, description), xbmc.LOGNOTICE)
       
            
            


if __name__ == '__main__':
    Main()