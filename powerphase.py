import requests as re 
from random import getrandbits

link = 'https://docs.google.com/forms/d/e/1FAIpQLSepeZK22LZgura_2wMZ2vNkv3mhjnmRAUpC_ex123lal1Fv-A/viewform?c=0&w=1'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def main(limit):
	for i in range(1, limit):
		payload = {
			'entry.2111423237' : 'YOUR NAME', # ENTER YOUR FULL NAME HERE
			'entry.2648839' : 'YOUREMAIL+{}@gmail.com'.format(getrandbits(40)), # ENTER YOUR GMAIL WHERE IT SAYS YOUREMAIL. DO NOT EDIT THE REST OF IT
			'entry.1712332735' : 'Manhattan', # CHANGE MANHATTAN TO EITHER MANHATTAN, WOMEN'S OR MIAMI
			'entry.473600588' : '8', # CHANGE THE SIZE FROM 8-14. ONLY HALF SIZES ARE 8, 8.5, 9, 9.5, 10, 10.5, 11, AND 11.5
			'fvv' : '1', # DON'T CHANGE
			'draftResponse' : '[null,null,"-8673160571613629000"] ', # DON'T CHANGE
			'pageHistory' : '0', # DON'T CHANGE
			'fbzx' : '-8673160571613629000' # DON'T CHANGE
		}

		re.post(link, data=payload, headers=headers)
		print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(10) # HERE ENTER IN ANY NUMBER