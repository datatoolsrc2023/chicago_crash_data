import common
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# get data from database
prim_query = 'select * from primary_contributory_cause_by_crash_year'
make_query = 'select * from make_model_year_concat'
cnx = common.db_cnx(return_str=True)

prim_df = pd.read_sql(prim_query, cnx)
make_df = pd.read_sql(make_query, cnx)

# render on Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='hello world'),
    dcc.Graph(figure=px.bar(prim_df, x="year", y="count",
                            color="primary_contributory_cause",
                            title="Primary Contributory Cause by Year")),
    dcc.Graph(figure=px.bar(make_df, x="year", y="count",
                            color="make_model_year"))
])

if __name__ == '__main__':
    app.run_server(debug=True)
