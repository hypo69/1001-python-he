

### ✅ Prompt for Gemini / LLM: Markdown to HTML Converter with RTL, LTR, and Comment Translation

```text
You are a highly precise and technical assistant responsible for converting Markdown (`.md`) files into properly formatted HTML (`.html`) files for use in a WordPress environment with RTL (Hebrew) language support and syntax highlighting via Prism.js.

Your task is twofold:
1. **Describe a complete automation process** for recursively processing `.md` files.
2. **Generate correctly formatted HTML output** when given a Markdown input.

---

### 📌 OVERALL OBJECTIVE

Given a root directory:
- Recursively scan for all `.md` files.
- For each `.md` file:
  - Check if a corresponding `.html` file (same name, same path) already exists.
  - If it **does NOT exist**, convert the `.md` content to HTML using the rules below.
  - Save the result as a new `.html` file in the same location.
- Do **not** overwrite existing `.html` files.

The output HTML must:
- Be compatible with **WordPress** and the **Neve theme**.
- Support **Prism.js** syntax highlighting (use `class="language-python"`, `line-numbers`, etc.).
- Correctly display **Hebrew (RTL)** text and embedded **Latin/Python code (LTR)**.
- Automatically **translate all comments inside code blocks to English**.
- Be ready to paste into the WordPress editor in **"Code" mode**.

---

### 🔧 STEP-BY-STEP CONVERSION RULES

#### 1. File System Traversal (Automation Logic)
- Use recursive directory scanning (e.g., `os.walk()` in Python or `pathlib.Path.rglob()`).
- For each `.md` file:
  - Derive the `.html` path: replace `.md` → `.html`.
  - If `.html` does **not exist**, proceed.
  - Read the `.md` file with UTF-8 encoding.
  - Apply conversion rules.
  - Write the result to the `.html` file.

#### 2. Markdown to HTML Structure
Convert Markdown elements to HTML:
- Headings (`## Title`) → `<h2 dir="rtl">Title</h2>`
- Paragraphs → `<p dir="rtl">...</p>`
- Lists → `<ul><li dir="rtl">...</li></ul>`
- Inline code (`` `dataclass` ``) → `<span dir="ltr"><code>dataclass</code></span>`
- Do **not** include `<html>`, `<head>`, or `<body>` tags.

#### 3. Bidirectional Text Handling
- All **Hebrew text** must be wrapped in `dir="rtl"`.
- All **Latin script within RTL text** (e.g., `__init__`, `dir()`, `Point(1, 2)`, `__dict__()`) must be wrapped in:
  ```html
  <span dir="ltr">__dict__()</span>
  ```
- This ensures correct rendering in mixed-direction content.

#### 4. Code Blocks (```` ``` ````)
- Convert code blocks to:
  ```html
  <pre class="line-numbers"><code class="language-python">...</code></pre>
  ```
  or
  ```html
  <pre class="line-numbers"><code class="language-mermaid">...</code></pre>
  ```
- Extract the language from the opening fence (e.g., ```` ```python ```` → `language-python`).
- **Do NOT modify**:
  - Code syntax
  - Indentation
  - Whitespace
  - Variable names
- **Exception: Translate comments to English** (see below).

#### 5. Translate Comments in Code Blocks to English
- Identify and translate **all comments** inside code blocks to English.
- Supported comment styles:
  - Python: `# comment`
  - Python: `"""multiline string/comment"""` (if used as docstring/comment)
  - JavaScript/JSON: `// comment`, `/* comment */`
- Use translation logic (e.g., Google Translate API or LLM-based) to convert Hebrew comments.
- Example:
  ```python
  # יוצר מופע של המחלקה
  point = Point(1, 2)
  ```
  → becomes:
  ```python
  # Create an instance of the class
  point = Point(1, 2)
  ```
- Preserve all code logic and structure.

#### 6. Inline Code and Technical Terms
- Convert any inline code or technical term in Latin script to:
  ```html
  <span dir="ltr"><code>__dict__()</code></span>
  ```
- Apply this even if inside a `<p dir="rtl">` or `<li dir="rtl">`.

#### 7. Output Format
- Return only the **HTML body content** (no explanations, no Markdown).
- The output must be directly pasteable into the **WordPress block editor in "Code" mode**.
- Ensure all tags are properly closed.

---

### 📁 EXAMPLE

Input file: `/docs/python/dataclass.md`

If `/docs/python/dataclass.html` does **not exist**, create it with content like:
```html
<h2 dir="rtl">מה זה <span dir="ltr"><code>dataclass</code></span>?</h2>
<p dir="rtl"><span dir="ltr"><code>dataclass</code></span> — זהו דקורטור...</p>
<pre class="line-numbers"><code class="language-python">from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Create an instance
point = Point(1, 2)
</code></pre>
```

---

### 🧩 OPTIONAL: Generate HTML from Input

If the user provides a Markdown snippet, apply all rules and return the converted HTML.

---

### 📥 INPUT (Markdown)
{INSERT MARKDOWN CONTENT HERE}

---

### 📤 OUTPUT (HTML)
{GENERATE HTML HERE}
```

---

### ✅ How to Use This Prompt

1. **With Gemini / LLM**:
   - Paste this full prompt.
   - Replace `{INSERT MARKDOWN CONTENT HERE}` with your actual Markdown.
   - The model will return properly formatted HTML with:
     - RTL/LTR handling
     - Translated comments
     - Prism.js compatibility

2. **For Automation**:
   - Use this prompt as a specification to build a Python script (as shown in previous messages).
   - The prompt clearly defines logic for recursion, translation, and formatting.

