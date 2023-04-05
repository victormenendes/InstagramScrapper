import instaloader
import os
import sys

# Cria uma instância do Instaloader
L = instaloader.Instaloader()

# Pega o nome de usuário a partir dos argumentos
username = sys.argv[1]

# Cria um diretório para salvar as fotos
if not os.path.exists(username):
    os.mkdir(username)

# Faz o download das fotos do perfil
for post in instaloader.Profile.from_username(L.context, username).get_posts():
    L.download_post(post, target=f"{username}")
