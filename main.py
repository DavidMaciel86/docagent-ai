import os

from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

from prompts.document_prompts import DOCUMENT_AGENT_INSTRUCTIONS
from services.pdf_service import extrair_texto_pdf


load_dotenv()


def criar_agente() -> Agent:
    return Agent(
        model=Groq(
            id=os.getenv("GPT_OSS_120B"),
            api_key=os.getenv("GROQ_API_KEY"),
        ),
        instructions=DOCUMENT_AGENT_INSTRUCTIONS,
        markdown=True,
    )


def solicitar_pdf() -> str:
    while True:
        caminho_pdf = input("Informe o caminho do arquivo PDF: ").strip()

        if not caminho_pdf:
            print("O caminho do arquivo não pode estar vazio.\n")
            continue

        try:
            return extrair_texto_pdf(caminho_pdf)
        except (FileNotFoundError, ValueError) as erro:
            print(f"Erro: {erro}\n")


def main() -> None:
    print("\nDocAgent AI")
    print("Assistente inteligente para análise de documentos PDF.\n")

    texto_pdf = solicitar_pdf()

    print("\nDocumento carregado com sucesso.")

    agente = criar_agente()

    print("Digite uma pergunta sobre o documento.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Você: ").strip()

        if pergunta.lower() == "sair":
            print("DocAgent AI encerrado.")
            break

        if not pergunta:
            continue

        prompt = f"""
            Responda à pergunta utilizando somente as informações do documento.
            
            DOCUMENTO:
            {texto_pdf}
            
            PERGUNTA:
            {pergunta}
        """

        agente.print_response(
            prompt,
            stream=True,
        )


if __name__ == "__main__":
    main()
