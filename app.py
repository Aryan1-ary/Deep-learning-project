import streamlit as st

st.set_page_config(
    page_title="Smart MCQ Solver",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Smart MCQ Solver")
st.write("DL & GenAI Course Project — Smart MCQ Solver")

st.subheader("Enter your MCQ")

question = st.text_area(
    "Question",
    placeholder="Enter the question here..."
)

options = {}

for letter in ["A", "B", "C", "D", "E"]:
    options[letter] = st.text_input(
        f"Option {letter}",
        placeholder=f"Enter option {letter}..."
    )

if st.button("Solve MCQ", type="primary"):
    if not question or any(not options[x] for x in options):
        st.warning("Please enter the question and all five options.")
    else:
        st.success("MCQ received successfully!")

        st.write("### Question")
        st.write(question)

        st.write("### Options")
        for letter, option in options.items():
            st.write(f"**{letter}.** {option}")

        st.info(
            "Model inference interface is ready. "
            "The trained DistilRoBERTa model can be connected here."
        )
