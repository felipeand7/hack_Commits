import git
import os
import random
from datetime import datetime, timedelta

# Caminho do repositório
repo_path = '/caminho/para/hack_Commits'

# Inicializa o repositório
repo = git.Repo(repo_path)

# Função para criar commits falsos
def criar_commit_falso(data):
    # Altera o arquivo de texto (ou cria um novo)
    with open(os.path.join(repo_path, 'fake_commit.txt'), 'a') as f:
        f.write(f"Commit falso em {data}\n")
    
    # Adiciona as mudanças
    repo.index.add(['fake_commit.txt'])
    
    # Configura a data do commit
    os.environ['GIT_AUTHOR_DATE'] = data
    os.environ['GIT_COMMITTER_DATE'] = data
    
    # Faz o commit
    repo.index.commit(f"Commit falso em {data}")

# Define o intervalo de datas
data_inicial = datetime(2023, 1, 1)
data_final = datetime(2023, 12, 31)

# Loop para criar commits em datas aleatórias
while data_inicial <= data_final:
    # Decide aleatoriamente se vai ter commit no dia ou não (70% de chance de ter commit)
    if random.random() < 0.7:
        # Número de commits no dia (1 a 5)
        num_commits = random.randint(1, 5)
        for _ in range(num_commits):
            # Gera um horário aleatório no dia
            hora = random.randint(0, 23)
            minuto = random.randint(0, 59)
            segundo = random.randint(0, 59)
            data_commit = data_inicial.replace(hour=hora, minute=minuto, second=segundo)
            criar_commit_falso(data_commit.strftime('%Y-%m-%d %H:%M:%S'))
    
    # Avança para o próximo dia
    data_inicial += timedelta(days=1)

# Envia os commits pro GitHub
repo.remotes.origin.push()