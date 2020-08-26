import dash
import dash_bootstrap_components as dbc
# from flask_sqlalchemy import SQLAlchemy


# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.PULSE, "https://fonts.googleapis.com/css2?family=Alata&display=swap"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
#
# app.server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:/data_files/report.db"
# db = SQLAlchemy(app.server)

# app.server.config[]
app.config.suppress_callback_exceptions = True