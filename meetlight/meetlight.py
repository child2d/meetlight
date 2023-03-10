import pynecone as pc

from dao.message import messages, add_message

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

    prompt_id = ""
    prompt = ""
    reply_msg = ""
    square_reload = False
    show: bool = False

    def notice(self):
        self.show = not self.show

    def reload_square(self):
        self.square_reload = not self.square_reload

    def color_change(self):
        pass

    def submit_chat(self):
        add_message(self.prompt, "red")
        self.prompt = ""

    def submit_reply(self, uuid, content, color):
        pass

    def submit_reply1(self):
        pass


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
                on_click=State.submit_chat,
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
            "padding_left": "8%",
            "padding_right": "8%",
            "padding_top": "3%",
            "padding_bottom": "1%",
            "border_color": color,
            "border_width": 5,
            "background_image": "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            "background_clip": "text",
        }

    pc_list = []
    for prompt_id, message in reversed(messages.items()):
        pc_list.append(
            pc.list_item(
                pc.popover(
                    pc.popover_trigger(
                        pc.button(
                            pc.stat(
                                pc.stat_label(message["content"]),
                                pc.stat_help_text(message["created_at"], color="gray"),
                                style=get_text_style(message["color"]),
                            ),
                        )
                    ),
                    pc.popover_content(
                        pc.popover_header("reply"),
                        pc.popover_body(get_reply_data(message)),
                        pc.popover_footer(pc.text(init_reply_footer())),
                        pc.popover_close_button(),
                        font_size=".5em",
                    ),
                )
            )
        )
    return pc.list(
        *pc_list,
        spacing=".5em",
    )


def init_reply_footer():
    return pc.vstack(
        pc.input(
            placeholder="wanna say something?",
            font_size="10px",
            on_change=State.set_reply_msg,
            bg="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(40,0%,60%,0) 49%)",
            font_color="black",
        ),
        pc.box(
            pc.button(
                pc.icon(tag="check"),
                font_size="0.3em",
                bg="#484878",
                color="white",
                width="5em",
                on_click=[State.submit_reply1, State.notice],
                align="right",
            ),
            pc.modal(
                pc.modal_overlay(
                    pc.modal_content(
                        pc.modal_header("notice"),
                        pc.modal_body("your message has been sent ^_^"),
                        pc.modal_footer(pc.button("close", on_click=State.notice)),
                    )
                ),
                is_open=State.show,
            ),
        ),
    )


def get_reply_data(message):
    replies = []
    for reply in message.get("reply", []):
        replies.append(
            pc.list_item(
                pc.badge(
                    reply["content"],
                    variant="solid",
                    color_scheme=reply["color"],
                    font_size="1em",
                ),
            )
        )
    return pc.list(*replies, spacing=".2em")


def get_chat_data():
    return pc.vstack(
        pc.image(
            src="chat_bg.png",
            width="100%",
            height="100%",
        ),
        pc.input(
            value=State.prompt,
            placeholder="wanna say something?",
            font_size="10px",
            on_change=State.set_prompt,
            bg="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(40,0%,60%,0) 49%)",
            font_color="black",
        ),
        pc.box(
            pc.button(
                pc.icon(tag="check"),
                font_size="0.3em",
                bg="#484878",
                color="white",
                width="5em",
                on_click=[State.submit_chat, State.notice],
                align="right",
            ),
            pc.modal(
                pc.modal_overlay(
                    pc.modal_content(
                        pc.modal_header("notice"),
                        pc.modal_body("your message has been sent ^_^"),
                        pc.modal_footer(pc.button("close", on_click=[State.notice, ])),
                    )
                ),
                is_open=State.show,
            ),
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
