import streamlit as st
import pandas as pd
import numpy as np

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
    ["🏠 Home", "📊 Data Visualization", "🎲 Simulation Lab", "📈 Regression (Simple)", "ℹ️ About"]
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
    📈 회귀분석 (단순 회귀)  

    위와 같은 기능을 통해 '데이터를 이해하고 활용하는 과정'을 
    직접 경험할 수 있습니다.  
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

        column = st.selectbox("시각화할 변수를 선택하세요", df.columns)
        if pd.api.types.is_numeric_dtype(df[column]):
            st.bar_chart(df[column])
            st.line_chart(df[column])
        else:
            st.write(df[column].value_counts())
            st.bar_chart(df[column].value_counts())

# --------------------------
# Simulation Lab
# --------------------------
elif menu == "🎲 Simulation Lab":
    st.title("🎲 Simulation Lab")

    st.subheader("동전 던지기 시뮬레이션")
    n = st.slider("던질 횟수", 10, 1000, 100)
    flips = np.random.choice(["앞면", "뒷면"], size=n)
    counts = pd.Series(flips).value_counts()
    st.write(counts)
    st.bar_chart(counts)

    st.subheader("중심극한정리 시뮬레이션")
    sample_size = st.slider("표본 크기", 5, 100, 30)
    samples = [np.mean(np.random.exponential(scale=2, size=sample_size)) for _ in range(500)]
    st.write("표본평균 500개 분포")
    st.histogram(samples, bins=30)

# --------------------------
# Simple Regression
# --------------------------
elif menu == "📈 Regression (Simple)":
    st.title("📈 Simple Linear Regression")
    uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"], key="reg")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())

        y_col = st.selectbox("종속변수(y) 선택", df.columns)
        x_col = st.selectbox("독립변수(x) 선택", [c for c in df.columns if c != y_col])

        if pd.api.types.is_numeric_dtype(df[x_col]) and pd.api.types.is_numeric_dtype(df[y_col]):
            # 단순 회귀 계산 (수학식으로 직접 구현)
            X = df[x_col]
            Y = df[y_col]
            n = len(X)
            x_mean, y_mean = X.mean(), Y.mean()

            b1 = np.sum((X - x_mean) * (Y - y_mean)) / np.sum((X - x_mean)**2)
            b0 = y_mean - b1 * x_mean

            Y_pred = b0 + b1 * X

            st.write(f"회귀식: **y = {b0:.2f} + {b1:.2f}x**")

            # 시각화
            chart_df = pd.DataFrame({x_col: X, "실제 y": Y, "예측 y": Y_pred})
            st.line_chart(chart_df.set_index(x_col))
        else:
            st.warning("숫자형 변수만 선택할 수 있습니다.")

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
    - **단순 회귀분석**: 실제 데이터를 활용해 선형 관계 탐구  

    목표는 단순히 결과를 보여주는 것이 아니라,  
    **데이터에서 통찰을 얻는 과정**을 직접 탐험할 수 있도록 돕는 것입니다.
    """)
