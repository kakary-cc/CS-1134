from ChainingHashTableMap import *
from DoublyLinkedList import *


class PlayList:
    def __init__(self):
        self.ht = ChainingHashTableMap()
        self.dll = DoublyLinkedList()

    def add_song(self, new_song_name):
        self.ht[new_song_name] = self.dll.add_last(new_song_name)

    def add_song_after(self, song_name, new_song_name):
        self.dll.add_after(self.ht[song_name], new_song_name)

    def play_song(self, song_name):
        val = self.ht[song_name]
        print("Playing " + song_name)

    def play_list(self):
        for i in self.dll:
            print("Playing " + i)


# Test Code
p1 = PlayList()
p1.add_song("Jana Gana Mana")
p1.add_song("Kimi Ga Yo")
p1.add_song("The Star-Spangled Banner")
p1.add_song("March of the Volunteers")
p1.add_song_after("The Star-Spangled Banner", "La Marcha Real")
p1.add_song_after("Kimi Ga Yo", "Aegukga")
p1.add_song("Arise, O Compatriots")
p1.add_song("Chant de Ralliement")
p1.add_song_after("Chant de Ralliement", "Himno Nacional Mexicano")
p1.add_song_after("Jana Gana Mana", "God Save The Queen")

p1.play_song("The Star-Spangled Banner")
p1.play_song("Jana Gana Mana")

p1.play_list()
