from langchain_openai import ChatOpenAI
from browser_use import Agent
from langchain.tools import Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv
import os
import asyncio
import logging

# הגדרת רישום (יומן)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# 1. הגדרת מפתחות API
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")  # יש להחליף במפתח ה-API האישי שלך
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


async def main():
    # 2. אתחול LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # 3. טעינת כלים
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Ищу в Google: {query}",
        description="מחפש מידע ב-Google.",
    )

    # 4. הגדרת המשימה
    task = """
    מצא ב-Google את החדשות האחרונות אודות חברת OpenAI.
    לאחר מכן, בקר באחד האתרים שנמצאו ומצא את שמות המייסדים.
    """

    # 5. יצירת סוכן
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # 6. הפעלת הסוכן
    try:
        result = await agent.arun(task)  # קריאה אסינכרונית לסוכן
        print(f"תוצאה: {result}")
    except Exception as e:
        logging.error(f"אירעה שגיאה: {e}")


if __name__ == "__main__":
    asyncio.run(main())