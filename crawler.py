import requests
from bs4 import BeautifulSoup

genre = ['action','comedy','animation']
fp = open('movies','w')
fp.write("List prepared using IMDB\n\n")

def crawler ():
	for gen in genre:
		fp.write("\n\nTop 100 "+gen+" movies\n")
		i=1
		for page in range(1,3):
			url = 'http://www.imdb.com/search/title?genres='+str(gen)+'&title_type=feature&num_votes\
			=100000,&sort=user_rating,desc&page='+str(page)+'&ref_=adv_nxt'
			source_code = requests.get(url)
			plain_text = source_code.text
			soup = BeautifulSoup(plain_text, 'html.parser')

			for link in soup.findAll('h3',class_="lister-item-header"):
					j = link.find('a')
					ttle = j.string
					fp.write("{}.".format(i)+ttle+'\n')
					i+=1

crawler()
print("Done!!")