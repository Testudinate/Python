import urllib.request
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Boxing_at_the_1948_Summer_Olympics_%E2%80%93_Men%27s_heavyweight"
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html)
    table = soup.find('table',style="font-size: 90%; margin:1em 2em 1em 1em;")
    rownum = 1
    text2 =''
    r=''
    g = 0
    m = 0
    lis = []
    k = 0
    k1 = 0
    kk = 0
    for item in table.find_all('tr'):
        td = item.find_all('td')
        td2 = item.find_all('td', align ='center') 
        row = [i.get_text() for i in td]
        row2 = [i2.get_text() for i2 in td2]
        for j in range(0,len(row)):
            p = {'rownum':rownum,
                 'name':row,
                 'rez': row2
                 }
        rownum = rownum + 1
        #if row!='':
            #lis.append(p)
        #print(p)
        #if p['rownum']==1:
            #for h in p['name']:
                #k = k + 1
                #l = len(p['name'])
                #if h !='':
                    #print(p['rownum'],h,k,l)#,type(h))
        k = 0
        k11 = 0
        if p['rownum']>=4:
            for h in p['name']:           
                k = k + 1
                for h2 in p['rez']:
                    text = h2       
                if h!='' and len(h)>5 and h!='Third place': #and h2!='Third place' :
                    k1 = k1 + 1
                    
                    if kk == p['rownum'] and k1 == 2:
                        text2 = p['rez'][1] 
                        p['rownum'] = p['rownum']
                    elif kk == p['rownum'] and k1 ==1:
                        text2 = p['rez'][0] 
                        p['rownum'] = p['rownum']
                    else:
                        text2 = p['rez'][0]
                        
                    if k == 2:
                        r = 'Round of 32'
                    elif k ==6:
                        r = 'Round of 16'
                        g = g + k
                    elif k == 7 and (g==12 or g/12==3 or g/12==5 or g/12==7):
                        r = 'Quarter-finals'
                        if m ==1:
                            g = 6
                            m = m + 1
                    elif k == 7 and (g==24 or g/24==3):
                        r = 'Semi-finals'
                    elif k ==7 and g/12==4:
                        r = 'Final'
                    elif k == 9 or k == 10:
                        r = 'Third place'
                        
                    hname = h.split('(')[0]
                    hcountry = h.split('(')[1].replace(')','')
                    #print(p['rownum'],h,text2,k11,k,r,g)
                    lis.append(r+str(';')+hname+str(';')+hcountry+str(';')+text2)
                    kk = p['rownum']
                    k11 = k1
                r = ''
        m = 0 #обнуление параметра m
        k = 0 #обнуление параметра k 
        k1 = 0 #обнуление параметра k1
    f = open('c:\\Arkadium\\result.csv', 'a', encoding='utf-8')
    f.write(str('Round name;Boxer name;Country;Result')+'\n')
    for index in range(0,len(lis)):#а - параметр позволяет не создавать каждый раз файл, если он есть уже по указанному пути; дозапись данных
       f.write(str(lis[index])+'\n')
    f.close()
def main():
        parse(get_html(url))

if __name__ == '__main__':
    main()
