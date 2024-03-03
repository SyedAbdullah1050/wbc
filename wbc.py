import streamlit as st

# Create an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)

# Function to delete a task
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        st.error("Task not found!")

# Function to display tasks
def view_tasks():
    st.write("### Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        st.write(f"{i}. {task}")

# Main function to run the Streamlit app
def main():
    st.title("Routine Management API")
    
    # Sidebar to perform actions
    st.sidebar.title("Actions")
    action = st.sidebar.selectbox("Select Action", ["Add Task", "Delete Task", "View Tasks"])
    
    if action == "Add Task":
        new_task = st.text_input("Enter new task:")
        if st.button("Add"):
            add_task(new_task)
            st.success("Task added successfully!")
    
    elif action == "Delete Task":
        task_to_delete = st.selectbox("Select task to delete:", tasks)
        if st.button("Delete"):
            delete_task(task_to_delete)
            st.success("Task deleted successfully!")
    
    elif action == "View Tasks":
        view_tasks()

if __name__ == "__main__":
    main()
