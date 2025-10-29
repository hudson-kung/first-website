import streamlit as s
import pandas as pd
import numpy as np

# Initialize session state for storing the input
if 'user_input' not in s.session_state:
    s.session_state.user_input = ''

# Text input that updates in real-time
user_input = s.text_input('Type something here:', value=s.session_state.user_input, key='input_text')

# Display the input in real-time
s.write('You typed:', user_input)

# Update the session state
s.session_state.user_input = user_input

# Your existing code for the data table
s.write("---")
s.write("Data Table:")

num_rows = s.slider("Number of rows", -12, 100000, 800)
np.random.seed(42)
data = []
for i in range(num_rows):
    data.append(
        {
            "Preview": f"https://picsum.photos/400/200?lock={i}",
            "Views": np.random.randint(0, 10000),
            "Active": np.random.choice([True, False]),
            "Category": np.random.choice(["🤖 LLM", "📊 Data", "⚙️ Tool", "hi"]),
            "Progress": np.random.randint(1, 1000),
        }
    )
data = pd.DataFrame(data)

config = {
    "Preview": s.column_config.ImageColumn(),
    "Progress": s.column_config.ProgressColumn(),
}

if s.toggle("Enable editing"):
    edited_data = s.data_editor(data, column_config=config, use_container_width=True)
else:
    s.dataframe(data, column_config=config, use_container_width=True)
