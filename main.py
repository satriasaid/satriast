import streamlit as st
st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")
st.title("My Portfolio")
st.header("Data Science Enthusiast")
st.sidebar.title("Navigation Bar")
page = st.sidebar.radio("My Pages",
                        ["About Me", 
                         "Projects", 
                         "Data Science", 
                         "Contact Me"])

if page == 'My Pages':
    import kontak
    kontak.tampilkan_kontak()
elif page == 'About Me':
    import tentang
    tentang.tampilkan_tentang()
elif page == 'Projects':
    import proyek
    proyek.tampilkan()   
elif page == 'Data Science':
    import prediksi
    prediksi.prediksi()
elif page == 'Contact Me':
    st.text("My Email: satriasaid@xyz.com")
    st.text("My Phone Number: 081234567890")
    st.text("My Linked In: linked.in/in/satriaxyz")

# pip freeze > requirements.txt (untuk memastikan bahwa streamlit akan menginstall library yang kita gunakan untuk file ini)