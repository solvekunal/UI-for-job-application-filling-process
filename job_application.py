import streamlit as st

# Title of the application
st.title("Job Application Form")
st.header("Personal Information")

# Initialize session state variables to store the inputs
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'email' not in st.session_state:
    st.session_state['email'] = ''
if 'phone' not in st.session_state:
    st.session_state['phone'] = ''
if 'position' not in st.session_state:
    st.session_state['position'] = ''
if 'experience' not in st.session_state:
    st.session_state['experience'] = ''
if 'resume' not in st.session_state:
    st.session_state['resume'] = None

def submit_form():
    st.session_state.submitted = True

# Personal Information
st.session_state['name'] = st.text_input('Full Name:', value=st.session_state['name'])
st.session_state['email'] = st.text_input('Email Address:', value=st.session_state['email'])
st.session_state['phone'] = st.text_input('Phone Number:', value=st.session_state['phone'])

# Job Position
st.session_state['position'] = st.selectbox('Position Applied For:', ['Software Engineer', 'Data Scientist', 'Product Manager', 'Designer'])

# File uploader for resume
st.session_state['resume'] = st.file_uploader('Upload Your Resume (PDF only):', type='pdf')

st.session_state['experience'] = st.text_area('Briefly describe your relevant experience:')


# Submit button
if st.button('Submit'):
    submit_form()

# Display submission status
if st.session_state.submitted:
    st.success('Your application has been submitted successfully!')
    st.write(f"Name: {st.session_state['name']}")
    st.write(f"Email: {st.session_state['email']}")
    st.write(f"Phone: {st.session_state['phone']}")
    st.write(f"Position Applied For: {st.session_state['position']}")
    st.write(f"Experience: {st.session_state['experience']}")
    if st.session_state['resume']:
        st.write(f"Resume: {st.session_state['resume'].name}")

