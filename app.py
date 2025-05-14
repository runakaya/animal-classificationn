import streamlit as st
from PIL import Image
from utils import predict_image

st.set_page_config(page_title="Hayvan Sınıflandırıcı", layout="centered")

st.title("Hayvan Sınıflandırıcı")
st.markdown("Bir görsel yükleyin ve hangi hayvana ait olduğunu tahmin edelim.")

st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
uploaded_file = st.file_uploader("Bir hayvan görseli yükleyin", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Yüklenen Görsel", width=250)

    if st.button("Tahmin Et"):
        prediction = predict_image(image)
        st.success(f"Bu görsel büyük olasılıkla: **{prediction}**")
