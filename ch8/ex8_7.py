def make_album(name, title, track= ''):
    music_album = {'Artic name': name.title(), 'Album title': title.title()}
    if track:
        music_album['Track'] = track
    return music_album

htoo = make_album('htoo eain thin', 'may may')
print(htoo)
taylor = make_album('taylor switch', 'lover', '1M')
print(taylor)