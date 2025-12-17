class Musica:
    nome = ''
    artista = ''
    genero = ''

musica1 = Musica()
musica1.nome = 'Only God Can Judge Me'
musica1.artista = 'Tupac'
musica1.genero = 'Rap'

musica2 = Musica()
musica2.nome = 'XTRANHO'
musica2.artista = 'Matuê'
musica2.genero = 'Trap'

musica3 = Musica()
musica3.nome = 'Lonely Day'
musica3.artista = 'System of a Down'
musica3.genero = 'Rock'

print(f'Música: {musica1.nome} | Artista: {musica1.artista} | Gênero: {musica1.genero}')
print(f'Música: {musica2.nome} | Artista: {musica2.artista} | Gênero: {musica2.genero}')
print(f'Música: {musica3.nome} | Artista: {musica3.artista} | Gênero: {musica3.genero}')