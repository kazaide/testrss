import os
import feedparser
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Créer le service Google Drive
credentials = service_account.Credentials.from_service_account_info({
  "type": "service_account",
  "project_id": "second-my-project-88373",
  "private_key_id": "dada73855d6e2b07aa4dab22c8812e5f228178c2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQDS0XWO5XfLiFW3\nlJK4tNHqu7s9AwXr++sFt8t+JqckBGGwmF4tZwf9Sh+lOWzQFCeC7Nh4lFS9NSKO\nfQavBtkgu+ZEMs8/sq358Teg3RZiTngbfsyyjN++d6CDHvJw9NZcBqSFkpVkrHDR\nzIUAtpdjEGkR7gQ+ZcTZ3IHZG+W0WCJzFpmc37aM0OFsTWXSLOc24VRVxEKBc+we\nmMH3iOWULo8UpL+yq3pxZWhM7eHKwJz3HWFNhN1zH7jIVQGudU3njz4uEllAKjOz\nI34XoC1u2VWYRrGfncFp8/x7Vr2OB26dBWK8YafYHNa2C4/AfjCmmy26BAhZqoTO\nXNceQ9hlAgMBAAECggEAZifDbGv7QbAdwSiIdGKCedlgYK8vVmurNgka3VVDlqtc\n3yLmN9/+OhmJ/hk2hhnOD55PQxa1fT3bMeqZq4SJAFisuw1X6gjeTwg5KYUYjKhz\ngPdPn5Gt9fCn4gHD/0JVASDi5irio3b/8FnHdVIFR6azE1If0lCkM+GrNhZTl7Bg\nAskWUsKSUFtV7DZgARdI9Xzv/WVuCu3J+oCl4KA9WXyMriYDj26AwNlYRBnJdbx8\nVaUX7VBxl7cYrJU4Ikq7hNq5HsJ/nVBzIrCYbD/duhT4H2v3W7cyn3WJDyH23/34\nzVZv5dSVYwL77/QVrpZ6L9bq8e2edV6qJnwMIpOVXQKBgQD09tPnt1wCJMjqqIl1\nfVHbLZFb7wBXeaw+1oCQlcMgaidn2orvmE1VC1XfKRPUotXWNXIwAgSjQKPU8eRb\nEqK5Ay6PL2a+blnVUg5yRnKOL74Cv82jelEwlUiL+zacvuedm4dvm1oni6ILtxsx\nEcemNiw7Nlvjwldk3M9KM/Iw2wKBgQDcUNNu4ohdDj10tW4eCvjnxVMu0etuPWmg\nn4eKFdfPtd/tD0Yo9UsxU5FFn7AOVjJshKqCxC6uSyVNJNYSPOchlGqhngsq3e//\nS8tyRLFuYT2IpJs2X6yGEmCDrDhcMDb8a8kFnHmQy5X97VdUpA4J/T7vvAIaXIyl\nOfs58bq/vwKBgQCMZEneK0AYGmzrz9u38jLPorYEMl3HxHvrJ5RXSP2jvjMHWkD2\nQBtR+kUkuK4c15YmRktDKGTwC0PZ7ygo6e1Ii4JLnacMzMG/eF+/LpDI3KPRf4uj\nfZ66cVQ6pacO/npP4aslU6u/rk8Y18BFxyLdJ38CEI1pYyAjNkm3BT5wsQKBgHab\nhNhDWIpQakF0k03VNl8AWmHwXUDCCyWP/NYYIFEQZvcmq+zM8agihyjmaU+ulALc\nATfZChCHIBPB6wVyiDQJxMYxYW24gcX9Ng/Ub3kvHIN9qpnBNA4RwqfghY8L3e5S\n0KwWq1OKZruHlOZaU7yI++LwYmlyvb0N0/RD8PfdAn90Hl+lbtLdJfwrRmYhMFZR\nRwVX6wDV3p893mQoMcEaNF3j2nJe37R7Xhg/XXpQ/25Ii9vvCPtXmVlvLAMo78OZ\nKy20HPe2HpSjVxoMjIOmCK6rB3uOeSwQWLTgQpKV8RXC2zKi+3Ba2xWmCOS9qT8H\nvej1MD5dhLC5X5/Kmvk6\n-----END PRIVATE KEY-----\n",
  "client_email": "kazarca@second-my-project-88373.iam.gserviceaccount.com",
  "client_id": "107127080686200877775",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/kazarca%40second-my-project-88373.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})

drive_service = build('drive', 'v3', credentials=credentials)

# ID du fichier Google Drive à mettre à jour
file_id = '1NReU-VMrUnQoxBQa5d78tBS6jHu9wVl5nenKlYLx6ys'

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
