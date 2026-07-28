
from pathlib import Path
from typing import Optional
import base64
import streamlit as st


ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
CSS = ROOT / "css" / "style.css"


def load_css() -> None:
    """Load custom CSS if available."""
    if CSS.exists():
        st.markdown(f"<style>{CSS.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def asset_path(filename: str) -> Path:
    """Return full path to an asset."""
    return ASSETS / filename


def show_image(filename: str, caption: Optional[str] = None, width: bool = True) -> None:
    """Display an image if it exists."""
    img = asset_path(filename)
    if img.exists():
        st.image(str(img), caption=caption, use_container_width=width)
    else:
        st.warning(f"Missing asset: {filename}")


def resume_download_button(filename: str = "resume.pdf") -> None:
    """Render a download button for the resume."""
    resume = asset_path(filename)
    if resume.exists():
        with open(resume, "rb") as f:
            st.download_button(
                "📄 Download Resume",
                f,
                file_name="Sumit_Kumar_Bajpai_Resume.pdf",
                mime="application/pdf",
            )
    else:
        st.info("Place resume.pdf inside assets/")


def social_links() -> None:
    """Display social profile buttons."""
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.link_button("GitHub", "https://github.com/sumit-069")

    with c2:
        st.link_button("LinkedIn", "https://www.linkedin.com/")

    with c3:
        st.link_button("LeetCode", "https://leetcode.com/")

    with c4:
        st.link_button("CodeChef", "https://www.codechef.com/")


def metric_cards():
    """Quick stats."""
    a, b, c, d = st.columns(4)
    a.metric("Projects", "3")
    b.metric("CGPA", "8.7")
    c.metric("Tech Stack", "20+")
    d.metric("Languages", "4")


def project_card(title: str, image: str, description: str,
                 tech_stack: list[str],
                 github: str = "#",
                 demo: str = "#") -> None:
    """Reusable project card."""
    with st.container(border=True):
        show_image(image)

        st.subheader(title)
        st.write(description)

        st.markdown("**Tech Stack**")
        cols = st.columns(min(4, max(1, len(tech_stack))))
        for i, tech in enumerate(tech_stack):
            cols[i % len(cols)].caption(f"✅ {tech}")

        c1, c2 = st.columns(2)
        with c1:
            st.link_button("GitHub", github)
        with c2:
            st.link_button("Live Demo", demo)


def image_to_base64(filename: str) -> Optional[str]:
    """Convert image to base64 string if needed."""
    img = asset_path(filename)
    if not img.exists():
        return None
    return base64.b64encode(img.read_bytes()).decode("utf-8")
