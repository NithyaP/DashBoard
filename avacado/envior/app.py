
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("avocado.csv")
print(data)
data = data.query("data_class == 'Iris-setosa'")


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="flower Analytics",),
        html.P(
            children="Analyze the behavior of flower styles"
            " and the number of flower sold in the US"
            " between 2015 and 2018",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "y": data["sepal_length_cm"],
                        "x": data["data_class"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Types of flower"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "y": data["sepal_width_cm"],
                        "x": data["data_class"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)
if __name__ == "__main__":
    app.run_server(debug=True)