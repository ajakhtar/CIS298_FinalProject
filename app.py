import streamlit as st
import json
import os

st.set_page_config(
    page_title="No Reservations: The Afterlife Tour",
    page_icon="🍷",
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
    with open("story/nodes.json", "r") as file:
        raw_data = json.load(file)
    nodes = {}
    for node_id, data in raw_data.items():
        nodes[node_id] = StoryNode(node_id, data)
    return nodes


story_data = load_story()

if "started" not in st.session_state:
    st.session_state.started = False

if "current_node_id" not in st.session_state:
    st.session_state.current_node_id = "start"


# Title screen
if not st.session_state.started:
    if os.path.exists("tonyy.png"):
        st.image("tonyy.png", use_container_width=True)
    st.title("🍷 No Reservations: The Afterlife Tour")
    st.write("The city sleeps. Somewhere, one final table is waiting...")
    if st.button("Begin the Tour"):
        st.session_state.started = True
        st.rerun()

# Game screen
else:
    current_node = story_data[st.session_state.current_node_id]

    st.title("🍷 No Reservations: The Afterlife Tour")
    st.subheader(current_node.title)
    st.write(current_node.text)

    if current_node.image:
        image_path = os.path.join("assets/images", current_node.image)
        if os.path.exists(image_path):
            st.image(image_path)

    if st.session_state.current_node_id == "tokyo" and os.path.exists("tokyovideo.mp4"):
        st.video("tokyovideo.mp4")

    if st.session_state.current_node_id == "new_orleans" and os.path.exists("jazz.m4a"):
        st.audio("jazz.m4a")

    st.divider()

    if current_node.ending:
        if current_node.ending_type == "good":
            st.success("🍽️ Another unforgettable meal. The End.")
            st.balloons()
        elif current_node.ending_type == "bad":
            st.error("💀 Some tables you shouldn't have sat at. The End.")
            st.snow()
        else:
            st.info("The End.")

        if st.button("Take Another Trip"):
            st.session_state.current_node_id = "start"
            st.session_state.started = False
            st.rerun()
    else:
        for choice in current_node.choices:
            if st.button(choice["text"]):
                st.session_state.current_node_id = choice["next"]
                st.rerun()