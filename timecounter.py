import flet as ft
from time import sleep

def main(page:ft.Page):
    """Countdown application"""
    page.title = "Countdown Type"
    page.window_height = 700
    page.window_width = 500
    page.window_minimizable = False
    page.window_maximizable = False
    
    # Event function
    def countdown(e):       
        sec = fillcounter.value
        fillcounter.value = ''  
        fillcounter.update()

        if sec.isnumeric():
            sec = int(sec)           
            seclist = [s for s in range(sec + 1)]
            rev = [r for r in reversed(seclist)]
            for count in rev:
                showcounter.size = 144
                showcounter.value = count
                sleep(1)
                showcounter.update()
            showcounter.size = 48
            showcounter.value = 'COMPLETE!'        
        else:
            fillcounter.error_text = "Please enter full number only" 
        
        showcounter.update()        
        fillcounter.clean()   
        fillcounter.update()

    # Contents
    #  > Counter viewer
    showcounter = ft.Text(        
        value = "Fill the second and click the button to start the countdown",
        style = "displayLarge",
        weight = 'w900',
        color = ft.colors.RED_300,
        text_align = 'center',                
    )
    # > User input
    fillcounter = ft.TextField(
        expand = 6,
        label = 'Enter the second',              
    )
    # > Submit Button
    submitbtn = ft.FilledButton(
        expand = 4,
        text = 'Start Counting',            
        on_click = countdown       
    )

    # Content Wrappers
    # > Wrapper for app control
    controlwrapper = ft.Row(
        expand = 2,
        controls = [fillcounter, submitbtn]
    )
    # > Wrapper for counter viewer
    msgwrapper = ft.Container(
        expand = 8,
        content = showcounter,
        alignment = ft.alignment.center
    )
    # > Combining both wrappers to a column layout 
    counterwrapper = ft.Column(
        controls = [msgwrapper, controlwrapper],
        alignment = 'center',
        horizontal_alignment = 'center',
    )

    # Application Layout
    wrapping = ft.Container(
        content = counterwrapper,
        bgcolor= ft.colors.AMBER_100,
        alignment = ft.alignment.center,
        width = page.window_width * 0.9,
        height = page.window_height * 0.9,
        border_radius = 15
    )
    
    # Add layout to window
    page.add(wrapping)

# Build App
ft.app(target = main)