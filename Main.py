import streamlit as st
from langchain_community.llms import CTranslate2

# Initialize the Llama-3 model
model_id = 'NHL2-13b-chat-Llama2-ct2'
tokenizer_id = 'Nous-Hermes-Llama2-13b'
llm = CTranslate2(model_path=model_id, tokenizer_name=tokenizer_id, device="auto", compute_type="int8")

def main():
    # Configure Streamlit page
    st.set_page_config(page_title="Chat with Llama-3")
    st.header("Chat with Llama-3")

    # Create a text input for the user to ask a question
    user_input = st.text_input("Ask a question:")

    # Create an infinite loop to enable the user to chat with Llama-3
    while True:
        if user_input:
            # Run the Llama-3 model on the user's question and get the response
            response = llm.run(user_input)
            st.write(response)

            # Clear the user's input to enable them to ask another question
            user_input = st.text_input("Ask a question:")

# if _name_ == "_main_":
#     main()