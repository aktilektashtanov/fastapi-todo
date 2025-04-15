# 📝 FastAPI To-Do API

A simple RESTful To-Do API built with FastAPI.  
It allows users to create, retrieve, update, and delete tasks.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aktilektashtanov/fastapi-todo.git
cd fastapi-todo
```
### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```

Open your browser at: http://127.0.0.1:8000/docs
You'll see an interactive API documentation (Swagger UI)

## 📦 API Endpoints

| Method | Endpoint      | Description               |
|--------|---------------|---------------------------|
| GET    | /tasks        | Get all tasks             |
| POST   | /tasks        | Create a new task         |
| PUT    | /tasks/{id}   | Mark task as completed    |
| DELETE | /tasks/{id}   | Delete a task by ID       |

## 🧪 Testing

You can test the API using:
- Swagger UI: http://127.0.0.1:8000/docs
- Postman / Insomnia (manual JSON requests)
- Python unit tests with pytest (optional)

## 👤 Author
[aktilektashtanov](https://github.com/aktilektashtanov)

---

## ✅ What to Do Next

1. Paste this into `README.md`
2. Save it
3. Push changes:

```bash
git add README.md
git commit -m "Add English README"
git push
