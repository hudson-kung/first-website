import streamlit as st

# Initialize session state for todos if it doesn't exist
if 'todos' not in st.session_state:
    st.session_state.todos = []

# Function to add a new todo
def add_todo():
    if st.session_state.new_todo:  # Check if there's text in the input
        st.session_state.todos.append({
            'task': st.session_state.new_todo,
            'completed': False
        })
        # Clear the input by setting it to an empty string
        st.session_state.new_todo = ""

# Function to toggle todo completion status
def toggle_complete(index):
    if 0 <= index < len(st.session_state.todos):
        st.session_state.todos[index]['completed'] = not st.session_state.todos[index]['completed']

# Function to delete a todo
def delete_todo(index):
    if 0 <= index < len(st.session_state.todos):
        st.session_state.todos.pop(index)

# App title
st.title('📝 My Todo App')

# Add todo section
with st.container():
    st.subheader('Add a new task')
    col1, col2 = st.columns([4, 1])
    with col1:
        # Text input for new todo
        st.text_input(
            'Task description',
            key='new_todo',
            label_visibility='collapsed',
            placeholder='Enter a new task...',
            on_change=add_todo,
            args=()
        )
    with col2:
        st.button('Add ➕', on_click=add_todo, use_container_width=True)

# Display todos
if st.session_state.todos:
    st.subheader('My Tasks')
    
    # Create columns for task and actions
    for i, todo in enumerate(st.session_state.todos):
        col1, col2, col3 = st.columns([1, 8, 2])
        with col1:
            # Checkbox to mark as complete
            st.checkbox(
                'Complete',  # Label for screen readers
                value=todo['completed'],
                key=f'check_{i}',
                on_change=toggle_complete,
                args=(i,),
                label_visibility='collapsed'
            )
        with col2:
            # Strikethrough text if completed
            if todo['completed']:
                st.markdown(f"~~{todo['task']}~~")
            else:
                st.write(todo['task'])
        with col3:
            # Delete button
            if st.button('❌', key=f'del_{i}', help='Delete this task'):
                delete_todo(i)
                st.rerun()

# Add some styling
st.markdown("""
    <style>
    .stButton>button {
        height: 2.5em;
    }
    [data-testid="stCheckbox"] {
        margin-top: 0.7em;
    }
    </style>
""", unsafe_allow_html=True)

