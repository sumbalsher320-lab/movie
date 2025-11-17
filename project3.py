#........MOVIE TIKECT BOOK SYSTEM...

import streamlit as st

st.set_page_config(page_title="Movie Ticket Booking", page_icon="🎬")

# ---------------- SESSION STATE ----------------
if "movies" not in st.session_state:
    st.session_state.movies = {
        "1: Frozen 2": 20,
        "2: Spider Man": 30,
        "3: King Kong": 15
    }

# ---------------- UI TITLE ----------------
st.title("🎬 Movie Ticket Booking System")

menu = st.selectbox(
    "Choose an option",
    ["Show available movies", "Book Ticket", "Cancel Booking", "Add New Movie", "Exit"]
)

# ---------------- OPTION 1: SHOW MOVIES ----------------
if menu == "Show available movies":
    st.subheader("📢 Available Movies")

    for name, seats in st.session_state.movies.items():
        st.write(f"**{name}** — {seats} seats available")

# ---------------- OPTION 2: BOOK TICKET ----------------
elif menu == "Book Ticket":
    st.subheader("🎟 Book Ticket")

    movie_list = list(st.session_state.movies.keys())
    selected = st.selectbox("Select movie", movie_list)

    if st.button("Book Ticket"):
        if st.session_state.movies[selected] > 0:
            st.session_state.movies[selected] -= 1
            st.success(
                f"Ticket booked for **{selected}**. Remaining seats: {st.session_state.movies[selected]}"
            )
        else:
            st.error("Sorry, no seats available!")

# ---------------- OPTION 3: CANCEL BOOKING ----------------
elif menu == "Cancel Booking":
    st.subheader("❌ Cancel Booking")

    movie_list = list(st.session_state.movies.keys())
    selected = st.selectbox("Select movie", movie_list)

    if st.button("Cancel Ticket"):
        st.session_state.movies[selected] += 1
        st.success(
            f"Booking cancelled for **{selected}**. Seats now: {st.session_state.movies[selected]}"
        )

# ---------------- OPTION 4: ADD NEW MOVIE ----------------
elif menu == "Add New Movie":
    st.subheader("➕ Add New Movie")

    new_name = st.text_input("Enter movie name")
    seats = st.number_input("Enter number of seats", min_value=1, step=1)

    if st.button("Add Movie"):
        if new_name.strip() == "":
            st.error("Movie name cannot be empty!")
        else:
            st.session_state.movies[new_name] = seats
            st.success(f"Movie **{new_name}** added with {seats} seats!")

# ---------------- OPTION 5: EXIT ----------------
elif menu == "Exit":
    st.success("Program ended. Thank you!")

