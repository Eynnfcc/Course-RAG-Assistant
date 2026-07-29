import streamlit as st
from rag_pipeline import ask_question

st.set_page_config(
    page_title="Course RAG Assistant",
    page_icon="📚",
    layout="centered"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e293b,#111827);
}

.main{
animation:fadeIn 1s ease-in;
}

@keyframes fadeIn{
from{
opacity:0;
transform:translateY(20px);
}
to{
opacity:1;
transform:translateY(0);
}
}

.title{
font-size:55px;
font-weight:800;
text-align:center;
color:white;
animation:float 3s ease-in-out infinite;
}

@keyframes float{
0%{transform:translateY(0);}
50%{transform:translateY(-8px);}
100%{transform:translateY(0);}
}

.subtitle{
text-align:center;
font-size:18px;
color:#d1d5db;
margin-bottom:30px;
}

.course-box{
background:#1e293b;
padding:18px;
border-radius:15px;
margin-top:10px;
margin-bottom:10px;
transition:0.3s;
border:1px solid #334155;
}

.course-box:hover{
transform:scale(1.03);
border:1px solid #60a5fa;
box-shadow:0px 0px 25px rgba(96,165,250,.5);
}

.answer-box{
background:#111827;
padding:20px;
border-radius:15px;
border-left:6px solid #38bdf8;
animation:fadeIn 0.8s ease-in;
}

div.stButton > button{
width:100%;
background:#2563eb;
color:white;
border:none;
border-radius:12px;
height:55px;
font-size:18px;
font-weight:bold;
transition:0.3s;
}

div.stButton > button:hover{
background:#3b82f6;
transform:scale(1.04);
box-shadow:0px 0px 20px rgba(59,130,246,.7);
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📚 Course RAG Assistant</div>', unsafe_allow_html=True)

st.markdown(
"""
<div class="subtitle">
Ask questions from your university course materials using AI.
</div>
""",
unsafe_allow_html=True
)

st.markdown("## 📖 Available Courses")

col1,col2,col3=st.columns(3)

with col1:
    st.markdown("""
<div class="course-box">
<h4>📘 MATH203</h4>
Differential Equations
</div>
""",unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="course-box">
<h4>💻 CSCI221</h4>
Digital Logic
</div>
""",unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="course-box">
<h4>⚛️ PHYS101C</h4>
Physics
</div>
""",unsafe_allow_html=True)

st.divider()

question=st.text_input(
"Enter your question",
placeholder="Example: What is De Morgan's Law?"
)

if st.button("🚀 Ask AI"):

    if question:

        with st.spinner("Searching course material..."):

            answer=ask_question(question)

        st.markdown("## 🤖 Answer")

        st.markdown(
        f"""
<div class="answer-box">

{answer}

</div>
""",
unsafe_allow_html=True
)