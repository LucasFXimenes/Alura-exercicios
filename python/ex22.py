class Musica:
    
    musicas = []
    
    def __init__(self, nome, artista, album, duracao):
        self.nome = nome
        self.artista = artista
        self.album = album
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def __str__(self):
        return f'{self.nome} - {self.artista} - {self.album} - {self.duracao}'
    
    def exibir_musicas():
        for musica in Musica.musicas:
            print(musica)


musica1 = Musica('Imagine esse cenário', 'Matuê', '333', '3:45')
musica2 = Musica('Blinding Lights', 'The Weeknd', 'After Hours', '3:20')

Musica.exibir_musicas()
