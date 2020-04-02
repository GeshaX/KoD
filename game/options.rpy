








init -1 python hide:





    config.developer = False


    config.screen_width = 1120
    config.screen_height = 840




    config.window_title = u"Kingdom of Deception"



    config.name = "Kingdom of Deception"
    config.version = "0.10.2"




    config.window_icon = "icon.png"










    theme.tv(
        
        

        
        
        widget = "#6F6B87",

        
        
        widget_hover = "#A5A5A8",

        
        
        widget_text = "#3B3B3C",

        
        
        
        widget_selected = "#616162",

        
        
        disabled = "#454546",

        
        
        disabled_text = "#767577",

        
        
        label = "#e0e0eb",

        
        
        frame = "#A8A8AA",

        
        
        
        
        mm_root = "title.jpg",

        
        
        
        gm_root = "#594f4f",

        
        
        rounded_window = False,

        
        
        
        )










    style.window.background = Frame("system/textbox.png", 0, 0)












    style.window.left_padding = 20
    style.window.right_padding = 20
    style.window.top_padding = 20
    style.window.bottom_padding = 20




    style.window.yminimum = 154
    style.window.ymaximum = 154



























    style.default.font = "Lora.ttf"















    config.has_sound = True



    config.has_music = True



    config.has_voice = False

















    config.main_menu_music = "<loop 11.425 to 241.897>music/title.mp3"













    config.help = "README.html"






    config.enter_transition = None


    config.exit_transition = None


    config.intra_transition = None


    config.main_game_transition = None


    config.game_main_transition = None


    config.end_splash_transition = None


    config.end_game_transition = None


    config.after_load_transition = None


    config.window_show_transition = None


    config.window_hide_transition = None


    config.adv_nvl_transition = dissolve


    config.nvl_adv_transition = dissolve


    config.enter_yesno_transition = None


    config.exit_yesno_transition = None


    config.enter_replay_transition = None


    config.exit_replay_transition = None


    config.say_attribute_transition = None


    if persistent.custommouse == True:
        config.mouse = { 'default' : [ ('system/mouse.png', 0, 0)] }







python early:
    config.save_directory = "KoD-1453134816"

init -1 python hide:









    config.default_fullscreen = False



    config.default_text_cps = 0



    config.default_afm_time = 10







init python:




    build.directory_name = "Kingdom_of_Deception"




    build.executable_name = "Kingdom of Deception"



    build.include_update = False



























    build.archive("script", "all")



    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)



    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')


    build.classify('**.rpyc', 'script')




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
