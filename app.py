import streamlit as st

from resume_parser import extract_text
from skill_matcher import extract_skills
from ats_checker import calculate_score

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    skills = extract_skills(text)

    score = calculate_score(skills)

    st.subheader("Resume Score")
    st.success(f"{score}/100")

    st.subheader("Detected Skills")

    for skill in skills:
        st.write("✅", skill)

    st.subheader("Suggestions")

    if score < 50:
        st.warning(
            "Add more technical skills and projects."
        )

    elif score < 75:
        st.info(
            "Good Resume. Add certifications and internships."
        )

    else:
        st.success(
            "Excellent Resume!"
        )