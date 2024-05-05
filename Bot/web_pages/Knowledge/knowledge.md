<style>
.fullwidth{
width:100% !important;
}

</style>


<|20 80|layout|gap=30px|
<|sidebar|
<|20 60 20|layout|
<|{logo_}|image|height="5px"|width="5px"|id=setting-button|>

<|{company_name}|text|height=30px|width=30px|>

<|{img}|image|label=This is an image|on_action=setting_button|height=20px|width=20px|id=setting-button|>
|>
<br/><br/>
<|{create}|button|on_action=create_new|>

<|card|
<|text-center|
<|{name}|>

|> 
|>
|>


<|main_page |

<|container|
<|text-center|
<|{name}|>
|>
|>
<|text-center |
<|navbar|lov={navigation}|>
<|text-center |
<br/><br/>
<|{path}|file_selector|extensions=.txt|label=Import File|on_action=analyze_file|>
|>


<br/><br/><br/><br/><br/>
<|80 20|layout|gap=30px|
<|{File_description}|table|show_all|rowsw = [1:]|style=even_odd_style|>

<|{img}|image|label=Database Setting|on_action=setting_button|height="20px"|width="20px"|id=setting-button|>

|>

|main_page>
|>
