import json
import streamlit as st


# Mengatur konfigurasi halaman
st.set_page_config(page_title="Cek Followers Instagram", layout="centered")

hide_menu_style = """
        <style>
        #
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Fungsi untuk menemukan akun yang tidak follow back
def find_not_following_back(followers_data, following_data):
    # Extract followers - gunakan field 'value' yang sudah berisi username
    followers = [j["value"] for i in followers_data if "string_list_data" in i for j in i["string_list_data"] if "value" in j]
    
    # Extract following - ambil dari 'href' dan bersihkan dari '_u/'
    following = []
    for i in following_data['relationships_following']:
        if "string_list_data" in i:
            for j in i["string_list_data"]:
                if "href" in j:
                    # Extract username dari URL dan hapus '_u/' jika ada
                    username = j["href"].replace("https://www.instagram.com/_u/", "").replace("https://www.instagram.com/", "")
                    following.append(username)
    
    return [user for user in following if user not in followers]

# Fungsi untuk menemukan akun yang tidak kita follow balik
def find_not_following_them_back(followers_data, following_data):
    # Extract followers - gunakan field 'value' yang sudah berisi username
    followers = [j["value"] for i in followers_data if "string_list_data" in i for j in i["string_list_data"] if "value" in j]
    
    # Extract following - ambil dari 'href' dan bersihkan dari '_u/'
    following = []
    for i in following_data['relationships_following']:
        if "string_list_data" in i:
            for j in i["string_list_data"]:
                if "href" in j:
                    # Extract username dari URL dan hapus '_u/' jika ada
                    username = j["href"].replace("https://www.instagram.com/_u/", "").replace("https://www.instagram.com/", "")
                    following.append(username)
    
    return [user for user in followers if user not in following]

# Judul aplikasi
# st.markdown(
#     """
#     # My first app
#     Aplikasi ini adal
#     """
# )


st.title("Cek Followers Instagram")
st.caption('Copyright by @yusufandrika')

st.text('Hello! Please make sure the selected folder is correct.')
st.text('Pay close attention to the upload column name for each file and avoid mixing them up.')
st.text('Enjoy! 😊')

st.markdown("""
    <h4>Video Tutorial:</h4>
    <a href="https://vt.tiktok.com/ZSjkxHcns/" target="_blank">
        <button style="background-color: #ff2d55; color: white; padding: 10px; border: none; cursor: pointer;">
            Tonton di TikTok
        </button>
    </a>
""", unsafe_allow_html=True)
# Upload file JSON untuk followers dan following
followers_file = st.file_uploader("Upload File Followers (JSON)", type="json")
following_file = st.file_uploader("Upload File Following (JSON)", type="json")

# Proses file saat file di-upload
if followers_file and following_file:
    followers_data = json.load(followers_file)
    following_data = json.load(following_file)
    
    # Dapatkan daftar akun yang tidak follow-back
    not_following_back = find_not_following_back(followers_data, following_data)
    
    # Dapatkan daftar akun yang tidak kita follow balik
    not_following_them_back = find_not_following_them_back(followers_data, following_data)
    
    # Tampilkan hasil dalam format daftar
    st.subheader("📊 Hasil Analisis:")
    
    # Tab untuk memisahkan kedua kategori
    tab1, tab2 = st.tabs(["❌ Tidak Follow Back Kita", "✅ Tidak Kita Follow Back"])
    
    with tab1:
        st.markdown("**Akun yang kita follow tapi tidak follow back:**")
        if not_following_back:
            st.info(f"Ditemukan {len(not_following_back)} akun")
            for user in not_following_back:
                st.write(f"- [Instagram: {user}](https://instagram.com/{user})", unsafe_allow_html=True)
        else:
            st.success("🎉 Semua akun yang kita follow sudah follow back!")
    
    with tab2:
        st.markdown("**Akun yang follow kita tapi tidak kita follow back:**")
        if not_following_them_back:
            st.info(f"Ditemukan {len(not_following_them_back)} akun")
            for user in not_following_them_back:
                st.write(f"- [Instagram: {user}](https://instagram.com/{user})", unsafe_allow_html=True)
        else:
            st.success("🎉 Kita sudah follow back semua followers!")
