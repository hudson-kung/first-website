import streamlit as st

st.image("image (6).png")
st.title("Carrie Wang")
st.write("Born in Taipei, shaped in Los Angeles — a city girl at heart. I connect ideas, people, and execution. I thrive in client-facing, fast-paced environments, that’s why I know how to keep both customers and vendors happy. I blend creative thinking with solution-oriented approaches, and even under high pressure, still am a happy team player.")
st.write("“For those who change fields every 3-4 years, they’re more likely to learn quickly in a short period of time. Because they constantly push themselves out of their comfort zone and must acquire new skills within a limited timeframe, they usually develop a steeper learning curve and achieve better work efficiency.” — Patty McCord (Former Netflix CTO)")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("""
<style>
.footer {
    position: relative;
    bottom: 0;
    width: 100%;
    margin-top: 200px; /* pushes toward bottom if page is short */
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 6px; /* spacing between elements */
    padding: 10px 0;
    font-size: 16px;
    color: black;
}

.footer a {
    text-decoration: underline;
    color: black;
    font-weight: 500;
    transition: opacity 0.2s ease;
}

.footer a:hover {
    opacity: 0.6;
}

.footer span {
    color: black;
}

.footer .title {
    font-weight: 700;
    font-size: 20px; /* subheader size */
}
</style>

<div class="footer">
    <span class="title">BetteranOops than a whatIF&nbsp;&nbsp;&nbsp;</span>
    <a href="https://www.linkedin.com/in/carrie-w-77997484/" target="_blank">LinkedIn</a>
    <span>/</span>
    <a href="https://www.instagram.com/carrrieon/" target="_blank">Instagram</a>
    <span>&nbsp;&nbsp;Designed with Curiosity</span>
</div>
""", unsafe_allow_html=True)