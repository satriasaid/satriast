import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Portfolio", layout="wide", page_icon=":rocket:")

# --- Theme-Adaptive CSS for Tabs ---
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        font-size: 1.3rem;
        font-weight: 700;
        height: 60px;
        background: var(--background-color);
        border-radius: 12px 12px 0 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        padding-left: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 18px 36px;
        margin-right: 8px;
        border-radius: 12px 12px 0 0;
        background: var(--secondary-background-color);
        color: var(--text-color);
        border: 1px solid var(--primary-color);
        border-bottom: none;
        transition: background 0.2s, color 0.2s;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .stTabs [aria-selected="true"] {
        background: var(--primary-color);
        color: var(--background-color);
        border-bottom: 2px solid var(--primary-color);
        z-index: 2;
    }
    .stTabs [aria-selected="false"]:hover {
        background: var(--primary-color);
        color: var(--background-color);
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
            gender = st.selectbox(
                "Gender",
                options=df['Gender'].unique(),
                index=0
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
        ((df['Gender'] == gender)) &
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

    st.subheader("Age Distribution")
    age_hist = alt.Chart(filtered_df).mark_bar().encode(
        alt.X("Age:Q", bin=alt.Bin(maxbins=30), title="Age"),
        y=alt.Y('count()', title='Count'),
        tooltip=['count()']
    ).properties(
        width=400,
        height=300,
        title="Histogram of Age"
    )
    st.altair_chart(age_hist, use_container_width=False)

    st.subheader("Salary Distribution")
    salary_hist = alt.Chart(filtered_df).mark_bar(color='#00b894').encode(
        alt.X("EstimatedSalary:Q", bin=alt.Bin(maxbins=30), title="Estimated Salary"),
        y=alt.Y('count()', title='Count'),
        tooltip=['count()']
    ).properties(
        width=400,
        height=300,
        title="Histogram of Estimated Salary"
    )
    st.altair_chart(salary_hist, use_container_width=False)

    # Optional: Download filtered data
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Download filtered data as CSV",
        data=csv,
        file_name="filtered_churn_data.csv",
        mime="text/csv"
    )

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
