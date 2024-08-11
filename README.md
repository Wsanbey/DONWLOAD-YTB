projeto **DOWNLOAD-YTB**:

---

# DOWNLOAD-YTB

**DOWNLOAD-YTB** é uma aplicação gráfica simples que permite baixar vídeos do YouTube em diferentes resoluções diretamente para o seu computador. A interface foi construída utilizando a biblioteca `customtkinter` e o download é gerenciado pela `yt-dlp`, uma biblioteca poderosa para download de vídeos.

## Funcionalidades

- **Busca de Resoluções Disponíveis:** Insira a URL de um vídeo e a aplicação exibirá todas as resoluções disponíveis para download.
- **Seleção de Resolução:** Escolha a resolução desejada diretamente no menu suspenso.
- **Download do Vídeo:** Baixe o vídeo na resolução selecionada diretamente para a pasta escolhida no seu computador.
- **Combinação de Áudio e Vídeo:** Os vídeos baixados são automaticamente combinados com a melhor qualidade de áudio disponível.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python: `yt-dlp`, `customtkinter`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/download-ytb.git
   cd download-ytb
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

1. Execute o aplicativo:
   ```bash
   python main.py
   ```

2. Insira a URL do vídeo que você deseja baixar e clique em "Buscar".
   
3. Após a busca, selecione a resolução desejada no menu suspenso.
   
4. Clique em "Baixar Vídeo" e escolha o local onde deseja salvar o vídeo.

5. O vídeo será baixado e combinado automaticamente.

## Estrutura do Projeto

```plaintext
.
├── .venv                  # Fica a seu criterio criar um ambiente virtual
├── main.py                # Arquivo principal do aplicativo
├── video_downloader.py    # Módulo que lida com o download e resolução do vídeo
├── requirements.txt       # Arquivo de dependências
└── README.md              # Documentação do projeto
```

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorar o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

---

**Desenvolvido por @wellfulstack**  
Telegram: [https://t.me/wellfulstack](https://t.me/wellfulstack)
