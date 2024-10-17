import os
import shutil

def reorganizar_pastas(caminho_root):
    # Verifica se a pasta raiz existe
    if not os.path.exists(caminho_root):
        print(f"A pasta raiz '{caminho_root}' não existe.")
        return
    
    # Lista todos os meses (ex: Mês 09, Mês 10, ...)
    pastas_meses = [mes for mes in os.listdir(caminho_root) if os.path.isdir(os.path.join(caminho_root, mes))]

    for mes in pastas_meses:
        caminho_mes = os.path.join(caminho_root, mes)
        
        # Percorre todas as datas dentro de cada mês
        datas = [data for data in os.listdir(caminho_mes) if os.path.isdir(os.path.join(caminho_mes, data))]
        
        for data in datas:
            caminho_data = os.path.join(caminho_mes, data)
            
            # Percorre todos os pontos (Ponto 1, Ponto 2, ...)
            pontos = [ponto for ponto in os.listdir(caminho_data) if os.path.isdir(os.path.join(caminho_data, ponto))]
            
            for ponto in pontos:
                caminho_ponto = os.path.join(caminho_data, ponto)
                
                # Define o novo caminho para a pasta de Ponto (diretamente na pasta Root)
                novo_caminho_ponto = os.path.join(caminho_root, ponto)
                
                # Cria a pasta do Ponto na raiz, se não existir
                if not os.path.exists(novo_caminho_ponto):
                    os.makedirs(novo_caminho_ponto)
                
                # Cria a pasta do Mês dentro do novo caminho do Ponto
                novo_caminho_mes = os.path.join(novo_caminho_ponto, mes)
                if not os.path.exists(novo_caminho_mes):
                    os.makedirs(novo_caminho_mes)

                # Verifica se a pasta de Data ainda existe antes de mover
                if os.path.exists(caminho_data):
                    try:
                        # Move a pasta de Data para o novo caminho (dentro do Mês)
                        shutil.move(caminho_data, os.path.join(novo_caminho_mes, data))
                        print(f"Movido: {caminho_data} -> {os.path.join(novo_caminho_mes, data)}")
                    except Exception as e:
                        print(f"Erro ao mover {caminho_data}: {e}")
                else:
                    print(f"Pasta {caminho_data} não encontrada, talvez já tenha sido movida.")

        # Após mover todas as pastas de data, remove o mês original (se estiver vazio)
        if os.path.exists(caminho_mes) and not os.listdir(caminho_mes):
            try:
                os.rmdir(caminho_mes)
                print(f"Pasta '{caminho_mes}' removida.")
            except Exception as e:
                print(f"Erro ao remover a pasta '{caminho_mes}': {e}")

# Exemplo de uso - Altere este caminho para a sua estrutura de diretórios
caminho_da_pasta_raiz = r'D:\Igor\Modelo Atual'
reorganizar_pastas(caminho_da_pasta_raiz)
