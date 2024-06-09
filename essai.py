import os
import feedparser
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Charger les credentials depuis le fichier JSON
credentials = service_account.Credentials.from_service_account_file(
    os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
)

# Créer le service Google Drive
drive_service = build('drive', 'v3', credentials=credentials)

# ID du fichier Google Drive à mettre à jour
file_id = 'VOTRE_FICHIER_ID'

def get_rss_feed(url):
    return feedparser.parse(url)

def parse_feed(feed):
    entries = feed['entries']
    summary = ''
    for entry in entries:
        title = entry.get('title', 'No Title')
        link = entry.get('link', '')
        published = entry.get('published', 'No Date')
        summary += f"- **{title}** ({published})\n{link}\n\n"
    return summary

# Liste des flux RSS à lire
rss_feeds = [
    'https://www.france24.com/fr/rss',
    'https://www.lemonde.fr/rss/en_continu.xml'
]

all_news = '### Résumé de l\'actualité politique récente\n\n'
for url in rss_feeds:
    feed = get_rss_feed(url)
    all_news += parse_feed(feed)

# Écriture dans un fichier temporaire
file_name = 'Résumé_Actualité_Politique.txt'
with open(file_name, 'w') as file:
    file.write(all_news)

# Upload the updated file to Google Drive
media = MediaFileUpload(file_name, mimetype='text/plain')
updated_file = drive_service.files().update(fileId=file_id, media_body=media).execute()

print(f"File updated with ID: {updated_file.get('id')}")
