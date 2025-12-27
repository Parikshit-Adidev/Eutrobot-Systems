# eutrobot_systems.py
# Single-file Streamlit app for "Eutrobot Systems" — minimal, visual-first homepage + prototypes + media + contact
# Instructions:
# 1) Place this file in a project folder and create an `assets/` folder alongside it.
#    Put your images and video there using these filenames (or change the constants below):
#       assets/eutrobot1.jpg
#       assets/eutrobot2.jpg
#       assets/eutrobot3.jpg
#       assets/eutrobotx.jpg
#       assets/eutrobot_industrial.jpg
#       assets/media1.jpg, assets/media2.jpg, ... (for the media carousel)
# 2) Run the app with `streamlit run eutrobot_systems.py`.
# 3) Replace the placeholder texts, descriptions, and email addresses where noted.

import streamlit as st
import os
from pathlib import Path
import streamlit.components.v1 as components

# --- CONFIG ---
ASSETS_DIR = Path("assets")
PROTOTYPES = [
    {"id": "e1", "name": "Eutrobot 1.0", "img": ASSETS_DIR / "eutrobot1.jpg", "short": "First prototype: autonomous bioremediation basics.", "desc": "Eutrobot 1.0 was the first field prototype focusing on automated sampling and corrective dosing for small ponds."},
    {"id": "e2", "name": "Eutrobot 2.0", "img": ASSETS_DIR / "eutrobot2.jpg", "short": "Improved sensors and mobility.", "desc": "Eutrobot 2.0 added multi-sensor fusion for turbidity, pH, and dissolved oxygen and improved navigation."},
    {"id": "e3", "name": "Eutrobot 3.0", "img": ASSETS_DIR / "eutrobot3.jpg", "short": "AI-integrated skin and environment analysis.", "desc": "Eutrobot 3.0 integrates edge AI and HuskyLens-based object tracking for precise remediation."},
    {"id": "ex", "name": "Eutrobot X", "img": ASSETS_DIR / "eutrobotx.jpg", "short": "Experimental modular payload system.", "desc": "Eutrobot X explores modular swappable payloads for different remediation tasks."},
    {"id": "ind", "name": "Eutrobot Industrial", "img": ASSETS_DIR / "eutrobot_industrial.jpg", "short": "Coming soon: industrial-scale system.", "desc": "Industrial-scale Eutrobot will be aimed at sewage plants, canals, and lagoons. Contact us to learn about funding and partnership."},
]
TEAM = [
    {"name": "Parikshit", "role": "Founder"},
    {"name": "Shubhranshu", "role": "Co-Founder"},
]
DEFAULT_CONTACT_EMAIL = "youremail@example.com"  # change this in code or later via the UI

st.set_page_config(page_title="Eutrobot Systems", layout="wide", initial_sidebar_state="collapsed")

# -- helper utilities --

def asset_exists(p: Path):
    return p.exists()


def img_tag(path: Path, alt: str = "image", styles: str = "max-width:100%; height:auto; border-radius:12px;"):
    if asset_exists(path):
        return f'<img src="{path.as_posix()}" alt="{alt}" style="{styles}">'
    # fallback placeholder SVG
    svg = f"""
    <div style='width:100%;padding:48px 8px;border-radius:12px;border:1px dashed rgba(255,255,255,0.06);text-align:center;color:var(--muted,#999);'>
      <svg width='120' height='80' xmlns='http://www.w3.org/2000/svg'>
        <rect width='120' height='80' rx='8' fill='#efefef'/>
      </svg>
      <div style='margin-top:8px;color:#666;font-size:13px'>No image</div>
    </div>
    """
    return svg

# Minimal CSS for the app: clean, big visuals, simple animations
APP_CSS = """
:root{
  --bg:#0f1720; --card:#0b1220; --muted:#9aa3b2; --accent:#00d1b2;
}
body { background-color: var(--bg); }
section.hero { padding:60px 8%; display:flex; align-items:center; gap:40px; }
.hero .left { flex:1 }
.hero .right { flex:1; display:flex; justify-content:center }
h1.big { font-size:46px; margin:0; line-height:1.02 }
p.lead{ font-size:18px; color:var(--muted); margin-top:10px }
.card { background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); padding:18px; border-radius:16px; box-shadow: 0 6px 20px rgba(2,6,23,0.6); }
.prototypes-grid { display:flex; gap:18px; flex-wrap:wrap }
.proto { width:260px; border-radius:14px; overflow:hidden; transform: translateY(0); transition: transform .25s ease, box-shadow .25s ease; }
.proto:hover{ transform: translateY(-8px) rotateX(3deg); box-shadow: 0 18px 40px rgba(2,6,23,0.8); }
.proto .meta{ padding:12px }
.btn { display:inline-block; padding:10px 14px; border-radius:10px; background:var(--accent); color:#012; font-weight:600; text-decoration:none; }
.team { display:flex; gap:12px; }
.team .person { padding:12px; border-radius:10px; min-width:160px }
.media-carousel { width:100%; height:420px; border-radius:14px; overflow:hidden; }
/* fade-in on load */
.fade-in{ animation: fadeIn .9s ease both }
@keyframes fadeIn{ from{opacity:0; transform: translateY(8px)} to{opacity:1; transform:none} }
/* simple responsive tweaks */
@media (max-width:800px){ h1.big{ font-size:34px } .hero{ padding:40px 6% } .proto{ width:100% } }
"""

