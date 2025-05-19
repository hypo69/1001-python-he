## /src/endpoints/hypo69/code_assistant/make_summary.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
module: src.endpoints.hypo69.code_assistant.make_summary
    :platform: Windows, Unix
    :synopsis: מודול המרכיב את הקובץ `summary.md` לצורך הידור באמצעות `mdbook`.
    מידע נוסף: https://chatgpt.com/share/6742f054-aaa0-800d-9f84-0ab035a2a2c2
"""

from pathlib import Path
from typing import Optional
import argparse



def make_summary(docs_dir: Path, lang: str = 'en') -> None:
    """
    יוצר את הקובץ SUMMARY.md באמצעות מעבר רקורסיבי על התיקייה.

    Args:
        docs_dir (Path): נתיב לספריית המקור 'src'.
        lang (str): שפת סינון הקבצים. ערכים אפשריים: 'ru' או 'en'.
    """
    # שימוש בנתיב השורש ליצירת הנתיב לקובץ SUMMARY.md
    summary_file = Path.cwd() / '500' / 'SUMMARY.md'
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    _make_summary(docs_dir, summary_file, lang)


def _make_summary(src_dir: Optional[Path] = Path.cwd() , summary_file_path: Optional[Path] = Path.cwd() / 'SUMMARY.MD', lang: str = 'en') -> bool:
    """
    עובר רקורסיבית על תיקייה ויוצר קובץ SUMMARY.md עם פרקים המבוססים על קבצי .md.

    Args:
        src_dir (Path): נתיב לתיקיית קובצי המקור מסוג .md.
        summary_file (Path): נתיב לשמירת הקובץ SUMMARY.md.
        lang (str): שפת סינון הקבצים. ערכים אפשריים: 'ru' או 'en'.
    """
    try:
        if summary_file_path.exists():
            print(f"הקובץ {summary_file_path} כבר קיים. תוכנו יידרס.")

        with summary_file_path.open('w', encoding='utf-8') as summary:
            summary.write('# Summary\n\n')

            for path in sorted(src_dir.rglob('*.md')):
                if path.name == 'SUMMARY.md':
                    continue

                # סינון קבצים לפי שפה
                if lang == 'ru' and not path.name.endswith('.ru.md'):
                    # דילוג על קבצים ללא הסיומת .ru.md
                    continue

                elif lang == 'en' and path.name.endswith('.ru.md'):
                    # דילוג על קבצים עם הסיומת .ru.md
                    continue

                relative_path = path.relative_to(src_dir.parent)
                summary.write(f'- [{path.stem}]({relative_path.as_posix()})\n')
        return True
    except Exception as ex:
        print(f"שגיאה ביצירת הקובץ `summary.md`: {ex}")
        return False


if __name__ == '__main__':
    # ניתוח ארגומנטים משורת הפקודה
    # parser = argparse.ArgumentParser(description="יצירת קובץ SUMMARY.md עם סינון לפי שפה.")
    # parser.add_argument('-lang', type=str, choices=['ru', 'en'], default='en', help="שפת סינון הקבצים (ru או en). ברירת המחדל היא 'en'.")
    # parser.add_argument('src_dir', type=str, help="נתיב לספריית המקור 'src'.")
    # args = parser.parse_args()

    # המרת הנתיב לאובייקט Path
    src_dir = input(f"ספריית התחלה (ברירת מחדל {Path.cwd()/ '500'})") or Path.cwd() / '500'
    ...
    # קריאה לפונקציה make_summary עם הארגומנטים שהועברו
    make_summary(src_dir,'en')