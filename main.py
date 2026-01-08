import os
from auth import autenticar_youtube
from playlist import pegar_videos_playlist
from videos import pegar_estatisticas_videos

PLAYLIST_ID = "PLM5UhJqBbAfmwMHPgnbOgPnX8eYoEByY5"

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    youtube = autenticar_youtube()
    ids_video = pegar_videos_playlist(youtube, PLAYLIST_ID)
    stats = pegar_estatisticas_videos(youtube, ids_video)

    for id_video, views in stats:
        print(id_video, "-", views)

if __name__ == "__main__":
    main()
