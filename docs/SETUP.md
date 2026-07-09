# TapGol Setup Guide 🚀

## Voraussetzungen

- **Node.js** v16+ & npm
- **Python** 3.8+
- **PostgreSQL** 12+ (oder verwende eine Cloud-Datenbank)
- **Git**

---

## Backend Setup (Python)

### 1. Python Virtual Environment erstellen

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Dependencies installieren

```bash
pip install -r requirements.txt
```

### 3. Umgebungsvariablen einrichten

```bash
# Kopiere .env.example zu .env
cp .env.example .env

# Bearbeite .env mit deiner Datenbank-URL
```

### 4. Datenbank initialisieren

```bash
# Starten Sie PostgreSQL lokal oder verwenden Sie Heroku PostgreSQL

flask db init
flask db migrate
flask db upgrade
```

### 5. Backend starten

```bash
python app.py
```

Backend läuft unter: `http://localhost:5000`

---

## Frontend Setup (React Native)

### 1. Dependencies installieren

```bash
cd frontend
npm install
```

### 2. Expo installieren (global)

```bash
npm install -g expo-cli
```

### 3. App starten

```bash
# Starten Sie Expo
npm start

# iOS Simulator (macOS only)
npm run ios

# Android Emulator
npm run android

# Web Browser
npm run web
```

---

## Datenbank Setup

### Option 1: PostgreSQL lokal
```bash
# macOS
brew install postgresql
brew services start postgresql

# Linux
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start

# Datenbank erstellen
createdb tapgol
```

### Option 2: Cloud Database (Heroku PostgreSQL, AWS RDS, etc.)
Nutze einen Cloud-Provider und trage die Connection URL in `.env` ein.

---

## API Testing

### Mit Postman oder cURL:

```bash
# Health Check
curl http://localhost:5000/api/health

# Registrierung (wird noch implementiert)
curl -X POST http://localhost:5000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
```bash
# Stelle sicher, dass dein venv aktiviert ist
source venv/bin/activate  # oder venv\Scripts\activate auf Windows
pip install -r requirements.txt
```

### "Port 5000 already in use"
```bash
# Nutze einen anderen Port
PORT=5001 python app.py
```

### React Native Fehler
```bash
# Cache löschen und neu starten
cd frontend
npm start -- --reset-cache
```

---

## Nächste Schritte

1. ✅ Backend: User-Authentifizierung implementieren
2. ✅ Frontend: Login-Screen erstellen
3. ✅ Backend: Gruppen-API implementieren
4. ✅ Frontend: Chat-Interface bauen
5. ✅ Backend: Poll-System

Viel Erfolg! 🎉