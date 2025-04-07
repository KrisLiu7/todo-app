import streamlit as st
from datetime import date, datetime
import requests
import uuid

st.set_page_config(page_title="To-Do List", page_icon="📝")

# API endpoints
ADD_API_URL = "https://be4okvqmdc.execute-api.us-east-1.amazonaws.com/prod/add_task"
DELETE_API_URL = "https://be4okvqmdc.execute-api.us-east-1.amazonaws.com/prod/delete"
UPDATE_API_URL = "https://be4okvqmdc.execute-api.us-east-1.amazonaws.com/prod/update_status"
GET_TASKS_API_URL = "https://be4okvqmdc.execute-api.us-east-1.amazonaws.com/prod/get_tasks"

# Login form
def login():
    st.title("To-Do List Login")

    st.markdown("""
        <script>
        const inputBox = window.parent.document.querySelector('input[type="password"]');
        inputBox?.addEventListener("keydown", function(e) {
            if (e.key === "Enter") {
                setTimeout(() => {
                    window.parent.document.querySelector('button[kind="formSubmit"]').click();
                }, 50);
            }
        });
        </script>
    """, unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Enter password", type="password")
        submitted = st.form_submit_button("Enter")

        if submitted:
            if password == "NoBobaToday":
                st.session_state.logged_in = True
                st.session_state.user_id = username.strip() or "default_user"

                # 🔄 Load tasks from DynamoDB
                response = requests.post(GET_TASKS_API_URL, json={
                    "user_id": st.session_state.user_id
                })

                if response.status_code == 200:
                    st.session_state.tasks = response.json().get("tasks", [])
                else:
                    st.session_state.tasks = []
                    st.warning("⚠️ Could not load tasks from DynamoDB.")

            else:
                st.error("Incorrect password. Try again.")

# Login check
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

# Initialize task list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add Task UI
st.title("To-Do List")
st.subheader("Add a New Task")

title = st.text_input("Task Title")
description = st.text_area("Description")
status = st.selectbox("Status", ["Waiting to start", "In Progress", "Finished"])
due_date = st.date_input("Due Date", date.today())

if st.button("Add Task"):
    if not title.strip():
        st.error("At least type something you lazy dog! 🐶")
    else:
        task_id = str(uuid.uuid4())
        user_id = st.session_state.get("user_id", "default_user")

        task = {
            "user_id": user_id,
            "task_id": task_id,
            "title": title.strip(),
            "description": description.strip(),
            "status": status,
            "due_date": str(due_date)
        }

        response = requests.post(ADD_API_URL, json=task)

        if response.status_code == 200:
            st.session_state.tasks.append({
                **task,
                "created_at": datetime.now()
            })
            st.success("✅ Task added to DynamoDB!")
        else:
            st.error("Failed to add task. Please try again.")

# Task List Display
st.subheader("Your Tasks")

if not st.session_state.tasks:
    st.info("No tasks yet!")
else:
    tasks_sorted = sorted(st.session_state.tasks, key=lambda x: x.get("created_at", datetime.now()))

    for i, task in enumerate(tasks_sorted):
        if not task["title"].strip():
            continue

        st.markdown(f"**📝 {task['title']}**")

        if task["description"].strip():
            st.write(f"📄 {task['description']}")
        else:
            st.write("📝")

        st.write(f"📅 Due: {task['due_date']}")

        new_status = st.selectbox(
            "📌 Status",
            ["Waiting to start", "In Progress", "Finished"],
            index=["Waiting to start", "In Progress", "Finished"].index(task["status"]),
            key=f"status_{i}"
        )

        if new_status != task["status"]:
            payload = {
                "user_id": task["user_id"],
                "task_id": task["task_id"],
                "status": new_status
            }
            response = requests.post(UPDATE_API_URL, json=payload)

            if response.status_code == 200:
                task["status"] = new_status
                st.success("🔁 Status updated in DynamoDB!")
            else:
                st.error("Failed to update status.")

        if st.button(f"🗑️ Delete", key=f"delete_{i}"):
            response = requests.post(DELETE_API_URL, json={
                "user_id": task["user_id"],
                "task_id": task["task_id"]
            })

            if response.status_code == 200:
                st.session_state.tasks.remove(task)
                st.success("🗑️ Task deleted!")
                st.rerun()
            else:
                st.error("Failed to delete task.")

        st.markdown("---")