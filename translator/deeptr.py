from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

def TransLate(text: str, scr: str = 'auto', dest: str = 'en') -> str:
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        lang = detect(text)
        if set == "lang":
            return lang
        elif set == "confidence":
            langs = detect_langs(text)
            return str(langs[0].prob)
        else:
            langs = detect_langs(text)
            return f"{langs[0].lang} ({langs[0].prob:.2%})"
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"


def CodeLang(lang: str) -> str:
    mapping = {"ukrainian": "uk", "uk": "Ukrainian", "english": "en", "en": "English"}
    lang_lower = lang.lower()
    return mapping.get(lang_lower, "Мову не знайдено")


def LanguageList(out: str = "screen", text: str = None) -> str:
    print("Функція LanguageList в deep_translator реалізована частково.")
    return "Ok (часткова реалізація)"