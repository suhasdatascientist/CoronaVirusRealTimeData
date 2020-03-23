from flask import *
import pandas as pd
import numpy as np
app = Flask(__name__)

@app.route("/corona_status")
def show_tables():
    data = pd.read_csv('dummy_data1.csv',index_col=0)
    data = data.replace(np.nan,"No Cases")
    data.set_index(['Countries'])
    data.index.name=None
    females = data.loc[:]
    males = data.loc[data.Countries == 'India']
    return render_template('view.html',tables=[males.to_html(classes='male'),females.to_html(classes='female')],
    titles = ['na','Indian Cases Only', 'WorldWide Cases'])

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)