st.markdown(f"<style>{APP_CSS}</style>", unsafe_allow_html=True)

# Initialize page/state
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Top navigation as a compact row
nav_cols = st.columns([1,1,1,1,4])
with nav_cols[0]:
    if st.button('Home'):
        st.session_state['page'] = 'home'
with nav_cols[1]:
    if st.button('Prototypes'):
        st.session_state['page'] = 'prototypes'
with nav_cols[2]:
    if st.button('Media'):
        st.session_state['page'] = 'media'
with nav_cols[3]:
    if st.button('Contact'):
        st.session_state['page'] = 'contact'
# tiny spacer on right for logo or empty
with nav_cols[4]:
    st.markdown("<div style='text-align:right;color:#9aa3b2;font-weight:600'>Eutrobot Systems</div>", unsafe_allow_html=True)

# --- PAGES ---

def home_page():
    st.markdown("<section class='hero card fade-in'>", unsafe_allow_html=True)
    col1, col2 = st.columns([6,5])
    with col1:
        st.markdown("<div class='left'>", unsafe_allow_html=True)
        st.markdown("<h1 class='big' style='color:white'>Eutrobot Systems</h1>", unsafe_allow_html=True)
        st.markdown("<p class='lead'>Autonomous, AI-assisted bioremediation robots — small teams building practical solutions for real water ecosystems.</p>", unsafe_allow_html=True)
        st.markdown("<div style='margin-top:18px'><a class='btn' href='?page=prototypes'>Explore prototypes</a></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        # team
        st.markdown("<div style='margin-top:28px'><h3 style='color:#e6eef4'>Who built it</h3></div>", unsafe_allow_html=True)
        tcols = st.columns(len(TEAM))
        for i, member in enumerate(TEAM):
            with tcols[i]:
                st.markdown(f"<div class='person card'><strong>{member['name']}</strong><div style='color:var(--muted)'>{member['role']}</div></div>", unsafe_allow_html=True)
    with col2:
        # visual: show the first prototype image or placeholder
        first = PROTOTYPES[0]['img']
        html = img_tag(first, alt=PROTOTYPES[0]['name'], styles="width:90%; border-radius:12px; box-shadow: 0 12px 30px rgba(2,6,23,0.6);")
        st.markdown(f"<div class='right'>{html}</div>", unsafe_allow_html=True)
    st.markdown("</section>", unsafe_allow_html=True)

    # quick prototypes preview strip
    st.markdown("<div style='margin-top:26px'><h3 style='color:#e6eef4'>Prototypes</h3></div>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, proto in enumerate(PROTOTYPES):
        with cols[i]:
            phtml = img_tag(proto['img'], alt=proto['name'], styles="width:100%;height:140px;object-fit:cover;display:block;border-radius:10px;")
            st.markdown("<div class='proto card' style='padding:8px'>" + phtml + f"<div class='meta'><strong>{proto['name']}</strong><div style='color:var(--muted);font-size:13px'>{proto['short']}</div></div></div>", unsafe_allow_html=True)


def prototypes_page():
    st.markdown("<div class='card' style='padding:20px'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white'>Prototypes</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:var(--muted)'>Click any project to learn more. For Eutrobot Industrial, contact us to discuss funding and partnerships.</p>", unsafe_allow_html=True)

    grid_cols = st.columns(3)
    for i, proto in enumerate(PROTOTYPES):
        col = grid_cols[i % 3]
        with col:
            st.markdown("<div class='proto card fade-in'>", unsafe_allow_html=True)
            phtml = img_tag(proto['img'], alt=proto['name'], styles="width:100%;height:180px;object-fit:cover;display:block;")
            st.markdown(phtml, unsafe_allow_html=True)
            st.markdown(f"<div class='meta'><h4 style='margin:4px 0'>{proto['name']}</h4><div style='color:var(--muted)'>{proto['short']}</div></div>", unsafe_allow_html=True)
            if st.button(f"Learn more — {proto['name']}", key=f"btn_{proto['id']}"):
                st.session_state['open_proto'] = proto['id']
            st.markdown("</div>", unsafe_allow_html=True)

    # show details if selected
    if st.session_state.get('open_proto'):
        pid = st.session_state['open_proto']
        proto = next((p for p in PROTOTYPES if p['id'] == pid), None)
        if proto:
            st.markdown("<hr style='margin:20px 0'>", unsafe_allow_html=True)
            st.markdown(f"<div class='card' style='padding:18px'><div style='display:flex;gap:18px;align-items:center'>", unsafe_allow_html=True)
            # left: image
            left, right = st.columns([3,5])
            with left:
                st.image(proto['img'] if asset_exists(proto['img']) else None, caption=proto['name'], use_column_width=True)
            with right:
                st.markdown(f"<h3 style='margin:0'>{proto['name']}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='color:var(--muted)'>{proto['desc']}</p>", unsafe_allow_html=True)
                if proto['id'] == 'ind':
                    mail = DEFAULT_CONTACT_EMAIL
                    st.markdown(f"<p style='margin-top:10px'>Want to support or fund <strong>{proto['name']}</strong>? <a href='mailto:{mail}'>Contact us</a></p>", unsafe_allow_html=True)
                st.markdown("</div></div>", unsafe_allow_html=True)


def media_page():
    st.markdown("<h2 style='color:white'>Media</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:var(--muted)'>A looping gallery of images from our builds and demos.</p>", unsafe_allow_html=True)

    # Build a simple CSS carousel using the images in assets named media1..media6
    media_images = sorted([p for p in ASSETS_DIR.glob('media*')])
    if not media_images:
        st.info('No media images found in assets/. Add files named media1.jpg, media2.jpg, ... to the assets folder.')
        # show a couple of prototype images as fallback
        fallback = [p['img'] for p in PROTOTYPES if asset_exists(p['img'])]
        if fallback:
            st.image(fallback, caption=['Preview']*len(fallback), width=240)
        return

    # Prepare HTML for an autoplaying carousel with fade effect
    imgs_html = ''.join([f"<div class='slide'><img src='{p.as_posix()}' /></div>" for p in media_images])
    carousel_html = f"""
    <style>
    .carousel-wrapper{{width:100%;height:420px;border-radius:12px;overflow:hidden;}}
    .carousel-wrapper .slide{{position:absolute;top:0;left:0;right:0;bottom:0;display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity .9s ease;}}
    .carousel-wrapper img{{max-width:100%;max-height:100%;object-fit:cover;}}
    /* keyframes */
    @keyframes slideShow {{
      0%{{opacity:1}} 20%{{opacity:1}} 25%{{opacity:0}} 95%{{opacity:0}} 100%{{opacity:1}}
    }}
    .carousel-wrapper .slide:nth-child(1){{animation: slideShow 18s infinite 0s}}
    .carousel-wrapper .slide:nth-child(2){{animation: slideShow 18s infinite 3.6s}}
    .carousel-wrapper .slide:nth-child(3){{animation: slideShow 18s infinite 7.2s}}
    .carousel-wrapper .slide:nth-child(4){{animation: slideShow 18s infinite 10.8s}}
    .carousel-wrapper .slide:nth-child(5){{animation: slideShow 18s infinite 14.4s}}
    .carousel-wrapper .slide:nth-child(6){{animation: slideShow 18s infinite 18.0s}}
    </style>
    <div class='carousel-wrapper'>
    {imgs_html}
    </div>
    """
    components.html(carousel_html, height=440)


def contact_page():
    st.markdown('<h2 style="color:white">Contact</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:var(--muted)">Reach out to collaborate, sponsor, or ask questions.</p>', unsafe_allow_html=True)
    col1, col2 = st.columns([3,2])
    with col1:
        name = st.text_input('Your name')
        email = st.text_input('Your email')
        message = st.text_area('Message', height=160)
        if st.button('Create email to send'):
            mailto = f"mailto:{DEFAULT_CONTACT_EMAIL}?subject=Eutrobot%20Contact%20from%20{st.session_state.get('user_name','anon')}&body=From:%20{email}%0A%0A{message}"
            st.markdown(f"<a class='btn' href='{mailto}'>Open mail client</a>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="padding:12px" class="card"><h4>Quick contact</h4><div style="color:var(--muted)">Email:</div><div style="margin-top:6px"><a href="mailto:{0}">{0}</a></div></div>'.format(DEFAULT_CONTACT_EMAIL), unsafe_allow_html=True)

# Render current page
page = st.session_state.get('page','home')
if st.experimental_get_query_params().get('page'):
    st.session_state['page'] = st.experimental_get_query_params().get('page')[0]
    page = st.session_state['page']

if page == 'home':
    home_page()
elif page == 'prototypes':
    prototypes_page()
elif page == 'media':
    media_page()
elif page == 'contact':
    contact_page()
else:
    home_page()

# footer
st.markdown("<div style='margin-top:40px;padding:14px 6%;color:var(--muted);font-size:13px'>© Eutrobot Systems — built by students. Replace contact email and images in assets/ for a live site.</div>", unsafe_allow_html=True)
