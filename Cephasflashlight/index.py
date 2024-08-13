from flet import *

def main(page:Page):
    page.title="صفاء"
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = "BLACK"
    page.theme_mode = ThemeMode.LIGHT

    flashlight = Flashlight()
    page.overlay.append(flashlight)

    ph = PermissionHandler()
    page.overlay.append(ph)


    def open_app(e):
       ph.open_app_settings()

    #page = Text('Safaa Cephas')

    page.add(
        AppBar(
            title=Text('FlashLight - تطبيق لاله البغدادية'),
            color='BLACK',
            bgcolor='white',
            actions= [IconButton(icons.SETTINGS,on_click=open_app)]
            
        ),

        Row([
            Text ('\n أشعلو اللاله ضلمت ألدنيه',size=31,color='white')
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Image(src="images.jpeg",width=360)
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            ElevatedButton(
                "شغلوا اللاله",
                width=100,
                icon=icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor='white',
                    color='black',
                    padding=10,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _: flashlight.turn_on
            )
            ,
            
                 ElevatedButton(
                "طفوا اللاله",
                width=100,
                icon=icons.PAUSE_SHARP,
                style=ButtonStyle(
                    bgcolor='white',
                    color='black',
                    padding=10,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _: flashlight.turn_on
                 )
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text ('❤️كل ما تنطفي كهرباء بالعراق العظيم❤️',size=15,color='white')
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            Text ('❤️افتح تطبيق صفاء ينور طريقك❤️',size=15,color='white')
        ],alignment=MainAxisAlignment.CENTER)
        ,
         Row([
            Text ('Developed by Safaa/Cephas | تم التطوير بواسطة صفاء/سيفاس ',size=10,color='Red')
        ],alignment=MainAxisAlignment.CENTER)
        

    
    )



    page.update()
app(main)

