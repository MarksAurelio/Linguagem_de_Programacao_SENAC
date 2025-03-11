""" Crie uma classe chamada Playlist que armazena uma lista de músicas. A classe deve ter os seguintes métodos:
adicionar_musica(titulo, artista): adiciona uma música à playlist.
listar_musicas(): exibe todas as músicas armazenadas. """
class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_musica(self, musica):
        self.lista.append(musica)

    def listar_musicas(self):
        print(f'{self.nome}:')
        for musica in self.lista:
            print(f'- Título: {musica["título"]}\n- Artista: {musica["artista"]}')

playlist = Playlist('Minha Playlist')

while True:
    nome = input('Digite uma música (ou sair para finalizar): ').capitalize()
    if nome.lower() == 'sair':
        break
    
    artista = input('Digite o artista: ')
    musica = {'título': nome, 'artista': artista}
    playlist.adicionar_musica(musica)

playlist.listar_musicas()
