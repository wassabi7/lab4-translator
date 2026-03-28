import asyncio
from translator.gtrans4 import TransLate, LangDetect, CodeLang, LanguageList

async def main():
    text = "Добрий день, як справи?"

    print("=== ДЕМОНСТРАЦІЯ МОДУЛЯ gtrans4 (googletrans 4.0.2) ===\n")

    print("TransLate:", await TransLate(text, 'auto', 'en'))
    print("LangDetect (all):", await LangDetect(text))
    print("LangDetect (lang):", await LangDetect(text, "lang"))
    print("CodeLang('ukrainian'):", CodeLang("ukrainian"))
    print("CodeLang('uk'):", CodeLang("uk"))

    print("\nLanguageList (перші 10 мов):")
    await LanguageList("screen", "Hello world")

if __name__ == "__main__":
    asyncio.run(main())