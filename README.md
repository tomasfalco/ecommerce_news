# 1. Clonar el repo
git clone https://github.com/tuusuario/ecommerce-news.git

cd ecommerce-news

# 2. Backend
cd backend

pip3 install -r requirements.txt

python3 scraper.py

uvicorn main:app --reload

# 3. Frontend (en otra terminal)
cd frontend

npm install

npm run dev
