# Laporan Proyek Machine Learning - Prediksi Performa Murid

## **Project Overview**
Proyek ini bertujuan untuk membangun model machine learning yang dapat memprediksi performa murid berdasarkan dataset yang mencakup fitur seperti **jam belajar**, **jam tidur**, **skor sosial ekonomi**, **kehadiran (%)**, dan **nilai akhir (grades)**. Dengan pendekatan ini, diharapkan dapat memberikan wawasan yang berguna untuk mendukung pengambilan keputusan dalam meningkatkan kualitas pendidikan.

Pentingnya proyek ini terletak pada potensinya untuk membantu pendidik dan institusi memahami faktor-faktor yang berpengaruh terhadap performa murid. Menurut jurnal dari **Ibrahim et al. (2024)**, faktor akademis dan non-akademis, seperti skor sebelumnya, jam belajar, serta motivasi, memiliki pengaruh signifikan terhadap hasil belajar. Dengan memanfaatkan pendekatan berbasis data ini, model yang dibangun diharapkan dapat menjadi alat pendukung untuk mengidentifikasi murid yang berisiko rendah sehingga memungkinkan intervensi dini.

**Referensi**: [Predictive Model for Factors Impacting Students' Academic Performance](https://www.researchgate.net/publication/384625747)

---

## **Business Understanding**

### **Problem Statements**
1. Bagaimana cara membuat model machine learning untuk memprediksi nilai akhir murid dengan akurasi yang baik?  
2. Model mana yang paling sesuai untuk memprediksi performa murid berdasarkan evaluasi?  
3. Bagaimana fitur seperti jam belajar, jam tidur, dan kehadiran memengaruhi performa murid?  

### **Goals**
1. Mengembangkan model regresi untuk memprediksi nilai akhir murid berdasarkan fitur yang tersedia.  
2. Mengevaluasi performa beberapa algoritma machine learning seperti **K-Nearest Neighbors**, **Random Forest**, dan **AdaBoost**.  
3. Memberikan wawasan dari analisis data untuk mendukung pemahaman lebih baik mengenai faktor yang memengaruhi nilai murid.  

---

## **Data Understanding**

### **Dataset**
- **Jumlah Data**: 1,388 baris, 5 kolom.  
- **Sumber Data**: Kaggle - [Predict Student Performance Dataset](https://www.kaggle.com/datasets/stealthtechnologies/predict-student-performance-dataset/data)  

### **Kondisi Data**
- **Missing Values**: Tidak ditemukan nilai yang hilang.  
- **Duplikat**: Tidak ditemukan duplikasi data.  
- **Outlier**: Ditemukan pada fitur numerik dan dihapus menggunakan metode **IQR**.  

### **Fitur Dataset**
- **Study Hours**: Rata-rata jam belajar per hari.  
- **Sleep Hours**: Rata-rata jam tidur per hari.  
- **Socioeconomic Score**: Skor sosial ekonomi murid.  
- **Attendance (%)**: Persentase kehadiran.  
- **Grades**: Nilai akhir murid (target prediksi).  

### **Visualisasi dan Insight**
- Distribusi fitur menunjukkan rata-rata **jam belajar di bawah 5 jam** dan **tingkat kehadiran di bawah 75%**.  
- Korelasi signifikan ditemukan antara **Study Hours** dan **Grades**. Korelasi lebih lemah terlihat antara **Sleep Hours** dan **Study Hours**.  

---

## **Data Preparation**
1. **Pembersihan Data**:
   - Menghapus outlier menggunakan metode **IQR**.  
2. **Scaling**:
   - Menggunakan **StandardScaler** untuk menormalkan fitur numerik.  
3. **Splitting**:
   - Membagi data menjadi **80% training** dan **20% testing** menggunakan `train_test_split`.  

---

## **Model Development**

### **Model 1: K-Nearest Neighbors (KNN)**
- **Cara Kerja**: Menggunakan jarak terdekat untuk membuat prediksi berdasarkan rata-rata nilai K tetangga.  
- **Parameter**: `n_neighbors=5` (default).  
- **Kelebihan**: Mudah diimplementasikan, cocok untuk dataset kecil.  
- **Kekurangan**: Tidak efisien pada dataset besar.  

### **Model 2: Random Forest**
- **Cara Kerja**: Model ensemble yang menggunakan banyak decision tree untuk menghasilkan prediksi yang lebih stabil.  
- **Parameter**: `n_estimators=100` (default).  
- **Kelebihan**: Mengurangi risiko overfitting, akurasi tinggi.  
- **Kekurangan**: Memerlukan sumber daya lebih besar.  

### **Model 3: AdaBoost**
- **Cara Kerja**: Boosting algoritma yang memperbaiki prediksi model sebelumnya dengan memberi bobot lebih besar pada kesalahan.  
- **Parameter**: `n_estimators=50`, `learning_rate=0.1`.  
- **Kelebihan**: Menguatkan model lemah menjadi model yang lebih kuat.  
- **Kekurangan**: Rentan terhadap noise.  

---

## **Evaluation**

### **Metrik Evaluasi**
- **Mean Squared Error (MSE)**: Rata-rata kuadrat kesalahan prediksi.  

### **Hasil Evaluasi**
| **Model**            | **Train MSE** | **Test MSE** |
|-----------------------|---------------|--------------|
| K-Nearest Neighbor    | 3.38          | 5.78         |
| Random Forest         | 0.23          | 1.72         |
| AdaBoost              | 3.73          | 6.75         |

### **Kesimpulan**
- **Model terbaik**: Random Forest dengan **Train MSE = 0.23** dan **Test MSE = 1.72**.  

---

## **Dampak Terhadap Business Understanding**
Model berhasil menjawab semua problem statement:  
1. Prediksi nilai akhir dapat dilakukan dengan akurasi tinggi.  
2. Random Forest adalah model yang paling sesuai.  
3. Semua tujuan tercapai dengan analisis data memberikan wawasan signifikan tentang faktor yang memengaruhi performa murid.  

---

## **Kesimpulan**
Model **Random Forest** memberikan performa terbaik untuk prediksi nilai murid.  
- **Faktor utama** yang memengaruhi performa murid adalah **Study Hours**, **Socioeconomic Score**, dan **Attendance (%)**.  
- Model ini dapat digunakan oleh institusi pendidikan untuk mengidentifikasi murid berisiko rendah dan memberikan intervensi dini.  
