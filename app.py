import json
import streamlit as st


# Mengatur konfigurasi halaman
st.set_page_config(page_title="Cek Followers Instagram", layout="centered")

# Menyembunyikan logo GitHub, Share
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    [title="View source"] {display: none;}
    [data-testid="stSidebar"] header {visibility: visible;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Fungsi untuk menemukan akun yang tidak follow back
def find_not_following_back(followers_data, following_data):
    followers = [j["value"] for i in followers_data for j in i["string_list_data"]]
    following = [j["value"] for i in following_data['relationships_following'] for j in i["string_list_data"]]
    return [user for user in following if user not in followers]

# Judul aplikasi
# st.markdown(
#     """
#     # My first app
#     Aplikasi ini adal
#     """
# )


st.title("Cek Followers Instagram")
st.caption('Copyright by @yusufandrika')

st.text('Hello, keep in mind that the folder entered must not be wrong')
st.text('pay attention to the name of the upload column for each file')
st.text('do not get confused. Enjoyyy!!!')
# Upload file JSON untuk followers dan following
followers_file = st.file_uploader("Upload File Followers (JSON)", type="json")
following_file = st.file_uploader("Upload File Following (JSON)", type="json")

# Proses file saat file di-upload
if followers_file and following_file:
    followers_data = json.load(followers_file)
    following_data = json.load(following_file)
    
    # Dapatkan daftar akun yang tidak follow-back
    not_following_back = find_not_following_back(followers_data, following_data)
    
    # Tampilkan hasil dalam format daftar
    st.subheader("Akun Not Follow-back:")
    if not_following_back:
        for user in not_following_back:
            st.write(f"- [Instagram: {user}](https://instagram.com/{user})", unsafe_allow_html=True)
    else:
        st.write("Semua akun sudah mengikuti balik.")
