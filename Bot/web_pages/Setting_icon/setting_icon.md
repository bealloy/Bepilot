<|toggle|theme|>
<|20 80|layout|
<|sidebar|
<|20 60 20|layout|
<|{logo_}|image|height="5px"|width="5px"|id=setting-button|>

<|{company_name}|text|height=30px|width=30px|>

<|{img}|image|label=This is an image|on_action=setting_button|height=20px|width=20px|id=setting-button|>
|>
<br/><br/>
<|{create}|button|on_action=create_new|>
|>


<|main_page |
<|text-center |
Setting
|>
<br/><br/>
<|10 90|layout|gap=30px|
Language :  

<|{Lang}|selector|lov=English;French|dropdown|>
|>
<br/>
My SQL Settings:
<|card|

<|layout|columns=1 1|
<option_list|
Host
|option_list>
<toggle_buttons|
<|input|text|>
|toggle_buttons>
|>

<|layout|columns=1 1|
<option_list|
Username
|option_list>
<toggle_buttons|
<|input|text|>
|toggle_buttons>
|>

<|layout|columns=1 1|
<option_list|
Password
|option_list>
<toggle_buttons|
<|input|text|>
|toggle_buttons>
|>


|>
<br/><br/>

MongoDB Settings :
<|card|

<|layout|columns=1 1|
<option_list|
Host
|option_list>
<toggle_buttons|
<|input|text|>
|toggle_buttons>
|>

<|layout|columns=1 1|
<option_list|
Port
|option_list>
<toggle_buttons|
<|input|text|>
|toggle_buttons>
|>

<|layout|columns=1 1|
<option_list|
Username
|option_list>
<toggle_buttons|
<|input|text|>
|toggle_buttons>
|>

<|layout|columns=1 1|
<option_list|
Passsword
|option_list>
<toggle_buttons|
<|input|text|>
|toggle_buttons>
|>

|>
|main_page>
|>