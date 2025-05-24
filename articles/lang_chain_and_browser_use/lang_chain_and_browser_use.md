## כיצד ליצור סוכן AI לעבודה עם דפדפן אינטרנט באמצעות LangChain ו-Browser-Use: מדריך צעד אחר צעד

מדריך זה צעד אחר צעד יראה לכם כיצד ליצור סוכן AI המסוגל לחפש מידע בגוגל ולנתח דפי אינטרנט, תוך שימוש ב-LangChain וב-Browser-Use.

**שלב 1: התקנת הספריות הדרושות**

ראשית, עליך להתקין את ספריות Python הדרושות. פתח טרמינל או שורת פקודה והפעל את הפקודה הבאה:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**שלב 2: הגדרת מפתחות API**

לעבודה עם OpenAI ו-SerpAPI דרושים מפתחות API.

*   **OpenAI API Key:** קבל את מפתח ה-API שלך באתר OpenAI (openai.com).
*   **SerpAPI API Key:** SerpAPI מספק API לעבודה עם תוצאות חיפוש. הירשם באתר serpapi.com (קיימת גרסת ניסיון חינמית), היכנס לחשבונך ומצא את מפתח ה-API שלך בעמוד ה-Dashboard.

צור קובץ `.env` באותה ספרייה בה ימוקם סקריפט ה-Python שלך, והוסף אליו את המפתחות בפורמט הבא:

```
OPENAI_API_KEY=ваш_openai_ключ
SERPAPI_API_KEY=ваш_serpapi_ключ
```

**שלב 3: יצירת סקריפט Python ‏(browser_agent.py)**

צור קובץ `browser_agent.py` והדבק לתוכו את הקוד הבא:

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# הגדרת רישום (logging)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# טעינת מפתחות API מקובץ .env
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # אתחול מודל השפה
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # ניתן לנסות מודלים אחרים

    # הגדרת כלי חיפוש (דוגמה פשוטה, ללא חיפוש בפועל בגוגל)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Ищу в Google: {query}",  # החלף בחיפוש אמיתי באמצעות SerpAPI במידת הצורך
        description="Ищет информацию в Google." # מחפש מידע בגוגל.
    )


    # הגדרת המשימה עבור הסוכן
    task = """
    Найди в Google последние новости о компании OpenAI. # מצא בגוגל את החדשות האחרונות אודות חברת OpenAI.
    Затем посети один из найденных сайтов и найди имена основателей. # לאחר מכן בקר באחד האתרים שנמצאו ומצא את שמות המייסדים.
    """

    # יצירת הסוכן
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # הפעלת הסוכן
    try:
        result = await agent.arun(task)
        print(f"Результат: {result}") # תוצאה: {result}
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}") # אירעה שגיאה: {e}

if __name__ == "__main__":
    asyncio.run(main())
```

**שלב 4: הפעלת הסוכן**

פתח טרמינל או שורת פקודה, עבור לספרייה עם הקובץ `browser_agent.py` והפעל אותו:

```bash
python browser_agent.py
```

**שלב 5: שיפור הסוכן (יכולות מתקדמות)**

*   **חיפוש אמיתי בגוגל:** החלף את פונקציית ה-`lambda` ב-`search_tool` בקוד המשתמש ב-SerpAPI לחיפוש אמיתי בגוגל. זה ידרוש לימוד התיעוד של SerpAPI.

*   **אינטראקציה עם דפי אינטרנט (Browser-Use):** כדי להוסיף פונקציונליות של אינטראקציה עם דפי אינטרנט (פתיחת קישורים, חילוץ טקסט וכו') יהיה צורך להשתמש בספריית `browser-use`. תיעוד הספרייה הזו יעזור לך להוסיף את הכלים המתאימים לסוכן שלך.

*   **שימוש בזיכרון:** כדי לשמור הקשר בין שאילתות ניתן להשתמש במנגנוני זיכרון של LangChain.

*   **שרשראות פעולה מורכבות יותר:** LangChain מאפשרת ליצור שרשראות פעולה מורכבות יותר (Chains) לפתרון משימות מורכבות יותר.

דוגמה זו מדגימה מבנה בסיסי. ליישום סוכן מלא, המקיים אינטראקציה עם הדפדפן ועם Google Search, יידרש עבודה נוספת עם SerpAPI ו-`browser-use`. אל תשכח לעיין בתיעוד של ספריות אלו לקבלת מידע מפורט יותר.