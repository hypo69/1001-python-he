**דרישה:**
נתונה רשימה של זוגות ערכים (tuple). יש ליצור על בסיסם מילון, כאשר, אם מפתח כבר קיים, אין לדרוס אותו אלא להוסיף את הערכים לרשימה הקיימת המשויכת למפתח זה.

**דוגמה:**

קלט:
`[('one', 1), ('two', 2), ('three', 3), ('one', 4), ('two', 5)]`

פלט:
```
{
   'one': [1,4],
   'two': [2,5],
   'three': [3]
}
```

קלט:
`[('a', 1), ('a', 2), ('b', 3), ('c', 4), ('b', 5)]`

פלט:
```
{
   'a': [1,2],
  'b': [3,5],
  'c': [4]
}
```