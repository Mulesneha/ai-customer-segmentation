import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Customer Segmentation",
    page_icon="🛒",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 25px;
    }

    .metric-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        background-color: #fafafa;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🛒 AI Customer Segmentation</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover customer groups using RFM Analysis and K-Means Machine Learning'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# LOAD DATASET
# =========================================================

@st.cache_data
def load_data():

    path = "data/customers.csv"

    df = pd.read_csv(path)

    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"]
    )

    df["TotalAmount"] = (
        df["Quantity"] *
        df["UnitPrice"]
    )

    return df


df = load_data()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚙️ Settings")

st.sidebar.info(
    "This application uses RFM Analysis and "
    "K-Means clustering to segment customers."
)


# Number of clusters

number_of_clusters = st.sidebar.slider(
    "Number of Customer Segments",
    min_value=2,
    max_value=8,
    value=4
)


# =========================================================
# DATASET PREVIEW
# =========================================================

with st.expander("📂 View Raw Dataset"):

    st.dataframe(
        df,
        use_container_width=True
    )


# =========================================================
# RFM ANALYSIS
# =========================================================

st.header("📊 RFM Analysis")


# Reference date

reference_date = (
    df["InvoiceDate"].max()
    + pd.Timedelta(days=1)
)


# RFM calculation

rfm = df.groupby("CustomerID").agg({

    "InvoiceDate": lambda x:
        (reference_date - x.max()).days,

    "InvoiceNo": "nunique",

    "TotalAmount": "sum"
})


# Rename columns

rfm.columns = [
    "Recency",
    "Frequency",
    "Monetary"
]


rfm = rfm.reset_index()


# =========================================================
# RFM METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "👥 Customers",
        len(rfm)
    )


with col2:

    st.metric(
        "💰 Total Revenue",
        f"${rfm['Monetary'].sum():,.2f}"
    )


with col3:

    st.metric(
        "🛍️ Avg Purchases",
        f"{rfm['Frequency'].mean():.1f}"
    )


with col4:

    st.metric(
        "💵 Avg Customer Value",
        f"${rfm['Monetary'].mean():,.2f}"
    )


st.divider()


# =========================================================
# DISPLAY RFM TABLE
# =========================================================

st.subheader("📋 Customer RFM Data")

st.dataframe(
    rfm,
    use_container_width=True
)


# =========================================================
# RFM DISTRIBUTIONS
# =========================================================

st.subheader("📈 RFM Distribution")


col1, col2, col3 = st.columns(3)


