import common
import pandas as pd
import plotly.express as px


def main():
    query = 'select * from primary_contributory_cause_by_year'

    cnx = common.db_cnx(return_str=True)
    df = pd.read_sql(query, cnx)

    fig = px.bar(df, x="Year", y="Count", color="Primary contributory crash cause",
                 title="Primary Contributory Cause by Year")
    fig.show()


if __name__ == '__main__':
    main()
