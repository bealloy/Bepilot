# importing taipy
from taipy.gui import Markdown, Gui

# importing markdowns and function from folders
from Local.en import *
from web_pages.root import root_ui
from web_pages.Knowledge.knowledge import *
from web_pages.Security.security import security_ui
from web_pages.Functions.function import function_ui
from web_pages.Flow.flow import flow_ui

import mysql.connector


# translation variable 
company_name = lang['company_name']

# Settings page markdown 
settings_ui = Markdown("web_pages/Settings/settings.md")


# Assigning markdowns to variable 
chatbot = settings_ui
security = security_ui
pub = lang["publish"]
save = lang["save"]
passw = lang["password"]
know = lang["knowledge"]
acc = lang["accept"]
allow = lang["allow"]
open_chat = lang["open-chat"]

navigation = [("/Setting", "Setting"), ("/Knowledge", "Knowledge"),("/Security", "Security"),("/Function", "Function"),("/Flow", "Flow")]