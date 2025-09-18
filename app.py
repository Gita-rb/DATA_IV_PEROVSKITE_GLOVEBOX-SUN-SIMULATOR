import streamlit as st
import pandas as pd

st.title("📄 Ekstraksi Data File ke Tabel")

uploaded_file = st.file_uploader("Unggah file teks", type=["txt"])

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
    sections = content.strip().split("\n\n")

    def parse_section(section):
        lines = section.strip().splitlines()
        header = lines[0].split("\t")
        data = [line.split("\t") for line in lines[1:]]
        return pd.DataFrame(data, columns=header)

    try:
        st.subheader("📌 Metadata")
        st.dataframe(parse_section(sections[0]))

        st.subheader("⚙️ Parameter Pengujian")
        st.dataframe(parse_section(sections[1]))

        st.subheader("📊 Hasil Pengujian")
        st.dataframe(parse_section(sections[2]))

        st.subheader("📈 Data IV Curve")
        df_iv = parse_section(sections[3])
        st.dataframe(df_iv)
        st.line_chart(df_iv.astype(float))
    except Exception as e:
        st.error(f"Gagal memproses file: {e}")
