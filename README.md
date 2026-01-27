# Anubhav Verma - Product Manager Portfolio

> Professional multi-page portfolio showcasing AI product development, structured PM frameworks, and end-to-end product execution.

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://portfolio-o5n7.onrender.com)
[![GitHub](https://img.shields.io/badge/github-repository-blue)](https://github.com/anubhav-product/Portfolio)
[![LinkedIn](https://img.shields.io/badge/linkedin-connect-0077B5)](https://www.linkedin.com/in/anubhav-verma-746740250/)

## 🎯 Overview

This portfolio demonstrates full-stack product management through a modern, production-ready web application. It showcases the ability to ship complete products independently—from user research through technical implementation to live deployment.

**Key Highlights:**
- **2 AI Products Shipped 0-to-1**: Product Playground (strategy platform) & AI Interview Copilot (screening tool)
- **Framework-Driven Thinking**: Applied RICE, Jobs-to-be-Done, Problem Framing Canvas to own products
- **90% Time Reduction**: Reduced product decision analysis from 3 hours to 15 minutes
- **Validated with 25+ Users**: PMs, recruiters, job seekers across tech and consulting

## ✨ Features & Pages

### 🏠 **Home Page**
- Hero section with quantifiable impact metrics
- Comprehensive "About Me" with professional journey
- "Why Me Over Other PMs?" differentiation (4 key strengths)
- Animated statistics counter
- Product principles and current availability status

### 💼 **Projects Page**
- **Product Playground**: AI-powered product strategy platform (7+ frameworks, GPT-4o)
  - Impact: 90% time reduction (3hr → 15min)
  - Validation: 10+ PMs tested, 8/10 urgency score
  - Tech: Python, Flask, OpenAI GPT-4o, Render
  
- **AI Interview Copilot**: Explainable resume screening platform
  - Impact: 65% recruiter time savings, 100% explainability
  - Validation: 8 recruiters, 15 job seekers
  - Ethical design: No numeric scores, human-in-the-loop

- Customer validation boxes with testimonials
- Links to live demos, GitHub repos, and case studies

### 📖 **Case Studies** (Deep-Dive Analysis)
- **Product Playground Case Study**: Applied Problem Framing Canvas, RICE prioritization, Jobs-to-be-Done
  - Shows framework application to validate problem before building
  - RICE scores for 8 features → shipped top 3
  - Retrospective using own frameworks
  
- **AI Interview Copilot Case Study**: RICE + Trust framework, ethical design decisions
  - Rejected numeric scoring despite faster build (Trust: 3/10)
  - Shipped qualitative indicators (Trust: 9/10)
  - Documented pivot from automation to explainability

### 🧠 **Product Thinking Page**
- Real product decisions and tradeoffs
- Responsible AI design philosophy
- Decision-support vs. automation approach
- Feature scoping rationale with validation data

### 📐 **Frameworks Page**
- **Problem Framing Canvas**: 4-step validation framework
- **RICE + Trust**: Modified prioritization for AI products
- **Jobs-to-be-Done**: User research methodology
- **AI Product Decision Tree**: When to automate vs. augment
- Real application examples from my products

### 🎯 **Product Teardowns**
- In-depth analyses of 5 products: Grammarly, Notion, Linear, Miro, Loom
- Structure: Problem → What Works → Strategic Risks → Improvements
- Demonstrates analytical thinking across product types
- "Patterns Across Great Products" synthesis

### 🛠️ **Skills Page**
- Product Management (Strategy, Research, Frameworks)
- Technical Skills (Python, AI/ML, SQL, Cloud)
- Soft Skills & Leadership
- Work Experience & Projects with quantified impact

### 📧 **Contact Page**
- Professional contact information
- Resume download (PDF)
- Portfolio summary (print-friendly one-page version)
- "What I'm Looking For" section
- Immediate availability status

## 📱 Mobile-First Design

**Desktop Navigation:**
- Top navigation bar with all sections
- Floating resume download button (bottom-right)
- Scroll-to-top button

**Mobile Navigation:**
- Hamburger menu for full navigation
- **Bottom navigation bar** with 4 key sections (Home, Projects, Thinking, Contact)
- Icons + labels for intuitive navigation
- Active state highlighting
- Touch-optimized spacing and buttons

## 🚀 Tech Stack

**Backend:**
- Python 3.11
- Flask 3.1.0
- Gunicorn 21.2.0 (production WSGI server)

**Frontend:**
- HTML5 with Jinja2 templating
- CSS3 (custom design system, 2200+ lines)
- Vanilla JavaScript (no frameworks)
- Google Fonts (Inter)

**Features:**
- Smooth page transitions (0.3s crossfade)
- Scroll-triggered animations (IntersectionObserver API)
- Mobile bottom navigation bar
- Responsive grid layouts
- Dark theme with cyan accent (#00d9ff)

**Deployment:**
- **Platform**: Render.com
- **Live URL**: https://portfolio-o5n7.onrender.com
- **Auto-deploy**: Connected to GitHub main branch
- **Build**: `pip install -r requirements.txt`
- **Start**: `gunicorn app:app`

**SEO & Social:**
- OpenGraph meta tags with custom OG image (1200×630px)
- Twitter card support
- Structured metadata for LinkedIn sharing

## 📦 Installation & Setup

### Prerequisites
- Python 3.11+
- pip
- Git

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anubhav-product/Portfolio.git
   cd Portfolio
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run development server:**
   ```bash
   python app.py
   ```

5. **Open browser:**
   ```
   http://localhost:5000
   ```

### Production Deployment (Render)

1. Fork this repository to your GitHub
2. Sign up at [render.com](https://render.com)
3. Create new "Web Service" from GitHub repo
4. Render auto-detects `render.yaml`:
   - Python 3.11
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
5. Deploy (takes ~2-3 minutes)

## 📁 Project Structure

```
Portfolio/
├── app.py                          # Flask app with 9 routes
├── requirements.txt                # Python dependencies
├── render.yaml                     # Render deployment config
├── create_og_image.py             # OG image generator (Pillow)
├── README.md                       # This file
├── static/
│   ├── style.css                  # Main stylesheet (2200+ lines)
│   ├── og-image.png               # Social media preview image (1200×630)
│   └── resume/
│       └── resume.pdf             # Resume PDF
├── templates/
│   ├── base.html                  # Base template (nav, footer, mobile menu)
│   ├── home.html                  # Homepage
│   ├── projects.html              # Projects showcase
│   ├── case_study.html            # Product Playground case study
│   ├── case_study_copilot.html    # AI Copilot case study
│   ├── product_thinking.html      # Product philosophy
│   ├── frameworks.html            # PM frameworks
│   ├── teardowns.html             # Product analyses
│   ├── skills.html                # Skills & experience
│   ├── contact.html               # Contact information
│   └── portfolio-summary.html     # Print-friendly summary
└── __pycache__/                   # Python bytecode cache
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
- Staggered entrance animations

## 🌟 Key Differentiators

**1. Framework-Driven Product Thinking**
- Not just projects—shows *how* I think about product decisions
- Applied same frameworks (RICE, Jobs-to-be-Done, Problem Framing) to my own products
- Documented trade-offs and retrospectives

**2. Comprehensive Case Studies**
- Deep-dive analysis for both products
- Problem validation → Research → Solution → Results → Learnings
- Shows ability to reflect on own work

**3. Product Teardowns Library**
- Analytical thinking across 5 products (Grammarly, Notion, Linear, Miro, Loom)
- Demonstrates strategic thinking and market analysis
- Pattern recognition across different product types

**4. Mobile-First Experience**
- Bottom navigation bar for mobile (app-like UX)
- Hamburger menu for full navigation
- Optimized for touch interactions

**5. Full Technical Ownership**
- Designed, built, and deployed entire portfolio independently
- No templates or themes—custom CSS from scratch
- Production-ready with CI/CD pipeline

## 📊 Metrics & Impact

**Product Playground:**
- 🎯 90% time reduction (3 hours → 15 minutes)
- 👥 10+ active PM users in first month
- ⭐ 9/10 framework quality rating
- 💰 $29-49/month willingness-to-pay validated

**AI Interview Copilot:**
- ⚡ 65% recruiter screening time reduction
- 🤝 8/8 recruiter adoption rate
- 🎓 13/15 candidates found feedback actionable
- 🔍 9.2/10 explainability rating

## 🔗 Links

- **Live Portfolio**: https://portfolio-o5n7.onrender.com
- **GitHub**: https://github.com/anubhav-product/Portfolio
- **Product Playground**: https://productplayground-1.onrender.com
- **AI Interview Copilot**: https://anubhavproduct.pythonanywhere.com
- **LinkedIn**: https://www.linkedin.com/in/anubhav-verma-746740250

## 📝 License

This project is open source and available for learning purposes. Feel free to fork and adapt for your own portfolio.

## 🤝 Contact

**Anubhav Verma**
- Email: vermaanubhav28@gmail.com
- LinkedIn: [anubhav-verma-746740250](https://www.linkedin.com/in/anubhav-verma-746740250)
- GitHub: [@anubhav-product](https://github.com/anubhav-product)
- Portfolio: [portfolio-o5n7.onrender.com](https://portfolio-o5n7.onrender.com)

---

**Open to**: Product Manager, APM, AI Product Manager roles | **Status**: Immediate joiner | **Location**: Remote/Hybrid (India)

Built with ❤️ for clarity, not clutter.

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