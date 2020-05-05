from flask import Flask, render_template, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb+srv://mustapha:mustapha123456@mycluster-dyvng.mongodb.net/BBC?retryWrites=true&w=majority"
app.config['MONGO_DBNAME'] = "BBC"

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all_data')
def get_data():
    articles = mongo.db.bbc_articles
    res = articles.find()
    
    data = ''
    for r in res:
        data += 'Headline:    ' + str(r['headline']).strip('[]"') + '<br>' \
               'Summary:    ' + str(r['summary']).strip('[]"') + '<br>' \
               'URL:  <a href ='+str(r['article_url']).strip('[]"')+'>click here</a> <br><br>'   
    return data


@app.route('/search_keyword', methods=['POST'])
def get_keyword():
    articles = mongo.db.bbc_articles
    res = articles.find()

    data = ''
    key = request.form.get('keyword')
    for r in res:
        if (str(r['headline']).find(key)>=0) or (str(r['summary']).find(key) >=0):
            data += 'Headline:    ' + str(r['headline']).strip('[]"') + '<br>' \
                   'Summary:    ' + str(r['summary']).strip('[]"') + '<br>' \
                   'URL:  <a href ='+str(r['article_url']).strip('[]"')+'>click here</a> <br><br>'
    if not data:
        data = '<h1>Keyword Not Found</h1>'
    return data
            

if __name__ == '__main__':
    app.run(debug=True)
