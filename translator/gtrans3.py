import sys
from googletrans import Translator, LANGUAGES

if sys.version_info >= (3, 13):
    print("УВАГА: googletrans==3.1.0a0 не рекомендується на Python 3.13+")

translator = Translator()

async def TransLate(text: str, scr: str = 'auto', dest: str = 'en') -> str:
    try:
        result = await translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"


async def LangDetect(text: str, set: str = "all") -> str:
    try:
        detection = await translator.detect(text)
        lang_name = LANGUAGES.get(detection.lang, detection.lang)

        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return f"{detection.confidence:.4f}"
        else:
            return f"{lang_name} ({detection.lang}), confidence: {detection.confidence:.2%}"
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"


async def CodeLang(lang: str) -> str:
    lang_lower = lang.lower()
    if lang_lower in LANGUAGES:
        return LANGUAGES[lang_lower]
    for code, name in LANGUAGES.items():
        if name.lower() == lang_lower:
            return code
    return "Мову не знайдено"


async def LanguageList(out: str = "screen", text: str = None) -> str:
    lines = ["N  Language             ISO-639 code   Text"]
    lines.append("-" * 55)

    for i, (code, name) in enumerate(list(LANGUAGES.items())[:40], 1):
        translated = ""
        if text:
            try:
                res = await translator.translate(text, dest=code)
                translated = res.text[:35]
            except:
                translated = "—"
        line = f"{i:2d} {name:<20} {code:<10} {translated}"
        lines.append(line)

    result = "\n".join(lines)

    if out == "file":
        with open("languages_gtrans3.txt", "w", encoding="utf-8") as f:
            f.write(result)
        return "Ok (збережено в languages_gtrans3.txt)"
    else:
        print(result)
        return "Ok"