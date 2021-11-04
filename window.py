from OpenGL.GL import *
import glfw

class Window:
    def resize(self, window, width, height):
        glViewport(0, 0, width, height)

    def __init__(self, width:int, height:int, title:str, drawSetup = None):
        
        if not glfw.init():
            raise Exception("Não foi possível iniciar a lib GLFW")

        #Cria a tela com os parametros necessários
        self._win = glfw.create_window(width, height, title, None, None)
        
        if not self._win:
            glfw.terminate()
            raise Exception("Não foi possível criar a tela GLFW")

        #Define a posição da tela no monitor
        glfw.set_window_pos(self._win, 400, 200)

        #Redimensionar viewport conforme tamanho da tela
        glfw.set_window_size_callback(self._win, self.resize)

        #Define o contexto atual
        glfw.make_context_current(self._win)

        if drawSetup != None:
            drawSetup()

    def mainLoop(self, drawFunction = None):
        #Loop principal
        while not glfw.window_should_close(self._win):
            glfw.poll_events()

            #Ao gerar um novo quadro, limpar também o z-buffer
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glShadeModel(GL_SMOOTH)

            if drawFunction != None:
                drawFunction()

            glfw.swap_buffers(self._win)
        
        glfw.terminate()