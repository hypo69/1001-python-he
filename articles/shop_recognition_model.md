# אימון מודל OpenAI לסיווג דפי אינטרנט
```

## מבוא

אימון מודל OpenAI לקביעה האם עמוד הוא חנות מקוונת.

- הכנת נתונים,
- טוקניזציה של טקסט,
- שליחת נתונים לאימון,
- בדיקת המודל.

## שלב 1: הרשמה והגדרת OpenAI API

על מנת להתחיל לעבוד עם OpenAI API, יש להירשם בפלטפורמת OpenAI ולקבל מפתח API. מפתח זה ישמש לאימות בעת קריאה למתודות ה-API.

```python
import openai

# הגדרת מפתח ה-API
openai.api_key = 'your-api-key'
```

## שלב 2: הכנת נתונים

לאימון המודל יש להכין ערכת נתונים שתכיל דוגמאות של דפי אינטרנט,
הן של חנויות והן שאינן חנויות.
כל רשומה צריכה לכלול את טקסט הדף ותווית מתאימה (`positive` עבור חנויות ו-`negative` עבור לא חנויות).

דוגמה לקובץ JSON:

```json
[
    {
        "text": "<html><body><h1>Welcome to Our Online Store</h1><p>We offer a wide range of products at competitive prices. Visit our store today!</p></body></html>",
        "label": "positive"
    },
    {
        "text": "<html><body><h1>About Us</h1><p>We are a leading provider of quality services. Contact us for more information.</p></body></html>",
        "label": "negative"
    }
]
```

## שלב 3: טוקניזציה של טקסט

לפני שליחת הנתונים למודל OpenAI, יש לבצע טוקניזציה של הטקסט.
טוקניזציה היא תהליך פיצול טקסט למילים בודדות או לטוקנים.
ב-Python, ניתן להשתמש בספריות כגון NLTK, spaCy או tokenizers מהספרייה transformers.

דוגמה לטוקניזציה באמצעות NLTK:

```python
import nltk
from nltk.tokenize import word_tokenize

# דוגמה לטקסט
text = "Это пример текста для токенизации."

# טוקניזציה של הטקסט
tokens = word_tokenize(text)
tokenized_text = ' '.join(tokens)
print(tokenized_text)
```

## שלב 4: שליחת נתונים לאימון

לאחר טוקניזציה של הטקסט, ניתן לשלוח את הנתונים לאימון מודל OpenAI.
להלן דוגמת קוד לשליחת הנתונים:

```python
import openai

def train_model(data, positive=True):
    try:
        response = openai.Train.create(
            model="text-davinci-003",
            documents=[entry["text"] for entry in data],
            labels=["positive" if positive else "negative"] * len(data),
            show_progress=True
        )
        return response.id
    except Exception as ex:
        print("An error occurred during training:", ex)
        return None

# דוגמת שימוש
data = [
    {"text": "Текст первой веб-страницы...", "label": "positive"},
    {"text": "Текст второй веб-страницы...", "label": "negative"}
]

job_id = train_model(data, positive=True)
print("Job ID:", job_id)
```

## שלב 5: בדיקת המודל

לאחר אימון המודל, יש לבדוק אותו על ערכת נתוני בדיקה.
להלן דוגמת קוד לבדיקה:

```python
def test_model(test_data):
    try:
        predictions = []
        for entry in test_data:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=entry["text"],
                max_tokens=1
            )
            prediction = response.choices[0].text.strip()
            predictions.append(prediction)
        return predictions
    except Exception as ex:
        print("An error occurred during testing:", ex)
        return None

# דוגמת שימוש
test_data = [
    {"text": "Текст тестовой веб-страницы...", "label": "positive"},
    {"text": "Текст другой тестовой страницы...", "label": "negative"}
]

predictions = test_model(test_data)
print("Predictions:", predictions)
```

## שלב 6: טיפול בשגיאות ושיפור המודל

אם המודל מספק חיזויים שגויים, ניתן לשפר אותו
על ידי הוספת נתונים נוספים או שינוי פרמטרי האימון. כמו כן, ניתן להשתמש במשוב לניתוח שגיאות.

דוגמה לטיפול בשגיאות:

```python
def handle_errors(predictions, test_data):
    for pred, entry in zip(predictions, test_data):
        if pred != entry["label"]:
            print(f"Incorrect prediction for page '{entry['name']}': Predicted {pred}, Actual {entry['label']}")

# דוגמת שימוש
handle_errors(predictions, test_data)