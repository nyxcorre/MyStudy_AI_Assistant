import streamlit as st
import pandas as pd
import time

from database import *
from ai import *


# PAGE CONFIG (always first streamlit command)

st.set_page_config(
    page_title="MyStudy",
    page_icon="📚",
    layout="wide"
)


# DATABASE

create_table()
create_attendance_table()
create_assignment_table()



# SESSION

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False


if "student" not in st.session_state:
    st.session_state.student=""



# DARK THEME


st.markdown(
"""
<style>

.stApp{
background:linear-gradient(135deg,#050008,#17002E,#2D0055);
color:white;
}


[data-testid="stSidebar"]{
background:#090011;
}


[data-testid="stSidebar"] *{
color:white;
}


.title{
text-align:center;
font-size:55px;
font-weight:bold;
}


.subtitle{
text-align:center;
font-size:20px;
}


.card{

background:#1B0033;
padding:25px;
border-radius:20px;
text-align:center;
box-shadow:0px 0px 15px #9D4EDD;

}

</style>
""",
unsafe_allow_html=True
)



# TITLE


st.markdown(
"""
<div class='title'>
📚 MyStudy
</div>

<div class='subtitle'>
Plan Better • Learn Smarter • Achieve More 🚀
</div>

<br>

""",
unsafe_allow_html=True
)



# LOGIN SYSTEM


if st.session_state.logged_in==False:


    choice=st.radio(
        "Account",
        [
        "Login",
        "Signup"
        ]
    )



    if choice=="Signup":


        st.subheader(
            "Create Account"
        )


        name=st.text_input(
            "Name"
        )


        email=st.text_input(
            "Email"
        )


        password=st.text_input(
            "Password",
            type="password"
        )


        branch=st.text_input(
            "Branch"
        )


        sem=st.text_input(
            "Semester"
        )


        if st.button(
            "Signup"
        ):

            add_user(
                name,
                email,
                password,
                branch,
                sem
            )


            st.success(
                "Account Created 💜 Login Now"
            )



    else:


        st.subheader(
            "Login"
        )


        email=st.text_input(
            "Email"
        )


        password=st.text_input(
            "Password",
            type="password"
        )


        if st.button(
            "Login"
        ):


            user=login_user(
                email,
                password
            )


            if user:


                st.session_state.logged_in=True

                st.session_state.student=user[1]


                st.rerun()


            else:

                st.error(
                    "Invalid Details"
                )



    st.stop()



# MENU

st.sidebar.write(
f"👤 {st.session_state.student}"
)


if st.sidebar.button(
    "Logout"
):


    st.session_state.logged_in=False

    st.session_state.student=""

    st.rerun()
menu=st.sidebar.radio(

"Navigation",

[
"Home",
"Dashboard",
"Student Profile",
"Attendance Manager",
"Assignment Guardian",
"CGPA Calculator",
"AI Study Planner",
"AI Assistant",
"Notes Generator",
"Flashcards",
"Focus Timer",
"Achievements",
"Analytics",
"About MyStudy"
]

)



# HOME


if menu=="Home":


    st.markdown(
    """
    <div class='card'>

    <h1>📚 Welcome to MyStudy</h1>

    <h3>Your Personal AI Academic Companion</h3>


    ✨ Smart Attendance Tracking

    <br>

    🤖 AI Learning Assistant

    <br>

    📚 Notes Generator

    <br>

    🎯 Personalized Planner


    </div>
    """,
    unsafe_allow_html=True
    )



# DASHBOARD


elif menu=="Dashboard":


    st.header(
    f"Welcome {st.session_state.student} 👋"
    )


    a,b,c=st.columns(3)


    with a:

        st.markdown(
        """
        <div class='card'>
        📅 Attendance
        <h1>86%</h1>
        </div>
        """,
        unsafe_allow_html=True
        )


    with b:

        st.markdown(
        """
        <div class='card'>
        🎓 CGPA
        <h1>8.9</h1>
        </div>
        """,
        unsafe_allow_html=True
        )



    with c:

        st.markdown(
        """
        <div class='card'>
        🔥 Streak
        <h1>12 Days</h1>
        </div>
        """,
        unsafe_allow_html=True
        )
        # STUDENT PROFILE


elif menu=="Student Profile":


    st.header("👩‍🎓 Student Profile")


    name=st.text_input("Name")

    branch=st.text_input("Branch")


    semester=st.selectbox(
        "Semester",
        ["1","2","3","4","5","6","7","8"]
    )


    goal=st.text_area(
        "Academic Goal 🎯"
    )


    if st.button("Save Profile"):


        st.success(
        f"""
        Welcome {name} ✨

        Branch: {branch}

        Semester: {semester}

        Goal: {goal}
        """
        )




