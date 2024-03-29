import requests
from lxml import etree
import pandas as pd
import numpy as np

def FinalUrl(start,arrive):
    link = 'http://www.tcl.fr/Me-deplacer/Itineraires/Mon-trajet/(_rd)/1560947891554?ItinDepart='+start+'&valueItinDepart='+start+'&valueItinDepartFavoris='+start+'&ItinArrivee='+arrive+'&valueItinArrivee='+arrive+'&valueItinArriveeFavoris='+arrive+'&radioTiming=DepartImm&DepartMinute=00&radioSens=HorPartir&radioOption=OptionArrivRapid&no_js=no_js&lancer_recherche=Rechercher'
    Url= requests.get(link)
    X = False
    print(Url.status_code)
    if Url.status_code == 200:
        X = True
    return Url, X
    #根据不同的起始站，生成对应的搜索链接

def Time(Url):
    html = Url.content.decode('utf-8')
    dom_tree = etree.HTML(html)
    links = dom_tree.xpath('//*[@id="COLONNE-L"]/div[2]/span[3]')
    time = -1
    try:
        time = links[0].xpath('string(.)').strip()
    except IndexError:
        pass
    return time
    #把时间提取出出来，然后再变成数字输出

if __name__ == '__main__':
    Station=['Boutasse-Camille+Rousset%2C+Bron',
                'Boutasse-Camille+Rousset%2C+Bron',
                'De+Tassigny-Curial%2C+Bron',
                'Essarts-Iris%2C+Bron',
                'Essarts-Iris%2C+Bron',
                'Europe-Université%2C+Bron',
                'Hôtel+de+Ville+- Bron%2C+Bron',
                'Hôtel+de+Ville+- Bron%2C+Bron',
                'Les+Alizés%2C+Bron',
                'Les+Alizés%2C+Bron',
                'Lycée+Jean-Paul+Sartre%2C+Bron',
                'Parc+du+Chêne%2C+Bron',
                'Parilly-Université+—+Hippodrome%2C+Bron',
                'Rebufer%2C+Bron',
                'Cuire%2C+Caluire-et-Cuire',
                'Eurexpo%2C+Chassieu',
                'Eurexpo 2 %2C+Chassieu',
                'René+Cassin %2C+Chassieu',
                'Décines-Centre%2C+Décines-Charpieu',
                'Décines-Grand+Large%2C+Décines-Charpieu',
                'Hôpital+Feyzin+Vénissieux%2C+Feyzin et Vénissieux',
                'Croix-Paquet%2C+Lyon',
                'Hôtel+de+Ville-Louis+Pradel%2C+Lyon',
                'Croix-Rousse%2C+Lyon',
                'Ampère-Victor+Hugo%2C+Lyon',
                'Bellecour%2C+Lyon',
                'Cordeliers%2C+Lyon',
                'Hôtel+de+Région-Montrochet%2C+Lyon',
                'Musée+des+Confluences%2C+Lyon',
                'Perrache%2C+Lyon',
                'Perrache%2C+Lyon',
                'Perrache%2C+Lyon',
                'Sainte-Blandine%2C+Lyon',
                'Suchet%2C+Lyon',
                'Archives+départementales%2C+Lyon',
                'Dauphiné-Lacassagne%2C+Lyon',
                'Gare+Part-Dieu-Villette%2C+Lyon',
                'Gare+Part-Dieu-Villette%2C+Lyon',
                'Gare+Part-Dieu-Vivier+Merle%2C+Lyon',
                'Gare+Part-Dieu-Vivier+Merle%2C+Lyon',
                'Liberté%2C+Lyon',
                'Palais+de+Justice-Mairie+du 3e%2C+Lyon',
                'Part-Dieu-Servient%2C+Lyon',
                'Place+Guichard-Bourse+du+Travail%2C+Lyon',
                'Reconnaissance-Balzac%2C+Lyon',
                'Saxe-Préfecture%2C+Lyon',
                'Manufacture-Montluc%2C+Lyon',
                'Garibaldi%2C+Lyon',
                'Guillotière-Gabriel+Péri%2C+Lyon',
                'Saxe-Gambetta%2C+Lyon',
                'Grange+Blanche%2C+Lyon',
                'Monplaisir-Lumière%2C+Lyon',
                'Sans+Souci%2C+Lyon',
                'Hénon%2C+Lyon',
                'Vieux+Lyon-Cathédrale+Saint-Jean%2C+Lyon',
                'Brotteaux%2C+Lyon',
                'Collège+Bellecombe%2C+Lyon',
                'Collège+Bellecombe%2C+Lyon',
                'Foch%2C+Lyon',
                'Masséna%2C+Lyon',
                'Thiers-Lafayette%2C+Lyon',
                'Thiers-Lafayette%2C+Lyon',
                'Centre+Berthelot%2C+Lyon',
                'Debourg%2C+Lyon',
                'Debourg%2C+Lyon',
                'ENS+Lyon%2C+Lyon',
                'Garibaldi-Berthelot%2C+Lyon',
                'Guillotière-Gabriel+Péri%2C+Lyon',
                'Halle+Tony-Garnier%2C+Lyon',
                'Jean+Macé%2C+Lyon',
                'Jean+Macé%2C+Lyon',
                'Jet+d%27Eau-Mendès+France%2C+Lyon',
                'Place+Jean+Jaurès%2C+Lyon',
                'Quai+Claude-Bernard%2C+Lyon',
                'Route+de+Vienne%2C+Lyon',
                'Rue+de+l%27Université%2C+Lyon',
                'Saint-André%2C+Lyon',
                'Stade+de+Gerland%2C+Lyon',
                'Ambroise+Paré%2C+Lyon',
                'Ambroise+Paré%2C+Lyon',
                'Bachut-Mairie+du 8e%2C+Lyon',
                'États-Unis-Musée+Tony+Garnier%2C+Lyon',
                'États-Unis-Vivani%2C+Lyon',
                'Grange+Blanche%2C+Lyon',
                'Grange+Blanche%2C+Lyon',
                'Jean+XXIII-Maryse+Bastié%2C+Lyon',
                'Jet+d%27Eau-Mendès+France%2C+Lyon',
                'Laënnec%2C+Lyon',
                'Lycée+Colbert%2C+Lyon',
                'Lycée+Lumière%2C+Lyon',
                'Mermoz-Pinel%2C+Lyon',
                'Professeur+Beauvisage-CISL%2C+Lyon',
                'Villon%2C+Lyon',
                'Vinatier%2C+Lyon',
                'Gare+de+Vaise%2C+Lyon',
                'Gorge+de+Loup%2C+Lyon',
                'Valmy%2C+Lyon',
                'Meyzieu-Les+Panettes%2C+Meyzieu',
                'Meyzieu+Gare%2C+Meyzieu',
                'Meyzieu+Z.I.%2C+Meyzieu',
                'Gare+d%27Oullins%2C+Oullins',
                'Alfred+de+Vigny%2C+Saint-Priest',
                'Cordière%2C+Saint-Priest',
                'Esplanade+des+arts%2C+Saint-Priest',
                'Hauts+de+Feuilly%2C+Saint-Priest',
                'Jules+Ferry%2C+Saint-Priest',
                'Parc+Technologique%2C+Saint-Priest',
                'Porte+des+Alpes%2C+Saint-Priest',
                'Saint-Priest -+Bel+Air%2C+Saint-Priest',
                'Saint-Priest -+Hôtel+de+Ville%2C+Saint-Priest',
                'Salvador+Allende%2C+Saint-Priest',
                'Vaulx-en-Velin-La+Soie%2C+Vaulx-en-Velin',
                'Vaulx-en-Velin-La+Soie%2C+Vaulx-en-Velin',
                'Croizat-Paul+Bert%2C+Vénissieux',
                'Darnaise%2C+Vénissieux',
                'Division+Leclerc%2C+Vénissieux',
                'Gare+de+Vénissieux%2C+Vénissieux',
                'Gare+de+Vénissieux%2C+Vénissieux',
                'Herriot-Cagne%2C+Vénissieux',
                'Joliot+Curie-Marcel+Sembat%2C+Vénissieux',
                'La+Borelle%2C+Vénissieux',
                'Lénine-Corsière%2C+Vénissieux',
                'Lycée+Jacques+Brel%2C+Vénissieux',
                'Marcel+Houël-Hôtel+de+Ville%2C+Vénissieux',
                'Maurice+Thorez%2C+Vénissieux',
                'Parilly%2C+Vénissieux',
                'Vénissy%2C+Vénissieux',
                'Bel+Air-Les+Brosses%2C+Villeurbanne',
                'Charpennes-Charles+Hernu%2C+Villeurbanne',
                'Charpennes-Charles+Hernu%2C+Villeurbanne',
                'Charpennes-Charles+Hernu%2C+Villeurbanne',
                'Condorcet%2C+Villeurbanne',
                'Condorcet%2C+Villeurbanne',
                'Croix-Luizet%2C+Villeurbanne',
                'Cusset%2C+Villeurbanne',
                'Flachet-Alain+Gilles%2C+Villeurbanne',
                'Gare+de+Villeurbanne%2C+Villeurbanne',
                'Gratte-Ciel%2C+Villeurbanne',
                'INSA -+Einstein%2C+Villeurbanne',
                'IUT-Feyssine%2C+Villeurbanne',
                'La+Doua -+Gaston+Berger%2C+Villeurbanne',
                'La+Doua -+Gaston+Berger%2C+Villeurbanne',
                'Laurent+Bonnevay%2C+Villeurbanne',
                'Tonkin%2C+Villeurbanne',
                'Tonkin%2C+Villeurbanne',
                'République-Villeurbanne%2C+Villeurbanne',
                'Université+Lyon+1%2C+Villeurbanne',
                'Université+Lyon+1%2C+Villeurbanne']
    Num=len(Station)
    print(Num)
    matrix = pd.DataFrame(np.identity(len(Station)), columns=Station, index=Station)
    for n in range(Num):
        start = Station[n]
        for m in range(Num):
            arrive = Station[m]
            if arrive != start:
                #print(start,arrive)
                Url, X =FinalUrl(start,arrive )
                if X == True :
                    time = Time(Url)
                    matrix.ix[m,n]=time
                    matrix.ix[n,m]=time
                    print(start,arrive,time)
                else:
                    matrix.ix[n,m]=998
                    #print(n,m,998)
            else:
                #print(start,arrive)
                matrix.ix[n,m] = 0
                #print(n,m,)
    print(matrix)
    matrix.to_excel('result.xlsx',sheet_name = 'Sheet1')

    #建立不同站点形成的矩阵，然后把时间提取出来，放进去


