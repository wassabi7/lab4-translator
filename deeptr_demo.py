from translator.deeptr import TransLate, LangDetect, CodeLang, LanguageList

def main():
    text = "Добрий день, як справи?"

    print("=== ДЕМОНСТРАЦІЯ МОДУЛЯ deeptr ===\n")

    print("TransLate:", TransLate(text, 'auto', 'en'))
    print("LangDetect:", LangDetect(text))
    print("CodeLang('ukrainian'):", CodeLang("ukrainian"))
    LanguageList("screen")

if __name__ == "__main__":
    main()