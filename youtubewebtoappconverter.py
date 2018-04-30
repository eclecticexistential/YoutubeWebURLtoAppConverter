
def geturl(url):
    give = url.split('https://www.youtube.com/watch?v=')
    location = 'https://youtu.be/' + give[1]
    return location

print(geturl('https://www.youtube.com/watch?v=z8cgNLGnnK4'))
