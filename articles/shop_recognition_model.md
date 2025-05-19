# אימון מודל OpenAI לסיווג דפי אינטרנט

## מבוא

אימון מודל OpenAI לקביעה האם דף אינטרנט הוא חנות מקוונת.

התהליך כולל את השלבים הבאים:
- הכנת נתונים,
- טוקניזציית טקסט,
- שליחת נתונים לאימון
- בדיקת המודל.

## שלב 1: הרשמה והגדרת תצורה של OpenAI API

כדי להתחיל לעבוד עם OpenAI API, יש להירשם לפלטפורמת OpenAI ולקבל מפתח API. מפתח זה ישמש לאימות בעת קריאה למתודות ה-API.

```python
import openai

# Установка ключа API
openai.api_key = 'your-api-key'
```

## שלב 2: הכנת נתונים

לאימון המודל נדרש להכין מערך נתונים שיכיל דוגמאות של דפי אינטרנט,
הן של חנויות מקוונות והן של דפים שאינם חנויות.
כל רשומה צריכה לכלול את טקסט הדף ואת התגית המתאימה (`positive` עבור חנויות ו-`negative` עבור דפים שאינם חנויות).

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

## שלב 3: טוקניזציית טקסט

לפני שליחת הנתונים למודל OpenAI, יש לבצע טוקניזציה לטקסט.
טוקניזציה היא תהליך פיצול הטקסט למילים או טוקנים נפרדים.
ב-Python ניתן להשתמש בספריות כמו NLTK, spaCy או tokenizers מהספרייה transformers.

דוגמה לטוקניזציה באמצעות NLTK:

```python
import nltk
from nltk.tokenize import word_tokenize

# Пример текста
text = "Это пример текста для токенизации."

# Токенизация текста
tokens = word_tokenize(text)
tokenized_text = ' '.join(tokens)
print(tokenized_text)
```

## שלב 4: שליחת נתונים לאימון

לאחר טוקניזציית הטקסט, ניתן לשלוח את הנתונים לאימון מודל OpenAI.
להלן דוגמת קוד לשליחת נתונים:

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

# Пример использования
data = [
    {"text": "Текст первой веб-страницы...", "label": "positive"},
    {"text": "Текст второй веб-страницы...", "label": "negative"}
]

job_id = train_model(data, positive=True)
print("Job ID:", job_id)
```

## שלב 5: בדיקת המודל

לאחר אימון המודל, יש לבדוק אותו על מערך נתונים לבדיקה.
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

# Пример использования
test_data = [
    {"text": "Текст тестовой веб-страницы...", "label": "positive"},
    {"text": "Текст другой тестовой страницы...", "label": "negative"}
]

predictions = test_model(test_data)
print("Predictions:", predictions)
```

## שלב 6: טיפול בשגיאות ושיפור המודל

אם המודל מספק תחזיות שגויות, ניתן לשפר אותו
על ידי הוספת נתונים נוספים או שינוי פרמטרי האימון. כמו כן, ניתן להשתמש במשוב לניתוח שגיאות.

דוגמה לטיפול בשגיאות:

```python
def handle_errors(predictions, test_data):
    for pred, entry in zip(predictions, test_data):
        if pred != entry["label"]:
            print(f"Incorrect prediction for page '{entry['name']}': Predicted {pred}, Actual {entry['label']}")

# Пример использования
handle_errors(predictions, test_data)
```