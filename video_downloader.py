import yt_dlp
from pathlib import Path

def obter_resolucoes_disponiveis(url):
    """Obtém a lista de resoluções disponíveis para o vídeo."""
    try:
        ydl_opts = {'quiet': True, 'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            if not formats:
                return None, "Nenhum formato encontrado."

            # Filtra e lista as resoluções disponíveis
            resolucoes_disponiveis = sorted(
                {fmt.get('height') for fmt in formats if fmt.get('height') is not None}
            )
            resolucoes_disponiveis = [f"{res}p" for res in resolucoes_disponiveis]
            return resolucoes_disponiveis, "Resoluções encontradas com sucesso."
    
    except Exception as e:
        return None, f"Erro ao obter as resoluções disponíveis: {e}"

def baixar_video(url, resolucao, pasta_destino):
    """Baixa o vídeo na resolução especificada e combina vídeo e áudio se necessário."""
    try:
        path_to_download = Path(pasta_destino)
        ydl_opts = {
            'format': f'bestvideo[height<={resolucao[:-1]}]+bestaudio/best',
            'outtmpl': str(path_to_download / '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',  # Combina áudio e vídeo em um único arquivo MP4
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        return "Vídeo baixado com sucesso!\n\nDesenvolvido por @wellfulstack Telegram: https://t.me/wellfulstack\n\n"
    except Exception as e:
        return f"Erro ao baixar o vídeo: {e}"
