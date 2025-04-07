# todo-app
Created a webpage via Streamlit Cloud with AWS LambDa, IAM, APIs and DynamoDB.

# 📝 To-Do List Web App (Serverless, Streamlit + AWS)
This is a fully serverless to-do list application built using **Streamlit** for the frontend and **AWS services** for the backend.

Users can:
- ✅ Log in with a password
- ✅ Add, view, update, and delete tasks
- ✅ Filter by task status: *Waiting to start*, *In Progress*, *Finished*
- ✅ Automatically sync all data to **DynamoDB**
- ✅ Host the app on **Streamlit Cloud** and connect to AWS via API Gateway and Lambda

---

## 🔧 Tech Stack

| Layer       | Tech                  |
|-------------|------------------------|
| Frontend    | Streamlit (Python)     |
| Auth        | Simple password-based login in-app |
| Backend API | AWS API Gateway        |
| Logic       | AWS Lambda Functions   |
| Database    | DynamoDB               |
| Deployment  | Streamlit Cloud        |
| Versioning  | Git + GitHub           |

---

## 🚀 How to Use

1. 🧠 Log in using a username and password (`NoBobaToday`)
2. ✅ Add a task (title + optional description, status, due date)
3. 🔄 Update its status using a dropdown
4. 🗑 Delete a task with the delete button
5. 🔐 Tasks are linked to your `user_id` (username) and persist in DynamoDB

---

## 🗃 DynamoDB Table Setup
- **Table Name**: `Tasks`
- **Primary Key**: `user_id` *(String)*
- **Sort Key**: `task_id` *(String)*

Each item contains:

| Field        | Type     | Description                  |
|--------------|----------|------------------------------|
| user_id      | String   | ID of the logged-in user     |
| task_id      | String   | Unique task ID (UUID)        |
| title        | String   | Task title                   |
| description  | String   | Task notes or details        |
| status       | String   | "Waiting to start", "In Progress", "Finished" |
| due_date     | String   | Due date (YYYY-MM-DD)        |

---

## ☁ Lambda Functions

Source code for all Lambdas is in the [`/lambda`](lambda/) folder:

| Function Name              | Purpose                     |
|---------------------------|-----------------------------|
| `add_task.py`             | Add new tasks to DynamoDB   |
| `delete_task.py`          | Delete a task by keys       |
| `update_task_status.py`   | Update a task's status      |
| `Auto_Loading_From_DynamoDB.py` | Load all tasks for a given user |

Each function is exposed via **API Gateway POST routes** like:
/add_task /delete /update_status /get_tasks

👤 Author
Kris Liu
Email: kris.shuyi.l@gmail.com
GitHub: @KrisLiu7

📌 Notes
This is a class project built to demonstrate:
Serverless architecture
Multi-user support
Cloud-based deployment
Secure API integration using AWS Lambda and DynamoDB
