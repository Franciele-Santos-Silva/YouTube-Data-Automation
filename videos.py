def pegar_estatisticas_videos(youtube, video_ids):
    """Retorna uma lista de tuplas (id_do_video, quantidade_de_views)."""
    request = youtube.videos().list(
        part="statistics",
        id=",".join(video_ids)
    )
    response = request.execute()
    return [(video["id"], video["statistics"]["viewCount"]) for video in response["items"]]
