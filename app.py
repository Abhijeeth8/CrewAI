# import gradio as gr
# from src.project1.main import run

# print("Starting the app")

# # Callback function
# # def handle_submit(requirements, module_name, class_name):
# #     run(requirements, module_name, class_name)
# #     # return f"You entered: {text}"

# # # Gradio interface
# with gr.Blocks() as demo:
#     print("Server started")

#     gr.Markdown("## Simple Gradio App")

#     # requirements = gr.Textbox(label="Enter requirements", lines=4, placeholder="Type here...")
#     # module_name = gr.Textbox(label="Enter module_name", lines=1, placeholder="Type here...")
#     # class_name = gr.Textbox(label="Enter class_name", lines=1, placeholder="Type here...")

#     # # output_text = gr.Textbox(label="Output")

#     # submit_btn = gr.Button("Submit")

#     # # Link the button to the function
#     # submit_btn.click(fn=handle_submit, inputs=[requirements, module_name, class_name])

# # # Launch the app
# demo.launch(server_name="0.0.0.0", server_port=7860)


import streamlit as st
from src.project1.main import run

print("app starting...")

st.title("📋 Python Application Creator app")

# Input fields
requirements = st.text_area("Enter requirements")
module_name = st.text_input("Enter module name(should end with .py)")
class_name = st.text_input("Enter class name")

# Submit button
if st.button("Submit"):
    st.write("Running...")
    run(requirements, module_name, class_name)
    st.success("Task completed.")