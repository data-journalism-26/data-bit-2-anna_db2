import plotly.express as px
import pandas as pd

df = pd.read_csv("data/wta_final.csv")

df['earnings_millions'] = df['earnings'] / 1_000_000

df_full = df.copy()
df_no_sabalenka = df[df['name'] != 'Aryna Sabalenka']

fig1 = px.scatter(
    df_full,
    x="earnings_millions",
    y="instagram",
    text="name",
    size="wiki_views",
    color="ranking",
    color_continuous_scale="RdYlGn_r",
    hover_data=["earnings", "wiki_views"],
    title="WTA Top 20: Career Earnings vs Instagram Followers",
    labels={
        "earnings_millions": "Career Prize Money (Millions USD)",
        "instagram": "Instagram Followers",
        "wiki_views": "Wikipedia Views",
        "ranking": "WTA Ranking"
    }
)

fig1.update_traces(textposition='top center', textfont_size=10)
fig1.update_layout(
    width=1000,
    height=700,
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray')
)

fig1.write_html("output/scatter.html")

fig2 = px.scatter(
    df_no_sabalenka,
    x="wiki_views",
    y="instagram",
    text="name",
    size="earnings",
    size_max=40,
    hover_data=["ranking", "earnings_millions"],
    title="WTA Top 20: Wikipedia Views vs Instagram Followers (ex Sabalenka)",
    labels={
        "wiki_views": "Wikipedia Page Views",
        "instagram": "Instagram Followers"
    }
)

fig2.update_traces(
    textposition='top center',
    textfont_size=10,
    marker=dict(color='#1f77b4', line=dict(width=0)),
    hovertemplate='<b>%{text}</b><br>Wiki: %{x:,.0f}<br>IG: %{y:,.0f}<br>Earnings: $%{marker.size:,.0f}M<extra></extra>'
)

fig2.update_layout(
    width=1000,
    height=700,
    xaxis=dict(
        showline=True,
        linecolor='black',
        linewidth=1,
        gridcolor='lightgray',
        showgrid=True,
        gridwidth=0.5
    ),
    yaxis=dict(
        showline=True,
        linecolor='black',
        linewidth=1,
        gridcolor='lightgray',
        showgrid=True,
        gridwidth=0.5
    ),
    plot_bgcolor='white'
)

fig2.add_annotation(
    x=0.98,
    y=0.02,
    xref="paper",
    yref="paper",
    text="Bubble size = Career earnings (USD)",
    showarrow=False,
    font=dict(size=11, color='gray'),
    bgcolor='rgba(255,255,255,0.8)'
)

fig2.write_html("output/wiki_vs_instagram.html")