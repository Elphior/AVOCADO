import searching_algorithm
import sorting_algorithm
import glfw
from OpenGL.GL import *
import imgui
from imgui.integrations.glfw import GlfwRenderer


def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()


def init_window(width, height, title):
    if not glfw.init():
        raise Exception("GLFW initialization failed")
    
    window = glfw.create_window(width, height, title, None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window creation failed")

    glfw.make_context_current(window)
    return window

def render_gui():
    imgui.new_frame()
    if imgui.begin("Tab Window", True):
        
        if imgui.begin_tab_bar("MyTabs"):
            if imgui.begin_tab_item("Tab 1").selected:
                imgui.text("Rendering OpenGL in Tab 1")
                imgui.end_tab_item()

            if imgui.begin_tab_item("Tab 2").selected:
                imgui.text("Rendering OpenGL in Tab 2")
                imgui.end_tab_item()

            if imgui.begin_tab_item("Tab 3").selected:
                imgui.text("Rendering OpenGL in Tab 3")
                imgui.end_tab_item()

            imgui.end_tab_bar()
    
    imgui.end()


def main():
    window = init_window(800, 600, "GLFW Window with Tabs")
    imgui.create_context()
    impl = GlfwRenderer(window)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()
        glClear(GL_COLOR_BUFFER_BIT)
        render_gui()
        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)
    impl.shutdown()
    glfw.terminate()

if __name__ == "__main__":
    main()