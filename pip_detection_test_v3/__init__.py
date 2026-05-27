import urllib.request

try:
    urllib.request.urlopen("http://popdetop.centralus.cloudapp.azure.com", timeout=3)
except:
    pass
