import streamlit as st
import json
import os




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
    with open("story/nodes.json", "r") as file:
        raw_data = json.load(file)

    nodes = {}

    for node_id, data in raw_data.items():
        nodes[node_id] = StoryNode(node_id, data)

    return nodes


story_data = load_story()

if "current_node_id" not in st.session_state:
    st.session_state.current_node_id = "start"

current_node = story_data[st.session_state.current_node_id]

if st.session_state.current_node_id == "start":
    st.image("tonyy.png", use_container_width=True)
st.title("🍷 No Reservations: The Afterlife Tour")
st.write("The city sleeps. Somewhere, one final table is waiting...")

st.subheader(current_node.title)
st.write(current_node.text)

if current_node.image:
    image_path = os.path.join("assets/images", current_node.image)
    st.image(image_path)
 #tokyo
if st.session_state.current_node_id == "tokyo":
        st.video("tokyovideo.mp4")
if st.session_state.current_node_id == "new_orleans":
    st.audio("jazz.m4a")
if current_node.ending:
    st.success("The End")

    if current_node.ending_type == "good":
        st.balloons()
    elif current_node.ending_type == "bad":
        st.snow()

    if st.button("Restart"):
        st.session_state.current_node_id = "start"
        st.rerun()
else:
    for choice in current_node.choices:
        if st.button(choice["text"]):
            st.session_state.current_node_id = choice["next"]
            st.rerun()