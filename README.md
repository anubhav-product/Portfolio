# Anubhav Verma - Product Manager Portfolio

> A professional, multi-page portfolio showcasing AI product development, product thinking frameworks, and end-to-end execution capabilities.

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://portfolio-o5n7.onrender.com)
[![GitHub](https://img.shields.io/badge/github-repository-blue)](https://github.com/anubhav-product/Portfolio)
[![LinkedIn](https://img.shields.io/badge/linkedin-connect-0077B5)](https://www.linkedin.com/in/anubhav-verma-746740250/)

## 🎯 Overview

This portfolio demonstrates full-stack product management capabilities through a clean, modern web application. Built with Flask and deployed on Render, it showcases:

- **0-to-1 Product Development**: Two end-to-end AI products shipped independently
- **Product Thinking Frameworks**: Structured approaches to product decisions and prioritization
- **Technical Execution**: Full-stack development with Python, Flask, and modern web technologies
- **Professional Design**: Responsive, accessible, and performance-optimized user experience

## ✨ Features

### 🏠 **Home Page**
- Dynamic hero section with typing animation
- Comprehensive "About Me" section with professional journey timeline
- BITS Pilani Goa education integration
- Animated statistics counter
- Product philosophy and principles

### 💼 **Projects Page**
- Featured AI products with quantifiable metrics
- Detailed project breakdowns (Product Playground, AI Interview Copilot)
- Live demo links and GitHub repositories
- Impact-driven descriptions with technical details

### 🧠 **Product Thinking Page**
- Real product decisions and tradeoffs
- Responsible AI design choices
- Feature scoping rationale
- Decision-support vs. automation philosophy

### 📐 **Frameworks Page** (Unique Differentiator)
- Problem Framing Canvas (4-step framework)
- RICE + Trust prioritization matrix (AI-specific)
- AI Product Decision Tree
- Product teardown analysis (Grammarly case study)
- Core product principles

### 🛠️ **Skills Page**
- Product Strategy & Execution
- AI & Technical Capabilities
- Stakeholder Management & Analytics
- Tools & Platforms
- Education & Certifications

### 📧 **Contact Page**
- Professional contact grid layout
- Direct links to email, LinkedIn, GitHub, resume
- "What I'm Looking For" section
- "Why Work With Me?" highlights

## 🚀 Tech Stack

**Backend:**
- Python 3.11
- Flask 3.1.0
- Gunicorn 21.2.0 (production server)

**Frontend:**
- HTML5 with Jinja2 templating
- CSS3 (custom design system, no frameworks)
- Vanilla JavaScript (intersection observers, animations)
- Google Fonts (Inter)

**Deployment:**
- Render.com (auto-deploy from GitHub)
- Environment: Python 3.11
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`

**Design Features:**
- Smooth page transitions (0.3s crossfade)
- Scroll-triggered animations (IntersectionObserver API)
- Responsive design (mobile-first approach)
- Dark theme with cyan accent (#00d9ff)
- Accessibility features (skip links, ARIA labels, keyboard navigation)

## 📦 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anubhav-product/Portfolio.git
   cd Portfolio
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   ```
   http://localhost:5000
   ```

### Production Deployment (Render)

This project is configured for automatic deployment on Render.com:

1. Fork or clone this repository to your GitHub account
2. Sign up at [render.com](https://render.com)
3. Create a new "Web Service" and connect your GitHub repository
4. Render will automatically detect `render.yaml` and configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Python Version**: 3.11.0
5. Click "Create Web Service" and wait 2-3 minutes for deployment

Your portfolio will be live at `https://your-service-name.onrender.com`

## 📁 Project Structure

```
Portfolio/
├── app.py                      # Flask application with 6 routes
├── requirements.txt            # Python dependencies
├── render.yaml                 # Render deployment configuration
├── README.md                   # Project documentation
├── static/
│   ├── style.css              # Main stylesheet (2000+ lines)
│   ├── downloads/             # Downloadable assets
│   └── resume/
│       └── resume.pdf         # Resume PDF file
├── templates/
│   ├── base.html              # Base template with navigation
│   ├── home.html              # Landing page
│   ├── projects.html          # Featured AI products
│   ├── product_thinking.html  # Product decisions & tradeoffs
│   ├── frameworks.html        # Product frameworks (unique!)
│   ├── skills.html            # Technical & product skills
│   ├── contact.html           # Contact information
│   └── index.html             # Legacy single-page template
└── documentation/
    ├── ANIMATIONS_SUMMARY.md
    ├── RESUME_INSTRUCTIONS.md
    └── VISUAL_ENHANCEMENTS.md
```

## 🎨 Design System

**Colors:**
- Background: `#0a0e17` (dark navy)
- Secondary Background: `#1a1f2e`
- Primary Accent: `#00d9ff` (cyan)
- Text: `#e4e4e7` (light gray)
- Muted Text: `#a1a1aa`

**Typography:**
- Font Family: Inter (Google Fonts)
- Weights: 400 (regular), 500 (medium), 600 (semi-bold), 700 (bold)

**Animations:**
- Page transitions: 0.3s crossfade
- Scroll animations: IntersectionObserver-based
- Hover effects: 0.3s cubic-bezier transitions
- Staggered entrance animations with delay classes

## 🌟 Key Highlights

### Unique Differentiators
1. **Frameworks Page**: Shows structured product thinking methodology (not common in PM portfolios)
2. **RICE + Trust Matrix**: Modified prioritization framework with AI-specific dimension
3. **Product Teardown Sample**: Demonstrates analytical approach (Grammarly analysis)
4. **Quantifiable Metrics**: Every project has measurable impact indicators
5. **Responsible AI Focus**: Explicit design choices favoring explainability over automation

### Professional Polish
- **No Errors**: Validated with `get_errors` tool - clean codebase
- **Smooth Navigation**: Crossfade transitions between pages
- **Responsive Design**: Works on mobile, tablet, and desktop
- **Performance**: Minimal dependencies, optimized CSS, fast load times
- **Accessibility**: ARIA labels, keyboard navigation, skip links

## 📝 Routes

| Route | Page | Description |
|-------|------|-------------|
| `/` | Home | Hero, About Me, Stats, Product Principles |
| `/projects` | Projects | Featured AI products with metrics |
| `/product-thinking` | Thinking | Real product decisions & tradeoffs |
| `/frameworks` | Frameworks | Product methodology & structured thinking |
| `/skills` | Skills | Technical capabilities & education |
| `/contact` | Contact | Professional contact information |

## 👤 About the Developer

**Anubhav Verma** - Product Manager specializing in AI-powered decision-support products

- 🎓 B.E. Chemical Engineering, BITS Pilani Goa
- 🚀 Shipped 2 AI products end-to-end (Product Playground, AI Interview Copilot)
- 🧠 Focused on explainable AI and responsible product design
- 📊 Trained in product frameworks (Duke AI PM, McKinsey Forward)

**Connect:**
- LinkedIn: [linkedin.com/in/anubhav-verma-746740250](https://www.linkedin.com/in/anubhav-verma-746740250/)
- GitHub: [github.com/anubhav-product](https://github.com/anubhav-product)
- Email: vermaanubhav28@gmail.com

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Design inspiration: Modern developer portfolios with focus on clarity over clutter
- Typography: [Google Fonts - Inter](https://fonts.google.com/specimen/Inter)
- Deployment: [Render.com](https://render.com) for seamless Python hosting
- Framework: [Flask](https://flask.palletsprojects.com/) for lightweight web development

---

**Built with care by Anubhav Verma** | [View Live Demo](https://portfolio-o5n7.onrender.com) | [Report Issues](https://github.com/anubhav-product/Portfolio/issues)