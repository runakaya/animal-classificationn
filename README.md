# animal-classificationn
Animal Classification With PyCharm

hayvan-siniflandirici/
├── app.py
├── utils.py
├── backgorund.jpg       # Arka plan görseli
├── README.md
├── requirements.txt
└── .gitignore           # (Opsiyonel ama önerilir)


Hayvan Sınıflandırıcı

Bu proje, Hugging Face üzerindeki Vision Transformer (ViT) modelini kullanarak görsellerdeki hayvanları sınıflandıran bir yapay zeka uygulamasıdır. Streamlit arayüzü ile kullanıcı dostu, şık ve sezgisel bir deneyim sunar.

Özellikler

- Görsel yükleme ve önizleme
- Hugging Face ViT modeliyle sınıflandırma
- Sonuçların açıklayıcı metinle sunulması
- Şık ve özelleştirilmiş arka plan

Kurulum

bash
git clone https://github.com/kullanici-adi/hayvan-siniflandirici.git
cd hayvan-siniflandirici
pip install -r requirements.txt

streamlit run app.py


