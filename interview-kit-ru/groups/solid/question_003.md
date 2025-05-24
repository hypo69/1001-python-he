### `question_003.md` (SRP - רפקטורינג)

**שאלה 003.** נתונה המחלקה `OrderProcessor`, אשר אחראית על עיבוד הזמנות, כולל בדיקת זמינות פריטים במלאי ושליחת התראות למשתמש. מה הדרך הטובה ביותר לארגן מחדש מחלקה זו כדי שתתאים לעקרון האחריות היחידה (SRP)?

```python
class OrderProcessor:
    def __init__(self, order_data):
        self.order_data = order_data

    def process_order(self):
        if self._check_stock_availability():
            self._send_confirmation_email()
            return "Order processed successfully"
        else:
            return "Order processing failed: Out of stock"

    def _check_stock_availability(self):
        # Code to check stock availability
        return True  # Simplified for example

    def _send_confirmation_email(self):
        # Code to send confirmation email
        print("Sending confirmation email...")
```

A. אין צורך לשנות דבר, המחלקה `OrderProcessor` כבר עומדת בעקרון SRP, מכיוון שהיא אחראית על "עיבוד הזמנות".

B. יש ליצור מחלקות נפרדות: `OrderValidator` לבדיקת זמינות פריטים ו- `NotificationService` לשליחת התראות, והמחלקה `OrderProcessor` צריכה לתאם את פעולתן.

C. יש להוסיף למחלקה `OrderProcessor` שיטות לעבודה עם מסד נתונים, כדי שהיא תוכל לשמור מידע על הזמנות באופן עצמאי.

D. יש למחוק את השיטות `_check_stock_availability` ו- `_send_confirmation_email`, כדי שהמחלקה `OrderProcessor` תעסוק רק בתיאום פעולות.

**תשובה נכונה: B**

**הסבר:**

בגרסה הנוכחית, למחלקה `OrderProcessor` יש לפחות *שלוש* אחריויות:

1.  **ניהול תהליך עיבוד ההזמנה.**
2.  **בדיקת זמינות פריטים במלאי.**
3.  **שליחת התראות למשתמש.**

כדי לעמוד בעקרון SRP, יש להפריד אחריויות אלו למחלקות נפרדות.

*   **`OrderValidator`**: מחלקה האחראית על בדיקת היתכנות ביצוע ההזמנה (לדוגמה, בדיקת זמינות פריטים במלאי).
*   **`NotificationService`**: מחלקה האחראית על שליחת התראות למשתמש (לדוגמה, שליחת אישור הזמנה).
*   **`OrderProcessor`**: מחלקה האחראית על ניהול תהליך עיבוד ההזמנה.

**מדוע זהו שיפור:**

*   לכל מחלקה יש כעת רק *סיבה אחת* לשינוי. אם דרך בדיקת זמינות הפריטים במלאי תשתנה, יהיה צורך לשנות רק את `OrderValidator`, מבלי להשפיע על `OrderProcessor` או `NotificationService`.
*   הקוד הופך למודולרי יותר, ניתן לבדיקה ותחזוקה בקלות רבה יותר.

*   **אפשרות A אינה נכונה:** ל- `OrderProcessor` יש יותר מדי תחומי אחריות.
*   **אפשרות B נכונה:** פתרון נכון להפרדת תחומי האחריות.
*   **אפשרות C אינה נכונה:** הוספת עבודה עם מסד נתונים רק תחמיר את הפרת עקרון SRP.
*   **אפשרות D אינה נכונה:** מחיקת השיטות אינה פותרת את הבעיה, יש להעביר אותן למחלקות אחרות.

**לסיכום:**

כדי לעמוד בעקרון SRP, יש לארגן מחדש את המחלקה `OrderProcessor` על ידי ייחוד מחלקות נפרדות לבדיקת זמינות פריטים במלאי ולשליחת התראות, כאשר המחלקה `OrderProcessor` עצמה תתאם את עבודתן.

לפיכך, אפשרות B היא הנכונה.