import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

# ProcureIQ Brand Palette
NAVY = "#1F4E78"
TEAL = "#2A9D8F"
ORANGE = "#F4A261"
CORAL = "#E76F51"
LIGHT_BG = "#F7F9FC"
DARK_TEXT = "#243447"
MUTED_TEXT = "#667085"
BORDER = "#DDE3EA"

px.defaults.color_discrete_sequence = [NAVY, TEAL, ORANGE, CORAL]


st.set_page_config(
    page_title="ProcureIQ",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
:root {
    --procureiq-navy: #1F4E78;
    --procureiq-teal: #2A9D8F;
    --procureiq-orange: #F4A261;
    --procureiq-coral: #E76F51;
    --procureiq-bg: #F7F9FC;
    --procureiq-text: #243447;
    --procureiq-muted: #667085;
    --procureiq-border: #DDE3EA;
}

html, body, .stApp {
    font-family: Arial, Helvetica, sans-serif !important;
    color: var(--procureiq-text);
}
.stApp { background: #FFFFFF; }

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

h1, h2, h3, h4, h5, h6 {
    font-family: Arial, Helvetica, sans-serif !important;
    color: var(--procureiq-navy) !important;
}

p, label, .stCaption {
    font-family: Arial, Helvetica, sans-serif !important;
}

[data-testid="stSidebar"] {
    background: var(--procureiq-bg);
    border-right: 1px solid var(--procureiq-border);
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: var(--procureiq-navy) !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    font-family: Arial, Helvetica, sans-serif !important;
}

.hero {
    padding: 22px 26px;
    border: 1px solid var(--procureiq-border);
    border-left: 6px solid var(--procureiq-navy);
    border-radius: 18px;
    background: linear-gradient(135deg, #FFFFFF 0%, #F7F9FC 100%);
    margin-bottom: 18px;
}

.hero h1 {
    margin: 0;
    font-size: 2rem;
    color: var(--procureiq-navy) !important;
}

.hero p {
    margin: 6px 0 0;
    color: var(--procureiq-muted);
}

.section-note {
    color: var(--procureiq-muted);
    margin-top: -8px;
    margin-bottom: 12px;
}

[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid var(--procureiq-border);
    border-top: 4px solid var(--procureiq-teal);
    border-radius: 14px;
    padding: 14px 16px;
    box-shadow: 0 2px 8px rgba(31, 78, 120, 0.05);
}

[data-testid="stMetricLabel"] {
    color: var(--procureiq-muted) !important;
}

[data-testid="stMetricValue"] {
    color: var(--procureiq-navy) !important;
}

[data-testid="stDownloadButton"] button {
    background: var(--procureiq-navy) !important;
    color: #FFFFFF !important;
    border: 1px solid var(--procureiq-navy) !important;
    border-radius: 9px !important;
}

[data-testid="stDownloadButton"] button:hover {
    background: var(--procureiq-teal) !important;
    border-color: var(--procureiq-teal) !important;
    color: #FFFFFF !important;
}

[data-testid="stDataFrame"] {
    border: 1px solid var(--procureiq-border);
    border-radius: 12px;
    overflow: hidden;
}

hr {
    border-color: var(--procureiq-border) !important;
}

[data-testid="stNumberInput"] > label {
    min-height: 58px !important;
    display: flex !important;
    align-items: flex-start !important;
    margin-bottom: 6px !important;
}

[data-testid="stNumberInput"] > label p {
    margin: 0 !important;
    line-height: 1.35 !important;
}

.js-plotly-plot .plotly .modebar-container {
    top: auto !important;
    bottom: 4px !important;
    right: 8px !important;
}

.js-plotly-plot .plotly .modebar {
    top: auto !important;
    bottom: 0 !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_demo():
    return pd.read_csv(Path(__file__).parent / "sample_procurement_data.csv")

PROCUREMENT_REQUIRED_COLUMNS = [
    "PO_ID",
    "Supplier",
    "Category",
    "Unit_Cost",
    "MOQ",
    "Lead_Time_Days",
    "On_Time_Delivery_Pct",
    "Quality_Score",
    "Risk_Score",
    "Annual_Quantity",
    "Price_Variance_Pct",
    "Late_Orders"
]

def procurement_template_csv():
    template = pd.DataFrame([
        {
            "PO_ID": "PO-1001",
            "Supplier": "Supplier A",
            "Category": "Semiconductors",
            "Unit_Cost": 38.50,
            "MOQ": 500,
            "Lead_Time_Days": 21,
            "On_Time_Delivery_Pct": 94.0,
            "Quality_Score": 97.0,
            "Risk_Score": 25.0,
            "Annual_Quantity": 3000,
            "Price_Variance_Pct": 0.03,
            "Late_Orders": 1
        },
        {
            "PO_ID": "PO-1002",
            "Supplier": "Supplier B",
            "Category": "Mechanical",
            "Unit_Cost": 18.20,
            "MOQ": 200,
            "Lead_Time_Days": 14,
            "On_Time_Delivery_Pct": 91.0,
            "Quality_Score": 95.0,
            "Risk_Score": 32.0,
            "Annual_Quantity": 5000,
            "Price_Variance_Pct": -0.02,
            "Late_Orders": 2
        }
    ])
    return template.to_csv(index=False).encode("utf-8-sig")

def demand_template_csv():
    template = pd.DataFrame({
        "Date": [
            "2026-01-01",
            "2026-02-01",
            "2026-03-01",
            "2026-04-01",
            "2026-05-01",
            "2026-06-01"
        ],
        "Demand": [950, 1010, 980, 1080, 1120, 1090]
    })
    return template.to_csv(index=False).encode("utf-8-sig")

def normalize(series, reverse=False):
    s = series.astype(float)
    if s.max() == s.min():
        out = pd.Series(np.ones(len(s)), index=s.index)
    else:
        out = (s - s.min()) / (s.max() - s.min())
    return 1 - out if reverse else out

def supplier_summary(df):
    return df.groupby("Supplier", as_index=False).agg(
        Category=("Category","first"),
        Avg_Unit_Cost=("Unit_Cost","mean"),
        Avg_MOQ=("MOQ","mean"),
        Avg_Lead_Time=("Lead_Time_Days","mean"),
        OTD=("On_Time_Delivery_Pct","mean"),
        Quality=("Quality_Score","mean"),
        Risk=("Risk_Score","mean"),
        Annual_Spend=("Annual_Spend","sum"),
        Late_Orders=("Late_Orders","sum"),
        Price_Variance=("Price_Variance_Pct","mean")
    ).round(2)

def add_overall_score(summary):
    s = summary.copy()
    s["Cost_S"] = normalize(s["Avg_Unit_Cost"], reverse=True)
    s["Lead_S"] = normalize(s["Avg_Lead_Time"], reverse=True)
    s["OTD_S"] = normalize(s["OTD"])
    s["Quality_S"] = normalize(s["Quality"])
    s["Risk_S"] = normalize(s["Risk"], reverse=True)

    s["Overall_Score"] = (
        .30*s["Cost_S"] +
        .20*s["Lead_S"] +
        .20*s["OTD_S"] +
        .15*s["Quality_S"] +
        .15*s["Risk_S"]
    ) * 100

    s["Overall_Score"] = s["Overall_Score"].round(1)

    def grade(v):
        if v >= 85:
            return "A"
        if v >= 70:
            return "B"
        if v >= 55:
            return "C"
        return "D"

    s["Grade"] = s["Overall_Score"].apply(grade)
    return s

def plot_bar(data, x, y, title, y_label=""):
    fig = px.bar(data, x=x, y=y, title=title, color_discrete_sequence=[NAVY])
    fig.update_layout(
        xaxis_title="",
        yaxis_title=y_label,
        height=430,
        margin=dict(l=20, r=20, t=85, b=125),
        font=dict(family="Arial", size=14, color=DARK_TEXT),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        title=dict(
            text=title,
            x=0,
            xanchor="left",
            y=0.98,
            yanchor="top",
            font=dict(family="Arial", size=20)
        )
    )
    fig.update_xaxes(
        tickangle=0,
        automargin=True,
        tickfont=dict(family="Arial", size=12)
    )
    fig.update_yaxes(
        automargin=True,
        tickfont=dict(family="Arial", size=12)
    )
    st.plotly_chart(
        fig,
        width="stretch",
        config={
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["select2d", "lasso2d"]
        }
    )

def plot_horizontal_bar(data, label_col, value_col, title, x_label="", bar_color=TEAL):
    chart_data = data.sort_values(value_col, ascending=True)
    fig = px.bar(
        chart_data,
        x=value_col,
        y=label_col,
        orientation="h",
        title=title
    )
    fig.update_layout(
        xaxis_title=x_label,
        yaxis_title="",
        height=max(430, 58 * len(chart_data)),
        margin=dict(l=20, r=25, t=85, b=80),
        font=dict(family="Arial", size=14, color=DARK_TEXT),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        title=dict(
            text=title,
            x=0,
            xanchor="left",
            y=0.98,
            yanchor="top",
            font=dict(family="Arial", size=20)
        )
    )
    fig.update_yaxes(
        automargin=True,
        tickfont=dict(family="Arial", size=13)
    )
    fig.update_xaxes(
        automargin=True,
        tickfont=dict(family="Arial", size=12)
    )
    st.plotly_chart(
        fig,
        width="stretch",
        config={
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["select2d", "lasso2d"]
        }
    )

st.sidebar.title("ProcureIQ")
st.sidebar.caption(
    "Procurement & Supplier Decision Intelligence\n"
    "采购与供应商决策智能平台"
)

st.sidebar.download_button(
    "Download Procurement Template / 下载采购数据模板",
    data=procurement_template_csv(),
    file_name="ProcureIQ_Procurement_Template.csv",
    mime="text/csv"
)

uploaded = st.sidebar.file_uploader(
    "Upload procurement CSV / 上传采购 CSV",
    type=["csv"]
)

if uploaded is not None:
    uploaded_df = pd.read_csv(uploaded)

    missing_cols = [
        col for col in PROCUREMENT_REQUIRED_COLUMNS
        if col not in uploaded_df.columns
    ]

    if missing_cols:
        st.sidebar.error(
            "Invalid procurement file / 采购文件格式不正确\n\n"
            "Missing columns / 缺少字段：\n"
            + ", ".join(missing_cols)
        )
        df = load_demo()
        st.sidebar.warning(
            "Demo data is being used until a valid file is uploaded. / "
            "在上传正确格式文件前，系统继续使用演示数据。"
        )
    else:
        df = uploaded_df.copy()

        # Annual Spend is calculated automatically so the user does not need to provide it.
        df["Annual_Spend"] = (
            pd.to_numeric(df["Unit_Cost"], errors="coerce") *
            pd.to_numeric(df["Annual_Quantity"], errors="coerce")
        ).round(2)

        st.sidebar.success(
            "Using uploaded procurement data / 正在使用上传的采购数据"
        )
else:
    df = load_demo()
    st.sidebar.info(
        "Using demo procurement data / 正在使用演示数据"
    )

st.sidebar.caption(
    "Template fields can contain any supplier names, categories and values. "
    "Keep the column names unchanged. / "
    "供应商名称、类别和数值都可以自行替换，但请保留模板中的列名。"
)

page = st.sidebar.radio(
    "Navigation / 导航",
    [
        "Overview / 总览",
        "Supplier Scorecard / 供应商评分",
        "Supplier Comparison / 供应商比较",
        "Spend Analysis / 采购支出分析",
        "Risk Monitor / 风险监控",
        "Inventory Planning / 库存规划",
        "Scenario Analysis / 情景分析",
        "Demand Forecasting / 需求预测",
        "Decision Assistant / 决策助手",
        "Data / 数据"
    ]
)

summary = supplier_summary(df)
scored = add_overall_score(summary)

if page == "Overview / 总览":
    st.markdown("""
    <div class="hero">
      <h1>ProcureIQ</h1>
      <p>Procurement & Supplier Decision Intelligence Platform / 采购与供应商决策智能平台</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric(
        "Annual Spend / 年度支出",
        f"${df['Annual_Spend'].sum():,.0f}"
    )
    c2.metric(
        "Avg Lead Time / 平均交期",
        f"{df['Lead_Time_Days'].mean():.1f} days"
    )
    c3.metric(
        "On-Time Delivery / 准时交付率",
        f"{df['On_Time_Delivery_Pct'].mean():.1f}%"
    )
    c4.metric(
        "Average Risk / 平均风险",
        f"{df['Risk_Score'].mean():.1f}/100"
    )

    left, right = st.columns(2)

    with left:
        spend_df = summary[
            ["Supplier", "Annual_Spend"]
        ].sort_values("Annual_Spend", ascending=False)

        plot_horizontal_bar(
            spend_df,
            "Supplier",
            "Annual_Spend",
            "Spend by Supplier / 各供应商采购支出",
            "Annual Spend / 年度支出"
        )

    with right:
        score_df = scored[
            ["Supplier", "Overall_Score"]
        ].sort_values("Overall_Score", ascending=False)

        plot_horizontal_bar(
            score_df,
            "Supplier",
            "Overall_Score",
            "Supplier Score / 供应商综合评分",
            "Score / 评分"
        )

    st.subheader(
        "Supplier Performance Snapshot / 供应商绩效概览"
    )

    st.dataframe(
        scored[
            [
                "Supplier",
                "Category",
                "Avg_Unit_Cost",
                "Avg_Lead_Time",
                "OTD",
                "Quality",
                "Risk",
                "Overall_Score",
                "Grade"
            ]
        ].sort_values(
            "Overall_Score",
            ascending=False
        ),
        width="stretch",
        hide_index=True
    )

elif page == "Supplier Scorecard / 供应商评分":
    st.title("Supplier Scorecard / 供应商评分")
    st.caption(
        "Cost + Lead Time + Delivery + Quality + Risk / "
        "成本 + 交期 + 交付 + 质量 + 风险"
    )

    supplier = st.selectbox(
        "Choose supplier / 选择供应商",
        scored["Supplier"].tolist()
    )

    row = scored[
        scored["Supplier"] == supplier
    ].iloc[0]

    cols = st.columns(6)

    cols[0].metric(
        "Cost / 成本",
        f"${row['Avg_Unit_Cost']:.2f}"
    )
    cols[1].metric(
        "Lead Time / 交期",
        f"{row['Avg_Lead_Time']:.1f} d"
    )
    cols[2].metric(
        "OTD / 准时交付",
        f"{row['OTD']:.1f}%"
    )
    cols[3].metric(
        "Quality / 质量",
        f"{row['Quality']:.1f}"
    )
    cols[4].metric(
        "Risk / 风险",
        f"{row['Risk']:.1f}"
    )
    cols[5].metric(
        "Overall / 综合分",
        f"{row['Overall_Score']:.1f}"
    )

    st.subheader(
        f"{supplier} — Grade {row['Grade']} / 等级 {row['Grade']}"
    )

    metric_df = pd.DataFrame({
        "Metric": [
            "Cost / 成本",
            "Lead Time / 交期",
            "Delivery / 交付",
            "Quality / 质量",
            "Risk / 风险"
        ],
        "Score": [
            row["Cost_S"] * 100,
            row["Lead_S"] * 100,
            row["OTD_S"] * 100,
            row["Quality_S"] * 100,
            row["Risk_S"] * 100
        ]
    })

    plot_bar(
        metric_df,
        "Metric",
        "Score",
        "Supplier Scorecard / 供应商评分卡",
        "Score / 评分"
    )

    if row["Overall_Score"] >= 85:
        st.success(
            "Strong supplier candidate / "
            "综合表现优秀，可作为优先候选。"
        )
    elif row["Overall_Score"] >= 70:
        st.info(
            "Good supplier with manageable trade-offs / "
            "表现良好，但仍需权衡个别指标。"
        )
    elif row["Overall_Score"] >= 55:
        st.warning(
            "Further review recommended / "
            "建议进一步审查并制定改善措施。"
        )
    else:
        st.error(
            "High caution required / "
            "综合表现偏弱，采购决策需谨慎。"
        )

elif page == "Supplier Comparison / 供应商比较":
    st.title(
        "Supplier Comparison / 供应商比较"
    )

    selected = st.multiselect(
        "Select suppliers / 选择供应商",
        summary["Supplier"].tolist(),
        default=summary["Supplier"].tolist()[:4]
    )

    sub = summary[
        summary["Supplier"].isin(selected)
    ].copy()

    if len(sub) < 2:
        st.warning(
            "Select at least two suppliers. / "
            "请至少选择两个供应商。"
        )

    else:
        st.subheader(
            "Decision Weights / 决策权重"
        )

        c1, c2, c3, c4, c5 = st.columns(5)

        w_cost = c1.slider(
            "Cost / 成本", 0, 100, 30
        )
        w_lead = c2.slider(
            "Lead Time / 交期", 0, 100, 20
        )
        w_otd = c3.slider(
            "Delivery / 交付", 0, 100, 20
        )
        w_quality = c4.slider(
            "Quality / 质量", 0, 100, 15
        )
        w_risk = c5.slider(
            "Risk / 风险", 0, 100, 15
        )

        weights = np.array(
            [
                w_cost,
                w_lead,
                w_otd,
                w_quality,
                w_risk
            ],
            dtype=float
        )

        if weights.sum() == 0:
            weights = np.ones(5)

        weights = weights / weights.sum()

        sub["Cost_Score"] = normalize(
            sub["Avg_Unit_Cost"],
            reverse=True
        )
        sub["Lead_Score"] = normalize(
            sub["Avg_Lead_Time"],
            reverse=True
        )
        sub["Delivery_Score"] = normalize(
            sub["OTD"]
        )
        sub["Quality_Score_N"] = normalize(
            sub["Quality"]
        )
        sub["Risk_Score_N"] = normalize(
            sub["Risk"],
            reverse=True
        )

        matrix = sub[
            [
                "Cost_Score",
                "Lead_Score",
                "Delivery_Score",
                "Quality_Score_N",
                "Risk_Score_N"
            ]
        ].values

        sub["Weighted_Score"] = (
            matrix @ weights * 100
        ).round(1)

        ranked = sub.sort_values(
            "Weighted_Score",
            ascending=False
        )

        st.dataframe(
            ranked[
                [
                    "Supplier",
                    "Avg_Unit_Cost",
                    "Avg_Lead_Time",
                    "OTD",
                    "Quality",
                    "Risk",
                    "Weighted_Score"
                ]
            ],
            width="stretch",
            hide_index=True
        )

        comparison_chart = ranked[
            ["Supplier", "Weighted_Score"]
        ]

        plot_horizontal_bar(
            comparison_chart,
            "Supplier",
            "Weighted_Score",
            "Weighted Supplier Ranking / 加权供应商排名",
            "Weighted Score / 加权评分"
        )

        best = ranked.iloc[0]

        st.success(
            f"Recommended / 推荐："
            f"**{best['Supplier']}** — "
            f"Score / 评分 "
            f"**{best['Weighted_Score']}/100**"
        )

        export_comparison = ranked[
            [
                "Supplier",
                "Category",
                "Avg_Unit_Cost",
                "Avg_MOQ",
                "Avg_Lead_Time",
                "OTD",
                "Quality",
                "Risk",
                "Weighted_Score"
            ]
        ].copy()

        st.download_button(
            "Download Supplier Comparison / 下载供应商比较结果",
            data=export_comparison.to_csv(index=False).encode("utf-8-sig"),
            file_name="ProcureIQ_Supplier_Comparison.csv",
            mime="text/csv"
        )

elif page == "Spend Analysis / 采购支出分析":
    st.title("Spend Analysis / 采购支出分析")
    st.caption(
        "Review category spend, supplier concentration and price movement. / "
        "分析采购类别支出、供应商集中度与价格波动。"
    )

    category_df = (
        df.groupby("Category", as_index=False)["Annual_Spend"]
        .sum()
        .sort_values("Annual_Spend", ascending=False)
    )

    supplier_df = (
        df.groupby("Supplier", as_index=False)["Annual_Spend"]
        .sum()
        .sort_values("Annual_Spend", ascending=False)
    )

    total_spend = supplier_df["Annual_Spend"].sum()
    largest_supplier_share = (
        supplier_df.iloc[0]["Annual_Spend"] / total_spend * 100
        if total_spend else 0
    )

    top_supplier = supplier_df.iloc[0]["Supplier"]
    top_category = category_df.iloc[0]["Category"]

    price_df = (
        df.groupby("Supplier", as_index=False)["Price_Variance_Pct"]
        .mean()
        .sort_values("Price_Variance_Pct", ascending=False)
    )

    avg_abs_variance = (
        df["Price_Variance_Pct"].abs().mean() * 100
        if len(df) else 0
    )

    k1, k2, k3, k4 = st.columns(4)

    k1.metric(
        "Total Spend / 总采购支出",
        f"${total_spend:,.0f}"
    )

    k2.metric(
        "Largest Supplier Share / 最大供应商占比",
        f"{largest_supplier_share:.1f}%"
    )

    k3.metric(
        "Top Spend Category / 最大支出类别",
        str(top_category)
    )

    k4.metric(
        "Avg. Absolute Price Variance / 平均绝对价格波动",
        f"{avg_abs_variance:.1f}%"
    )

    st.divider()

    st.subheader("Spend by Category / 分类采购支出")

    category_fig = px.bar(
        category_df,
        x="Category",
        y="Annual_Spend",
        color_discrete_sequence=[NAVY]
    )

    category_fig.update_layout(
        xaxis_title="",
        yaxis_title="Annual Spend / 年度支出",
        height=400,
        margin=dict(l=30, r=20, t=25, b=95),
        font=dict(family="Arial", size=14)
    )

    category_fig.update_xaxes(
        tickangle=0,
        automargin=True
    )

    st.plotly_chart(
        category_fig,
        width="stretch",
        config={
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["select2d", "lasso2d"]
        }
    )

    st.subheader("Spend by Supplier / 供应商采购支出")

    supplier_fig = px.bar(
        supplier_df.sort_values("Annual_Spend", ascending=True),
        x="Annual_Spend",
        y="Supplier",
        orientation="h",
        color_discrete_sequence=[TEAL]
    )

    supplier_fig.update_layout(
        xaxis_title="Annual Spend / 年度支出",
        yaxis_title="",
        height=max(430, 54 * len(supplier_df)),
        margin=dict(l=25, r=30, t=25, b=80),
        font=dict(family="Arial", size=14)
    )

    supplier_fig.update_yaxes(
        automargin=True,
        tickfont=dict(family="Arial", size=13)
    )

    st.plotly_chart(
        supplier_fig,
        width="stretch",
        config={
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["select2d", "lasso2d"]
        }
    )

    st.info(
        f"Highest spend supplier / 采购支出最高供应商：**{top_supplier}** "
        f"({largest_supplier_share:.1f}% of total spend / 占总采购支出 {largest_supplier_share:.1f}%)"
    )

    st.subheader("Price Variance / 价格波动")

    price_fig = px.bar(
        price_df,
        x="Price_Variance_Pct",
        y="Supplier",
        orientation="h",
        color_discrete_sequence=[ORANGE]
    )

    price_fig.update_layout(
        xaxis_title="Price Variance / 价格波动",
        yaxis_title="",
        height=max(430, 54 * len(price_df)),
        margin=dict(l=25, r=30, t=25, b=80),
        font=dict(family="Arial", size=14)
    )

    price_fig.update_yaxes(
        automargin=True,
        tickfont=dict(family="Arial", size=13)
    )

    st.plotly_chart(
        price_fig,
        width="stretch",
        config={
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["select2d", "lasso2d"]
        }
    )

elif page == "Risk Monitor / 风险监控":
    st.title(
        "Supplier Risk Monitor / 供应商风险监控"
    )

    rt = summary.copy()

    rt["Operational_Risk_Index"] = (
        .35 * rt["Risk"] +
        .25 * (100 - rt["OTD"]) +
        .20 * (100 - rt["Quality"]) +
        .10 * np.clip(
            rt["Late_Orders"] * 3,
            0,
            100
        ) +
        .10 * np.clip(
            abs(rt["Price_Variance"]) * 500,
            0,
            100
        )
    ).round(1)

    def band(v):
        if v >= 45:
            return "High / 高"
        if v >= 25:
            return "Medium / 中"
        return "Low / 低"

    rt["Risk_Level / 风险等级"] = (
        rt["Operational_Risk_Index"]
        .apply(band)
    )

    rt = rt.sort_values(
        "Operational_Risk_Index",
        ascending=False
    )

    st.dataframe(
        rt[
            [
                "Supplier",
                "OTD",
                "Quality",
                "Late_Orders",
                "Price_Variance",
                "Operational_Risk_Index",
                "Risk_Level / 风险等级"
            ]
        ],
        width="stretch",
        hide_index=True
    )

    risk_chart = rt[
        ["Supplier", "Operational_Risk_Index"]
    ]

    plot_horizontal_bar(
        risk_chart,
        "Supplier",
        "Operational_Risk_Index",
        "Operational Risk Index / 运营风险指数",
        "Risk Index / 风险指数",
        bar_color=CORAL
    )

    high = rt[
        rt["Operational_Risk_Index"] >= 45
    ]

    if len(high):
        st.error(
            "High-risk suppliers / 高风险供应商："
            + ", ".join(
                high["Supplier"].tolist()
            )
        )
    else:
        st.success(
            "No high-risk suppliers detected. / "
            "当前未发现高风险供应商。"
        )


elif page == "Inventory Planning / 库存规划":
    st.title("Inventory Planning / 库存规划")
    st.caption(
        "Translate demand and supplier lead time into safety stock and reorder decisions. / "
        "将需求和供应商交期转化为安全库存与补货决策。"
    )

    supplier = st.selectbox(
        "Supplier / 供应商",
        summary["Supplier"].tolist(),
        key="inventory_supplier"
    )

    supplier_row = summary[
        summary["Supplier"] == supplier
    ].iloc[0]

    st.info(
        f"Selected supplier average lead time / 所选供应商平均交期："
        f"**{supplier_row['Avg_Lead_Time']:.1f} days / 天**"
    )

    c1, c2, c3, c4 = st.columns(4)

    avg_daily_demand = c1.number_input(
        "Average Daily Demand / 平均日需求",
        min_value=1.0,
        value=120.0,
        step=10.0
    )

    demand_std = c2.number_input(
        "Demand Std. Dev. / 日需求标准差",
        min_value=0.0,
        value=25.0,
        step=5.0
    )

    current_stock = c3.number_input(
        "Current Stock / 当前库存",
        min_value=0.0,
        value=2500.0,
        step=100.0
    )

    review_period = c4.number_input(
        "Review Period / 检查周期（天）",
        min_value=1,
        value=7,
        step=1
    )

    service_level = st.select_slider(
        "Target Service Level / 目标服务水平",
        options=[90, 95, 97.5, 99],
        value=95
    )

    z_map = {
        90: 1.28,
        95: 1.645,
        97.5: 1.96,
        99: 2.33
    }

    z = z_map[service_level]
    lead_time = float(supplier_row["Avg_Lead_Time"])

    safety_stock = z * demand_std * np.sqrt(lead_time)
    reorder_point = avg_daily_demand * lead_time + safety_stock
    days_of_cover = current_stock / avg_daily_demand if avg_daily_demand else 0
    target_stock = avg_daily_demand * (lead_time + review_period) + safety_stock
    recommended_order = max(0, target_stock - current_stock)

    m1, m2, m3, m4 = st.columns(4)

    m1.metric(
        "Safety Stock / 安全库存",
        f"{safety_stock:,.0f}"
    )

    m2.metric(
        "Reorder Point / 再订货点",
        f"{reorder_point:,.0f}"
    )

    m3.metric(
        "Days of Cover / 库存覆盖天数",
        f"{days_of_cover:.1f} days"
    )

    m4.metric(
        "Suggested Order / 建议补货量",
        f"{recommended_order:,.0f}"
    )

    st.subheader("Inventory Status / 库存状态")

    if current_stock <= safety_stock:
        st.error(
            "Critical inventory risk / 库存风险较高："
            "current stock is at or below safety stock. / 当前库存已接近或低于安全库存。"
        )
    elif current_stock <= reorder_point:
        st.warning(
            "Reorder recommended / 建议补货："
            "current stock is below the reorder point. / 当前库存低于再订货点。"
        )
    else:
        st.success(
            "Inventory is currently above the reorder point. / "
            "当前库存高于再订货点。"
        )

    st.subheader("Planning Logic / 规划逻辑")

    planning_df = pd.DataFrame({
        "Metric / 指标": [
            "Average Daily Demand / 平均日需求",
            "Supplier Lead Time / 供应商交期",
            "Demand Std. Dev. / 需求标准差",
            "Service Level / 服务水平",
            "Safety Stock / 安全库存",
            "Reorder Point / 再订货点",
            "Target Stock / 目标库存",
            "Current Stock / 当前库存",
            "Suggested Order / 建议补货量"
        ],
        "Value / 数值": [
            round(avg_daily_demand, 2),
            round(lead_time, 2),
            round(demand_std, 2),
            f"{service_level}%",
            round(safety_stock, 2),
            round(reorder_point, 2),
            round(target_stock, 2),
            round(current_stock, 2),
            round(recommended_order, 2)
        ]
    })

    st.dataframe(
        planning_df,
        width="stretch",
        hide_index=True
    )

    st.download_button(
        "Download Inventory Plan / 下载库存规划结果",
        data=planning_df.to_csv(index=False).encode("utf-8-sig"),
        file_name="ProcureIQ_Inventory_Plan.csv",
        mime="text/csv"
    )

    st.caption(
        "Formula / 公式：Safety Stock = Z × Demand Std. Dev. × √Lead Time; "
        "Reorder Point = Average Daily Demand × Lead Time + Safety Stock."
    )


elif page == "Scenario Analysis / 情景分析":
    st.title("Scenario Analysis / 情景分析")
    st.caption(
        "Test how changes in demand, lead time and service level affect inventory decisions. / "
        "测试需求、交期和服务水平变化对库存决策的影响。"
    )

    supplier = st.selectbox(
        "Supplier / 供应商",
        summary["Supplier"].tolist(),
        key="scenario_supplier"
    )

    supplier_row = summary[
        summary["Supplier"] == supplier
    ].iloc[0]

    base_lead_time = float(supplier_row["Avg_Lead_Time"])

    st.subheader("Baseline Inputs / 基准参数")

    b1, b2, b3, b4 = st.columns(4)

    base_daily_demand = b1.number_input(
        "Average Daily Demand / 平均日需求",
        min_value=1.0,
        value=120.0,
        step=10.0,
        key="scenario_base_demand"
    )

    base_demand_std = b2.number_input(
        "Demand Std. Dev. / 日需求标准差",
        min_value=0.0,
        value=25.0,
        step=5.0,
        key="scenario_base_std"
    )

    base_current_stock = b3.number_input(
        "Current Stock / 当前库存",
        min_value=0.0,
        value=2500.0,
        step=100.0,
        key="scenario_base_stock"
    )

    base_review_period = b4.number_input(
        "Review Period / 检查周期（天）",
        min_value=1,
        value=7,
        step=1,
        key="scenario_base_review"
    )

    base_service_level = st.select_slider(
        "Baseline Service Level / 基准服务水平",
        options=[90, 95, 97.5, 99],
        value=95,
        key="scenario_base_service"
    )

    st.subheader("Scenario Changes / 情景变化")

    s1, s2, s3 = st.columns(3)

    demand_change_pct = s1.slider(
        "Demand Change / 需求变化",
        min_value=-30,
        max_value=50,
        value=15,
        step=5,
        format="%d%%"
    )

    lead_time_change_pct = s2.slider(
        "Lead Time Change / 交期变化",
        min_value=-30,
        max_value=50,
        value=20,
        step=5,
        format="%d%%"
    )

    scenario_service_level = s3.selectbox(
        "Scenario Service Level / 情景服务水平",
        options=[90, 95, 97.5, 99],
        index=3
    )

    z_map = {
        90: 1.28,
        95: 1.645,
        97.5: 1.96,
        99: 2.33
    }

    base_z = z_map[base_service_level]
    scenario_z = z_map[scenario_service_level]

    scenario_daily_demand = base_daily_demand * (1 + demand_change_pct / 100)
    scenario_lead_time = base_lead_time * (1 + lead_time_change_pct / 100)

    base_safety_stock = (
        base_z * base_demand_std * np.sqrt(base_lead_time)
    )
    base_reorder_point = (
        base_daily_demand * base_lead_time + base_safety_stock
    )
    base_target_stock = (
        base_daily_demand * (base_lead_time + base_review_period)
        + base_safety_stock
    )
    base_order = max(
        0,
        base_target_stock - base_current_stock
    )

    scenario_safety_stock = (
        scenario_z * base_demand_std * np.sqrt(scenario_lead_time)
    )
    scenario_reorder_point = (
        scenario_daily_demand * scenario_lead_time
        + scenario_safety_stock
    )
    scenario_target_stock = (
        scenario_daily_demand * (
            scenario_lead_time + base_review_period
        )
        + scenario_safety_stock
    )
    scenario_order = max(
        0,
        scenario_target_stock - base_current_stock
    )

    comparison = pd.DataFrame({
        "Metric / 指标": [
            "Daily Demand / 日需求",
            "Lead Time / 交期",
            "Service Level / 服务水平",
            "Safety Stock / 安全库存",
            "Reorder Point / 再订货点",
            "Target Stock / 目标库存",
            "Suggested Order / 建议补货量"
        ],
        "Baseline / 基准": [
            round(base_daily_demand, 2),
            round(base_lead_time, 2),
            f"{base_service_level}%",
            round(base_safety_stock, 2),
            round(base_reorder_point, 2),
            round(base_target_stock, 2),
            round(base_order, 2)
        ],
        "Scenario / 情景": [
            round(scenario_daily_demand, 2),
            round(scenario_lead_time, 2),
            f"{scenario_service_level}%",
            round(scenario_safety_stock, 2),
            round(scenario_reorder_point, 2),
            round(scenario_target_stock, 2),
            round(scenario_order, 2)
        ]
    })

    st.subheader("Baseline vs Scenario / 基准与情景对比")

    st.dataframe(
        comparison,
        width="stretch",
        hide_index=True
    )

    metric_chart = pd.DataFrame({
        "Metric": [
            "Safety Stock",
            "Reorder Point",
            "Target Stock",
            "Suggested Order"
        ],
        "Baseline": [
            base_safety_stock,
            base_reorder_point,
            base_target_stock,
            base_order
        ],
        "Scenario": [
            scenario_safety_stock,
            scenario_reorder_point,
            scenario_target_stock,
            scenario_order
        ]
    })

    chart_long = metric_chart.melt(
        id_vars="Metric",
        value_vars=["Baseline", "Scenario"],
        var_name="Case",
        value_name="Value"
    )

    fig = px.bar(
        chart_long,
        x="Metric",
        y="Value",
        color="Case",
        barmode="group",
        color_discrete_map={"Baseline": NAVY, "Scenario": TEAL}
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Units / 单位",
        height=430,
        margin=dict(l=25, r=25, t=45, b=90),
        font=dict(family="Arial", size=14, color=DARK_TEXT),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        legend_title_text=""
    )

    st.plotly_chart(
        fig,
        width="stretch",
        config={
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["select2d", "lasso2d"]
        }
    )

    order_change = scenario_order - base_order
    order_change_pct = (
        order_change / base_order * 100
        if base_order > 0
        else None
    )

    st.subheader("Scenario Interpretation / 情景解释")

    if order_change > 0:
        if order_change_pct is not None:
            st.warning(
                f"Suggested order increases by {order_change:,.0f} units "
                f"({order_change_pct:.1f}%). / "
                f"建议补货量增加 {order_change:,.0f} 单位 "
                f"（{order_change_pct:.1f}%）。"
            )
        else:
            st.warning(
                f"Suggested order increases to {scenario_order:,.0f} units. / "
                f"建议补货量上升至 {scenario_order:,.0f} 单位。"
            )
    elif order_change < 0:
        st.success(
            f"Suggested order decreases by {abs(order_change):,.0f} units. / "
            f"建议补货量减少 {abs(order_change):,.0f} 单位。"
        )
    else:
        st.info(
            "Suggested order remains unchanged. / 建议补货量保持不变。"
        )

    risk_notes = []

    if demand_change_pct > 0:
        risk_notes.append(
            "Higher demand increases inventory requirements / 需求上升会提高库存需求"
        )

    if lead_time_change_pct > 0:
        risk_notes.append(
            "Longer lead time raises both safety stock and reorder point / "
            "交期延长会提高安全库存与再订货点"
        )

    if scenario_service_level > base_service_level:
        risk_notes.append(
            "A higher service level improves protection against stockouts but increases inventory holding / "
            "更高服务水平可降低缺货风险，但会增加库存持有量"
        )

    if risk_notes:
        for note in risk_notes:
            st.write("• " + note)

    st.download_button(
        "Download Scenario Analysis / 下载情景分析结果",
        data=comparison.to_csv(index=False).encode("utf-8-sig"),
        file_name="ProcureIQ_Scenario_Analysis.csv",
        mime="text/csv"
    )


elif page == "Demand Forecasting / 需求预测":
    st.title("Demand Forecasting / 需求预测")
    st.caption(
        "Use historical demand to compare simple forecasting methods. / "
        "使用历史需求比较基础预测方法。"
    )

    st.download_button(
        "Download Demand Template / 下载需求历史模板",
        data=demand_template_csv(),
        file_name="ProcureIQ_Demand_History_Template.csv",
        mime="text/csv"
    )

    st.caption(
        "Required columns / 必填字段：Date, Demand。"
        "You may replace all dates and demand values, but keep these two column names unchanged. / "
        "日期和需求数值可以全部替换，但请保留 Date 和 Demand 两个列名。"
    )

    demand_file = st.file_uploader(
        "Upload demand history CSV / 上传历史需求 CSV",
        type=["csv"],
        key="demand_history_upload"
    )

    if demand_file is not None:
        demand_df = pd.read_csv(demand_file)

        if not {"Date", "Demand"}.issubset(demand_df.columns):
            st.error(
                "CSV must contain Date and Demand columns. / "
                "CSV 必须包含 Date 和 Demand 两列。"
            )
            st.stop()

        demand_df["Date"] = pd.to_datetime(demand_df["Date"])
        demand_df = demand_df.sort_values("Date").reset_index(drop=True)
        st.success("Using uploaded demand history / 正在使用上传的需求历史数据")

    else:
        np.random.seed(17)

        periods = pd.date_range(
            end=pd.Timestamp.today().normalize(),
            periods=18,
            freq="MS"
        )

        base = np.linspace(900, 1180, len(periods))
        seasonality = 90 * np.sin(np.arange(len(periods)) * 2 * np.pi / 6)
        noise = np.random.normal(0, 45, len(periods))

        demand_df = pd.DataFrame({
            "Date": periods,
            "Demand": np.maximum(
                200,
                base + seasonality + noise
            ).round(0)
        })

        st.info(
            "Using synthetic demo demand data / 正在使用模拟需求数据"
        )

    st.subheader("Historical Demand / 历史需求")

    history_fig = px.line(
        demand_df,
        x="Date",
        y="Demand",
        markers=True,
        color_discrete_sequence=[NAVY]
    )

    history_fig.update_layout(
        xaxis_title="Date / 日期",
        yaxis_title="Demand / 需求",
        height=400,
        margin=dict(l=20, r=20, t=40, b=70),
        font=dict(family="Arial", size=14)
    )

    st.plotly_chart(
        history_fig,
        width="stretch",
        config={
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["select2d", "lasso2d"]
        }
    )

    col1, col2 = st.columns(2)

    ma_window = col1.slider(
        "Moving Average Window / 移动平均期数",
        min_value=2,
        max_value=6,
        value=3
    )

    alpha = col2.slider(
        "Exponential Smoothing Alpha / 指数平滑 α",
        min_value=0.1,
        max_value=0.9,
        value=0.4,
        step=0.1
    )

    demand_df["Moving_Average"] = (
        demand_df["Demand"]
        .rolling(ma_window)
        .mean()
    )

    exp_values = []
    for i, val in enumerate(demand_df["Demand"]):
        if i == 0:
            exp_values.append(float(val))
        else:
            exp_values.append(
                alpha * float(val) +
                (1 - alpha) * exp_values[-1]
            )

    demand_df["Exp_Smoothing"] = exp_values

    next_ma = (
        demand_df["Demand"]
        .tail(ma_window)
        .mean()
    )

    next_exp = (
        alpha * float(demand_df["Demand"].iloc[-1]) +
        (1 - alpha) * float(demand_df["Exp_Smoothing"].iloc[-1])
    )

    latest = float(demand_df["Demand"].iloc[-1])
    avg_hist = float(demand_df["Demand"].mean())

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Latest Demand / 最新需求",
        f"{latest:,.0f}"
    )

    c2.metric(
        "Historical Average / 历史平均",
        f"{avg_hist:,.0f}"
    )

    c3.metric(
        "Next MA Forecast / 下期移动平均预测",
        f"{next_ma:,.0f}"
    )

    c4.metric(
        "Next ES Forecast / 下期指数平滑预测",
        f"{next_exp:,.0f}"
    )

    forecast_plot_df = demand_df.melt(
        id_vars="Date",
        value_vars=[
            "Demand",
            "Moving_Average",
            "Exp_Smoothing"
        ],
        var_name="Series",
        value_name="Value"
    )

    forecast_fig = px.line(
        forecast_plot_df,
        x="Date",
        y="Value",
        color="Series",
        color_discrete_map={
            "Demand": NAVY,
            "Moving_Average": TEAL,
            "Exp_Smoothing": ORANGE
        }
    )

    forecast_fig.update_layout(
        xaxis_title="Date / 日期",
        yaxis_title="Demand / 需求",
        height=430,
        margin=dict(l=20, r=20, t=50, b=80),
        font=dict(family="Arial", size=14, color=DARK_TEXT),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        legend_title_text=""
    )

    st.plotly_chart(
        forecast_fig,
        width="stretch",
        config={
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["select2d", "lasso2d"]
        }
    )

    st.subheader("Forecast Interpretation / 预测解释")

    trend_change = (
        (latest - demand_df["Demand"].iloc[-4]) /
        demand_df["Demand"].iloc[-4] * 100
        if len(demand_df) >= 4 and demand_df["Demand"].iloc[-4] != 0
        else 0
    )

    if trend_change > 8:
        st.warning(
            f"Demand has increased by approximately {trend_change:.1f}% versus three periods ago. "
            f"/ 与三个周期前相比，需求约上升 {trend_change:.1f}%。"
        )
    elif trend_change < -8:
        st.info(
            f"Demand has decreased by approximately {abs(trend_change):.1f}% versus three periods ago. "
            f"/ 与三个周期前相比，需求约下降 {abs(trend_change):.1f}%。"
        )
    else:
        st.success(
            "Recent demand is relatively stable. / 近期需求相对稳定。"
        )

    st.write(
        "• Moving Average / 移动平均："
        "more stable but slower to react to sudden changes. / "
        "更稳定，但对突然变化反应较慢。"
    )

    st.write(
        "• Exponential Smoothing / 指数平滑："
        "gives more weight to recent observations and reacts faster. / "
        "给予近期数据更高权重，对变化反应更快。"
    )

    st.caption(
        "The forecasting module is intended for decision support and demonstration. "
        "For real use, model selection should be validated against forecast error. / "
        "本模块用于决策支持和项目展示；实际使用时应根据预测误差验证模型选择。"
    )


elif page == "Decision Assistant / 决策助手":
    st.title(
        "Decision Assistant / 决策助手"
    )

    supplier = st.selectbox(
        "Choose supplier / 选择供应商",
        summary["Supplier"].tolist()
    )

    row = summary[
        summary["Supplier"] == supplier
    ].iloc[0]

    strengths = []
    concerns = []

    if row["Avg_Lead_Time"] <= summary["Avg_Lead_Time"].median():
        strengths.append(
            "competitive lead time / 交期具有竞争力"
        )
    else:
        concerns.append(
            "longer lead time / 交期较长"
        )

    if row["OTD"] >= summary["OTD"].median():
        strengths.append(
            "strong delivery reliability / 交付可靠性较强"
        )
    else:
        concerns.append(
            "below-median on-time delivery / 准时交付率偏低"
        )

    if row["Quality"] >= summary["Quality"].median():
        strengths.append(
            "strong quality performance / 质量表现较强"
        )
    else:
        concerns.append(
            "weaker quality performance / 质量表现偏弱"
        )

    if row["Risk"] <= summary["Risk"].median():
        strengths.append(
            "relatively low supplier risk / 供应商风险相对较低"
        )
    else:
        concerns.append(
            "elevated supplier risk / 供应商风险偏高"
        )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Avg Unit Cost / 平均单位成本",
        f"${row['Avg_Unit_Cost']:.2f}"
    )
    c2.metric(
        "Lead Time / 交期",
        f"{row['Avg_Lead_Time']:.1f} days"
    )
    c3.metric(
        "OTD / 准时交付率",
        f"{row['OTD']:.1f}%"
    )
    c4.metric(
        "Risk / 风险",
        f"{row['Risk']:.1f}/100"
    )

    st.subheader("Strengths / 优势")
    for item in strengths:
        st.write("• " + item)

    st.subheader("Concerns / 关注点")
    for item in concerns:
        st.write("• " + item)

    if len(concerns) <= 1:
        st.success(
            "Recommendation / 建议："
            "Strong candidate for continued or expanded sourcing. / "
            "可考虑维持或扩大采购合作。"
        )
    elif len(concerns) <= 3:
        st.warning(
            "Recommendation / 建议："
            "Suitable with mitigation actions and comparison against alternatives. / "
            "可继续考虑，但建议制定风险缓释措施并与其他供应商比较。"
        )
    else:
        st.error(
            "Recommendation / 建议："
            "Further review before additional sourcing commitment. / "
            "在增加采购承诺前建议进一步审查。"
        )

else:
    st.title(
        "Procurement Data / 采购数据"
    )

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )

    st.download_button(
        "Download current data / 下载当前数据",
        df.to_csv(index=False).encode("utf-8"),
        file_name="procurement_data.csv",
        mime="text/csv"
    )
