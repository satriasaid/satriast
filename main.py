import streamlit as st
import pandas as pd

st.set_page_config(page_title="Portfolio", layout="wide", page_icon=":rocket:")

# --- Custom CSS for Big, Professional Tabs ---
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        font-size: 1.3rem;
        font-weight: 700;
        height: 60px;
        background: #f8f9fa;
        border-radius: 12px 12px 0 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        padding-left: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 18px 36px;
        margin-right: 8px;
        border-radius: 12px 12px 0 0;
        background: #ffffff;
        color: #222;
        border: 1px solid #e0e0e0;
        border-bottom: none;
        transition: background 0.2s, color 0.2s;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .stTabs [aria-selected="true"] {
        background: #0072ff;
        color: #fff;
        border-bottom: 2px solid #0072ff;
        z-index: 2;
    }
    .stTabs [aria-selected="false"]:hover {
        background: #e6f0ff;
        color: #0072ff;
    }
    .stTabs [data-baseweb="tab-highlight"] {
        background: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Tabs at the very top ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👤 About Me", 
    "📁 Projects", 
    "📊 Data Explorer",
    "🧪 Data Science Playground", 
    "✉️ Contact Me"
])

with tab1:
    st.title("My Portfolio")
    st.header("Data Science Enthusiast")
    st.markdown("""
    Hi! I'm Satria, a passionate data science enthusiast with experience in Python, machine learning, and data visualization.
    - 🔍 I love uncovering insights from data.
    - 🛠️ Skilled in pandas, scikit-learn, and Streamlit.
    - 🚀 Always eager to learn and grow!
    """)

with tab2:
    st.title("My Portfolio")
    st.header("Projects")
    st.markdown("""
    **1. Customer Churn Prediction**  
    Used machine learning to predict customer churn for a telecom company.

    **2. Sales Dashboard**  
    Built an interactive sales dashboard using Streamlit and Plotly.

    **3. Sentiment Analysis**  
    Analyzed social media sentiment using NLP techniques.
    """)
    
with tab3:
    st.title("Data Explorer")
    st.markdown("Explore and filter the customer churn data interactively.")

    # --- Load Data ---
    @st.cache_data
    def load_data():
        return pd.read_csv('Churn_Modelling.csv')
    df = load_data()

    # --- Filters ---
    with st.expander("🔎 Filter Data", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            geography = st.multiselect(
                "Geography", 
                options=df['Geography'].unique(), 
                default=list(df['Geography'].unique())
            )
        with col2:
            gender = st.multiselect(
                "Gender", 
                options=df['Gender'].unique(), 
                default=list(df['Gender'].unique())
            )
        with col3:
            age_range = st.slider(
                "Age Range", 
                int(df['Age'].min()), 
                int(df['Age'].max()), 
                (int(df['Age'].min()), int(df['Age'].max()))
            )

    # --- Filter DataFrame ---
    filtered_df = df[
        (df['Geography'].isin(geography)) &
        (df['Gender'].isin(gender)) &
        (df['Age'] >= age_range[0]) &
        (df['Age'] <= age_range[1])
    ]

    st.dataframe(filtered_df, use_container_width=True)

    # --- Visualizations ---
    st.subheader("Number of Customers by Geography")
    st.bar_chart(filtered_df['Geography'].value_counts())

    st.subheader("Churn Rate by Gender")
    churn_rate = filtered_df.groupby('Gender')['Exited'].mean()
    st.bar_chart(churn_rate)

    import matplotlib.pyplot as plt

    st.subheader("Age Distribution")
    fig, ax = plt.subplots(figsize=(5, 3))  # 5 inches wide, 3 inches tall
    ax.hist(filtered_df['Age'], bins=30, color='#0072ff', edgecolor='white')
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    st.subheader("Salary Distribution")
    fig, ax = plt.subplots(figsize=(5, 3))  # Adjust width and height as needed
    ax.hist(filtered_df['EstimatedSalary'], bins=30, color='#00b894', edgecolor='white')
    ax.set_xlabel('Estimated Salary')
    ax.set_ylabel('Count')
    ax.set_title('Histogram of Estimated Salary')
    st.pyplot(fig)

with tab4:
    st.title("My Portfolio")
    st.header("Data Science Playground")
    st.markdown("""
    Try out my latest data science experiments and prediction tools here!
    """)
    st.subheader("Demo: Predict if a number is even or odd")
    number = st.number_input("Enter a number:", value=0)
    if number % 2 == 0:
        st.success("This number is **Even** 🎉")
    else:
        st.warning("This number is **Odd** 🤖")

with tab5:
    st.title("My Portfolio")
    st.header("Contact Me")
    st.markdown("""
    - 📧 **Email:** satriasaid@xyz.com  
    - 📱 **Phone:** 081234567890  
    - 💼 **LinkedIn:** [linkedin.com/in/satriaxyz](https://linkedin.com/in/satriaxyz)
    """)