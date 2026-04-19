import streamlit as st
import requests




# Page config
st.set_page_config(
    page_title="TSOJI VICTOR RIKWEN | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {background-color: #0E1117;}
    .stApp {background-color: #0E1117; color: #FAFAFA;}
    h1, h2, h3 {color: #00FFAA;}
    .section-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem;}
    .card {
        background-color: #1E2130;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        border-left: 4px solid #00FFAA;
    }
    .tag {
        display: inline-block;
        background-color: #00FFAA22;
        color: #00FFAA;
        border-radius: 4px;
        padding: 2px 8px;
        font-size: 0.85rem;
        margin: 2px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🚀 Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio("Go to",
    ["🏠 Home", "👤 About Me", "🛠️ Skills", "💼 Projects", "📜 Experience", "📞 Contact"])

st.sidebar.markdown("---")


# ====================== HOME ======================
if page == "🏠 Home":
    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            from PIL import Image
            profile = Image.open("assets/Inter.jpg")
            st.image(profile, width=250, caption="TSOJI VICTOR RIKWEN")
        except:
            st.image("assets/inter.jpg", width=200, caption="TSOJI VICTOR RIKWEN")

    with col2:
        st.title("Hi, I'm **TSOJI VICTOR RIKWEN** 👋")
        st.subheader("Software Engineer")
        st.write("""
        Solutions-driven Computer Scientist skilled in **Python, React, JavaScript, and SQL/NoSQL** —
        passionate about Big Data, AI research, and building tools that solve real business problems.
        Currently building an AI-powered financial chatbot and options trading simulator for the African stock market.
        """)

       
           

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.link_button("📧 Email Me", "mailto:tsojivictor@gmail.com", use_container_width=True)
        with col_btn2:
            st.link_button("🔗 Visit GitHub", "https://github.com/Tsoji78", use_container_width=True)

# ====================== ABOUT ME ======================
elif page == "👤 About Me":
    st.header("About Me")

    st.markdown("""
    <div class="card">
    I'm a passionate Computer Scientist from <b>Abuja, Nigeria</b> with expertise in Python, Machine Learning, and building intelligent financial tools.
    <br><br>
    My mission is to leverage data and AI to drive meaningful impact — especially within African financial markets.
    I have contributed to Test and Manage RubixLogistics ERP systems, Develop websites and MOOC, working and researching fintech platforms, and AI-powered research tools.
    I also finished in the <b>Top 5</b> at the Tunga AI Hackathon.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎓 Education")
        st.markdown("""
        **BSc. Computer Science**
        Federal University Wukari
        Dec 2018 – May 2023
        *Specialization: Software Engineering*

        **Final Year Project:**
        Sentiment Analysis on S&P 500 data correlated with Stock Tweets using XGBoost Regressor,
        leveraging Jupyter Notebook and the Twitter API.
        """)

        st.subheader("📜 Certifications")
        st.markdown("""
        - CISCO Skills for All
        - Kaggle Data Science
        - Chartered Institute of Stock Brokers *(In View)*
        """)

    with col2:
        st.subheader("🌍 Languages")
        st.markdown("""
        - 🇬🇧 English — Fluent
        - 🇳🇬 Hausa — Fluent
        - NG Arabic — Basic
        """)

        st.subheader("📌 Location")
        st.markdown("House No 12, First Avenue, Gwarinpa, FCT, Nigeria")

        st.subheader("🏆 Highlights")
        st.markdown("""
        - Top 5 — Tunga AI Hackathon
        - Built AI investment tools & financial chatbot for the African stock market
        - Developing a live stock brokerage app for the Nigerian Stock Exchange
        - Researching and developing QR based Payment systems that model Phonepe and Paytm mode of payments

        """)

# ====================== SKILLS ======================
elif page == "🛠️ Skills":
    st.header("Technical Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("💻 Languages")
        st.progress(90, text="Python")
        st.progress(90, text="React(NextJs)")
        st.progress(75, text="SQL")
        st.progress(65, text="JavaScript")

        st.subheader("📊 Data & AI")
        st.progress(85, text="Data Analytics")
        st.progress(80, text="Sentiment Analysis")
        st.progress(75, text="Machine Learning (XGBoost, Regression)")

    with col2:
        st.subheader("🌐 Web & APIs")
        st.progress(80, text="REST API Development")
        st.progress(75, text="Web Development")
        st.progress(70, text="Streamlit / Taipy")

        st.subheader("🗄️ Databases")
        st.progress(80, text="PostgreSQL / PGAdmin")
        st.progress(75, text="Database Management")
        st.progress(75, text="Redis")

    with col3:
        st.subheader("🛠️ Tools & Platforms")
        st.progress(85, text="Jupyter Notebook / VSCode")
        st.progress(75, text="ERP/CRM Systems")
        st.progress(70, text="Tableau")
        st.progress(65, text="Hugging Face / OpenAI API")
        st.progress(70, text="Git & GitHub")
        st.progress(75, text="Docker")
        st.progress(75, text="Postman")
        st.progress(65, text="Zoho / Google Workspace")
        st.progress(60, text="Draw.io / Lucidchart")
        st.progress(70, text="Trading View")

# ====================== PROJECTS ======================
elif page == "💼 Projects":
    st.header("Featured Projects")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        " S&P 500 Sentiment",
        " Rabovel",
        " ShapPay",
        "Lera Communications",
        "Quiet Shelter Empowerment Foundation",
        "Tunga AI Hackathon"
    ])

    with tab1:
        st.subheader("Sentiment Analysis on S&P 500 (Final Year Project)")
        st.markdown("""
        Performed sentiment analysis on S&P 500 stock data correlated with Twitter/Stock Tweets
        using **XGBoost Regressor**. Leveraged the **Twitter API** and **Jupyter Notebook**
        to derive actionable insights on market sentiment.

        **Tech Stack:** Python · XGBoost · Twitter API · Jupyter Notebook · Pandas · Scikit-learn
        """)
        st.markdown('<span class="tag">Machine Learning</span> <span class="tag">NLP</span> <span class="tag">Python</span> <span class="tag">XGBoost</span>', unsafe_allow_html=True)
        st.link_button("View on GitHub", "https://github.com/Tsoji78")

    with tab2:
        st.subheader("AI Financial Research Tools — Rabovel")
        st.markdown("""
        As **Data Engineer at Rabovel**, built and developed:
        - **AI Investment Tool** — research assistant for African financial markets
        - **Financial Chatbot** (finchat-like) — enables intelligent queries on African stock market data
        - **Options Trading Simulator** — aims to improve liquidity on the Nigerian Stock Exchange

        **Tech Stack:** Python · OpenAI API · Hugging Face · REST APIs · PostgreSQL
        """)
        st.markdown('<span class="tag">AI</span> <span class="tag">Fintech</span> <span class="tag">OpenAI</span> <span class="tag">Data Engineering</span>', unsafe_allow_html=True)
        st.link_button("View on GitHub", "https://github.com/Tsoji78/RabovelBackend")
        st.link_button("Download the APK", "https://expo.dev/accounts/codewarriorstechs-organization/projects/rabovel-staking-platform-P6MFqD2RmgZz8VmOYWniM/builds/432410ed-a3e6-4801-bebe-22fa25ca4639")

    with tab3:
        st.subheader("ShapPay")
        st.markdown("""
        Building a live **QR code Based Payment System** that allows users to make seamless payments. Using Qr codes Like PhonePe and Paytm, 
        the app will enable users to make payments by scanning QR codes at participating merchants. The system will be designed to be secure, 
                    user-friendly, and efficient, providing a convenient payment solution for both consumers and businesses.

        **Tech Stack:** Python · REST APIs · Mono Api · NIBBS Sandbox · PostgreSQL
        """)
        st.markdown('<span class="tag">Fintech</span> <span class="tag">Stock Trading</span> <span class="tag">Python</span> <span class="tag">APIs</span>', unsafe_allow_html=True)
        st.link_button("View on GitHub", "https://github.com/Shappay-LTD/the-backend.git")
        st.link_button("View on Figma", "https://www.figma.com/design/SMeqcsRcTDDAYIrUaJhALL/ShapPay-User-app?t=cyBXcvpoLLcDro3V-0")

    with tab4:
        st.subheader("Lera Communications")
        st.markdown("""
        Built and devveloped Media commnunications Website and the admin that Shows Blog Forums and Podcast Display to users
        """)
        st.markdown('<span class="tag">Website/Newsportal</span> <span class="tag">Media</span> <span class="tag">Innovation</span>', unsafe_allow_html=True)
        st.link_button("View on the Website", "https://leracoms.com")


    with tab5:
        st.subheader("Quiet Shelter Empowerment Foundation")
        st.markdown("""
        Worked as an **IT Support Specialist** at the **Quiet Shelter Empowerment Foundation**, providing technical assistance and maintaining the organization's digital infrastructure.
        """)
        st.markdown('<span class="tag">MOOC</span> <span class="tag">NGO</span> <span class="tag">Volunteer</span>', unsafe_allow_html=True)
        st.link_button("View on the Website", "https://learn.quietshelter.org")

    with tab6:
        st.subheader("Tunga AI Hackathon — Top 5 Finish")
        st.markdown("""
        Participated in the **Tunga AI Hackathon** as a Team, competing against developers across Africa
        and emerging in the **Top 5**. The experience sharpened my ability to innovate and
        apply AI-driven solutions under pressure.
        """)
        st.markdown('<span class="tag">AI</span> <span class="tag">Hackathon</span> <span class="tag">Innovation</span>', unsafe_allow_html=True)
        st.link_button("View on Github", "https://github.com/kedinaimoke/ai_codecrafters.git")

# ====================== EXPERIENCE ======================
elif page == "📜 Experience":
    st.header("Work Experience")

    experiences = [
        {
            "role": "Service Center Officer",
            "company": "AccessArm Pensions",
            "dates": "September 2025 – Present",
            "points": [
                "Review and process retirement benefit applications",
                "Manage client complaints, inquiries, and requests"
            ]
        },
        {
            "role": "Mortgage Benefit Specialist",
            "company": "AccessArm Pensions",
            "dates": "April 2025 – September 2025",
            "points": [
                "Reviewed and processed mortgage applications",
                "Collaborated with the Tech Team to automate mortgage application workflows",
                "Worked with mortgage lenders to optimise the mode of client application submissions"
            ]
        },
        {
            "role": "Data Engineer",
            "company": "Rabovel",
            "dates": "January 2025 – Present",
            "points": [
                "Built and maintained the company website",
                "Developed an AI-powered investment research tool",
                "Built a financial chatbot (finchat-like) for the African stock market",
                "Developed an options trading simulator to increase liquidity on the NSE"
            ]
        },
        {
            "role": "IT Support",
            "company": "Quiet Shelter Empowerment Foundation",
            "dates": "June 2024 – December 2024",
            "points": [
                "Built and maintained the organization's website",
                "Developed custom email solutions using Zoho and Google Workspace"
            ]
        },
        {
            "role": "Software Engineer / Product Manager",
            "company": "Rubix Logistics",
            "dates": "May 2024 – November 2024",
            "points": [
                "Built and maintained the company's ERP system",
                "Developed custom email infrastructure using Zoho and Google Workspace"
            ]
        },
        {
            "role": "Tech Support (Held)",
            "company": "Mentors Innovation Hub",
            "dates": "October 2023 – July 2024",
            "points": [
                "Served as Data Analytics Tutor",
                "Mobile device and computer configuration and troubleshooting",
                "Software development and technical documentation",
                "Built REST APIs",
                "Microsoft Office Suite application and services support"
            ]
        },
        {
            "role": "Techno-Commercial Intern",
            "company": "Redleaf Solution",
            "dates": "January 2022 – May 2022",
            "points": [
                "Utilised ERP systems for operations management",
                "Data entry and reporting",
                "Procurement support",
                "Supported staff members, reducing workload burden",
                "Ran techno-commercial operations",
                "Sorted and organised files, spreadsheets, and reports"
            ]
        },
    ]

    for exp in experiences:
        with st.expander(f"💼 {exp['role']} — {exp['company']}"):
            st.markdown(f"**{exp['dates']}**")
            for point in exp["points"]:
                st.markdown(f"- {point}")

# ====================== CONTACT ======================
elif page == "📞 Contact":
    st.header("Get In Touch")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h4>📍 Location</h4>
        House No 12, First Avenue, Gwarinpa, FCT, Nigeria
        </div>
        <div class="card">
        <h4>📞 Phone</h4>
        +234 806 645 7723
        </div>
        <div class="card">
        <h4>📧 Email</h4>
        tsojivictor@gmail.com
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Connect with me:**")
        st.link_button("🐦 X (Twitter)", "https://x.com/TRikwen", use_container_width=True)
        st.link_button("💼 LinkedIn", "https://linkedin.com/in/tsoji-victor", use_container_width=True)
        st.link_button("🐙 GitHub", "https://github.com/Tsoji78", use_container_width=True)

    with col2:
        contact_form = """
        <form action="https://formsubmit.co/tsojivictor@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your Name" required
                style="width:100%; padding:10px; margin:8px 0; border-radius:6px; border:1px solid #00FFAA;
                background:#1E2130; color:#FAFAFA;">
            <input type="email" name="email" placeholder="Your Email" required
                style="width:100%; padding:10px; margin:8px 0; border-radius:6px; border:1px solid #00FFAA;
                background:#1E2130; color:#FAFAFA;">
            <textarea name="message" placeholder="Your Message" rows="5" required
                style="width:100%; padding:10px; margin:8px 0; border-radius:6px; border:1px solid #00FFAA;
                background:#1E2130; color:#FAFAFA;"></textarea>
            <button type="submit"
                style="background:#00FFAA; color:black; padding:10px 24px; border:none;
                border-radius:6px; cursor:pointer; font-weight:bold; width:100%;">
                🚀 Send Message
            </button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

# Footer
st.markdown("---")
