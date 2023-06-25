import streamlit as st
import os


file_tfidf = ("tfidf_vectorizer.pkl")
file_svm = ("svm_model.pkl")
file = ("stemmed_data.csv")

def delete_svm_file(filename):
    if os.path.exists("svm_model.pkl"):
        os.remove("svm_model.pkl")
        st.success(f"File '{filename}' telah dihapus.")
    else:
        st.warning(f"File '{filename}' tidak ditemukan.")

def delete_tfidf_file(filename):
    if os.path.exists("tfidf_vectorizer.pkl"):
        os.remove("tfidf_vectorizer.pkl")
        st.success(f"File '{filename}' telah dihapus.")
    else:
        st.warning(f"File '{filename}' tidak ditemukan.")

def delete_csv_file(filename):
    if os.path.exists("stemmed_data.csv"):
        os.remove("stemmed_data.csv")
        st.success(f"File '{filename}' telah dihapus.")
    else:
        st.warning(f"File '{filename}' tidak ditemukan.")
        
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="👋",
)

st.title("Home")
st.sidebar.success("Pilih Halaman diatas")

cek_file = os.path.exists("stemmed_data.csv")
# Streamlit app code
def main():
    st.markdown("")
    st.markdown("catatan :")
    st.markdown("1. Pada sistem sentiment analysis ini data menggunakan data file dengan format csv, jangan lupa menambahkan label (positif, netral, dan negatif) dan jangan lupa data teks kolom di ganti (full_text).")
    st.markdown("2. Isi dataset pada kolom jangan sampai kosong.")
    st.markdown("")
    col1, col2, col3 = st.columns(3)
    with col1:
    # Delete "stemmed_data.csv"
        if st.button("Delete stemmed_data.csv"):
            delete_csv_file(file)
                     
    with col2:
        # Delete "svm_model.pkl"
        if st.button("Delete svm_model.pkl"):
            delete_svm_file("svm_model.pkl")
            
    with col3:
        # Delete "tfidf_vectorizer.pkl"
        if st.button("Delete tfidf_vectorizer.pkl"):
            delete_tfidf_file("tfidf_vectorizer.pkl")
            

# Function to delete a file
def delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        st.error(f"Error deleting {file_path}: {e}")

# Run the Streamlit app
if __name__ == "__main__":
    main()