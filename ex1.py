import streamlit as st

st.title("📊 간단 데이터 시각화 대시보드 (No pandas/seaborn)")

uploaded_file = st.file_uploader("CSV 또는 Excel 파일 업로드", type=["csv", "xlsx"])

if uploaded_file:
    # Streamlit 자체 기능으로 읽기 (pandas 없이는 어렵지만 최소한으로 처리)
    if uploaded_file.name.endswith('.csv'):
        import csv
        import io

        decoded = uploaded_file.getvalue().decode("utf-8")
        reader = csv.reader(io.StringIO(decoded))
        rows = list(reader)
        header = rows[0]
        data = rows[1:]

        st.subheader("📄 데이터 미리보기")
        st.write(f"총 {len(data)}개의 행과 {len(header)}개의 열이 있습니다.")
        st.dataframe([dict(zip(header, row)) for row in data[:10]])

        # 숫자형 컬럼만 추출 (문자열을 숫자로 변환 시도)
        numeric_cols = []
        sample_row = data[0]

        for i, value in enumerate(sample_row):
            try:
                float(value)
                numeric_cols.append(header[i])
            except:
                pass

        if numeric_cols:
            st.subheader("📈 기본 시각화")

            selected_col = st.selectbox("그래프로 시각화할 컬럼 선택", numeric_cols)
            col_index = header.index(selected_col)

            values = []
            for row in data:
                try:
                    values.append(float(row[col_index]))
                except:
                    pass

            chart_type = st.radio("그래프 유형 선택", ["선 그래프", "막대 그래프", "면적 그래프"])

            import streamlit as st
            from collections import Counter
            import pandas as pd  # 이 부분은 최소한 chart용 데이터 프레임 변환 위해 사용

            df_chart = pd.DataFrame({selected_col: values})

            if chart_type == "선 그래프":
                st.line_chart(df_chart)
            elif chart_type == "막대 그래프":
                st.bar_chart(df_chart)
            else:
                st.area_chart(df_chart)
        else:
            st.warning("시각화할 수 있는 숫자형 데이터가 없습니다.")
    else:
        st.error("xlsx 파일은 pandas 없이 직접 처리하기 어렵습니다. CSV를 사용해주세요.")
else:
    st.info("파일을 업로드하세요.")
