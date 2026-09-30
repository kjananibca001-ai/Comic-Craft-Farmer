
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>ComicCraft - Farmer Story</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f1ff;
            margin: 0;
            padding: 30px;
        }

        .container {
            max-width: 1000px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 25px;
            box-shadow: 0 5px 20px #bbb;
        }

        h1 {
            text-align: center;
            color: #4b2aad;
            font-size: 40px;
        }

        .subtitle {
            text-align: center;
            font-size: 20px;
        }

        input, textarea {
            width: 95%;
            padding: 14px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 12px;
            font-size: 16px;
        }

        button {
            display: block;
            margin: 15px auto;
            padding: 14px 30px;
            background: #6c4cff;
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 18px;
            cursor: pointer;
        }

        button:hover {
            background: #4b2aad;
        }

        .download-btn {
            background: #159957;
        }

        .download-btn:hover {
            background: #0d713f;
        }

        .comic {
            margin-top: 35px;
        }

        .comic-title {
            text-align: center;
            color: #333;
            font-size: 30px;
        }

        .panels {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 25px;
        }

        .panel {
            background: #fff4c7;
            padding: 25px;
            border: 3px solid #333;
            border-radius: 18px;
            min-height: 190px;
        }

        .panel h2 {
            margin-top: 0;
            color: #333;
        }

        .panel p {
            font-size: 17px;
            line-height: 1.6;
        }

        .dialogue {
            background: white;
            padding: 12px;
            border-radius: 20px;
            border: 1px solid #aaa;
            margin-top: 15px;
            font-style: italic;
        }

        .story {
            margin-top: 30px;
            padding: 20px;
            background: #f1edff;
            border-radius: 15px;
            line-height: 1.7;
        }

        @media (max-width: 700px) {
            .panels {
                grid-template-columns: 1fr;
            }
        }

        @media print {

            body {
                background: white;
                padding: 0;
            }

            .container {
                box-shadow: none;
                max-width: 100%;
            }

            .input-area,
            .download-btn {
                display: none;
            }

            .comic {
                margin-top: 0;
            }

            .panel {
                break-inside: avoid;
            }
        }
    </style>
</head>

<body>

<div class="container">

    <div class="input-area">

        <h1>🎨 ComicCraft</h1>
       
        <p class="subtitle">
            Create your own comic story
        </p>

        <form method="POST">

            <input
                name="title"
                placeholder="Comic Title"
                required
            >

            <input
                name="character"
                placeholder="Main Character"
                required
            >

            <textarea
                name="story"
                rows="5"
                placeholder="Enter your story..."
                required
            ></textarea>

            <button type="submit">
                Create Comic
            </button>

        </form>

    </div>


    {% if title %}

    <div class="comic">

        <h2 class="comic-title">
            📖 {{ title }}
        </h2>

        <div class="panels">

            <div class="panel">

                <h2>🌱 Panel 1</h2>
                       <img src="/static/panel1.png" alt="Farmer Comic Panel 1"
     style="width:100%; border-radius:15px; margin-bottom:15px;">
                <p>
                    {{ character }} is a hardworking farmer
                    who takes care of the farm every day.
                </p>

                <div class="dialogue">
                    💬 "{{ character }}:
                    I will take good care of my crops."
                </div>

            </div>

              <div class="panel">

    <h2>🌧️ Panel 2</h2>

    <img src="{{ url_for('static', filename='panel2.png') }}"
         alt="Farmer Comic Panel 2"
         style="width:100%; border-radius:15px; margin-bottom:15px;">

    <p>
        Heavy rain damages the crops,
        but {{ character }} does not give up.
    </p>

    <div class="dialogue">
        💬 "{{ character }}: I will not give up!"
    </div>

</div>
            

</div>
                <p>
                    Heavy rain damages the crops,
                    but {{ character }} does not give up.
                </p>

                <div class="dialogue">
                    💬 "{{ character }}:
                    I will not give up!"
                </div>

            </div>


            <div class="panel">

                <div class="panel">

    <h2>🤝 Panel 3</h2>

    <img src="{{ url_for('static', filename='panel3.png') }}"
         alt="Farmer Comic Panel 3"
         style="width:100%; border-radius:15px; margin-bottom:15px;">

    <p>
        {{ character }} learns new farming
        methods and works together with
        other farmers.
    </p>

    <div class="dialogue">
        💬 "Together, we can solve this problem."
    </div>

</div>


            <div class="panel">

                <div class="panel">

    <h2>🌾 Panel 4</h2>

    <img src="{{ url_for('static', filename='panel4.png') }}"
         alt="Farmer Comic Panel 4"
         style="width:100%; border-radius:15px; margin-bottom:15px;">

    <p>
        The crops grow again.
        {{ character }} feels happy and proud.
    </p>

    <div class="dialogue">
        💬 "{{ character }}:
        Hard work, patience and teamwork bring success."
    </div>

</div>
                

        </div>


        <div class="story">

            <h2>📚 Full Story</h2>

            <p>
                {{ story }}
            </p>

        </div>


        <button
            class="download-btn"
            onclick="window.print()">
            📥 Download Comic
        </button>

    </div>

    {% endif %}

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    title = ""
    character = ""
    story = ""

    if request.method == "POST":

        title = request.form["title"]

        character = request.form["character"]

        story = request.form["story"]

    return render_template_string(
        HTML,
        title=title,
        character=character,
        story=story
    )


if __name__ == "__main__":
    app.run(debug=True)