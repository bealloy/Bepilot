# importing taipy
from taipy.gui import Gui,navigate

# importing markdowns and function from folders
from Local.en import *
from web_pages.root import root_ui
from web_pages.Knowledge.knowledge import *
from web_pages.Security.security import security_ui
from web_pages.Functions.function import function_ui
from web_pages.Flow.flow import flow_ui
from settings import *
from web_pages.Setting_icon.setting_icon import setting_icon_ui

name = " "
# main page markdown 
main_ui = Markdown("main.md")


# create new function
def create_new(state):
    state.name =  "New Chat"
    navigate(state, "Setting")

# setting page navigation function
def setting_button(state):
    state.name =  "New Chat"
    navigate(state, "Setting")


# Defining customized theme
my_theme = {
    "palette": {
    "background": {"default": "#222831"},
    "primary": {"main": "#9CAFAA"} 
    },
}


# Assigning markdowns to variable 
chatbot = settings_ui
security = security_ui

no_logo = ""
# translation variable    
company_name = lang['company_name']
create = lang['create-new']
open_chat = lang["open-chat"]
tag = lang["tag-line"]
setting = lang["setting"]
knowledge = lang["knowledge"]
security = lang["security"]
flow = lang["flow"] 
func= lang["function"]
pub = lang["publish"]
save = lang["save"]
passw = lang["password"]
know = lang["knowledge"]
acc = lang["accept"]
allow = lang["allow"]
upl = lang["upload"]


img = "setting_icon.png"
logo_ = "minibox_.png"
# assigning all markdown to pages variable
pages ={
    "main" :main_ui,
    "Setting":settings_ui,
    "Knowledge":knowledge_ui,
    "Security":security_ui,
    "Function":function_ui,
    "Flow":flow_ui,
    "Setting_Database" :setting_icon_ui
}


# to run all pages
if __name__ == "__main__":

    Gui(pages=pages).run(
        title=company_name,
        favicon="box_.png",
        image = ("box.png","minibox_.png","setting_icon.png"),
        use_reloader=True,
        theme=my_theme,
        watermark=no_logo,

    )


    