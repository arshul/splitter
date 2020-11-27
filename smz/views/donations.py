from flask import jsonify, request, render_template
from app import app
from smz.api.donations import split
from smz.constants.enum import SPLIT


@app.route("/get-donations", methods=['GET'])
def get_donations():
    try:
        args = request.args.to_dict()
        resp = split(float(args['amount']), SPLIT[args['split']])
        return render_template(
            "donations.html",
            donations=resp,
            split=SPLIT[args['split']]
        )
    except Exception as error:
        import traceback
        print(traceback.print_exc())
        return jsonify({"error": str(error)}), 400


@app.route("/", methods=['GET'])
def home():
    try:
        return render_template("index.html", base_url=app.config["BASE_URL"])
    except Exception as e:
        return str(e)
