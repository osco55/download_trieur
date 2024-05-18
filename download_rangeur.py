import os

# Demande à l'utilisateur de fournir le chemin de son répertoire Downloads
downloads_path = input("Veuillez entrer le chemin de votre répertoire Downloads : ").strip()

# Crée les dossiers nécessaires dans le répertoire Downloads spécifié
try:
    os.mkdir(os.path.join(downloads_path, "dossier_.zip"))
    os.mkdir(os.path.join(downloads_path, "dossier_images"))
    os.mkdir(os.path.join(downloads_path, "dossier_wordpdf"))
    os.mkdir(os.path.join(downloads_path, "dossier_.exe"))
    os.mkdir(os.path.join(downloads_path, "dossier_autres"))
    os.mkdir(os.path.join(downloads_path, "dossier_vidéo"))
    os.mkdir(os.path.join(downloads_path, "dossier_codage"))
except FileExistsError:
    print("Les dossiers étaient déjà créés")

# Liste les fichiers dans le répertoire Downloads spécifié
fichiers = os.listdir(downloads_path)

# Parcourt les fichiers et les déplace dans les dossiers appropriés
for i in range(100):  # si vous avez plus de 100 fichiers, changez cette variable ou exécutez le programme plusieurs fois
    for name in fichiers:
        if name in ["dossier_.zip", "dossier_images", "dossier_wordpdf", "dossier_.exe", "dossier_autres", "dossier_vidéo", "dossier_codage"]:
            print("C'est un des dossiers clé")  # vérifie que deux dossiers ne soient pas créés avec le même nom
        else:
            try:
                filepath = os.path.join(downloads_path, name)
                if name.endswith(".exe"):
                    os.rename(filepath, os.path.join(downloads_path, "dossier_.exe", name))
                elif any(name.endswith(ext) for ext in [".mp4", ".mp3", ".avi", ".wav"]):
                    os.rename(filepath, os.path.join(downloads_path, "dossier_vidéo", name))
                elif any(name.endswith(ext) for ext in [".zip", ".tar.gz", ".rar"]):
                    os.rename(filepath, os.path.join(downloads_path, "dossier_.zip", name))
                elif any(name.endswith(ext) for ext in [".jpg", ".PNG", ".webp", ".png", ".jpeg", ".bmp", ".ico", ".gif", ".JPG"]):
                    os.rename(filepath, os.path.join(downloads_path, "dossier_images", name))
                elif any(name.endswith(ext) for ext in [".pdf", ".pptx", ".docx", ".odt", ".ppt", ".odf", ".calc", ".xlsx", ".txt"]):
                    os.rename(filepath, os.path.join(downloads_path, "dossier_wordpdf", name))
                elif any(name.endswith(ext) for ext in [".php", ".html", ".css", ".sql", ".json", ".py", ".gpx", ".tcx"]):
                    os.rename(filepath, os.path.join(downloads_path, "dossier_codage", name))
                else:
                    os.rename(filepath, os.path.join(downloads_path, "dossier_autres", name))
            except (PermissionError, FileNotFoundError):
                print("ERROR 404")
