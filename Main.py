import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Eutrobot Systems",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for fade effects and 3D transforms
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .main-container {
        width: 100%;
        overflow-x: hidden;
    }
    
    /* Hero Section */
    .hero-section {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 2rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero-title {
        font-size: 5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        animation: fadeInUp 1s ease-out;
        transform-style: preserve-3d;
        perspective: 1000px;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #b0b0b0;
        font-weight: 300;
        margin-bottom: 2rem;
        animation: fadeInUp 1.2s ease-out;
    }
    
    .main-idea {
        max-width: 800px;
        font-size: 1.2rem;
        color: #d0d0d0;
        line-height: 1.8;
        animation: fadeInUp 1.4s ease-out;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Prototype Cards */
    .prototypes-section {
        min-height: 100vh;
        padding: 4rem 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    .section-title {
        font-size: 3rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 3rem;
        text-align: center;
        animation: fadeIn 1s ease-out;
    }
    
    .prototypes-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        width: 100%;
        max-width: 1400px;
        padding: 2rem;
    }
    
    .prototype-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 2rem;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.6s ease-out;
        transform-style: preserve-3d;
        perspective: 1000px;
        margin-bottom: 1rem;
    }
    
    .prototype-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        opacity: 0;
        transition: opacity 0.4s ease;
        z-index: 0;
    }
    
    .prototype-card:hover {
        transform: translateY(-15px) rotateX(8deg) rotateY(-8deg) scale(1.02);
        box-shadow: 0 25px 50px rgba(102, 126, 234, 0.4);
        border-color: rgba(102, 126, 234, 0.6);
    }
    
    .prototype-card:hover::before {
        opacity: 1;
    }
    
    .prototype-card-wrapper {
        position: relative;
        z-index: 1;
    }
    
    .prototype-card.coming-soon {
        opacity: 0.7;
        position: relative;
    }
    
    .prototype-name {
        font-size: 2rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .prototype-description {
        font-size: 1rem;
        color: #b0b0b0;
        line-height: 1.6;
        position: relative;
        z-index: 1;
    }
    
    .coming-soon-badge {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        z-index: 2;
    }
    
    /* Team Section */
    .team-section {
        min-height: 50vh;
        padding: 4rem 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        width: 100%;
        max-width: 800px;
        padding: 2rem;
    }
    
    .team-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.4s ease;
        animation: fadeInUp 0.6s ease-out;
    }
    
    .team-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
    }
    
    .team-name {
        font-size: 1.5rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    
    .team-role {
        font-size: 1rem;
        color: #b0b0b0;
    }
    
    /* Media Section */
    .media-section {
        min-height: 50vh;
        padding: 4rem 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    .media-link {
        display: inline-block;
        padding: 1rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-decoration: none;
        border-radius: 50px;
        font-size: 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        cursor: pointer;
        animation: fadeIn 1s ease-out;
    }
    
    .media-link:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    
    /* Contact Section */
    .contact-section {
        min-height: 50vh;
        padding: 4rem 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    .contact-info {
        max-width: 600px;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        animation: fadeInUp 1s ease-out;
    }
    
    .contact-email {
        font-size: 1.5rem;
        color: #667eea;
        font-weight: 600;
        margin-top: 1rem;
    }
    
    .contact-email a:hover {
        color: #764ba2;
        text-decoration: underline;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Smooth scrolling */
    html {
        scroll-behavior: smooth;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Configuration - Easy to update
CONTACT_EMAIL = "contact@eutrobotsystems.com"  # Update this with your email

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_prototype' not in st.session_state:
    st.session_state.selected_prototype = None

# Prototype details
prototype_details = {
    'Eutrobot 1.0': {
        'description': 'Our first generation robot, designed with cutting-edge technology and innovative features.',
        'features': ['Advanced AI Integration', 'Modular Design', 'High Performance', 'User-Friendly Interface'],
        'image': '🤖'
    },
    'Eutrobot 2.0': {
        'description': 'Enhanced version with improved capabilities and expanded functionality.',
        'features': ['Upgraded AI System', 'Enhanced Mobility', 'Better Sensors', 'Extended Battery Life'],
        'image': '🚀'
    },
    'Eutrobot 3.0': {
        'description': 'The latest generation featuring state-of-the-art technology and superior performance.',
        'features': ['Next-Gen AI', 'Advanced Navigation', 'Multi-Task Capability', 'Cloud Connectivity'],
        'image': '🌟'
    },
    'Eutrobot X': {
        'description': 'Experimental model pushing the boundaries of robotic innovation.',
        'features': ['Experimental Features', 'Cutting-Edge Tech', 'Research Platform', 'Future-Ready'],
        'image': '⚡'
    },
    'Eutrobot Industrial': {
        'description': 'Coming soon - Industrial-grade robot designed for heavy-duty applications.',
        'features': ['Industrial Strength', 'Scalable Solution', 'Enterprise Ready', 'Customizable'],
        'image': '🏭',
        'coming_soon': True,
        'contact_email': CONTACT_EMAIL
    }
}

# Media gallery images (placeholder - you can add actual images)
media_images = [
    '📸', '🎥', '📷', '🎬', '📹', '🎞️'
]

def render_homepage():
    st.markdown("""
    <div class="main-container">
        <div class="hero-section">
            <h1 class="hero-title">EUTROBOT SYSTEMS</h1>
            <p class="hero-subtitle">Innovating the Future of Robotics</p>
            <div class="main-idea">
                <p>At Eutrobot Systems, we are pioneering the next generation of robotic solutions. 
                Our mission is to create intelligent, adaptable, and efficient robots that transform 
                industries and enhance human capabilities. Through continuous innovation and cutting-edge 
                technology, we're building a future where robots seamlessly integrate into everyday life.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Prototypes Section
    st.markdown("""
    <div class="prototypes-section">
        <h2 class="section-title">Our Prototypes</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # First row of prototypes
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="prototype-card">
            <div class="prototype-card-wrapper">
                <div class="prototype-name">🤖 Eutrobot 1.0</div>
                <div class="prototype-description">Our first generation robot with cutting-edge technology</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Details →", key="proto1", use_container_width=True):
            st.session_state.selected_prototype = 'Eutrobot 1.0'
            st.session_state.current_page = 'prototype_detail'
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="prototype-card">
            <div class="prototype-card-wrapper">
                <div class="prototype-name">🚀 Eutrobot 2.0</div>
                <div class="prototype-description">Enhanced version with improved capabilities</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Details →", key="proto2", use_container_width=True):
            st.session_state.selected_prototype = 'Eutrobot 2.0'
            st.session_state.current_page = 'prototype_detail'
            st.rerun()
    
    # Second row
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="prototype-card">
            <div class="prototype-card-wrapper">
                <div class="prototype-name">🌟 Eutrobot 3.0</div>
                <div class="prototype-description">Latest generation with state-of-the-art technology</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Details →", key="proto3", use_container_width=True):
            st.session_state.selected_prototype = 'Eutrobot 3.0'
            st.session_state.current_page = 'prototype_detail'
            st.rerun()
    
    with col4:
        st.markdown("""
        <div class="prototype-card">
            <div class="prototype-card-wrapper">
                <div class="prototype-name">⚡ Eutrobot X</div>
                <div class="prototype-description">Experimental model pushing boundaries</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Details →", key="proto4", use_container_width=True):
            st.session_state.selected_prototype = 'Eutrobot X'
            st.session_state.current_page = 'prototype_detail'
            st.rerun()
    
    # Eutrobot Industrial - Centered
    st.markdown("""
    <div style="max-width: 600px; margin: 3rem auto;">
        <div class="prototype-card coming-soon">
            <div class="coming-soon-badge">Coming Soon</div>
            <div class="prototype-card-wrapper">
                <div class="prototype-name">🏭 Eutrobot Industrial</div>
                <div class="prototype-description">Industrial-grade robot for heavy-duty applications</div>
                <p style="margin-top: 1rem; color: #667eea; font-weight: 600;">
                    Contact us to learn more and help support by funding us
                </p>
            <p style="margin-top: 0.5rem; color: #ffffff;">
                Email: """ + CONTACT_EMAIL + """
            </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("View Details →", key="proto5", use_container_width=True):
        st.session_state.selected_prototype = 'Eutrobot Industrial'
        st.session_state.current_page = 'prototype_detail'
        st.rerun()
    
    # Team Section
    st.markdown("""
    <div class="team-section">
        <h2 class="section-title">Who is it Built By</h2>
        <div class="team-grid">
            <div class="team-card">
                <div class="team-name">Parikshit</div>
                <div class="team-role">Founder</div>
            </div>
            <div class="team-card">
                <div class="team-name">Shubhranshu</div>
                <div class="team-role">Co-Founder</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Media Section
    st.markdown("""
    <div class="media-section">
        <h2 class="section-title">Media</h2>
    """, unsafe_allow_html=True)
    
    if st.button("View Media Gallery", key="media", use_container_width=True):
        st.session_state.current_page = 'media'
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Contact Section
    st.markdown("""
    <div class="contact-section">
        <h2 class="section-title">Contact Us</h2>
        <div class="contact-info">
            <p style="color: #b0b0b0; font-size: 1.1rem; margin-bottom: 1rem;">Get in touch with us</p>
            <div class="contact-email">
                <a href="mailto:""" + CONTACT_EMAIL + """" style="color: #667eea; text-decoration: none;">""" + CONTACT_EMAIL + """</a>
            </div>
            <p style="color: #b0b0b0; font-size: 0.9rem; margin-top: 1.5rem;">We'd love to hear from you!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_prototype_detail():
    prototype = st.session_state.selected_prototype
    details = prototype_details.get(prototype, {})
    
    st.markdown(f"""
    <div style="padding: 2rem; max-width: 1000px; margin: 0 auto;">
        <button onclick="window.history.back()" style="background: rgba(255,255,255,0.1); color: white; border: none; padding: 0.5rem 1rem; border-radius: 10px; cursor: pointer; margin-bottom: 2rem;">← Back</button>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Home", key="back_home"):
        st.session_state.current_page = 'home'
        st.session_state.selected_prototype = None
        st.rerun()
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem;">
        <h1 style="font-size: 3rem; color: #ffffff; margin-bottom: 1rem;">{details.get('image', '🤖')} {prototype}</h1>
        <p style="font-size: 1.3rem; color: #b0b0b0; max-width: 800px; margin: 0 auto 2rem;">{details.get('description', '')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if details.get('coming_soon'):
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.05); padding: 2rem; border-radius: 20px; max-width: 800px; margin: 2rem auto; text-align: center;">
            <h2 style="color: #667eea; margin-bottom: 1rem;">Coming Soon</h2>
            <p style="color: #b0b0b0; margin-bottom: 1rem;">This project is currently in development. Contact us to learn more and support us through funding.</p>
            <p style="color: #ffffff; font-size: 1.2rem; font-weight: 600;">Email: {details.get('contact_email', CONTACT_EMAIL)}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="max-width: 800px; margin: 2rem auto;">
            <h2 style="color: #ffffff; margin-bottom: 1rem;">Key Features</h2>
        """, unsafe_allow_html=True)
        
        for feature in details.get('features', []):
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 10px; margin-bottom: 1rem; border-left: 4px solid #667eea;">
                <p style="color: #ffffff; font-size: 1.1rem;">✓ {feature}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

def render_media_gallery():
    if st.button("← Back to Home", key="back_from_media"):
        st.session_state.current_page = 'home'
        st.rerun()
    
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h1 style="font-size: 3rem; color: #ffffff; margin-bottom: 2rem;">Media Gallery</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a looping gallery with animation
    if 'gallery_index' not in st.session_state:
        st.session_state.gallery_index = 0
    
    # Display images in a grid
    num_images = len(media_images)
    
    # Create rows of 3 columns
    for row in range(3):
        cols = st.columns(3)
        for col_idx in range(3):
            img_idx = (st.session_state.gallery_index + row * 3 + col_idx) % num_images
            with cols[col_idx]:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.05); padding: 3rem; border-radius: 20px; margin: 1rem 0; text-align: center; font-size: 4rem; border: 1px solid rgba(255,255,255,0.1); animation: fadeIn 0.5s ease-out; transition: transform 0.3s ease;">
                    {media_images[img_idx]}
                </div>
                """, unsafe_allow_html=True)
    
    # Control buttons
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("⏸️ Pause", key="pause_gallery"):
            st.session_state.auto_advance = False
            st.rerun()
    with col_btn2:
        if st.button("▶️ Resume", key="resume_gallery"):
            st.session_state.auto_advance = True
            st.rerun()
    
    # Auto-advance gallery
    if st.session_state.get('auto_advance', True):
        time.sleep(2)
        st.session_state.gallery_index = (st.session_state.gallery_index + 1) % num_images
        st.rerun()

# Main app logic
if st.session_state.current_page == 'home':
    render_homepage()
elif st.session_state.current_page == 'prototype_detail':
    render_prototype_detail()
elif st.session_state.current_page == 'media':
    render_media_gallery()
