import google_auth_oauthlib.flow
import googleapiclient.discovery

CLIENT_SECRETS_FILE = "secrets.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def autenticar_youtube():
    """Autentica e retorna o serviço do YouTube."""
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES
    )
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    return youtube
