def pegar_videos_playlist(youtube, playlist_id, max_results=88):
    """Retorna a lista de IDs de vídeos de uma playlist."""
    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=max_results,
        playlistId=playlist_id
    )
    response = request.execute()
    return [video['contentDetails']['videoId'] for video in response['items']]
