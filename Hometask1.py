from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def internet_mag():
    context = {
        'title': 'Интернет Магазин',

    }
    return render_template('site.html', context=context)

@app.route('/jacket')
def jacket_s():
    context = {
        'title': 'Куртки',
        'p1': 'Здесь вы можете выбрать и  купить куртки'
    }
    return render_template('index.html', context=context)

@app.route('/shoes')
def Shoes_s():
    context = {
        'title': 'Обувь',
        'p1': 'Тут вы можете выбрать и приобрести ботинки'
    }
    return render_template('index.html', context=context)

@app.route('/trousers')
def Trousers_s():
    context = {
        'title': 'Штаны',
        'p1': 'Здесь вы можете выбрать и купить штаны'
    }
    return render_template('index.html', context=context)




if __name__ == "__main__":
    app.run(debug=True, port=5001)
