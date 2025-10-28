import fitz  # PyMuPDF
import re
import os
import glob
import traceback

pasta = "/home/pedro/Documentos/CC/Python/Boletim/documentos"

# Pattern permissivo (ajuste se quiser)
pattern_corrigido = re.compile(
    r'(\d+\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇa-z\s]+?)\s*Nota:\s*([0-9,.\s]+)',
    re.IGNORECASE
)

arquivos_pdf = glob.glob(os.path.join(pasta, '*.pdf'))
if not arquivos_pdf:
    print("Nenhum PDF encontrado em:", pasta)

for caminho_pdf in arquivos_pdf:
    print("\n=== Processando:", caminho_pdf, "===")
    try:
        pdf_document = fitz.open(caminho_pdf)
    except Exception as e:
        print("Erro ao abrir PDF:", e)
        traceback.print_exc()
        continue

    results = []
    try:
        for pagenum, page in enumerate(pdf_document, start=1):
            page_text = page.get_text("text") or ""
            # limpeza mínima
            page_text = re.sub(r'[\t\r\f\v]+', ' ', page_text)
            page_text = re.sub(r' {2,}', ' ', page_text)

            # debug: mostrar um trecho da página 1
            if pagenum == 1:
                print("Trecho página 1 (snippet):", repr(page_text[:400]))

            matches = pattern_corrigido.findall(page_text)
            print(f"Pág. {pagenum}: {len(matches)} matches encontrados")

            for nome_raw, notas_raw in matches:
                try:
                    # debug do match
                    print("DEBUG match -> nome_raw:", repr(nome_raw[:100]), " | notas_raw:", repr(notas_raw[:80]))

                    nome = ' '.join(nome_raw.split())
                    notas = re.findall(r'\d+,\d+|\d+\.\d+|\d+', notas_raw)

                    # extração segura da 'mb' (se não tiver 3 notas, pega o último disponível)
                    if len(notas) >= 3:
                        mb_raw = notas[-3]
                    elif len(notas) >= 1:
                        mb_raw = notas[-1]
                    else:
                        mb_raw = '0'

                    mb = mb_raw.replace(',', '.')
                    results.append(f"{nome}\t{mb}")
                except Exception as e:
                    print("Erro ao processar um match (continuando):", e)
                    traceback.print_exc()
                    # não interrompe todo o processamento por causa de 1 match ruim
                    continue

    finally:
        pdf_document.close()

    # caminho do arquivo de saída
    nome_arquivo_pdf = os.path.splitext(os.path.basename(caminho_pdf))[0]
    caminho_saida = os.path.join(pasta, f"{nome_arquivo_pdf}_resultado.txt")
    print("Tentando gravar:", caminho_saida, " (linhas a gravar:", len(results), ")")

    try:
        # garantir que a pasta exista (normalmente já existe)
        
        os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            for res in results:
                f.write(res + '\n')
            f.flush()
            os.fsync(f.fileno())  # força escrita em disco
        print("Arquivo gravado com sucesso:", caminho_saida)
    except Exception as e:
        print("Erro ao gravar arquivo:", e)
        traceback.print_exc()
