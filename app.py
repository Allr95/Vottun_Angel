from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # URL de la imagen que deseas mostrar
    image_url = 'https://ipfsgw.vottun.tech/ipfs/bafkreiejryfi2l5osnwmk4fswqbovnpackv46pz2fv22phb2owmezgjbxu'

    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=False)

