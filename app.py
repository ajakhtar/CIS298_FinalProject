import streamlit as st
import json
import os
import base64

def get_base64_file(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(
    page_title="Choose Your Own Adventure",
    page_icon="📖",
    layout="centered"
)

class StoryNode:
    def __init__(self, node_id, data):
        self.id = node_id
        self.title = data.get("title", "")
        self.text = data.get("text", "")
        self.choices = data.get("choices", [])
        self.ending = data.get("ending", False)
        self.ending_type = data.get("ending_type", None)
        self.image = data.get("image", None)

def load_story():
    with open("story/nodes.json", "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    nodes = {}
    for node_id, data in raw_data.items():
        nodes[node_id] = StoryNode(node_id, data)

    return nodes

story_data = load_story()

# -------------------------
# SESSION STATE
# -------------------------
if "current_node_id" not in st.session_state:
    st.session_state.current_node_id = "start"

if "nola_scene" not in st.session_state:
    st.session_state.nola_scene = "main"

if "selected_destination" not in st.session_state:
    st.session_state.selected_destination = None

current_node = story_data[st.session_state.current_node_id]

st.title("🍷 No Reservations: The Afterlife Tour")
st.write("The city sleeps. Somewhere, one final table is waiting...")

# -------------------------
# START PAGE WITH MAP + PLANE
# -------------------------
if st.session_state.current_node_id == "start":
    st.image("tonyy.png", use_container_width=True)

    st.subheader(current_node.title)
    st.write(current_node.text)

    # Plane positions on the map
    plane_positions = {
        "istanbul": ("61%", "36%"),
        "tokyo": ("84%", "41%"),
        "new_orleans": ("23%", "42%"),
        "mexico_city": ("17%", "50%")
    }

    # Default plane location if nothing selected yet
    plane_left = "50%"
    plane_top = "50%"

    if st.session_state.selected_destination in plane_positions:
        plane_left, plane_top = plane_positions[st.session_state.selected_destination]

    map_base64 = get_base64_file("worldmap.png")
    # Map + plane overlay
    st.markdown(
        f"""
        <div style="position: relative; width: 100%; max-width: 1000px; margin: auto;">
           <img src="data:image/png;base64,{map_base64}" style="width: 100%; border-radius: 14px;">
            <div style="
                position: absolute;
                left: {plane_left};
                top: {plane_top};
                transform: translate(-50%, -50%);
                font-size: 34px;
                transition: all 0.8s ease;
            ">
                ✈️
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("### Choose your first destination")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Istanbul, Turkey"):
            st.session_state.selected_destination = "istanbul"
            st.rerun()

        if st.button("Tokyo, Japan"):
            st.session_state.selected_destination = "tokyo"
            st.rerun()

    with col2:
        if st.button("New Orleans, USA"):
            st.session_state.selected_destination = "new_orleans"
            st.rerun()

        if st.button("Mexico City, Mexico"):
            st.session_state.selected_destination = "mexico_city"
            st.rerun()

    if st.session_state.selected_destination:
        st.success(f"Destination selected: {st.session_state.selected_destination.replace('_', ' ').title()}")

        if st.button("Begin Journey"):
            st.session_state.current_node_id = st.session_state.selected_destination

            if st.session_state.selected_destination != "new_orleans":
                st.session_state.nola_scene = "main"

            st.rerun()

# -------------------------
# SPECIAL NEW ORLEANS PAGE
# -------------------------
elif st.session_state.current_node_id == "new_orleans":
    st.subheader("New Orleans, USA")

    if st.session_state.nola_scene == "main":
        st.write(current_node.text)
    elif st.session_state.nola_scene == "gumbo":
        st.write(
            "A woman stirs a massive pot with practiced patience. "
            "Chef Anthony leans close. 'Good food takes time. So do people worth knowing.'"
        )
    elif st.session_state.nola_scene == "jazz":
        st.write(
            "Inside a crowded club, strangers dance like old friends. "
            "Chef Anthony laughs. 'Some people wait for permission to feel alive. Never do that.'"
        )
    elif st.session_state.nola_scene == "talk":
        st.write(
            "He watches the street quietly. "
            "'Because this place knows grief,' he says. 'And it still chose music.'"
        )

    st.audio("jazz.m4a")

    if st.session_state.nola_scene == "main":
        if st.button("Follow the scent of gumbo"):
            st.session_state.nola_scene = "gumbo"
            st.rerun()

        if st.button("Follow the trumpet into a jazz club"):
            st.session_state.nola_scene = "jazz"
            st.rerun()

        if st.button("Ask why this city matters so much"):
            st.session_state.nola_scene = "talk"
            st.rerun()
    else:
        if st.button("Back to New Orleans"):
            st.session_state.nola_scene = "main"
            st.rerun()

    if st.button("Return to destinations"):
        st.session_state.current_node_id = "start"
        st.session_state.nola_scene = "main"
        st.rerun()

# -------------------------
# ALL OTHER PAGES
# -------------------------
else:
    st.subheader(current_node.title)
    st.write(current_node.text)

    if current_node.image:
        image_path = os.path.join("assets/images", current_node.image)
        if os.path.exists(image_path):
            st.image(image_path)

    if st.session_state.current_node_id == "tokyo":
        st.video("tokyovideo.mp4")

    if current_node.ending:
        st.success("The End")

        if current_node.ending_type == "good":
            st.balloons()
        elif current_node.ending_type == "bad":
            st.snow()

    if st.button("Return to destinations"):
        st.session_state.current_node_id = "start"
        st.rerun()