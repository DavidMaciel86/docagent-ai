from pathlib import Path

from pypdf import PdfReader


def extrair_texto_pdf(caminho_pdf: str | Path) -> str:
    caminho = Path(caminho_pdf)

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    if caminho.suffix.lower() != ".pdf":
        raise ValueError("O arquivo informado não é um PDF.")

    reader = PdfReader(caminho)

    paginas = []

    for pagina in reader.pages:
        texto = pagina.extract_text()

        if texto:
            paginas.append(texto)

        conteudo = "\n\n".join(paginas)

        if not conteudo.strip():
            raise ValueError(
                "Não foi possível extrair texto do PDF. "
                "O documento pode ser digitalizado ou conter apenas imagens."
            )

        return conteudo
