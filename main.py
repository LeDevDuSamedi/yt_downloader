import webbrowser
from googleapiclient.discovery import build, Resource
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import requests
def download_vid(id):
    url = f"https://convert2mp3s.com/api/single/mp3?url=https://www.youtube.com/watch?v={id}"
    webbrowser.open(url)
def get_input():
    search_query = input_entry.get()
    search_youtube_videos(search_query, 1)

# Remplacez 'YOUR_API_KEY' par votre clé d'API YouTube
api_key = 'YOUR_API_KEY'
youtube = build('youtube', 'v3', developerKey=api_key)

def search_youtube_videos(query, max_results):
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results
    ).execute()

    for search_result in search_response.get('items', []):
        video_id = search_result['id'].get('videoId')
        if video_id:
            video_title = search_result['snippet']['title']
            thumbnail_url = search_result['snippet']['thumbnails'].get('high', {}).get('url')
            print(thumbnail_url)
            label = tk.Label(window, text=video_title, pady=10, bg="#00CED1")
            response = requests.get(thumbnail_url)
            image = Image.open(BytesIO(response.content))
            if response.status_code == 200:
                print("Image téléchargée avec succès")
            else:
                print("Échec du téléchargement de l'image")
            # Redimensionnement de l'image si nécessaire

            # Convertir l'image en un objet PhotoImage
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(window, image=photo, pady=20)
            image_label.image = photo 
            image_label.pack()
            label.pack()
            buttonr = tk.Button(window, text="Download", command=lambda: download_vid(video_id), pady=10, relief=tk.FLAT, bg="blue",highlightthickness=0, highlightbackground="blue", font=("Arial", 18), borderwidth=0, bd=0)
            buttonr.pack()
            input_entry.pack_forget()
            button.pack_forget()
            window.update()

# Création de la fenêtre
window = tk.Tk()
window.title("DownTube")
window.configure(bg="#00CED1")
window.geometry("300x300")

label = tk.Label(window, text="DownTube", font=("Arial", 24), padx=10, pady=10, bg="#00CED1")
label.pack()
# Création du champ de saisie
input_entry = tk.Entry(window)
input_entry.pack(pady=40)

# Création du bouton pour récupérer l'input
button = tk.Button(window, text="Rechercher", command=get_input, relief=tk.FLAT, highlightthickness=0, bg="blue", highlightbackground="blue", font=("Arial", 18), borderwidth=0, bd=0)
button.pack()
# Lancement de la boucle principale
window.mainloop()
