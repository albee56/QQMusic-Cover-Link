# search for 'albumid' in 'Response'

bigcover = 'http://imgcache.qq.com/music/photo/album/17/albumpic_6382717_0.jpg'
smallcover = 'http://imgcache.qq.com/music/photo/album_300/17/300_albumpic_6382717_0.jpg'

a = bigcover.find('17')
b = bigcover.find('6382717')

c = smallcover.find('17')
d = smallcover.find('6382717')

cover = input('albumid: ')
cover = cover.strip()

bigcover1 = bigcover[:a]
bigcover2 = bigcover[a+2:b]
bigcover3 = bigcover[b+7:]

smallcover1 = smallcover[:c]
smallcover2 = smallcover[c+2:d]
smallcover3 = smallcover[d+7:]

bigcover = bigcover1 + cover[5:] + bigcover2 + cover + bigcover3
smallcover = smallcover1 + cover[5:] + smallcover2 + cover + smallcover3

print('bigcover: ')
print(bigcover)
print('smallcover: ')
print(smallcover)
