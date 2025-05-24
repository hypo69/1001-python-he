import google.generativeai as genai

class GoogleGenerativeAI:
    """
    מחלקה לאינטראקציה עם מודלי Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, system_instruction: str = '', model_name: str = 'gemini-2.0-flash-exp'):
        """
        אתחול מודל GoogleGenerativeAI.

        :param api_key: מפתח API לגישה ל-Gemini.
        :type api_key: str
        :param system_instruction: הנחיה למודל (פרומפט מערכת).
        :type system_instruction: str
        :param model_name: שם המודל של Gemini הנמצא בשימוש. ברירת מחדל 'gemini-2.0-flash-exp'.
        :type model_name: str
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)  # הגדרת הספרייה עם מפתח ה-API
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # אתחול המודל עם ההנחיה

    def ask(self, q: str) -> str:
        """
        שולח שאילתת טקסט למודל ומחזיר את התשובה.

        ארגומנטים:
            q (str): השאלה שתישלח למודל.

        מחזיר:
            str: התשובה מהמודל.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"

################################################################################
#                                                                              #
#             INSERT YOUR GEMINI API KEY                                       #
#                                                                              #
################################################################################

API_KEY:str = input("מפתח API מ-`gemini`")
model = GoogleGenerativeAI(api_key = API_KEY)

q = input("שאלה: ")
response = model.ask(q)
print(response)