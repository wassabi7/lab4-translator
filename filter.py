import configparser
import asyncio
from translator.gtrans4 import TransLate, LangDetect

async def main():
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')

    filename = config['Settings']['filename']
    target_lang = config['Settings']['target_lang']
    module_name = config['Settings']['module']
    output = config['Settings'].get('output', 'screen')
    max_sentences = int(config['Settings'].get('max_sentences', 100))

    print(f"Файл: {filename}")
    print(f"Модуль: {module_name}")
    print(f"Мова перекладу: {target_lang}")
    print(f"Вивід: {output}\n")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            full_text = f.read().strip()
        print(f"Розмір файлу: {len(full_text)} символів")
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        return

    import re
    sentences = re.split(r'[.!?]+', full_text)
    sentences = [s.strip() for s in sentences if s.strip()]

    print(f"Кількість речень у файлі: {len(sentences)}")

    sentences = sentences[:max_sentences]
    text_to_translate = ". ".join(sentences) + "."

    print(f"\nМова тексту визначається...")

    lang_info = await LangDetect(text_to_translate)
    print(f"Мова тексту: {lang_info}\n")

    print("Виконується переклад...")
    translated = await TransLate(text_to_translate, 'auto', target_lang)

    if output.lower() == "file":
        output_filename = f"{filename.rsplit('.', 1)[0]}_{target_lang}.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(translated)
            print(f"\nOk. Результат збережено у файл: {output_filename}")
        except Exception as e:
            print(f"Помилка запису у файл: {e}")
    else:
        print(f"\nПереклад на {target_lang}:")
        print("-" * 50)
        print(translated)
        print("-" * 50)


if __name__ == "__main__":
    asyncio.run(main())