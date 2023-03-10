import sys

import pynecone as pc

from dao.message import messages

meet_vstack_style = {
    "bg": "#F7F7F7",
    "padding": "0.2em",
    "border_radius": "40px",
    "font_family": "Silkscreen",
}

meet_center_style = {
    "align_items": "top",
    "bg": "radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,5%,100%,0) 19%)",
    "overflow": "auto",
    "padding_top": "2.5%",
    "padding_right": "35%",
    "padding_left": "35%",
    "padding_bottom": "2.5%",
}


class State(pc.State):
    """The app state."""

    prompt = ""
    image_url = ""
    image_processing = False
    image_made = False

    def submit(self):
        print(1)
        sys.exit(1)


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("MeetLight", font_size="2em"),
            pc.box("Get started by editing ", pc.code("filename", font_size="1em")),
            pc.button(
                pc.icon(tag="arrow_up"),
                _hover={
                    "opacity": 0.85,
                    "color": "rgb(107,99,246)",
                },
                on_click=State.submit,
            ),
            pc.button(
                pc.icon(tag="moon"),
                on_click=pc.toggle_color_mode,
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        bg="#ededed",
        padding_top="10%",
    )


def meet():
    font_color = "#A585AD"
    return pc.center(
        pc.vstack(
            pc.tabs(
                pc.tab_list(
                    pc.tab(pc.icon(tag="spinner"), id_="chat", color=font_color),
                    pc.tab(pc.icon(tag="star"), id_="square", color=font_color),
                ),
                pc.tab_panels(
                    pc.tab_panel(get_chat_data()),
                    pc.tab_panel(get_square_data()),
                ),
                border_radius="40px",
                is_fitted=True,
                shadow="lg",
            ),
            font_size="2em",
            style=meet_vstack_style,
        ),
        style=meet_center_style,
    )


def get_square_data():
    def get_text_style(color):
        return {
            "font_family": "Comic Sans MS",
            "font_size": "0.7em",
            "box_shadow": "rgba(240, 46, 170, 0.4) 5px 5px, rgba(240, 46, 170, 0.3) 10px 10px",
            "border_radius": "20px",
            "padding_left": "5%",
            "padding_right": "5%",
            "padding_top": "1%",
            "padding_bottom": "1%",
            "border_color": color,
            "border_width": 5,
            "background_image": "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            "background_clip": "text",
        }

    pc_list = []
    for message in messages:
        pc_list.append(
            pc.list_item(message["content"], style=get_text_style(message["color"]))
        )
    return pc.list(
        *pc_list,
        spacing=".5em",
    )


def get_chat_data():
    return pc.vstack(
        pc.image(
            src="chat_bg.png",
            width="100%",
            height="100%",
        ),
        pc.input(
            placeholder="How are you feeling now",
            font_size="10px",
            on_blur=State.set_prompt,
            bg="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(40,0%,60%,0) 49%)",
            font_color="black",
        ),
        pc.button(
            pc.icon(tag="check"),
            font_size="0.3em",
            bg="#484878",
            color="white",
            width="5em",
            on_click=State.submit,
            align="right",
        ),
    )


# Add state and page to the app.
app = pc.App(
    state=State,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Silkscreen&display=swap",
    ],
)
app.add_page(index, title="MeetLight")
app.add_page(meet, title="MeetLight")
app.compile()
