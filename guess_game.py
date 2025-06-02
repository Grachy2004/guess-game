from flask import Flask, render_template, request
from supabase_config import supabase
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name     = request.form["name"]
        guess    = int(request.form["guess"])
        secret   = int(request.form["secret"])
        attempts = int(request.form["attempts"]) + 1

        # ¿Adivinó?
        if guess == secret:
            supabase.table("players").insert({"name": name,
                                              "score": attempts}).execute()
            return render_template("winner.html", name=name, attempts=attempts)
        else:
            msg = "🔻 Muy bajo" if guess < secret else "🔺 Muy alto"
            return render_template("index.html",
                                   name=name, message=msg,
                                   secret=secret, attempts=attempts)

    # Primera visita => generar número y contadores
    return render_template("index.html",
                           name="", message="",
                           secret=random.randint(1, 20),
                           attempts=0)

@app.route("/leaderboard")
def leaderboard():
    res = (supabase.table("players")
                    .select("*")
                    .order("score")
                    .limit(10)
                    .execute())
    return render_template("leaderboard.html", players=res.data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

