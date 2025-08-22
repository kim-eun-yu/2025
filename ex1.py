import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# --------------------------
# 페이지 설정
# --------------------------
st.set_page_config(
    page_title="통계 포트폴리오 웹사이트",
    page_icon="📊",
    layout="wide"
)

# --------------------------
# 사이드바 메뉴
# --------------------------
menu = st.sidebar.radio(
    "메뉴 선택",
    ["🏠 Home", "📊 Data Visualization", "🎲 Simulation Lab", "📈 Regression & ML", "ℹ️ About"]
)

# --------------------------
# Home
# --------------------------
if menu == "🏠 Home":
    st.title("🏠 Home")
    st.subheader("Welcome!")
    st.write("""
    이 웹사이트는 통계학의 주요 개념과 데이터 분석 과정을 
    직관적으로 보여주기 위해 제작되었습니다.  

    📊 데이터 시각화  
    🎲 확률·통계 시뮬레이션  
    📈 회귀분석 및 머신러닝  

    위와 같은 기능을 통해 '데이터를 이해하고 활용하는 과정'을 
    직접 경험할 수 있습니다.  
    왼쪽 메뉴에서 원하는 페이지를 선택해 탐험해 보세요!
    """)

# --------------------------
# Data Visualization
# --------------------------
elif menu == "📊 Data Visualization":
    st.title("📊 Data Visualization")
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("데이터 미리보기:")
        st.dataframe(df.head())

        st.subheader("기본 통계량")
        st.write(df.describe())

        st.subheader("히스토그램")
        column = st.selectbox("변수를 선택하세요", df.columns)
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)

        st.subheader("상관관계 Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

# --------------------------
# Simulation Lab
# --------------------------
elif menu == "🎲 Simulation Lab":
    st.title("🎲 Simulation Lab")

    st.subheader("동전 던지기 시뮬레이션")
    n = st.slider("던질 횟수", 10, 1000, 100)
    flips = np.random.choice(["앞면", "뒷면"], size=n)
    counts = {side: np.sum(flips == side) for side in ["앞면", "뒷면"]}
    st.write(counts)

    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values(), color=["blue", "red"])
    st.pyplot(fig)

    st.subheader("중심극한정리 시뮬레이션")
    sample_size = st.slider("표본 크기", 5, 100, 30)
    samples = [np.mean(np.random.exponential(scale=2, size=sample_size)) for _ in range(1000)]
    
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    st.pyplot(fig)
    st.caption("표본 크기가 커질수록 정규분포 형태로 수렴함")

# --------------------------
# Regression & ML
# --------------------------
elif menu == "📈 Regression & ML":
    st.title("📈 Regression & Machine Learning")
    uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"], key="ml")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())

        y_col = st.selectbox("종속변수(y) 선택", df.columns)
        x_cols = st.multiselect("독립변수(X) 선택", df.columns, default=[c for c in df.columns if c != y_col])

        if st.button("회귀분석 실행"):
            X = df[x_cols]
            y = df[y_col]

            model = LinearRegression()
            model.fit(X, y)
            y_pred = model.predict(X)

            st.write("회귀계수:", model.coef_)
            st.write("절편:", model.intercept_)
            st.write("R²:", model.score(X, y))

            fig, ax = plt.subplots()
            ax.scatter(y, y_pred)
            ax.plot([y.min(), y.max()], [y.min(), y.max()], "r--")
            ax.set_xlabel("실제값")
            ax.set_ylabel("예측값")
            st.pyplot(fig)

# --------------------------
# About
# --------------------------
elif menu == "ℹ️ About":
    st.title("ℹ️ About This Website")
    st.write("""
    이 웹사이트는 통계학적 사고와 데이터 분석 과정을 
    학습하고 공유하기 위해 만들어졌습니다.  

    주요 기능:
    - **데이터 시각화**: 업로드한 데이터를 요약하고 다양한 그래프로 표현  
    - **시뮬레이션**: 확률 및 통계 개념을 실험적으로 체험  
    - **회귀분석 & 머신러닝**: 실제 데이터를 활용한 모델링과 예측  

    목표는 단순히 결과를 보여주는 것이 아니라,  
    **데이터에서 통찰을 얻는 과정**을 직접 탐험할 수 있도록 돕는 것입니다.
    """)
