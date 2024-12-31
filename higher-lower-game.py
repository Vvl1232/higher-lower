import random as rd
import streamlit as st

instagram_followers = {
    "instagram": 676000000,
    "cristiano": 646000000,
    "leomessi": 504000000,
    "selenagomez": 423000000,
    "kyliejenner": 395000000,
    "therock": 394000000,
    "arianagrande": 376000000,
    "kimkardashian": 359000000,
    "beyonce": 313000000,
    "khloekardashian": 305000000,
    "viratkohli": 270000000,
    "nehakakkar": 105000000,
    "shraddhakapoor": 87000000,
    "deepikapadukone": 76000000,
    "aliaabhatt": 78000000,
    "akshaykumar": 62000000,
    "anushkasharma": 64000000,
    "amitabhbachchan": 34000000,
    "msdhoni": 42000000,
    "rohitsharma45": 28000000,
    "priyankachopra": 89000000,
    "jacquelinef143": 60000000,
    "kartikaaryan": 32000000,
    "narendramodi": 80000000,
    "sachintendulkar": 38000000,
    "ranveersingh": 47000000,
    "kapilsharma": 43000000,
    "parineetichopra": 37000000,
    "kritisanon": 41000000,
    "diljitdosanjh": 15000000,
    "tigerjackieshroff": 38000000,
    "vickykaushal09": 32000000,
    "arjunkapoor": 14000000,
    "karanjohar": 12200000,
    "madhuridixitnene": 34000000,
    "saraalikhan95": 45000000,
    "ananyapanday": 25000000,
    "sonamkapoor": 34000000,
    "sunnydeol": 20000000,
    "ajaydevgn": 29000000,
    "varundvn": 43000000,
    "shraddhaarya": 40000000,
    "hrithikroshan": 48000000,
    "shahidkapoor": 38000000,
    "kajol": 20000000,
    "A.R.rahman": 74000000,
    "maheshbabu": 30000000,
    "alluarjunonline": 36000000,
    "tamannaah": 27000000,
    "samantharuthprabhuoffl": 24000000,
    "kajalaggarwalofficial": 23000000,
    "rakulpreet": 22000000,
    "ramcharan": 28500000,
    "nayantharaaa": 15000000
}


st.title("Higher Lower Game 📱")

# Initialize session state variables
if "score" not in st.session_state:
    st.session_state.score = 0
if "choice1" not in st.session_state:
    st.session_state.choice1 = rd.choice(list(instagram_followers.keys()))
if "choice2" not in st.session_state:
    st.session_state.choice2 = None
if "game_over" not in st.session_state:
    st.session_state.game_over = False

if st.session_state.game_over:
    st.error(f"Game Over! 😭 Your final score is {st.session_state.score}.") #Used st.error
    if st.button("Play Again 🔄"):
        st.session_state.score = 0
        st.session_state.choice1 = rd.choice(list(instagram_followers.keys()))
        st.session_state.choice2 = None
        st.session_state.game_over = False
        st.rerun()

else:
    if st.session_state.choice2 is None or st.session_state.choice2 == st.session_state.choice1:
        while True:
            st.session_state.choice2 = rd.choice(list(instagram_followers.keys()))
            if st.session_state.choice2 != st.session_state.choice1:
                break

    st.info(f"{st.session_state.choice1} has {instagram_followers[st.session_state.choice1]:,} followers 👤") #Used st.info
    st.write("VS")
    st.info(f"Does {st.session_state.choice2} have lower or higher followers? 🤔") #Used st.info

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Lower 👇"):
            if instagram_followers[st.session_state.choice1] > instagram_followers[st.session_state.choice2]:
                st.session_state.score += 1
                st.success("Correct! ✅") #Used st.success
                st.session_state.choice1 = st.session_state.choice2
                st.session_state.choice2 = None
                st.rerun()
            else:
                st.session_state.game_over = True
                st.error("Incorrect! ❌") #Used st.error
                st.rerun()

    with col2:
        if st.button("Higher 👆"):
            if instagram_followers[st.session_state.choice1] < instagram_followers[st.session_state.choice2]:
                st.session_state.score += 1
                st.success("Correct! ✅") #Used st.success
                st.session_state.choice1 = st.session_state.choice2
                st.session_state.choice2 = None
                st.rerun()
            else:
                st.session_state.game_over = True
                st.error("Incorrect! ❌") #Used st.error
                st.rerun()

    st.info(f"Current Score: {st.session_state.score} 🏆") #Used st.info