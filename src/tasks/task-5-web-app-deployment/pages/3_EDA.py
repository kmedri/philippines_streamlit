import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
from PIL import Image

APP_TITLE = 'Philippines - Urban Vulnerability Levels'
st.set_page_config(page_title='EDA', layout='wide')


# Load the DATA and cache.
@st.cache_data
def get_data(url):
    df = pd.read_csv(url)
    return df


url = 'src/tasks/task-5-web-app-deployment/data/all_data.csv'
df1 = get_data(url)


def main():
    # Colors:
    # Blue = #182D40
    # Light Blue = #82a6c0
    # Green = #4abd82

    st.markdown(
        """
        <style>
        .css-k1ih3n {
            padding: 2rem 1rem 10rem;
        }
        .block-container.css-18e3th9.egzxvld2 {
        padding-top: 0;
        }
        header.css-vg37xl.e8zbici2 {
        background: none;
        }
        span.css-10trblm.e16nr0p30 {
        color: #2c39b1;
        }
        .css-1dp5vir.e8zbici1 {
        background-image: linear-gradient(
        90deg, rgb(130 166 192), rgb(74 189 130)
        );
        }
        .css-tw2vp1.e1tzin5v0 {
        gap: 10px;
        }
        .css-50ug3q {
        font-size: 1.2em;
        font-weight: 600;
        color: #2c39b1;
        }
        .row-widget.stSelectbox {
        padding: 10px;
        background: #ffffff;
        border-radius: 7px;
        }
        .row-widget.stRadio {
        padding: 10px;
        background: #ffffff;
        border-radius: 7px;
        }
        label.css-cgyhhy.effi0qh3, span.css-10trblm.e16nr0p30 {
        font-size: 1.1em;
        font-weight: bold;
        font-variant-caps: small-caps;
        text-decoration-line: underline;
        text-decoration-color: green;
        text-underline-offset: 8px;
        }
        .css-12w0qpk.e1tzin5v2 {
        background: #d2d2d2;
        border-radius: 8px;
        padding: 5px 10px;
        }
        label.css-18ewatb.e16fv1kl2 {
        font-variant: small-caps;
        font-size: 1em;
        }
        .css-1xarl3l.e16fv1kl1 {
        float: right;
        }
        div[data-testid="stSidebarNav"] li div a {
        margin-left: 1rem;
        padding: 1rem;
        width: 300px;
        border-radius: 0.5rem;
        }
        div[data-testid="stSidebarNav"] li div::focus-visible {
        background-color: rgba(151, 166, 195, 0.15);
        }
        svg.e1fb0mya1.css-fblp2m.ex0cdmw0 {
        width: 2rem;
        height: 2rem;
        }
        .css-184tjsw p {
        word-break: break-word;
        font-size: 1rem;
        font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns((1, 1, 1))
    with col1:
        image2 = Image.open('src/tasks/task-5-web-app-deployment/assets/Omdena.png')
        st.image(image2)

    with col2:
        st.write('')

    with col3:
        image1 = Image.open('src/tasks/task-5-web-app-deployment/assets/UNHABITAT.png')
        st.image(image1)

    st.title(APP_TITLE)

    st.markdown('#### df1.head(10)')
    st.dataframe(df1.head(10))
    st.markdown('#### df1.describe()')
    st.dataframe(df1.describe())

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### st.pyplot(fig1) - Vulnerability Economy")
        labels = 'High', 'Medium', 'Low'
        sizes = [472, 1024, 136]
        explode = (0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

    with col2:
        st.markdown("#### st.pyplot(fig1) - Vulnerability Disaster")
        labels = 'High', 'Medium', 'Low'
        sizes = [142, 1349, 141]
        explode = (0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

    with col3:
        st.markdown("#### st.pyplot(fig1) - Vulnerability Industry")
        labels = 'High', 'Medium', 'Low'
        sizes = [154, 543, 935]
        explode = (0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### st.pyplot(fig1) - Vulnerability Health")
        labels = 'High', 'Medium', 'Low'
        sizes = [567, 897, 168]
        explode = (0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

    with col2:
        st.markdown("#### st.pyplot(fig1) - Vulnerability Poverty")
        labels = 'High', 'Medium', 'Low'
        sizes = [247, 813, 572]
        explode = (0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

    with col3:
        st.write('')

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### sns.distplot(df1['pov_inc']")
        fig = plt.figure(figsize=(10, 10))
        sns.distplot(df1['pov_inc'], color='#4abd82', bins=100, hist_kws={'alpha': 0.4})
        st.pyplot(fig)

    with col2:
        st.markdown("#### df1['pov_inc'].describe()")
        st.dataframe(df1['pov_inc'].describe())
        st.markdown("#### df1.select_dtypes(include=['float64', 'int64'])")
        df1_num = df1.select_dtypes(include=['float64', 'int64'])
        st.dataframe(df1_num.head(5))
        df1.fillna(0, inplace=True)

    st.markdown("#### st.pyplot(fig) - Numeric Features Histograms")
    df = pd.DataFrame(df1_num)
    fig, ax = plt.subplots(figsize=(16, 20))
    ax = df.hist(bins=50, ax=ax)
    plt.show()
    st.pyplot(fig)

if __name__ == "__main__":
    main()
