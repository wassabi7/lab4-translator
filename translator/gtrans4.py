from googletrans import Translator, LANGUAGES

async def TransLate(text: str, scr: str = 'auto', dest: str = 'en') -> str:
    try:
        async with Translator() as translator:
            result = await translator.translate(text, src=scr, dest=dest)
            return result.text
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"


async def LangDetect(text: str, set: str = "all") -> str:
    try:
        async with Translator() as translator:
            detection = await translator.detect(text)
            lang_name = LANGUAGES.get(detection.lang, detection.lang)

            if set == "lang":
                return detection.lang
            elif set == "confidence":
                return str(detection.confidence)
            else:  # "all"
                return f"{lang_name} ({detection.lang}), confidence: {detection.confidence:.2%}"
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"


def CodeLang(lang: str) -> str:
    lang_lower = lang.lower()
    if lang_lower in LANGUAGES:
        return LANGUAGES[lang_lower]
    for code, name in LANGUAGES.items():
        if name.lower() == lang_lower:
            return code
    return "Мову не знайдено"


async def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        lines = ["N  Language          ISO-639 code   Text"]
        lines.append("-" * 50)

        for i, (code, name) in enumerate(list(LANGUAGES.items())[:30], 1):
            translated = ""
            if text:
                try:
                    async with Translator() as t:
                        res = await t.translate(text, dest=code)
                        translated = res.text[:40]
                except:
                    translated = "—"
            line = f"{i:2d} {name:18} {code:10} {translated}"
            lines.append(line)

        result = "\n".join(lines)

        if out == "file":
            with open("languages.txt", "w", encoding="utf-8") as f:
                f.write(result)
            return "Ok (збережено в languages.txt)"
        else:
            print(result)
            return "Ok"
    except Exception as e:
        return f"Помилка: {str(e)}"