with col1:

    fig = px.histogram(
        rfm,
        x="Recency",
        title="Recency Distribution",
        nbins=15
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with col2:

    fig = px.histogram(
        rfm,
        x="Frequency",
        title="Frequency Distribution",
        nbins=10
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with col3:

    fig = px.histogram(
        rfm,
        x="Monetary",
        title="Monetary Distribution",
        nbins=15
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# MACHINE LEARNING
# =========================================================

st.header("🤖 K-Means Customer Segmentation")


features = [
    "Recency",
    "Frequency",
    "Monetary"
]


# Log transformation

rfm_model = rfm.copy()

rfm_model[features] = np.log1p(
    rfm_model[features]
)


# Standardization

scaler = StandardScaler()

scaled_features = scaler.fit_transform(
    rfm_model[features]
)


# K-Means

kmeans = KMeans(
    n_clusters=number_of_clusters,
    random_state=42,
    n_init=10
)


rfm["Cluster"] = kmeans.fit_predict(
    scaled_features
)


# =========================================================
# CUSTOMER SEGMENT LABELS
# =========================================================

cluster_summary = (
    rfm
    .groupby("Cluster")
    [features]
    .mean()
)


# Find best/worst based on normalized metrics

cluster_summary["Score"] = (
    cluster_summary["Frequency"]
    + cluster_summary["Monetary"]
    - cluster_summary["Recency"]
)


cluster_summary = cluster_summary.sort_values(
    "Score",
    ascending=False
)


segment_names = {}


names = [
    "🏆 VIP Customers",
    "💎 Loyal Customers",
    "🌱 Potential Customers",
    "⚠️ At-Risk Customers",
    "😴 Lost Customers",
    "⭐ Regular Customers",
    "🚀 Promising Customers",
    "💤 Inactive Customers"
]


for i, cluster in enumerate(
    cluster_summary.index
):

    if i < len(names):

        segment_names[cluster] = names[i]

    else:

        segment_names[cluster] = (
            f"Customer Segment {i + 1}"
        )


rfm["Segment"] = rfm["Cluster"].map(
    segment_names
)


# =========================================================
# SEGMENT RESULTS
# =========================================================

st.subheader("🎯 Customer Segments")


segment_counts = (
    rfm["Segment"]
    .value_counts()
    .reset_index()
)


segment_counts.columns = [
    "Segment",
    "Customers"
]


fig = px.bar(
    segment_counts,
    x="Segment",
    y="Customers",
    title="Customers by Segment",
    text="Customers"
)


fig.update_layout(
    xaxis_title="Customer Segment",
    yaxis_title="Number of Customers"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# =========================================================
# SCATTER PLOT
# =========================================================

st.subheader("🔍 Customer Segmentation Map")


fig = px.scatter(
    rfm,
    x="Frequency",
    y="Monetary",
    size="Monetary",
    color="Segment",
    hover_data=[
        "CustomerID",
        "Recency",
        "Frequency",
        "Monetary"
    ],
    title="Customer Segmentation"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# =========================================================
# 3D VISUALIZATION
# =========================================================

st.subheader("🌐 3D Customer Segmentation")


fig = px.scatter_3d(
    rfm,
    x="Recency",
    y="Frequency",
    z="Monetary",
    color="Segment",
    hover_data=["CustomerID"],
    title="3D RFM Customer Segments"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# =========================================================
# SEGMENT SUMMARY
# =========================================================

st.subheader("📊 Segment Summary")


summary = (
    rfm
    .groupby("Segment")
    .agg(
        Customers=("CustomerID", "count"),
        Avg_Recency=("Recency", "mean"),
        Avg_Frequency=("Frequency", "mean"),
        Avg_Monetary=("Monetary", "mean")
    )
    .round(2)
)


st.dataframe(
    summary,
    use_container_width=True
)


# =========================================================
# BUSINESS INSIGHTS
# =========================================================

st.header("💡 Business Insights")


for segment in summary.index:

    data = summary.loc[segment]

    customers = int(data["Customers"])

    revenue = data["Avg_Monetary"]

    frequency = data["Avg_Frequency"]

    recency = data["Avg_Recency"]


    with st.expander(
        f"{segment} — {customers} customers"
    ):

        if "VIP" in segment:

            st.success(
                "These customers have strong purchasing "
                "behavior and high monetary value. "
                "Offer premium rewards and exclusive products."
            )

        elif "Loyal" in segment:

            st.info(
                "These customers purchase frequently. "
                "Use loyalty programs, personalized offers "
                "and membership benefits."
            )

        elif "Potential" in segment:

            st.info(
                "These customers show growth potential. "
                "Use targeted discounts and product recommendations."
            )

        elif "At-Risk" in segment:

            st.warning(
                "These customers may be becoming inactive. "
                "Use re-engagement campaigns and special offers."
            )

        elif "Lost" in segment:

            st.error(
                "These customers have low recent activity. "
                "Consider win-back campaigns."
            )

        else:

            st.write(
                "Monitor this segment and create "
                "personalized marketing campaigns."
            )


# =========================================================
# DOWNLOAD RESULTS
# =========================================================

st.header("📥 Export Results")


csv = rfm.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="⬇️ Download Customer Segmentation CSV",
    data=csv,
    file_name="customer_segments.csv",
    mime="text/csv"
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🛒 AI Customer Segmentation | "
    "RFM Analysis + K-Means Machine Learning + Streamlit"
)