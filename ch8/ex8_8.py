def make_album(name, title, track= ''):
    music_album = {'Artic name': name.title(), 'Album title': title.title()}
    if track:
        music_album['Track'] = track
    return music_album

while True:
    print("Enter the artic name and name of the album(`q` to quick)")
    name = input("Enter artic name: ")
    if name == 'q': break
    album = input("Enter the ablim's name: ")
    full_info = make_album(name, album)
    print(full_info)
    print()
    