import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify
import dash_daq as daq
import dash_ag_grid as dag
from dash import html
from data_preparation import *


affix = dmc.Affix(
    DashIconify(icon="twemoji:world-map", width=40),
    position={"top": 10, "right": 10},
    style={"position": "relative"}
)

timeline = dmc.Timeline(
    active=1,
    bulletSize=10,
    lineWidth=1,
    color="red",
    align="left",
    className="mt-4 timeline",
    children=[
        dmc.TimelineItem(
            title=html.P(id="date-events2"),
            children=[
                html.P(id="notes2"),
            ],
        ),
        
        dmc.TimelineItem(
            title=html.P(id="date-events"),
            children=[
                html.P(id="notes"),
            ],
        ),
        
        dmc.TimelineItem(
            title=html.P(id="date-events3"),
            children=[
                html.P(id="notes3"),
            ],
        ),
        
    ],
)


defaultColDef = {
    "resizable": True,
    "wrapHeaderText": True,
    "autoHeaderHeight": True,
}


columnDefs = [
    {
        "headerName": "Countries Europe",
        "stickyLabel": True,
        "children": [
            {"field": "country", "pinned": True, },
        ],
    },
    {
        "headerName": "Total events and fatalities",
        "children": [
            {"field": "events"},
            {"field": "fatalities"},
        ],
    },

    {
        "headerName": "Total events by type",
        "stickyLabel": True,
        "children": [
            {"field": col} for col in list(df["event_type"].unique())
        ],
    },

    {
        "headerName": "Total event by Disorder Type",
        "stickyLabel": True,
        "children": [
            {"field": col} for col in list(df["disorder_type"].unique())
        ],
    },

    {
        "headerName": "City with most events",
        "stickyLabel": True,
        "children": [
            {"field": col} for col in ["location", "Events"]
        ],
    },
]

grid = dag.AgGrid(
    id="get-started-example-basic",
    rowData=data.to_dict("records"),
    columnDefs=columnDefs,
    className="ag-theme-alpine-dark",
    style={'height': '500px'},
    defaultColDef=defaultColDef
)


active_tab_style = {
    "font-family": "serif",
    "border-bottom": "none"
}

tab_style = {"marginLeft": "auto"}


theme = {
    'dark': True,
    'detail': 'lightgray',
}

def daq_comp(classname):
    return html.Div(className="div-daq", children=[
        daq.DarkThemeProvider(
            theme=theme,
            children=[
                html.Div(className="daq", children=[
                    daq.Slider(
                        id=classname,
                        min=1,
                        max=40,
                        value=10,
                        targets={"10": {"label": "Ideal"}},
                        color="gray",
                        className='dark-theme-control'
                    )
                ])
            ]
        )
    ])
    
    

