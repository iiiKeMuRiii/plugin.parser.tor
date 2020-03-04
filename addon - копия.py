# -*- coding: utf-8 -*-
"""
    IMDB Trailers Kodi Addon
    Copyright (C) 2018 gujal
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Imports
import html.parser
from bs4 import BeautifulSoup, SoupStrainer
import requests
import lxml

url = 'http://filmitorrent.biz'
r = requests.get(url)

def main():
    soup = BeautifulSoup(r.text, 'lxml', parse_only=SoupStrainer('div', id='dle-content'))
    pages = soup.find('div', class_='navigation')
    for pgs in pages:
        pg = soup.find('a')
    #total_pages = pages.split('/')[2]
    print(pages)



    
if __name__ == '__main__':
  main()
