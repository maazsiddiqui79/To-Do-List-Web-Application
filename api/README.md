## 📝 Go‑Todo Task

A lightweight, intuitive task manager built with a clean UI and minimalistic design. Users can quickly add, complete, edit, and clear tasks in a streamlined interface.

---

### 🌐 Live Demo

Visit the live app here:
🔗 [https://go‑todo‑task.vercel.app/](https://go‑todo‑task.vercel.app/)

---

### 🚀 Overview & Key Features

Based on the site content:

* Displays current pending tasks (e.g., “You have 0 pending task” when none exist) ([todo-next-tasks.vercel.app][1])
* **Add tasks**: Quick entry via input box
* **Mark completed**: Click to toggle task status
* **Clear all**: Remove all tasks at once

---

### 📁 Project Structure (Suggested)

```
To-Do-List-Web-Application/
├── instance/
│   ├── TODO_DATABASE.db
├── static/
│   ├── Complete-Button.png
│   ├── dtom.jpeg
│   ├── style.css
│   └── Task-Title.png
│
├── templates/
│   ├── base.html
│   ├── connect.html
│   ├── docs.html
│   ├── index.html
│   └── update.html
│
├── venv/                   
│
├── index.py                
├── requirements.txt        
├── thumbnail.png
├── todo video.mp4
└── vercel.json          
```

---

### 🧰 Tech Stack

* **HTML5 & CSS3** – Structure and styling
* **Flask** – For effortless deployment and hosting
* **Vercel** – For effortless deployment and hosting

---

### ✅ Features at a Glance

| Feature         | Description                                   |
| --------------- | --------------------------------------------- |
| Add Task        | Enter text and submit via button or key       |
| Complete Task   | Click task to toggle completed status         |
| Edit Task       | *(Add if implemented—otherwise note planned)* |
| Remove & Clear  | Individual deletion or clear-all control      |
| Pending Counter | Live count of active tasks displayed          |

---

### 🛠️ Running Locally

1. **Clone the repo**

   ```bash
   git clone https://github.com/maazsiddiqui79/To-Do-List-Web-Application.git
   ```
2. **Install dependencies** (if using Node):

   ```bash
   cd go-todo-task
   npm install
   ```
3. **Start development server**:

   ```bash
   npm run dev
   # or
   yarn dev
   ```
4. **View app** in browser at `http://localhost:3000`

---

### 🚢 Deployment

Easily deploy using Vercel:

1. Connect your repo to Vercel
2. Configure build command (e.g., `npm run build`) and output directory
3. Deploy with a single click

---

### ✅ Planned Enhancements

* **Edit task** functionality
* **Persistent storage** via localStorage or a backend
* **Due dates & priorities** for tasks
* **Filter views**: All, Active, Completed
* **Animations & accessibility improvements**

---

### ✍️ Author

**Maaz Siddiqui**
Computer Engineering student with a keen interest in front‑end web development and productivity tools.
GitHub: [ github.com/maazsiddiqui79]( https://github.com/maazsiddiqui79)

---
