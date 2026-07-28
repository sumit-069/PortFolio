"""
Sumit Kumar Bajpai — Interactive AI Portfolio
Single-file Streamlit app with all pages built inline.
"""

import json
import base64
from pathlib import Path
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# ─────────────────────────────────────────────
#  PAGE CONFIG  (called ONCE at the top)
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Sumit Kumar Bajpai | AI Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  PATHS
# ─────────────────────────────────────────────
ROOT   = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
CSS    = ROOT / "css" / "style.css"
DATA   = ROOT / "data" / "project.json"


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def load_css() -> None:
    if CSS.exists():
        st.markdown(f"<style>{CSS.read_text(encoding='utf-8')}</style>",
                    unsafe_allow_html=True)


def asset(filename: str) -> Path:
    return ASSETS / filename


def show_image(filename: str, caption: str | None = None, width: bool = True):
    img = asset(filename)
    if img.exists():
        st.image(str(img), caption=caption, use_container_width=width)
    else:
        st.markdown(
            f"""<div style="background:rgba(99,102,241,0.1);border:1px dashed rgba(99,102,241,0.3);
            border-radius:12px;padding:3rem;text-align:center;color:#6366F1;font-weight:600;">
            📷 {filename}</div>""",
            unsafe_allow_html=True,
        )


def load_data() -> dict:
    if DATA.exists():
        with open(DATA, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"owner": {}, "projects": []}


def html(content: str) -> None:
    st.markdown(content, unsafe_allow_html=True)


def section_header(title: str, subtitle: str = "") -> None:
    html(f"""
    <div style="text-align:center;margin-bottom:2.5rem;animation:fadeInUp 0.6s ease-out;">
        <h2 style="font-size:2rem;font-weight:800;color:#F8FAFC;margin-bottom:0.4rem;">{title}</h2>
        {'<p style="color:#64748B;font-size:1rem;margin:0;">' + subtitle + '</p>' if subtitle else ''}
    </div>
    """)


def stat_card(number: str, label: str, icon: str = "") -> None:
    html(f"""
    <div class="stat-card">
        <div style="font-size:2rem;margin-bottom:0.2rem;">{icon}</div>
        <div class="stat-number">{number}</div>
        <div class="stat-label">{label}</div>
    </div>
    """)


def skill_badge(name: str, icon: str = "✦") -> str:
    return f'<span class="skill-badge">{icon} {name}</span>'


# ─────────────────────────────────────────────
#  LOAD CSS & DATA
# ─────────────────────────────────────────────
load_css()
data    = load_data()
owner   = data.get("owner", {})
projects = data.get("projects", [])

# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    html("""
    <div class="sidebar-profile">
        <div style="font-size:2.5rem;margin-bottom:0.4rem;">🤖</div>
        <div style="font-size:1.1rem;font-weight:700;color:#F8FAFC;">Sumit Kumar Bajpai</div>
        <div style="font-size:0.78rem;color:#6366F1;font-weight:600;margin-top:0.3rem;">AI Engineer</div>
    </div>
    """)

    page = st.radio(
        "Navigation",
        options=[
            "🏠 Home",
            "👨 About",
            "🚀 Projects",
            "💻 Skills",
            "📄 Resume",
            "📬 Contact",
        ],
        label_visibility="collapsed",
    )

    st.divider()

    html("""
    <div style="text-align:center;padding:0.5rem;">
        <div style="font-size:0.75rem;color:#475569;margin-bottom:0.8rem;">CONNECT</div>
    </div>
    """)
    st.link_button("🐙 GitHub",   owner.get("github",   "https://github.com/sumit-069"),   use_container_width=True)
    st.link_button("💼 LinkedIn", owner.get("linkedin", "https://linkedin.com/"),           use_container_width=True)
    st.link_button("💻 LeetCode", owner.get("leetcode", "https://leetcode.com/"),           use_container_width=True)

    st.divider()
    html('<p style="text-align:center;font-size:0.72rem;color:#334155;">Made with ❤️ using Streamlit</p>')


# ═══════════════════════════════════════════════════════════
#  PAGE: HOME
# ═══════════════════════════════════════════════════════════
if page == "🏠 Home":

    # Hero
    html("""
    <div class="hero-section">
        <div class="glow-badge">🟢 Available for AI/ML Internships</div>
        <h1 style="font-size:3rem;font-weight:900;margin:0.5rem 0;">
            Hi, I'm <span class="gradient-text">Sumit Kumar Bajpai</span> 👋
        </h1>
        <h2 style="font-size:1.4rem;font-weight:500;color:#94A3B8;margin:0.5rem 0 1.5rem;">
            AI Engineer · Machine Learning · Computer Vision · Agentic AI
        </h2>
        <p style="font-size:1.1rem;color:#94A3B8;max-width:600px;line-height:1.8;">
            I build intelligent AI-powered applications using <strong style="color:#6366F1;">Python</strong>,
            <strong style="color:#8B5CF6;">LangGraph</strong>,
            <strong style="color:#06B6D4;">FastAPI</strong>, TensorFlow and Streamlit.
            Welcome to my interactive portfolio!
        </p>
    </div>
    """)

    # CTA Buttons
    btn1, btn2, btn3, _ = st.columns([1, 1, 1, 3])
    with btn1:
        st.link_button("🚀 View Projects", "#", use_container_width=True)
    with btn2:
        resume_path = asset("resume.pdf")
        if resume_path.exists():
            with open(resume_path, "rb") as f:
                st.download_button(
                    "📄 Download Resume",
                    f,
                    file_name="Sumit_Kumar_Bajpai_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
        else:
            st.button("📄 Resume", disabled=True, use_container_width=True)
    with btn3:
        st.link_button("📬 Contact Me", "#", use_container_width=True)

    st.divider()

    # Quick Stats
    section_header("📊 Quick Stats", "A snapshot of my journey so far")
    c1, c2, c3, c4 = st.columns(4)
    with c1: stat_card(f"{len(projects)}", "AI Projects",    "🚀")
    with c2: stat_card("8.7",  "CGPA / 10",      "🎓")
    with c3: stat_card("20+",  "Tech Stack",      "💻")
    with c4: stat_card("4",    "Languages",       "🌐")

    st.divider()

    # Featured Projects
    section_header("⭐ Featured Projects", "My most impactful AI builds")

    displayed = projects if projects else []
    if not displayed:
        st.info("Add projects to data/project.json")
    else:
        for i, proj in enumerate(displayed):
            with st.container():
                left_col, right_col = st.columns([1, 2], gap="large")
                with left_col:
                    show_image(Path(proj.get("image", "")).name)
                with right_col:
                    html(f"""
                    <div style="animation:slideInRight 0.5s ease-out;">
                        <div style="font-size:0.78rem;color:#06B6D4;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:0.4rem;">
                            {proj.get('subtitle', '')}
                        </div>
                        <h3 style="font-size:1.6rem;font-weight:800;color:#F8FAFC;margin:0 0 0.8rem;">{proj['title']}</h3>
                        <p style="color:#94A3B8;line-height:1.8;margin-bottom:1rem;">{proj['description']}</p>
                    </div>
                    """)

                    # Tech stack badges
                    badges = " ".join(skill_badge(t) for t in proj.get("tech_stack", [])[:6])
                    html(f'<div style="margin-bottom:1rem;">{badges}</div>')

                    b1, b2 = st.columns(2)
                    with b1:
                        gh = proj.get("github", "")
                        if gh:
                            st.link_button("💻 GitHub", gh, use_container_width=True)
                    with b2:
                        dm = proj.get("demo", "")
                        if dm:
                            st.link_button("🌐 Live Demo", dm, use_container_width=True)
                st.divider()

    # Current Focus
    section_header("🔥 Current Focus")
    f1, f2, f3 = st.columns(3)
    focuses = [
        ("🤖", "Agentic AI", "Building autonomous AI systems with LangGraph multi-agent pipelines."),
        ("🧠", "LLM Applications", "Developing intelligent assistants powered by modern LLMs (Groq, Gemini, OpenAI)."),
        ("⚡", "AI Software Engineering", "Creating tools that automate software development workflows end-to-end."),
    ]
    for col, (icon, title, desc) in zip([f1, f2, f3], focuses):
        with col:
            html(f"""
            <div class="glass-card" style="text-align:center;height:100%;">
                <div style="font-size:2.5rem;margin-bottom:0.8rem;">{icon}</div>
                <h3 style="color:#F8FAFC;margin-bottom:0.6rem;">{title}</h3>
                <p style="color:#94A3B8;font-size:0.9rem;line-height:1.7;">{desc}</p>
            </div>
            """)


# ═══════════════════════════════════════════════════════════
#  PAGE: ABOUT
# ═══════════════════════════════════════════════════════════
elif page == "👨 About":
    section_header("👨 About Me", "The story behind the code")

    left, right = st.columns([3, 2], gap="large")

    with left:
        html(f"""
        <div class="glass-card" style="margin-bottom:1.5rem;">
            <h2 style="font-size:1.8rem;font-weight:800;color:#F8FAFC;margin-bottom:0.3rem;">
                {owner.get('name', 'Sumit Kumar Bajpai')}
            </h2>
            <div style="font-size:0.9rem;color:#6366F1;font-weight:600;margin-bottom:1.2rem;">
                {owner.get('title', 'AI Engineer | Machine Learning | Agentic AI | Computer Vision')}
            </div>
            <p style="color:#94A3B8;line-height:1.9;font-size:1rem;">
                I am a <strong style="color:#F8FAFC;">Computer Science undergraduate</strong> passionate
                about building AI-powered software using <strong style="color:#6366F1;">Machine Learning</strong>,
                <strong style="color:#8B5CF6;">Computer Vision</strong>,
                <strong style="color:#06B6D4;">Large Language Models (LLMs)</strong> and
                <strong style="color:#EC4899;">Agentic AI</strong>.
            </p>
            <p style="color:#94A3B8;line-height:1.9;font-size:1rem;margin-top:0.8rem;">
                My goal is to build intelligent systems that automate software development,
                improve developer productivity, and solve real-world problems through AI.
            </p>
            <p style="color:#94A3B8;line-height:1.9;font-size:1rem;margin-top:0.8rem;">
                I enjoy designing AI agents, developing end-to-end ML applications,
                and deploying production-ready Python solutions.
            </p>
        </div>
        """)

        # Education
        html("""
        <div class="glass-card">
            <div style="font-size:1.3rem;font-weight:800;color:#F8FAFC;margin-bottom:1rem;">🎓 Education</div>
            <div style="display:flex;align-items:flex-start;gap:1rem;">
                <div style="font-size:2rem;">🏫</div>
                <div>
                    <div style="font-weight:700;color:#F8FAFC;font-size:1rem;">Kamla Nehru Institute of Technology</div>
                    <div style="color:#6366F1;font-size:0.85rem;font-weight:600;margin:0.2rem 0;">Sultanpur, Uttar Pradesh</div>
                    <div style="color:#94A3B8;font-size:0.9rem;">B.Tech — Computer Science & Engineering</div>
                    <div style="margin-top:0.6rem;">
                        <span style="background:rgba(99,102,241,0.15);border:1px solid rgba(99,102,241,0.3);
                        border-radius:100px;padding:0.2rem 0.8rem;font-size:0.8rem;color:#6366F1;font-weight:700;">
                            CGPA: 8.7 / 10
                        </span>
                    </div>
                </div>
            </div>
        </div>
        """)

    with right:
        show_image("profile.png")

        # Quick Info
        html("""
        <div class="glass-card" style="margin-top:1rem;">
            <div style="font-size:1rem;font-weight:700;color:#F8FAFC;margin-bottom:1rem;">📌 Quick Info</div>
            <div style="display:flex;flex-direction:column;gap:0.7rem;">
                <div style="display:flex;gap:0.8rem;align-items:center;">
                    <span style="font-size:1.2rem;">📍</span>
                    <span style="color:#94A3B8;font-size:0.9rem;">Uttar Pradesh, India</span>
                </div>
                <div style="display:flex;gap:0.8rem;align-items:center;">
                    <span style="font-size:1.2rem;">🌐</span>
                    <span style="color:#94A3B8;font-size:0.9rem;">English, Hindi</span>
                </div>
                <div style="display:flex;gap:0.8rem;align-items:center;">
                    <span style="font-size:1.2rem;">💼</span>
                    <span style="color:#6366F1;font-size:0.9rem;font-weight:600;">Open to AI/ML Internships</span>
                </div>
                <div style="display:flex;gap:0.8rem;align-items:center;">
                    <span style="font-size:1.2rem;">📧</span>
                    <span style="color:#94A3B8;font-size:0.9rem;">bsushil435@gmail.com</span>
                </div>
            </div>
        </div>
        """)

    st.divider()

    # Areas of Interest
    section_header("💡 Areas of Interest")
    interests = [
        ("🤖", "Agentic AI", "Building autonomous multi-agent systems"),
        ("🧠", "Machine Learning", "Supervised, unsupervised & reinforcement learning"),
        ("👁️", "Computer Vision", "OpenCV, image processing, object detection"),
        ("🔗", "Large Language Models", "RAG, fine-tuning, prompt engineering"),
        ("⚡", "Backend Development", "FastAPI, REST APIs, microservices"),
        ("📊", "Deep Learning", "Neural networks, TensorFlow, Keras"),
    ]
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(interests):
        with cols[i % 3]:
            html(f"""
            <div class="glass-card" style="text-align:center;margin-bottom:1rem;padding:1.2rem;">
                <div style="font-size:2rem;margin-bottom:0.5rem;">{icon}</div>
                <div style="font-weight:700;color:#F8FAFC;font-size:0.95rem;margin-bottom:0.3rem;">{title}</div>
                <div style="color:#64748B;font-size:0.82rem;">{desc}</div>
            </div>
            """)

    st.divider()

    # Learning Journey Timeline
    section_header("📈 Learning Journey", "From zero to AI engineer")

    journey = [
        ("2024", "🐍", "Started Programming", "Began with Python, DSA, and competitive programming."),
        ("2024", "📐", "Data Structures & Algorithms", "Mastered arrays, trees, graphs, and dynamic programming."),
        ("2025", "🤖", "Machine Learning", "Learned supervised/unsupervised ML with Scikit-learn."),
        ("2025", "🧠", "Deep Learning", "Built neural networks with TensorFlow and Keras."),
        ("2025", "👁️", "Computer Vision", "Developed video analysis and signal processing projects."),
        ("2026", "🔗", "LangGraph & LLM Applications", "Built AI agents and published CLI tools on PyPI."),
        ("Now",  "🚀", "AI Software Engineering", "Developing full-stack AI platforms for software automation."),
    ]

    for year, icon, event, detail in journey:
        html(f"""
        <div class="timeline-card">
            <div class="timeline-year">{icon} {year}</div>
            <div class="timeline-event">{event}</div>
            <div style="color:#64748B;font-size:0.85rem;margin-top:0.3rem;">{detail}</div>
        </div>
        """)


# ═══════════════════════════════════════════════════════════
#  PAGE: PROJECTS
# ═══════════════════════════════════════════════════════════
elif page == "🚀 Projects":
    section_header("🚀 Featured Projects", "AI and Machine Learning builds that solve real problems")

    if not projects:
        st.info("Add projects to data/project.json")
    else:
        # Filter by tech
        all_techs = sorted({t for p in projects for t in p.get("tech_stack", [])})
        selected_tech = st.selectbox(
            "🔍 Filter by Technology",
            options=["All Technologies"] + all_techs,
            key="tech_filter",
        )

        filtered = projects if selected_tech == "All Technologies" else [
            p for p in projects if selected_tech in p.get("tech_stack", [])
        ]

        html(f'<div style="color:#64748B;font-size:0.85rem;margin-bottom:1.5rem;">Showing {len(filtered)} project(s)</div>')

        for proj in filtered:
            with st.container():
                c_img, c_info = st.columns([1, 2], gap="large")

                with c_img:
                    img_name = Path(proj.get("image", "")).name
                    show_image(img_name)

                    status = proj.get("status", "")
                    if status:
                        color = "#10B981" if status == "Completed" else "#F59E0B"
                        html(f"""
                        <div style="text-align:center;margin-top:0.8rem;">
                            <span style="background:rgba(16,185,129,0.1);border:1px solid {color};
                            border-radius:100px;padding:0.2rem 0.8rem;font-size:0.8rem;color:{color};font-weight:700;">
                                ● {status}
                            </span>
                        </div>
                        """)

                with c_info:
                    html(f"""
                    <div style="font-size:0.78rem;color:#06B6D4;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:0.4rem;">
                        {proj.get('subtitle', '')}
                    </div>
                    <h2 style="font-size:1.8rem;font-weight:800;color:#F8FAFC;margin:0 0 0.8rem;">{proj['title']}</h2>
                    <p style="color:#94A3B8;line-height:1.8;margin-bottom:1.2rem;">{proj['description']}</p>
                    """)

                    # Tech Stack
                    st.markdown("**🛠 Tech Stack**")
                    badges = " ".join(skill_badge(t) for t in proj.get("tech_stack", []))
                    html(f'<div style="margin:0.5rem 0 1rem;">{badges}</div>')

                    # Features
                    features = proj.get("features", [])
                    if features:
                        with st.expander("✨ View Features"):
                            for f in features:
                                html(f'<div style="padding:0.3rem 0;color:#94A3B8;">✓ &nbsp;{f}</div>')

                    # Metrics
                    metrics = proj.get("metrics", {})
                    if metrics:
                        st.markdown("**📊 Metrics**")
                        mcols = st.columns(len(metrics))
                        for idx, (k, v) in enumerate(metrics.items()):
                            mcols[idx].metric(k, v)

                    # Buttons
                    bb1, bb2, bb3 = st.columns(3)
                    with bb1:
                        gh = proj.get("github", "")
                        if gh:
                            st.link_button("💻 GitHub", gh, use_container_width=True)
                    with bb2:
                        dm = proj.get("demo", "")
                        if dm:
                            st.link_button("🌐 Live Demo", dm, use_container_width=True)
                        else:
                            st.button("🌐 Demo", disabled=True, key=f"demo_{proj['id']}", use_container_width=True)
                    with bb3:
                        dc = proj.get("documentation", "")
                        if dc:
                            st.link_button("📚 Docs", dc, use_container_width=True)
                        else:
                            st.button("📚 Docs", disabled=True, key=f"docs_{proj['id']}", use_container_width=True)

            st.divider()

    # Other Repositories Section
    section_header("📂 Other Open-Source Repositories", "Additional tools, web apps, and experiments on GitHub")
    
    other_repos = [
        {
            "name": "Multi-Disease-prediction-app",
            "desc": "A Machine Learning powered Streamlit web app for predicting Diabetes, Breast Cancer, and Heart Disease using classification models.",
            "tech": ["Python", "Machine Learning", "Streamlit", "Scikit-Learn"],
            "url": "https://github.com/sumit-069/Multi-Disease-prediction-app"
        },
        {
            "name": "green-cycle-rewards",
            "desc": "An eco-friendly TypeScript web application providing token rewards for sustainable cycling behaviors.",
            "tech": ["TypeScript", "React", "Node.js", "Web3"],
            "url": "https://github.com/sumit-069/green-cycle-rewards"
        },
        {
            "name": "fwi-prediction-app1",
            "desc": "A Forest Fire Weather Index (FWI) prediction app utilizing weather parameters to evaluate fire danger indices.",
            "tech": ["Python", "Flask", "Machine Learning", "HTML/CSS"],
            "url": "https://github.com/sumit-069/fwi-prediction-app1"
        },
        {
            "name": "docs",
            "desc": "A comprehensive personal archive and reference documentation setup for unified LangChain and LangGraph patterns.",
            "tech": ["Markdown", "LangChain", "Documentation"],
            "url": "https://github.com/sumit-069/docs"
        }
    ]
    
    r1, r2 = st.columns(2)
    for idx, repo in enumerate(other_repos):
        col = r1 if idx % 2 == 0 else r2
        with col:
            html(f"""
            <div class="glass-card" style="margin-bottom:1.5rem; min-height: 200px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h4 style="color:#06B6D4; margin:0 0 0.5rem 0;">📁 {repo['name']}</h4>
                    <p style="color:#94A3B8; font-size:0.88rem; line-height:1.6; margin-bottom:1rem;">{repo['desc']}</p>
                </div>
            """)
            # Tech badges
            badges = " ".join(f'<span class="skill-badge" style="font-size:0.75rem; padding:0.2rem 0.6rem;">{t}</span>' for t in repo['tech'])
            html(f'<div style="margin-bottom:1rem;">{badges}</div>')
            st.link_button("⭐ View Code", repo['url'], use_container_width=True)
            html("</div>")
            
    st.divider()

    # Current Focus
    section_header("🔥 Current Focus")
    f1, f2, f3 = st.columns(3)
    focuses = [
        ("🤖", "Agentic AI",           "Building autonomous AI systems using LangGraph."),
        ("🧠", "LLM Applications",     "Developing intelligent assistants powered by modern LLMs."),
        ("⚡", "AI Software Engineering","Creating tools that automate software development workflows."),
    ]
    for col, (icon, title, desc) in zip([f1, f2, f3], focuses):
        with col:
            html(f"""
            <div class="glass-card" style="text-align:center;">
                <div style="font-size:2.5rem;margin-bottom:0.7rem;">{icon}</div>
                <h3 style="color:#F8FAFC;">{title}</h3>
                <p style="color:#94A3B8;font-size:0.9rem;">{desc}</p>
            </div>
            """)


# ═══════════════════════════════════════════════════════════
#  PAGE: SKILLS
# ═══════════════════════════════════════════════════════════
elif page == "💻 Skills":
    section_header("💻 Skills & Technologies", "Technologies and tools I use to build AI applications")

    # Tab layout
    tab1, tab2, tab3 = st.tabs(["📊 Proficiency Chart", "🏷 Skill Badges", "📈 Roadmap"])

    with tab1:
        # Interactive Radar + Bar charts
        skills_data = {
            "Python":            95,
            "LangGraph":         90,
            "Machine Learning":  90,
            "TensorFlow":        88,
            "LangChain":         88,
            "OpenCV":            85,
            "FastAPI":           85,
            "Streamlit":         85,
            "Scikit-learn":      90,
            "Prompt Engineering":85,
            "NumPy / Pandas":    90,
            "SQL":               75,
            "C++":               80,
            "Git":               85,
        }

        col_chart, col_bar = st.columns([1, 1], gap="large")

        with col_chart:
            st.markdown("#### 🕸 Radar Chart")
            categories = list(skills_data.keys())[:8]
            values     = [skills_data[c] for c in categories]
            values.append(values[0])
            categories.append(categories[0])

            fig_radar = go.Figure(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                fillcolor='rgba(99,102,241,0.2)',
                line=dict(color='#6366F1', width=2),
                marker=dict(size=6, color='#8B5CF6'),
            ))
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, 100],
                                    gridcolor='rgba(255,255,255,0.05)',
                                    linecolor='rgba(255,255,255,0.05)',
                                    tickfont=dict(color='#64748B', size=10)),
                    angularaxis=dict(gridcolor='rgba(255,255,255,0.05)',
                                     linecolor='rgba(255,255,255,0.05)',
                                     tickfont=dict(color='#94A3B8', size=11)),
                    bgcolor='rgba(0,0,0,0)',
                ),
                showlegend=False,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(t=20, b=20, l=20, r=20),
                height=420,
            )
            st.plotly_chart(fig_radar, use_container_width=True)

        with col_bar:
            st.markdown("#### 📊 Proficiency Levels")
            sorted_skills = dict(sorted(skills_data.items(), key=lambda x: x[1], reverse=True))

            fig_bar = go.Figure(go.Bar(
                x=list(sorted_skills.values()),
                y=list(sorted_skills.keys()),
                orientation='h',
                marker=dict(
                    color=list(sorted_skills.values()),
                    colorscale=[[0, '#8B5CF6'], [0.5, '#6366F1'], [1, '#06B6D4']],
                    line=dict(color='rgba(0,0,0,0)', width=0),
                ),
                text=[f"{v}%" for v in sorted_skills.values()],
                textposition='inside',
                textfont=dict(color='white', size=11, family='Inter'),
            ))
            fig_bar.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(range=[0, 100], showgrid=False, showticklabels=False,
                           zeroline=False),
                yaxis=dict(showgrid=False, tickfont=dict(color='#94A3B8', size=11),
                           linecolor='rgba(255,255,255,0.05)'),
                margin=dict(t=20, b=20, l=10, r=20),
                height=420,
            )
            st.plotly_chart(fig_bar, use_container_width=True)

    with tab2:
        categories_map = {
            "👨‍💻 Programming Languages": [
                ("Python", "🐍"), ("C++", "⚡"), ("Java", "☕"),
                ("SQL", "🗄️"), ("C", "🔧"), ("JavaScript", "🌐"),
            ],
            "🤖 Machine Learning & AI": [
                ("Scikit-learn", "🔬"), ("TensorFlow", "🔥"), ("Keras", "🧠"),
                ("XGBoost", "📈"), ("OpenCV", "👁️"), ("NumPy", "📊"),
                ("Pandas", "🐼"), ("Matplotlib", "📉"), ("SciPy", "⚗️"),
            ],
            "🧠 LLM & Agentic AI": [
                ("LangGraph", "🕸"), ("LangChain", "🔗"), ("Prompt Engineering", "💬"),
                ("RAG", "📚"), ("OpenAI", "🤖"), ("Gemini", "✨"),
                ("Groq", "⚡"),
            ],
            "⚡ Backend & Tools": [
                ("FastAPI", "🚀"), ("Streamlit", "🖥️"), ("Typer", "🖊️"),
                ("Git", "🐙"), ("VS Code", "📝"), ("Jupyter", "📓"),
                ("PyPI", "📦"), ("Google Colab", "☁️"),
            ],
        }

        for cat, items in categories_map.items():
            st.markdown(f"### {cat}")
            badges_html = " ".join(skill_badge(name, icon) for name, icon in items)
            html(f'<div style="margin-bottom:1.5rem;line-height:2.5;">{badges_html}</div>')
            st.divider()

    with tab3:
        st.markdown("### 📈 Learning Roadmap")
        html('<p style="color:#64748B;margin-bottom:1.5rem;">Skills I am currently mastering and planning to learn.</p>')

        roadmap_items = [
            ("✅", "Advanced LangGraph",        True,  "Building complex multi-agent architectures"),
            ("✅", "FastAPI + Async",            True,  "Production-ready async API development"),
            ("🔄", "MLOps & Model Deployment",  False, "Deploying ML models to production with CI/CD"),
            ("🔄", "AWS / Cloud Infrastructure",False, "Scalable cloud deployments for AI apps"),
            ("🎯", "Kubernetes & Docker",        False, "Container orchestration for microservices"),
            ("🎯", "Distributed AI Systems",     False, "Building scalable multi-node AI pipelines"),
            ("🎯", "Reinforcement Learning",     False, "Advanced RL algorithms and environments"),
        ]

        for icon, skill, done, desc in roadmap_items:
            color = "#10B981" if done else "#6366F1" if icon == "🔄" else "#475569"
            bg    = "rgba(16,185,129,0.08)" if done else "rgba(99,102,241,0.05)"
            border= "#10B981" if done else "rgba(99,102,241,0.2)" if icon == "🔄" else "rgba(255,255,255,0.06)"
            html(f"""
            <div style="background:{bg};border:1px solid {border};border-radius:12px;
                 padding:1rem 1.5rem;margin-bottom:0.8rem;display:flex;align-items:center;gap:1rem;">
                <span style="font-size:1.5rem;">{icon}</span>
                <div style="flex:1;">
                    <div style="font-weight:700;color:#F8FAFC;font-size:0.95rem;">{skill}</div>
                    <div style="color:#64748B;font-size:0.82rem;margin-top:0.2rem;">{desc}</div>
                </div>
                <span style="font-size:0.78rem;font-weight:700;color:{color};
                     background:rgba(255,255,255,0.05);border-radius:100px;padding:0.2rem 0.7rem;">
                    {'Done' if done else 'In Progress' if icon == '🔄' else 'Planned'}
                </span>
            </div>
            """)


# ═══════════════════════════════════════════════════════════
#  PAGE: RESUME
# ═══════════════════════════════════════════════════════════
elif page == "📄 Resume":
    section_header("📄 Resume", "Preview and download my latest resume")

    left, right = st.columns([2, 1], gap="large")

    with left:
        html("""
        <div class="glass-card">
            <h3 style="color:#F8FAFC;margin-bottom:1.2rem;">🎯 Professional Summary</h3>
            <div style="display:flex;flex-direction:column;gap:0.8rem;">
        """)

        summary_items = [
            ("🤖", "AI Engineer", "Building production AI systems with LangGraph & LLMs"),
            ("👁️", "Computer Vision Dev", "Signal processing, PPG analysis, OpenCV"),
            ("⚡", "FastAPI Developer", "RESTful APIs, async backends, microservices"),
            ("🐍", "Python Expert", "Strong foundation in Python for data science & backend"),
            ("📦", "Open Source", "Published packages on PyPI (Annukriti CLI)"),
        ]

        for icon, role, detail in summary_items:
            html(f"""
            <div style="display:flex;align-items:flex-start;gap:1rem;padding:0.8rem;
                 background:rgba(255,255,255,0.03);border-radius:10px;">
                <span style="font-size:1.4rem;">{icon}</span>
                <div>
                    <div style="font-weight:700;color:#F8FAFC;font-size:0.95rem;">{role}</div>
                    <div style="color:#64748B;font-size:0.85rem;margin-top:0.2rem;">{detail}</div>
                </div>
            </div>
            """)

        html("</div></div>")

    with right:
        html("""
        <div class="glass-card" style="text-align:center;">
            <div style="font-size:4rem;margin-bottom:1rem;">📄</div>
            <h3 style="color:#F8FAFC;margin-bottom:0.5rem;">Resume</h3>
            <p style="color:#64748B;font-size:0.9rem;margin-bottom:1.5rem;">
                Download my latest resume in PDF format
            </p>
        """)

        resume_path = asset("resume.pdf")
        if resume_path.exists():
            with open(resume_path, "rb") as f:
                st.download_button(
                    "📥 Download Resume",
                    f,
                    file_name="Sumit_Kumar_Bajpai_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
        else:
            st.warning("⚠️ Place resume.pdf inside the assets/ folder")

        html("</div>")

    st.divider()

    # Resume Preview
    st.subheader("📑 Resume Preview")

    resume_path = asset("resume.pdf")
    if resume_path.exists():
        with open(resume_path, "rb") as pdf:
            pdf_bytes = pdf.read()
        pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")
        html(f"""
        <iframe
            src="data:application/pdf;base64,{pdf_b64}"
            width="100%"
            height="900"
            type="application/pdf"
            style="border:1px solid rgba(255,255,255,0.08);border-radius:16px;margin-top:1rem;">
        </iframe>
        """)
    else:
        html("""
        <div style="background:rgba(99,102,241,0.05);border:1px dashed rgba(99,102,241,0.3);
             border-radius:16px;padding:5rem;text-align:center;">
            <div style="font-size:3rem;margin-bottom:1rem;">📄</div>
            <div style="color:#6366F1;font-weight:600;font-size:1.1rem;">
                Place your <code>resume.pdf</code> inside the <code>assets/</code> folder
            </div>
            <div style="color:#475569;font-size:0.9rem;margin-top:0.5rem;">
                The PDF preview will appear here automatically.
            </div>
        </div>
        """)

    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("Education",  "B.Tech CSE")
    c2.metric("CGPA",       "8.7 / 10")
    c3.metric("AI Projects", f"{len(projects)}")


# ═══════════════════════════════════════════════════════════
#  PAGE: CONTACT
# ═══════════════════════════════════════════════════════════
elif page == "📬 Contact":
    section_header("📬 Contact Me", "Let's connect and build something amazing together!")

    left, right = st.columns([3, 2], gap="large")

    with left:
        html("""
        <div class="glass-card" style="margin-bottom:1rem;">
            <h3 style="color:#F8FAFC;margin-bottom:1.5rem;">✉️ Send a Message</h3>
        """)

        with st.form("contact_form", clear_on_submit=True):
            col_n, col_e = st.columns(2)
            with col_n:
                name = st.text_input("Your Name *", placeholder="John Doe")
            with col_e:
                email = st.text_input("Your Email *", placeholder="john@example.com")

            subject = st.text_input("Subject *", placeholder="Project Collaboration / Internship Opportunity")
            message = st.text_area(
                "Message *",
                placeholder="Write your message here...",
                height=180,
            )

            col_s, col_clear = st.columns([2, 1])
            with col_s:
                submitted = st.form_submit_button(
                    "🚀 Send Message",
                    use_container_width=True,
                    type="primary",
                )

            if submitted:
                if not name.strip():
                    st.error("⚠️ Please enter your name.")
                elif not email.strip() or "@" not in email:
                    st.error("⚠️ Please enter a valid email address.")
                elif not subject.strip():
                    st.error("⚠️ Please enter a subject.")
                elif not message.strip():
                    st.error("⚠️ Please enter your message.")
                else:
                    st.success(
                        f"✅ Thank you {name}! Your message has been received. "
                        "I'll get back to you at **" + email + "** soon. "
                        "(To enable actual email delivery, integrate with FormSubmit, EmailJS, or Supabase.)"
                    )
                    st.balloons()

        html("</div>")

    with right:
        html('<h3 style="color:#F8FAFC;margin-bottom:1.2rem;">👨‍💻 Contact Information</h3>')

        contact_items = [
            ("📧", "Email",        "bsushil435@gmail.com",      "#6366F1"),
            ("📍", "Location",     "Uttar Pradesh, India",       "#8B5CF6"),
            ("💼", "Availability", "Open to AI/ML Internships",  "#10B981"),
            ("🕐", "Response Time","Within 24-48 hours",         "#06B6D4"),
        ]

        for icon, label, value, color in contact_items:
            html(f"""
            <div class="contact-info-card">
                <span style="font-size:1.5rem;">{icon}</span>
                <div>
                    <div style="font-size:0.75rem;color:#64748B;font-weight:700;text-transform:uppercase;letter-spacing:0.05em;">{label}</div>
                    <div style="font-size:0.95rem;color:{color};font-weight:600;margin-top:0.1rem;">{value}</div>
                </div>
            </div>
            """)

        html('<h3 style="color:#F8FAFC;margin:1.5rem 0 1rem;">🌐 Social Profiles</h3>')

        socials = [
            ("🐙 GitHub",   owner.get("github",   "https://github.com/sumit-069")),
            ("💼 LinkedIn", owner.get("linkedin", "https://www.linkedin.com/in/sumit-kumar-bajpai-8ab2452bb/")),
            ("💻 LeetCode", owner.get("leetcode", "https://leetcode.com/")),
            ("🏆 CodeChef", owner.get("codechef", "https://www.codechef.com/")),
        ]

        for label, url in socials:
            st.link_button(label, url, use_container_width=True)

    st.divider()

    # Why Work With Me
    section_header("🤝 Why Work With Me?")
    w1, w2, w3, w4 = st.columns(4)
    why_items = [
        ("🚀", f"{len(projects)} AI Projects", "Hands-on experience building end-to-end AI products"),
        ("🐍", "Python Expert",  "Strong foundation in Python for ML and backend dev"),
        ("📦", "Open Source",    "Published on PyPI, contributes to open source"),
        ("🎯", "Agentic AI",     "Specializing in LangGraph multi-agent systems"),
    ]
    for col, (icon, title, desc) in zip([w1, w2, w3, w4], why_items):
        with col:
            html(f"""
            <div class="glass-card" style="text-align:center;padding:1.2rem;">
                <div style="font-size:2rem;margin-bottom:0.6rem;">{icon}</div>
                <div style="font-weight:700;color:#F8FAFC;font-size:0.9rem;margin-bottom:0.4rem;">{title}</div>
                <div style="color:#64748B;font-size:0.8rem;">{desc}</div>
            </div>
            """)

    html("""
    <div style="text-align:center;margin-top:3rem;padding:2rem;
         background:linear-gradient(135deg,rgba(99,102,241,0.1),rgba(139,92,246,0.08));
         border:1px solid rgba(99,102,241,0.2);border-radius:20px;">
        <p style="color:#94A3B8;font-size:1rem;margin:0;">
            Made with <span style="color:#EC4899;">❤️</span> using
            <strong style="color:#6366F1;">Python</strong> &
            <strong style="color:#8B5CF6;">Streamlit</strong>
        </p>
    </div>
    """)
