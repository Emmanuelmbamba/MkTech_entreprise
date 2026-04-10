# InnovaTech SARL - Plateforme de Formation Professionnelle

## 🎯 Projet

Plateforme web moderne pour le Centre Professionnel en Technologie (InnovaTech) offrant des formations en développement web, administration réseau, cybersécurité et maintenance informatique.

## 🚀 Fonctionnalités Implémentées

### ✅ Authentification & Gestion Utilisateurs
- **Système de connexion** (`login.html`) avec validation
- **Page d'inscription** (`register.html`) avec vérification de force de mot de passe
- **Rôles utilisateurs** : Admin vs User avec permissions différenciées
- **Gestion complète** : Créer, modifier, supprimer des utilisateurs

### 📊 Tableaux de Bord
- **Dashboard Admin** (`admin-dashboard.html`) :
  - Statistiques en temps réel
  - Gestion des utilisateurs avec interface CRUD
  - Graphiques Chart.js (évolution des inscriptions, répartition des formations)
  - Interface Material Design moderne

- **Dashboard User** (`user-dashboard.html`) :
  - Suivi de progression personnelle
  - Statistiques d'apprentissage
  - Historique d'activité
  - Profil modifiable

### 🎨 Design Moderne
- **Material Design** avec Google Fonts (Poppins) et Material Icons
- **Design responsive** adaptatif mobile/desktop
- **Animations fluides** : scroll reveal, parallax, transitions
- **Thème cohérent** avec variables CSS et glassmorphism

### 📈 Statistiques & Visualisation
- **Chart.js intégré** pour :
  - Graphiques linéaires (évolution des inscriptions)
  - Graphiques circulaires (répartition des formations)
  - Tableaux de bord interactifs

### 🔐 Sécurité & Permissions
- **Gestion des rôles** : Admin accès complet, User accès limité
- **Session sécurisée** avec localStorage
- **Redirections automatiques** selon le rôle

## 📁 Structure du Projet

```
d:\Projet_ENLIGNE\
├── login.html                 # Page de connexion
├── register.html              # Page d'inscription  
├── admin-dashboard.html       # Dashboard administrateur
├── user-dashboard.html        # Dashboard utilisateur
├── index.html                 # Page d'accueil (modernisée)
├── inscription.html          # Formulaire d'inscription aux formations
├── service.html               # Page des services
├── formation.html             # Page des formations
├── about.html                 # Page à propos
├── contact.html              # Page de contact
├── mycv.html                  # Page CV
├── solution.html             # Page solutions
├── Dasgboard.html            # Dashboard original (backup)
├── Dasgboard2.html           # Dashboard v2 (backup)
├── styleindex.css            # Styles modernisés (Material Design)
├── styleMenuMobF.css         # Styles menu mobile
├── styleinscription.css      # Styles inscription
├── stylecontact.css         # Styles contact
├── styleformation.css       # Styles formations
├── stylepropos.css          # Styles à propos
├── styleservice.css         # Styles services
├── stylesolution.css       # Styles solutions
├── scriptAcceuil.js        # Scripts accueil original
├── script-animations.js    # Animations modernes
├── javascrptMenus.js       # Scripts menus
├── README.md               # Ce fichier
└── [Images & Assets]      # Logo, images du slider, etc.
```

## 🛠️ Technologies Utilisées

- **HTML5** : Structure sémantique moderne
- **CSS3** : Material Design, Glassmorphism, Animations
- **JavaScript Vanilla** : Gestion authentification, animations, interactions
- **Chart.js** : Visualisation de données
- **Google Fonts** : Poppins
- **Material Icons** : Icônes Google
- **LocalStorage** : Stockage client-side

## 🎯 Points d'Accès

### Pour les Utilisateurs
1. **Inscription** : `register.html`
2. **Connexion** : `login.html`
3. **Dashboard personnel** : `user-dashboard.html`

### Pour les Administrateurs
1. **Connexion admin** : `login.html` (admin@innovatech.com / admin123)
2. **Dashboard admin** : `admin-dashboard.html`

### Comptes de Démo
- **Admin** : `admin@innovatech.com` / `admin123`
- **User** : `user@innovatech.com` / `user123`

## ✨ Caractéristiques Techniques

### Performance
- **Animations optimisées** avec CSS transforms
- **Chargement progressif** des éléments
- **Responsive design** mobile-first

### UX/UI
- **Interface intuitive** Material Design
- **Feedback visuel** sur toutes les interactions
- **Navigation fluide** avec transitions
- **Accessibilité** : balisage sémantique, contrastes

### Sécurité
- **Validation coté client** des formulaires
- **Gestion des sessions** sécurisée
- **Permissions** basées sur les rôles

## 🚀 Comment Utiliser

1. **Ouvrir `index.html`** pour la page d'accueil
2. **S'inscrire** via `register.html` ou utiliser les comptes démo
3. **Se connecter** via `login.html`
4. **Accéder au dashboard** selon le rôle (admin ou user)

## 🔄 Fonctionnalités Futures Possibles

- [ ] Backend Node.js/Express pour données persistantes
- [ ] Base de données MongoDB/PostgreSQL
- [ ] Système de paiement pour formations
- [ ] Chat en temps réel
- [ ] Notifications push
- [ ] Certificats PDF générés automatiquement
- [ ] API REST complète
- [ ] Tests automatisés

## 📞 Contact

**InnovaTech SARL** - Centre Professionnel en Technologie  
Directeur : Emmanuel Mbamba  
Localisation : Kinshasa, RDC

---

*Développé avec ❤️ pour la formation technologique en Afrique*
