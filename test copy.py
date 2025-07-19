import os
from PIL import Image
import re

def redimensionar_imagens(diretorio_raiz, largura_nova=600, altura_nova=600):
    """
    Percorre os subdiretórios de um diretório raiz, encontra imagens PNG e JPG,
    e as redimensiona para a resolução especificada, sobrescrevendo os arquivos originais.

    Args:
        diretorio_raiz (str): O caminho para o diretório raiz do seu site.
        largura_nova (int): A nova largura desejada para as imagens.
        altura_nova (int): A nova altura desejada para as imagens.
    """
    contagem_redimensionadas = 0
    contagem_ignoradas = 0

    print(f"Iniciando o redimensionamento de imagens em: {diretorio_raiz}")
    print(f"Redimensionando para: {largura_nova}x{altura_nova} pixels\n")

    for pasta_atual, subpastas, arquivos in os.walk(diretorio_raiz):
        # Verifica se o nome da pasta atual contém "imagens" (ou "images", etc.)
        # Você pode ajustar esta condição para ser mais específica se necessário
        if "imagens" in pasta_atual.lower() or "images" in pasta_atual.lower():
            print(f"Verificando pasta: {pasta_atual}")
            for arquivo in arquivos:
                nome_arquivo_completo = os.path.join(pasta_atual, arquivo)

                # Usa expressão regular para verificar a extensão do arquivo
                if re.search(r"\.(png|jpg|jpeg)$", arquivo, re.IGNORECASE):
                    try:
                        with Image.open(nome_arquivo_completo) as img:
                            largura_original, altura_original = img.size
                            if largura_original == largura_nova and altura_original == altura_nova:
                                print(f"  - Imagem já na resolução correta, ignorando: {arquivo}")
                                contagem_ignoradas += 1
                                continue

                            img_redimensionada = img.resize((largura_nova, altura_nova), Image.Resampling.LANCZOS)
                            img_redimensionada.save(nome_arquivo_completo)
                            print(f"  + Redimensionado: {arquivo} (de {largura_original}x{altura_original} para {largura_nova}x{altura_nova})")
                            contagem_redimensionadas += 1
                    except Exception as e:
                        print(f"  ! Erro ao processar {arquivo}: {e}")
                else:
                    print(f"  - Ignorando arquivo não-imagem ou extensão inválida: {arquivo}")

    print(f"\nProcesso concluído!")
    print(f"Total de imagens redimensionadas: {contagem_redimensionadas}")
    print(f"Total de imagens ignoradas (já na resolução ou não processadas): {contagem_ignoradas}")

if __name__ == "__main__":
    # --- CONFIGURAÇÃO ---
    # Altere este caminho para o diretório raiz do seu site
    DIRETORIO_DO_SEU_SITE = "C:\Users\SAMSUNG\Documents\GitHub\EbooksKidspython redimensionar_imagens.py" # EX: C:/Users/SeuUsuario/MeuSite ou /home/SeuUsuario/MeuSite

    # Dimensões desejadas
    NOVA_LARGURA = 600
    NOVA_ALTURA = 600
    # --- FIM DA CONFIGURAÇÃO ---

    # Verifique se o diretório existe antes de tentar processar
    if os.path.isdir(DIRETORIO_DO_SEU_SITE):
        redimensionar_imagens(DIRETORIO_DO_SEU_SITE, NOVA_LARGURA, NOVA_ALTURA)
    else:
        print(f"Erro: O diretório '{DIRETORIO_DO_SEU_SITE}' não foi encontrado.")
        print("Por favor, verifique o caminho e tente novamente.")