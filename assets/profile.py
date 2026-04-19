"""
assets/profile.py
-----------------
Handles loading and displaying the profile image for the portfolio.
Place your profile photo as: assets/profile.jpg  (or .png / .webp)
"""

import streamlit as st
from pathlib import Path

# Supported image formats (in priority order)
_SUPPORTED = ["profile.jpg", "profile.jpeg", "profile.png", "profile.webp"]

# Directory where this file lives
_ASSETS_DIR = Path(__file__).parent


def get_profile_image_path() -> Path | None:
    """Return the Path to the first found profile image, or None if missing."""
    for filename in _SUPPORTED:
        candidate = _ASSETS_DIR / filename
        if candidate.exists():
            return candidate
    return None


def show_profile_image(width: int = 250, caption: str = "Tsoji Victor Rikwen") -> None:
    """
    Render the profile image in the Streamlit app.
    Falls back to a styled placeholder if no image is found.

    Usage (in your main app):
        from assets.profile import show_profile_image
        show_profile_image(width=250)
    """
    img_path = get_profile_image_path()

    if img_path:
        st.image(str(img_path), width=width, caption=caption)
    else:
        # Styled SVG avatar placeholder
        st.markdown(
            f"""
            <div style="
                width:{width}px;
                height:{width}px;
                border-radius:50%;
                background:linear-gradient(135deg,#00FFAA,#0E1117);
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:{width // 3}px;
                margin-bottom:0.5rem;
            ">👤</div>
            <p style="color:#888; font-size:0.85rem; margin-top:0;">{caption}</p>
            """,
            unsafe_allow_html=True,
        )
        st.caption("💡 Add your photo as `assets/profile.jpg` to display it here.")