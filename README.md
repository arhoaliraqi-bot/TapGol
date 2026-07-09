# TapGol ⚽

**TapGol** ist eine moderne Mobile-App für Fußball-Enthusiasten. Gruppiere dich mit deinen Freunden, chatte in Echtzeit und organisiere Fußball-Matches durch Abstimmungen!

## Features 🎯

- 💬 **Live Chat** - Kommuniziere mit deinen Fußball-Gruppen
- 🗳️ **Abstimmungen** - Entscheide gemeinsam, wer kommt zum nächsten Match
- 👥 **Gruppen-Management** - Erstelle und verwalte Fußball-Gruppen
- 🔐 **Sichere Authentifizierung** - User-Accounts mit Login/Signup
- 📱 **Cross-Platform** - iOS & Android Support

## Tech Stack 🛠️

### Frontend
- **React Native** - Cross-Platform Mobile Development
- **JavaScript/TypeScript**
- **Redux** - State Management
- **Firebase Realtime DB** - Live Chat & Notifications

### Backend
- **Python** (Flask/FastAPI)
- **PostgreSQL** - Hauptdatenbank
- **JWT Authentication** - Sicherheit
- **RESTful API**

## Project Structure 📁

```
TapGol/
├── frontend/              # React Native App
│   ├── src/
│   ├── screens/
│   ├── components/
│   └── package.json
├── backend/               # Python Backend
│   ├── app/
│   ├── models/
│   ├── routes/
│   ├── requirements.txt
│   └── config.py
├── docs/                  # Dokumentation
└── README.md
```

## Getting Started 🚀

### Voraussetzungen
- Node.js & npm (für Frontend)
- Python 3.8+ (für Backend)
- Git

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

## API Endpoints 📡

- `POST /api/auth/signup` - Benutzer registrieren
- `POST /api/auth/login` - Benutzer anmelden
- `GET /api/groups` - Alle Gruppen abrufen
- `POST /api/groups` - Neue Gruppe erstellen
- `POST /api/messages` - Nachricht senden
- `POST /api/polls` - Abstimmung erstellen
- `POST /api/polls/:id/vote` - Für Poll abstimmen

## Roadmap 🗺️

- [ ] User Authentication (Backend)
- [ ] Chat-System (Frontend + Backend)
- [ ] Gruppen-Verwaltung
- [ ] Polls/Abstimmungen
- [ ] Push Notifications
- [ ] User Profile
- [ ] Match History

## Contributing 🤝

Beiträge sind willkommen! Bitte erstelle einen Pull Request mit deinen Änderungen.

## License 📄

MIT License - siehe LICENSE Datei für Details

## Support 💬

Fragen? Erstelle ein Issue oder kontaktiere uns!

---

**Viel Spaß beim Entwickeln mit TapGol!** ⚽🎉