import customtkinter as ctk
import video_downloader
from tkinter import filedialog

class VideoDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Video Downloader")
        self.geometry("500x280")
        
        # URL Input
        self.url_label = ctk.CTkLabel(self, text="URL do Vídeo:")
        self.url_label.pack(pady=10)
        
        # URL Entry and Search Button
        self.url_frame = ctk.CTkFrame(self)
        self.url_frame.pack(pady=5)
        
        self.url_entry = ctk.CTkEntry(self.url_frame, width=400)
        self.url_entry.pack(side="left", padx=5)
        
        self.search_button = ctk.CTkButton(self.url_frame, text="Buscar", command=self.buscar_resolucoes)
        self.search_button.pack(side="left", padx=5)
        
        # Resolution Menu (Initially hidden)
        self.resolution_var = ctk.StringVar(value="")
        self.resolution_menu = ctk.CTkOptionMenu(self, variable=self.resolution_var, values=[])
        self.resolution_menu.pack(pady=10)
        self.resolution_menu.pack_forget()  # Hide the resolution menu initially
        
        # Download Button (Initially hidden)
        self.download_button = ctk.CTkButton(self, text="Baixar Vídeo", command=self.choose_save_location, state="disabled")
        self.download_button.pack(pady=10)
        self.download_button.pack_forget()  # Hide the download button initially
        
        # Status Label
        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=10)
        
    def buscar_resolucoes(self):
        url = self.url_entry.get().strip()
        if not url:
            self.status_label.configure(text="URL não fornecida.")
            return
        
        # Obter a lista de resoluções disponíveis
        resolucoes, mensagem = video_downloader.obter_resolucoes_disponiveis(url)
        if not resolucoes:
            self.status_label.configure(text=mensagem)
            self.resolution_menu.pack_forget()  # Hide the resolution menu if no resolutions
            self.download_button.pack_forget()  # Hide the download button if no resolutions
            return
        
        # Atualizar o menu de resoluções com as resoluções disponíveis
        self.resolution_menu.configure(values=resolucoes)
        self.resolution_menu.pack(pady=10)  # Show the resolution menu
        
        # Enable and show download button if resolutions are available
        self.download_button.configure(state="normal")
        self.download_button.pack(pady=10)
        
    def choose_save_location(self):
        # Open file dialog to choose save location
        folder_selected = filedialog.askdirectory(title="Escolha o local para salvar o vídeo")
        if not folder_selected:
            self.status_label.configure(text="Nenhum local selecionado.")
            return
        
        # Start the download process
        self.start_download(folder_selected)

    def start_download(self, folder_selected):
        url = self.url_entry.get().strip()
        if not url:
            self.status_label.configure(text="URL não fornecida.")
            return
        
        # Obter a resolução selecionada pelo usuário
        resolucao_selecionada = self.resolution_var.get()
        
        if not resolucao_selecionada:
            self.status_label.configure(text="Primeiro escolha a Resolução.")
            return
        
        # Baixar o vídeo na resolução selecionada
        mensagem = video_downloader.baixar_video(url, resolucao_selecionada, folder_selected)
        self.status_label.configure(text=mensagem)

if __name__ == "__main__":
    app = VideoDownloaderApp()
    app.mainloop()
