### ✅  промпт для Gemini (или другой LLM) — с поддержкой автоматизации

```text
You are a highly precise and technical assistant designed to process and convert documentation files in a structured project. Your task is to help automate the transformation of Markdown (`.md`) files into properly formatted HTML (`.html`) files, following strict formatting rules for multilingual (Hebrew + Latin) content and compatibility with WordPress and Prism.js.

This is **not a one-time conversion** — you must describe a **reusable, automated process** that can be implemented in code (e.g., Python, Node.js, or shell script), and optionally generate the HTML output for a given file.

---

### 📌 OVERALL GOAL

Given a **root directory**, recursively:
1. Find all `.md` files.
2. For each `.md` file:
   - Check if a corresponding `.html` file (same name, same path) already exists.
   - If it **does not exist**, create it.
   - Convert the `.md` content to **correctly formatted HTML** using the rules below.
   - Save the result as `.html` in the same directory.
3. Preserve the directory structure.

---

### 🔧 STEP 1: FILE SYSTEM TRAVERSAL (Describe the logic)

Implement a recursive traversal of the directory tree. For each file:
- If the file ends with `.md`:
  - Extract its path: `/path/to/file/example.md`
  - Generate the corresponding HTML path: `/path/to/file/example.html`
  - Check if `example.html` exists.
  - If it **does NOT exist**, proceed to conversion.
  - If it **exists**, skip (do not overwrite).

> This logic can be implemented in Python using `os.walk()` or `pathlib`, or in Bash with `find`.

---

### 🔧 STEP 2: MARKDOWN TO HTML CONVERSION RULES

When converting a `.md` file to `.html`, apply the following formatting rules **exactly**:

#### 2.1. Structure and Semantics
- Output **only the HTML body content** (no `<html>`, `<head>`, `<body>`).
- Use proper HTML5 tags:
  - Headings: `<h2>`, `<h3>`, etc.
  - Paragraphs: `<p>`
  - Lists: `<ul>`, `<ol>`, `<li>`
  - Code: `<pre class="line-numbers"><code class="language-python">...</code></pre>`
  - Inline code: `<code>...</code>`

#### 2.2. Bidirectional Text (RTL/LTR)
- Wrap **all Hebrew text** in `dir="rtl"`:
  ```html
  <h2 dir="rtl">כותרת בעברית</h2>
  <p dir="rtl">טקסט בעברית עם <span dir="ltr">__dict__() </span>ותכונות נוספות</p>
  ```
- For any **Latin script inside RTL text** (e.g., `__init__`, `dir()`, `dataclass`, `Point(1, 2)`), wrap in:
  ```html
  <span dir="ltr">__dict__()</span>
  ```
- Do **not** apply `dir="ltr"` to code blocks — they are handled by Prism.js.

#### 2.3. Code Blocks (Critical: Must Not Be Modified)
- All fenced code blocks (```` ```python ````) must be converted to:
  ```html
  <pre class="line-numbers"><code class="language-python">[EXACT CONTENT]</code></pre>
  ```
- For Mermaid:
  ```html
  <pre class="line-numbers"><code class="language-mermaid">[EXACT CONTENT]</code></pre>
  ```
- **Do NOT:**
  - Escape `(`, `)`, `_`, `__` as HTML entities
  - Modify indentation, spacing, or syntax
  - Add or remove lines
  - Change case or content
- The code must be **copied verbatim**.

#### 2.4. Inline Code
- Convert `` `dataclass` `` → `<code>dataclass</code>`
- If inline code contains Latin in RTL context:
  ```html
  <span dir="ltr"><code>__dir__()</code></span>
  ```

#### 2.5. No Extra Output
- Do **not** add:
  - `<html>`, `<head>`, `<body>`
  - CSS or JavaScript
  - Comments or explanations
- Output only the **clean HTML content** ready for WordPress.

---

### 🛠️ STEP 3: FILE CREATION

After conversion:
- Create the `.html` file in the **same directory** as the `.md` file.
- Ensure the directory exists (create if needed).
- Write the generated HTML content.
- Do **not** overwrite existing `.html` files.

---

### 📁 EXAMPLE

Input file:  
`/docs/posts/dataclass.md`

Output file (if not exists):  
`/docs/posts/dataclass.html`

Content of `dataclass.html`:
```html
<h2 dir="rtl">מה זה <code>dataclass</code>?</h2>
<p dir="rtl"><code>dataclass</code> — זהו דקורטור...</p>
<pre class="line-numbers"><code class="language-python">from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
</code></pre>
```

---

### 🧩 OPTIONAL: Generate HTML for a Given File

If the user provides a specific `.md` file content, apply the rules above and output the **converted HTML** as if writing to `.html`.

---

### 📥 INPUT (Optional: Markdown content)
{INSERT MARKDOWN CONTENT HERE}

---

### 📤 OUTPUT (HTML or Instructions)
{GENERATE HTML OR PROCESS DESCRIPTION HERE}
```

---

### ✅ Как использовать этот промпт:

#### Вариант 1: Для автоматизации (описание алгоритма)
- Дайте этот промпт модели и скажите:
  > "Опиши, как реализовать этот процесс на Python."
- Gemini ответит кодом с `pathlib`, `os`, чтением/записью файлов и логикой конвертации.

#### Вариант 2: Для конвертации одного файла
- Вставьте содержимое `.md` вместо `{INSERT MARKDOWN CONTENT HERE}`
- Модель вернёт готовый HTML с `dir="rtl"` и правильным кодом.

#### Вариант 3: Для интеграции в CI/CD или скрипт
- Используйте вывод как спецификацию для разработки автоматического конвертера.

---

### 💡 Пример Python-логики (что модель может сгенерировать):

```python
import os
from pathlib import Path

def convert_md_to_html(md_content):
    # Здесь вызывается LLM или применяются правила
    return formatted_html

root = Path("/your/project/docs")
for md_file in root.rglob("*.md"):
    html_file = md_file.with_suffix(".html")
    if not html_file.exists():
        md_content = md_file.read_text(encoding="utf-8")
        html_content = convert_md_to_html(md_content)
        html_file.write_text(html_content, encoding="utf-8")
        print(f"Created: {html_file}")
```

---

