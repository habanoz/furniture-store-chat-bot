import streamlit as st
from streamlit_chat import message
from chat import Chat


def start_chat_loop():
    chat = Chat()

    st.subheader("Hoşgeldiniz...")

    if 'responses' not in st.session_state:
        st.session_state['responses'] = ["Size nasıl yardımcı olabilirim?"]

    if 'requests' not in st.session_state:
        st.session_state['requests'] = []

    if 'buffer_memory' not in st.session_state:
        st.session_state.buffer_memory = chat.memory

    # container for chat history
    response_container = st.container()
    # container for text box
    textcontainer = st.container()

    with textcontainer:
        query = st.text_input("Query: ", key="input")
        if query:
            with st.spinner("yazıyor..."):
                response = chat.predict(query)

            st.session_state.requests.append(query)
            st.session_state.responses.append(response)

    with response_container:
        if st.session_state['responses']:

            for i in range(len(st.session_state['responses'])):
                message(st.session_state['responses'][i], key=str(i))
                if i < len(st.session_state['requests']):
                    message(st.session_state["requests"][i], is_user=True, key=str(i) + '_user')


if __name__ == '__main__':
    start_chat_loop()
