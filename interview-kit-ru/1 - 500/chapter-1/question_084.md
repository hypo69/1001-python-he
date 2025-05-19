### `question_084.md`

**שאלה 84.** מה תהיה התוצאה בעת ביצוע קוד הפייתון הבא?

```python
def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

print(anagram("cinema", "iceman"))
print(anagram("cool", "loco"))
print(anagram("men", "women"))
print(anagram("python", "pythno"))
```

-   א. `True True True True`
-   ב. `True False True False`
-   ג. `False True False True`
-   ד. `True True False True`

**תשובה נכונה: ד**

**הסבר:**

הקוד בודק האם שתי מילים הן אנאגרמות (מורכבות מאותן אותיות, אך בסדר שונה).

1.  **הפונקציה `anagram(word1, word2)`:**
    -   ממירה את שתי המילים לאותיות קטנות (`lower()`).
    -   ממיינת את האותיות של כל מילה (`sorted()`).
    -   אם האותיות הממוינות זהות, מחזירה `True` (המילים הן אנאגרמות), אחרת `False`.

2.  **תוצאות הקריאות לפונקציה:**
    -   "`cinema`" ו-"`iceman`": אנאגרמות. `sorted("cinema") == sorted("iceman")` -> `True`
    -   "`cool`" ו-"`loco`": אנאגרמות. `sorted("cool") == sorted("loco")` -> `True`
    -   "`men`" ו-"`women`": לא אנאגרמות. `sorted("men") != sorted("women")` -> `False`
    -   "`python`" ו-"`pythno`": אנאגרמות. `sorted("python") == sorted("pythno")` -> `True`

לפיכך, פלט התוכנית: `True True False True`.