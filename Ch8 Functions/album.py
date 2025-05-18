def make_album(artistName, albumTitle, numberSongs=None):
    # Create dictionary assign keys to arguments
    album = {'artist': artistName, 'album': albumTitle}

    # If number is entered it needs to get converted to string
    if numberSongs:
        album['numberSongs'] = numberSongs
    return album

# This loops allows users to keep adding to dictionary
while True:
    #Prompt the user
    print("\nPlease enter artist and title")
    print("(enter 'q' at any time to quit)")
    
    # Takes user input and assigns to artist 
    artist = input("Artist name: ")
    if artist == 'q':
        break
    
    # takes user input and assigns to title
    title = input("Album Title: ")
    if title == 'q':
        break

# Create new variable that takes function
musicInfo = make_album(artist, title)

# print the result
print(musicInfo)

"""musicInfo = make_album('Jay-Z', '444', 11)
print(musicInfo)

musicInfo = make_album('BEAM', 'ALIEN', 19)
print(musicInfo)"""