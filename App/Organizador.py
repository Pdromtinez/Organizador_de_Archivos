import os
import shutil


documentos_dir = 'Documentos'
fotos_dir = 'Imágenes'
videos_dir = 'Vídeos'
musica_dir = 'Música'

os.makedirs(documentos_dir, exist_ok=True)
os.makedirs(fotos_dir, exist_ok=True)
os.makedirs(videos_dir, exist_ok=True)
os.makedirs(musica_dir, exist_ok=True)


extensiones_documentos = ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx')
extensiones_fotos = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
extensiones_videos = ('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv')
extensiones_musica = ('.mp3', '.wav', '.aac', '.flac', '.ogg')


archivos = [f for f in os.listdir() if os.path.isfile(f)]

def mover_archivo(archivo, destino):
    try:
        shutil.move(archivo, destino)
        print(f"Movido {archivo} a {destino}")
    except Exception as e:
        print(f"Error al mover {archivo}: {e}")


for archivo in archivos:
    if archivo.endswith(extensiones_documentos):
        mover_archivo(archivo, documentos_dir)
    elif archivo.endswith(extensiones_fotos):
        mover_archivo(archivo, fotos_dir)
    elif archivo.endswith(extensiones_videos):
        mover_archivo(archivo, videos_dir)
    elif archivo.endswith(extensiones_musica):
        mover_archivo(archivo, musica_dir)

print("Organización de archivos completada.")