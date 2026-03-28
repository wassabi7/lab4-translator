import asyncio
from translator.gtrans3 import TransLate, LangDetect, CodeLang, LanguageList


async def main():
    text = "Добрий день, як справи?"

    print("=== ДЕМОНСТРАЦІЯ МОДУЛЯ gtrans3 ===\n")

    translated_text = await TransLate(text, 'auto', 'en')
    detected_lang = await LangDetect(text)

    lang_code = await CodeLang('uk')

    print("TransLate:", translated_text)
    print("LangDetect:", detected_lang)
    print("CodeLang('uk'):", lang_code)

    print("\nLanguageList (список мов):")
    await LanguageList("screen", text=text)

    print("\nДемонстрація завершена.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Виникла помилка: {e}")
