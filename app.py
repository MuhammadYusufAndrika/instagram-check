from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

# Fungsi untuk memproses data followers dan following
def find_not_following_back(followers_data, following_data):
    followers = [j["value"] for i in followers_data for j in i["string_list_data"]]
    following = [j["value"] for i in following_data['relationships_following'] for j in i["string_list_data"]]
    return [user for user in following if user not in followers]

# Halaman utama untuk upload file
@app.route('/')
def index():
    return render_template('upload.html')

# Endpoint untuk meng-handle file upload dan memprosesnya
@app.route('/check', methods=['POST'])
def check_followers():
    followers_file = request.files.get('followers_file')
    following_file = request.files.get('following_file')
    
    if followers_file and following_file:
        followers_data = json.load(followers_file)
        following_data = json.load(following_file)
        
        # Proses data untuk menemukan akun yang tidak follow back
        not_following_back = find_not_following_back(followers_data, following_data)
        
        # Tampilkan hasil di halaman hasil
        return render_template('result.html', not_following_back=not_following_back)
    
    return "Pastikan kedua file telah diunggah", 400

if __name__ == '__main__':
    app.run(debug=True)
