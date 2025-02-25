from flask import Flask, render_template, request
from google import genai

# Konfigurasi API Google GenAI
client = genai.Client(api_key="INSERT YOUR API KEY IN HERE")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form['user_input']  # Ambil teks dari form
        try:
            # Generate response using Google GenAI
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=f"Generate only the SQL query for: {user_input}"
            )
            result = response.text.strip()  # Hasil dari model, di-trim untuk menghapus spasi ekstra
        except Exception as e:
            result = f"Error: {e}"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
