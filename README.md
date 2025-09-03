# Foldar CLI

**Foldar** is a lightweight CLI tool built with [Typer](https://typer.tiangolo.com/) that scaffolds a **Next.js boilerplate** project structure.  
It automatically generates common folders and prebuilt components so you can start coding immediately without repetitive setup.

---

## 📦 Installation

Clone the repository and install locally in editable mode:

```bash
git clone https://github.com/yourusername/foldar-cli.git
cd foldar-cli
pip install -e .
```

To uninstall:

```bash
pip uninstall foldar -y
```

---

## ⚡ Usage

Currently, `foldar` supports **Next.js** projects only.

Run the following command inside your Next.js project root:

```bash
foldar next-create app
```

This will create a folder structure like:

```
app/
├─ components/
│  ├─ includes/
│  │  └─ Navbar.tsx
│  ├─ ui/
│  │  ├─ Button.tsx
│  │  ├─ theme-provider.tsx
│  │  └─ theme-switcher.tsx
│  └─ Hero.tsx
│
├─ types/
│  └─ uiTypes.ts
│
├─ public/
│  └─ assets/
│
├─ about/
├─ contact/
├─ blogs/
└─ page.tsx
```

---

## NOTE

ths won't create a new next.js project currently, this only creates some boilerplate next.js code

---

## 🔧 Commands

- **Create boilerplate (Next.js only)**
  run it in the root of next.js project

  ```bash
  foldar next-create app
  ```

- **Show help**

  ```bash
  foldar --help
  ```

- **Check version**

  ```bash
  foldar version
  ```

---

## 🛠 Customization

The boilerplate code is stored in `code_templates.py`.
You can modify the template strings (`NAVBAR_CODE`, `BUTTON_CODE`, etc.) to suit your preferred project setup.

---

## 📜 License

MIT [License](LICENSE).
