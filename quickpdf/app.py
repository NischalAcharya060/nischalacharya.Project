from flask import Flask, request, Response, send_file,render_template
from PIL import Image
import io

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/jpgtopng", methods=["GET"])
def jpg_to_png():
    return render_template("jpgtopng.html")

@app.route("/pngtojpg", methods=["GET"])
def png_to_jpg():
    return render_template("pngtojpg.html")

@app.route("/webptopng", methods=["GET"])
def webp_to_png():
    return render_template("webptopng.html")

@app.route("/bmptopng", methods=["GET"])
def bmp_to_png():
    return render_template("bmptopng.html")

@app.route("/pngtopdf", methods=["GET"])
def png_to_pdf():
    return render_template("pngtopdf.html")

if __name__ == "__main__":
    app.run()



app = Flask(__name__)

@app.route("/api/jpgtopng", methods=["POST"])
def jpg_to_png():
    image = request.files.get("image")
    if not image:
        return "No image provided", 400

    image = Image.open(image)
    png_image = io.BytesIO()
    image.save(png_image, format="PNG")
    png_image.seek(0)

    return send_file(
        png_image,
        mimetype="image/png",
        as_attachment=True,
        attachment_filename="image.png"
    )

if __name__ == "__main__":
    app.run()


app = Flask(__name__)

@app.route("/api/pngtojpg", methods=["POST"])
def png_to_jpg():
    image = request.files.get("image")
    if not image:
        return "No image provided", 400

    image = Image.open(image)
    jpeg_image = io.BytesIO()
    image.save(jpeg_image, format="JPEG")
    jpeg_image.seek(0)

    return send_file(
        jpeg_image,
        mimetype="image/jpeg",
        as_attachment=True,
        attachment_filename="image.jpeg"
    )

if __name__ == "__main__":
    app.run()


app = Flask(__name__)

@app.route("/api/webptopng", methods=["POST"])
def webp_to_png():
    image = request.files.get("image")
    if not image:
        return "No image provided", 400

    image = Image.open(image)
    png_image = io.BytesIO()
    image.save(png_image, format="PNG")
    png_image.seek(0)

    return send_file(
        png_image,
        mimetype="image/png",
        as_attachment=True,
        attachment_filename="image.png"
    )

if __name__ == "__main__":
    app.run()


app = Flask(__name__)

@app.route("/api/bmptopng", methods=["POST"])
def bmp_to_png():
    image = request.files.get("image")
    if not image:
        return "No image provided", 400

    image = Image.open(image)
    png_image = io.BytesIO()
    image.save(png_image, format="PNG")
    png_image.seek(0)

    return send_file(
        png_image,
        mimetype="image/png",
        as_attachment=True,
        attachment_filename="image.png"
    )

if __name__ == "__main__":
    app.run()


app = Flask(__name__)

@app.route("/api/pngtopdf", methods=["POST"])
def png_to_pdf():
    image = request.files.get("image")
    if not image:
        return "No image provided", 400

    image = Image.open(image)
    pdf_image = io.BytesIO()
    image.save(pdf_image, format="PDF")
    pdf_image.seek(0)

    return send_file(
        pdf_image,
        mimetype="application/pdf",
        as_attachment=True,
        attachment_filename="image.pdf"
    )

if __name__ == "__main__":
    app.run()
