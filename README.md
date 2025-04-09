# 📝 To-Do List Web App (Serverless, Streamlit + AWS)

This is a fully serverless to-do list application built using **Streamlit** for the frontend and **AWS services** for the backend.

## 🚀 How to Use:
- 🧠  Log in with a password (`NoBobaToday`)
- ✅ Add, view, update, and delete tasks (title + optional description, status, due date)
- 🔄 Update and filter by task status with dropdown: *Waiting to start*, *In Progress*, *Finished*
- 🔐 Automatically sync all data to **DynamoDB**, tasks are linked to your `user_id` (username).
- ✅ Host the app on **Streamlit Cloud** and connect to AWS via API Gateway and Lambda

---
## Features

| Feature | Description |
|---------|-------------|
| **Task Creation** | Add new tasks with a title and description. Requires at least 1 character in the task name. |
| **Task Management** | View, update, and delete your tasks in an intuitive interface. |
| **Progress Tracking** | Update and track the progress of each task (Not Started, In Progress, Completed). |
| **Persistence** | Tasks are automatically saved to and loaded from AWS DynamoDB using your user ID. |
| **Data Retention** | Your tasks remain accessible even after browser refresh or reopening the application. |
| **Creation Time Sorting** | Tasks are displayed in order of creation time for better organization. |

## Technology Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | AWS Lambda (Python) |
| **Database** | AWS DynamoDB |
| **Authentication** | AWS Cognito |
| **Deployment** | AWS Amplify |
---

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

```
/add_task
/delete
/update_status
/get_tasks
```

All routes share one API Gateway instance.

---

## 🌐Deployed on Streamlit Cloud
[https://todo-app-qs9amf4wq5e4xeilsfjkqs.streamlit.app/](https://todo-app-aws-7.streamlit.app/](https://todo-app-aws-7.streamlit.app/)

---
## Future Enhancements

| Feature | Description |
|---------|-------------|
| **Soft Delete** | Implement a soft delete functionality to maintain deleted tasks in DynamoDB for potential recovery |
| **Task Categories** | Add ability to categorize tasks for better organization |
| **Priority Levels** | Implement priority settings for tasks |
| **Due Dates** | Add calendar integration with due date reminders |
| **Mobile App** | Develop a companion mobile application |


## 👤 Author

**Kris Liu**  
Email: kris.shuyi.l@gmail.com  
GitHub: [@KrisLiu7](https://github.com/KrisLiu7)

---

## 📌 Notes

This is a class project built to demonstrate:
- Serverless architecture
- Multi-user support
- Cloud-based deployment
- Secure API integration using AWS Lambda and DynamoDB


## Screenshot
![Screenshot 2025-04-09 182656](https://github.com/user-attachments/assets/c8b78e54-8ac9-4e41-9d48-379baed3aea3)
![Screenshot 2025-04-09 182613](https://github.com/user-attachments/assets/f56aa921-1d3e-49b7-8217-b74cd2e8766b)
![Screenshot 2025-04-09 182534](https://github.com/user-attachments/assets/a799cfac-3d20-458b-b85e-536cc4022b26)