# ATTENDANCE


elif menu=="Attendance Manager":


    st.header("📅 Attendance Manager")


    subject=st.text_input("Subject")


    total=st.number_input(
        "Total Classes",
        min_value=1
    )


    attended=st.number_input(
        "Classes Attended",
        min_value=0
    )


    if st.button("Save"):


        add_attendance(
            subject,
            total,
            attended
        )


        percentage=(attended/total)*100


        st.success(
        f"Attendance: {round(percentage,2)}%"
        )


    st.table(
        view_attendance()
    )




# ASSIGNMENTS


elif menu=="Assignment Guardian":


    st.header("⏰ Assignment Guardian")


    name=st.text_input(
        "Assignment Name"
    )


    subject=st.text_input(
        "Subject"
    )


    deadline=st.date_input(
        "Deadline"
    )


    if st.button("Add"):


        add_assignment(
            name,
            subject,
            str(deadline)
        )


        st.success(
            "Assignment Added"
        )


    st.table(
        view_assignments()
    )





# CGPA


elif menu=="CGPA Calculator":


    st.header("🎓 CGPA Calculator")


    marks=st.number_input(
        "Percentage"
    )


    if st.button("Calculate"):


        st.success(
        f"Your CGPA is {round(marks/9.5,2)}"
        )





# AI STUDY PLANNER


elif menu=="AI Study Planner":


    st.header("🤖 AI Study Planner")


    subjects=st.text_area(
        "Enter Subjects"
    )


    days=st.number_input(
        "Days Left",
        min_value=1
    )


    hours=st.slider(
        "Hours per day",
        1,
        12
    )


    if st.button("Generate Plan"):


        result=create_plan(
            subjects,
            days,
            hours
        )


        st.write(result)





# AI ASSISTANT


elif menu=="AI Assistant":


    st.header(
        "🤖 Ask MyStudy AI"
    )


    question=st.text_area(
        "Ask your doubt"
    )


    if st.button("Ask"):


        st.write(
            ask_ai(question)
        )





# NOTES


elif menu=="Notes Generator":


    st.header(
        "📚 Notes Generator"
    )


    topic=st.text_input(
        "Topic"
    )


    if st.button(
        "Generate"
    ):


        st.write(
        generate_notes(topic)
        )





# FLASHCARDS


elif menu=="Flashcards":


    st.header(
        "🃏 Flashcards"
    )


    topic=st.text_input(
        "Topic"
    )


    if st.button(
        "Create"
    ):


        st.write(
        make_flashcards(topic)
        )





# TIMER


elif menu=="Focus Timer":


    st.header(
        "⏳ Focus Timer"
    )


    minutes = st.slider(
        "Select Focus Minutes",
        1,
        120
    )


    seconds = minutes * 60


    timer = st.empty()


    start = st.button(
        "Start Focus Session 🚀"
    )


    if start:


        while seconds:


            mins, secs = divmod(
                seconds,
                60
            )


            timer.markdown(
            f"""
            <h1 style='text-align:center;'>

            ⏳ {mins:02d}:{secs:02d}

            </h1>
            """,
            unsafe_allow_html=True
            )


            time.sleep(1)


            seconds -= 1



        st.success(
        "🎉 Focus Session Completed!"
        )




# ACHIEVEMENTS


elif menu=="Achievements":


    st.header(
        "🏆 Achievements"
    )


    c1,c2,c3=st.columns(3)


    c1.success(
        "🔥 7 Day Streak"
    )


    c2.success(
        "📚 Study Master"
    )


    c3.success(
        "🎯 Goal Crusher"
    )





# ANALYTICS


elif menu=="Analytics":


    st.header(
        "📊 Analytics"
    )


    data=pd.DataFrame(

    {

    "Subject":
    [
    "Python",
    "DBMS",
    "Maths",
    "OS"
    ],


    "Progress":
    [
    90,
    80,
    75,
    85
    ]

    }

    )


    st.bar_chart(
        data,
        x="Subject",
        y="Progress"
    )





# ABOUT


elif menu=="About MyStudy":


    st.header(
        "About 📚 MyStudy"
    )


    st.write(
    """

    MyStudy is an AI-powered academic assistant
    that helps students organize their academic life.


    Features:

    📅 Attendance Tracking

    ⏰ Assignment Management

    🎓 CGPA Calculator

    🤖 AI Learning Assistant

    📚 Notes Generator

    📊 Analytics


    """
    )


    st.success(
    "Plan Better • Learn Smarter • Achieve More 🚀"
    )