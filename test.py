class Account:
    acc_list = []
    def __init__(self, name, ID, albums = [], playlists = []):
        self.name = name
        self.ID = ID
        self.albums = albums
        self.playlists = playlists
        Account.acc_list.append(self)