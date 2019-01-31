import mido
import urllib.request
from bs4 import BeautifulSoup
import requests
import os

mid=mido.MidiFile("MIDI_sample.mid")
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))

    for msg in track:
    	print(msg)
    	if msg.is_meta:
    		print(msg.type)



def download_mid_file(liste_url):
    os.system("mkdir database")
    for url in liste_url:
        urllib.request.urlretrieve(url, './database/{}'.format(url.split('/')[-1]))


def get_mid_file_url():
    url="http://www.piano-midi.de/midi_files.htm"
    rep=requests.get(url=url)
    soup=BeautifulSoup(rep.text,'html.parser')
    s=list(soup.find_all('tr',attrs={"class":"midi"}))
    liste_url=[]
    for item in s[1:]:
        liste_url.append('http://www.piano-midi.de/'+str(item.find('a')['href']))
    all_dl=[]
    for item in liste_url:
        rep=requests.get(url=item)
        soup=BeautifulSoup(rep.text,'html.parser')
        s=list(soup.find_all('table',attrs={"class":"midi"}))# ['href']
        for table in s:
            s2=list(table.find_all('a',attrs={"class":"navi"}))
            for a in s2:
                all_dl.append('http://www.piano-midi.de/'+str(a['href']))
    return all_dl
def get_mid_file():
    print("getting url")
    liste_url=get_mid_file_url()
    print("downloading...")
    download_mid_file(liste_url)


if __name__=="__main__":
    get_mid_file()


"""url="http://www.piano-midi.de/midi_files.htm"
rep=requests.get(url=url)
soup=BeautifulSoup(rep.text,'html.parser')
s=list(soup.find_all('tr',attrs={"class":"midi"}))
liste_url=[]
for item in s[1:]:
    liste_url.append('http://www.piano-midi.de/'+str(item.find('a')['href']))
all_dl=[]
for item in liste_url:
    rep=requests.get(url=item)
    soup=BeautifulSoup(rep.text,'html.parser')
    s=list(soup.find_all('table',attrs={"class":"midi"}))# ['href']
    for table in s:
        s2=list(table.find_all('a',attrs={"class":"navi"}))
        for a in s2:
            all_dl.append('http://www.piano-midi.de/'+str(a['href']))

print("{}".format(len(all_dl)))"""