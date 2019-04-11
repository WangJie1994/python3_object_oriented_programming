song_library = [
    ('song A', 'singer A'),
    ('song B', 'singer C'),
    ('song C', 'singer C'),
    ('song D', 'singer B')]


artists = set()
for song, artist in song_library:
    artists.add(artist)

print(artists)

print('singer A' in artists)

for artist in artists:
    print("{} plays good music".format(artist))

artists_list = list(artists)
artists_list.sort()
print(artists_list)

my_artists = {'singer A', 'singer B', 'singer C'}
sister_artists = {'singer B', 'singer C', 'singer D'}
print("all: {}".format(my_artists.union(sister_artists)))
print("both: {}".format(my_artists.intersection(sister_artists)))
print("either but not both: {}".format(my_artists.symmetric_difference(sister_artists)))

my_artists = {'singer A', 'singer B', 'singer C'}
bands = {'singer A', 'singer B'}
print("my artists is to bands:")
print("issuperset: {}".format(my_artists.issuperset(bands)))
print("issubset: {}".format(my_artists.issubset(bands)))
print("difference: {}".format(my_artists.difference(bands)))
print("*"*20)
print("bands is to  my artists:")
print("issuperset: {}".format(bands.issuperset(my_artists)))
print("issubset: {}".format(bands.issubset(my_artists)))
print("difference: {}".format(bands.difference(my_artists)))