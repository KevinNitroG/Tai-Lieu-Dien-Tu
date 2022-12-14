import json
import bs4
import subprocess
import sys
import re

def checker(package):
    #return str(subprocess.run(["pip", "freeze"], capture_output=True, text=True).stdout).split('\n')
    return str(subprocess.run(["pip", "install", package], capture_output=True, text=True).stdout)

def parser(filename, type, chapter=None):
	links = []

	with open(filename, encoding='utf-8') as f:
		data = json.load(f)

	for i in data['log']['entries']:
		try:
			# elems = bs4.BeautifulSoup(str(content), 'html.parser').find('source').get('src')
			content = str(i['request']['url'])
			if ('__sd.mp4' in content) and ('m3u8' in content): 
				links.append(content)
		except Exception:
			pass

	links = [f"{i.replace('__sd', '')[:i.find('?nimblesessionid')-4]}" for i in links]
	#links.sort(key=lambda n: int(n[n.find('-bai-')+5 : n.find('-', n.find('-bai-')+5 )]))

	if (type==1):
		return links
	elif (type==2):
		return '\n\n'.join(links)

res = parser('tu_lanh_pana.har', 2, '')
print(res)

'''
Sử dụng hàm "parser":
	"1" nếu in dạng list
	"2" nếu in từng dòng
	"3" để in full
'''