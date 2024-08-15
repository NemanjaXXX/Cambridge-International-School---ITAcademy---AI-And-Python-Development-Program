import urllib.request
 
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
 
 #---------------------Analiziraj ili kopiraj u drugi fajl------------------------------------
fhand = open('romeo.txt')
for linija in fhand:
    print(linija.strip())

    import urllib.request, urllib.parse, urllib.error
 
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
 
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)