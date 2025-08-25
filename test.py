import streamlit as st

st.set_page_config(page_title="성적 통계 분석기", layout="wide")

st.title("📊 시험 성적 통계 분석기")
st.write("CSV 파일을 업로드하면 과목별 통계 정보를 확인할 수 있어요.")

uploaded_file = st.file_uploader("📁 CSV 파일 업로드", type="csv")

if uploaded_file:
    # 데이터 읽기
    content = uploaded_file.getvalue().decode("utf-8").splitlines()
    header = content[0].strip().split(',')
    data = [row.strip().split(',') for row in content[1:]]

    st.subheader("📋 데이터 미리보기")
    st.write(f"총 {len(data)}명의 학생 데이터가 있습니다.")
    st.dataframe([dict(zip(header, row)) for row in data])

    st.subheader("📌 과목별 통계 정보")

    # 숫자형 열만 선택 (이름, 성별 같은 문자 제외)
    numeric_cols = []
    for i, col in enumerate(header):
        try:
            float(data[0][i])  # 첫 번째 값이 숫자인지 확인
            numeric_cols.append((i, col))
        except:
            continue

    if not numeric_cols:
        st.warning("숫자 데이터가 있는 열이 없습니다. 점수 데이터가 포함된 파일을 올려주세요.")
    else:
        for index, col in numeric_cols:
            try:
                values = [float(row[index]) for row in data]
                avg = sum(values) / len(values)
                sorted_vals = sorted(values)
                mid = len(values) // 2
                if len(values) % 2 == 0:
                    median = (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
                else:
                    median = sorted_vals[mid]
                variance = sum((x - avg) ** 2 for x in values) / len(values)
                std_dev = variance ** 0.5

                st.markdown(f"### 📚 {col}")
                st.markdown(f"- 평균: **{avg:.2f}**")
                st.markdown(f"- 중앙값: **{median:.2f}**")
                st.markdown(f"- 표준편차: **{std_dev:.2f}**")
                st.markdown("---")
            except:
                continue
else:
    st.info("CSV 파일을 업로드하면 분석 결과가 나타납니다.")

