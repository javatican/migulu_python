import os, random, pygame
from director import Scene
from director import Director
from statement import Statement

class SceneHome(Scene):
    WHITE = (255, 255, 255)
    BLACK1 = (0, 0, 0)
    BLACK2 = (32, 32, 32)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    GREY = (192, 192, 192)
    ORIGIN_X = 1
    ORIGIN_Y = 1
    FONT=None
    STM_SURFACE=None
    VISIBLE_STM_COUNT=0
    #
    @classmethod
    def get_text(cls, filename):
        dir_name = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_name, filename)
        text_list = []
        source_file = open(file_path, "r")
        for line in source_file:
            #remove newline char
            if line[-1] == '\n':
                line = line[:-1]
            text_list.append(line)
        return text_list
    @classmethod
    def get_font(cls):
        if not cls.FONT:
            cls.FONT = pygame.font.SysFont("dejavuserif", 18)
        return cls.FONT

    @classmethod
    def get_stm_surface(cls):
        if not cls.STM_SURFACE:
            font = cls.get_font()
            width = Director.WIDTH
            height = font.get_height()+0.5*font.get_linesize()
            cls.STM_SURFACE = pygame.Surface((width, height))
        return cls.STM_SURFACE
    @classmethod
    def get_visible_stm_count(cls):
        if not cls.VISIBLE_STM_COUNT:
            stm_sur = cls.get_stm_surface()
            cls.VISIBLE_STM_COUNT = Director.HEIGHT//stm_sur.get_rect().height
        return cls.VISIBLE_STM_COUNT

    def __init__(self, director, filename):
        super().__init__(director)
        self.filename = filename
        #
        self.stms_list = Statement.create_stms(
            SceneHome.get_text(self.filename))

        director.screen.fill(SceneHome.BLACK1)
        self.display_text(17)

    def display_text(self, start=0):
        font = SceneHome.get_font()
        stm_surface = SceneHome.get_stm_surface()
        lines = len(self.stms_list)
        end = min(lines, start+SceneHome.get_visible_stm_count())
        line_no_width = font.size(str(lines*10))[0]
        text_y = (stm_surface.get_rect().height-font.get_height())*0.5
        for i, stm in enumerate(self.stms_list[start:end]):
            if i%2:
                stm_surface.fill(SceneHome.BLACK1)
            else:
                stm_surface.fill(SceneHome.BLACK2)
            pos_x = SceneHome.ORIGIN_X
            #display line no
            line_no_sur = font.render(str(stm.get_line_no()), True, SceneHome.RED, SceneHome.GREY)
            stm_surface.blit(line_no_sur, (pos_x, text_y))
            #display text
            pos_x = SceneHome.ORIGIN_X + line_no_width
            text_sur = font.render(stm.get_text(), True, SceneHome.YELLOW)
            stm_surface.blit(text_sur, (pos_x, text_y))
            #blit stm_surface to root window
            pos_y = SceneHome.ORIGIN_Y + i*(stm_surface.get_rect().height)
            self.director.screen.blit(stm_surface, (pos_x, pos_y))

    def on_update(self):
        pass

    def on_event(self, event):
        pass

    def on_draw(self, screen):
        pass
