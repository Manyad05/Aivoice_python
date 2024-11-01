import streamlit as st
import pyttsx3
import threading

# Function to speak the text


def speak_text(input_text):
    # Create a new TTS engine instance inside the thread
    engine = pyttsx3.init()
    engine.say(input_text)
    engine.runAndWait()

# Main function to run the Streamlit app


def main():
    st.title("Text to Speech Converter")

    # Input text box
    input_text = st.text_area("Enter text here:", height=200)

    # File uploader for text files
    uploaded_file = st.file_uploader("Upload a text file", type="txt")

    if uploaded_file is not None:
        # Read the contents of the uploaded file
        file_contents = uploaded_file.read().decode("utf-8")
        input_text = file_contents  # Update the text area with the file contents
        st.text_area("File content:", file_contents, height=200)

    # Button to speak the text
    if st.button("Speak"):
        if input_text:
            # Use threading to prevent blocking
            threading.Thread(target=speak_text, args=(input_text,)).start()
            st.success("Speaking...")
        else:
            st.warning("Please enter or upload text before clicking 'Speak'.")


if __name__ == "__main__":
    main()
