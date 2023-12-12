from langdetect import detect

def langDetect(text):
    lang = detect(text)
    if (lang=='es' or lang=='en'):
        return lang
    else:
        return f"language {lang.capitalize()} not allowed"    


