from flask import Flask
from flask import Blueprint, render_template, request, flash, jsonify, Flask
import csv

app = Flask(__name__)

# this is where I got the dataset from
#https://www.kaggle.com/datasets/a9ece97f83e99ab5955ddf7ab9c3f3a9047ba5cdbb08189b11e7243630d969d8

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    genre = request.form.get('genre')
    type_ = request.form.get('type')
    score = request.form.get('score')
    episodes = request.form.get('episodes')
    studio = request.form.get('studio')

    results = []

    with open('static/Anime.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (
                    (not genre or genre.lower() in row['Genres'].lower()) and
                    (not type_ or type_.lower() == row['Type'].lower()) and
                    (not score or float(score) <= float(row['Score'])) and
                    (not episodes or int(episodes) == int(row['Episodes'])) and
                    (not studio or studio.lower() == row['Studio'].lower())
            ):
                results.append(row)
                if len(results) >= 50:
                    break
    return jsonify(results)

@app.route('/clear', methods=['POST'])
def clear():
    # Redirect back to search.html without processing any data
    return render_template('search.html')


if __name__ == '__main__':
    app.run()
