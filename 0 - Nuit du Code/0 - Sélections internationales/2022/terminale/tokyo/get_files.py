import requests, os
code = 'vw6j-al4y'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/ndc.py')
with open('ndc.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/')
print(py.content.decode())
os.system('pyxel run "ndc.py"')
