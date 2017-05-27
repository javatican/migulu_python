import os, random, pygame, math
from director import Scene
from director import Director
from statement import Statement

class SceneHome(Scene):
    WHITE = (255, 255, 255)
    BLACK1 = (0, 0, 0)
    BLACK2 = (32, 32, 32)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREY = (192, 192, 192)
    MOUSE_LEFT = 1
    WHEEL_UP = 4
    WHEEL_DOWN = 5
    ORIGIN_X = 1
    ORIGIN_Y = 1
    FONT = None
    LARGE_FONT = None
    STM_SURFACE = None
    VISIBLE_STM_COUNT = 0
    MAGNIFIER_WIDTH = Director.WIDTH
    MAGNIFIER_TEXT_WIDTH = MAGNIFIER_WIDTH - 20
    #

    @classmethod
    def split(cls, text, font):
        txt_list = []
        required_size = font.size(text)
        if required_size[0] <= SceneHome.MAGNIFIER_TEXT_WIDTH:
            txt_list.append(text)
        else:
            portions = math.ceil(required_size[0]/SceneHome.MAGNIFIER_TEXT_WIDTH)
            length = len(text)
            print("length:",length)
            sect = math.ceil(length/portions)
            print("sect:",sect)
            #
            t = text
            while len(t):
                print("t:",t)
                if font.size(t)[0] > SceneHome.MAGNIFIER_TEXT_WIDTH:
                    i = sect
                    while i > 0 and (t[i-1].isalnum() and t[i].isalnum() or font.size(t[:i])[0] > SceneHome.MAGNIFIER_TEXT_WIDTH):
                        i -= 1
                    txt_list.append(t[:i])
                    t = t[i:]
                else:
                    txt_list.append(t)
                    break
            # start = 0
            # for i in range(portions):
            #     txt_list.append(text[start:min(start+sect, length)])
            #     start += sect
        return txt_list

    @classmethod
    def get_text(cls, filename):
        """ extract text from filename """
        dir_name = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_name, filename)
        text_list = []
        source_file = open(file_path, "r")
        for line in source_file:
            # remove newline char
            if line[-1] == '\n':
                line = line[:-1]
            text_list.append(line)
        return text_list

    @classmethod
    def get_font(cls):
        if not cls.FONT:
            #cls.FONT = pygame.font.SysFont("dejavuserif", 18)
            cls.FONT = pygame.font.Font("Cyberbit.ttf", 18)
        return cls.FONT

    @classmethod
    def get_large_font(cls):
        if not cls.LARGE_FONT:
            #cls.LARGE_FONT = pygame.font.SysFont("dejavuserif", 36)
            cls.LARGE_FONT = pygame.font.Font("Cyberbit.ttf", 36)
        return cls.LARGE_FONT

    @classmethod
    def get_stm_surface(cls):
        """ a rectangle surface on which a text of statement will be blitted"""
        if not cls.STM_SURFACE:
            font = cls.get_font()
            width = Director.WIDTH
            height = font.get_height()+0.5*font.get_linesize()
            cls.STM_SURFACE = pygame.Surface((width, height))
        return cls.STM_SURFACE

    @classmethod
    def get_visible_stm_count(cls):
        """ total lines of statements that can be shown in the root window """
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

        self.visiable_start = 0
        self.visiable_end = 0
        self.magnifier = False
        self.display_text()

    def display_text(self, start=0, force=False):
        font = SceneHome.get_font()
        stm_surface = SceneHome.get_stm_surface()
        lines = len(self.stms_list)
        # end: the last line index that is visible
        end = min(lines, start+SceneHome.get_visible_stm_count())
        # recalcate start
        start = min(start, max(end-SceneHome.get_visible_stm_count(), 0))
        if (not force) and start == self.visiable_start and end == self.visiable_end:
            return
        self.director.screen.fill(SceneHome.BLACK1)
        # line_no_width: width in pixel for the line number
        line_no_width = font.size(str(lines*10))[0]
        # y position used by bliting for the statement text
        text_y = (stm_surface.get_rect().height-font.get_height())*0.5
        for i, stm in enumerate(self.stms_list[start:end]):
            if i % 2:
                stm_surface.fill(SceneHome.BLACK1)
            else:
                stm_surface.fill(SceneHome.BLACK2)
            pos_x = SceneHome.ORIGIN_X
            # display line no
            line_no_sur = font.render(str(stm.get_line_no()), True, SceneHome.RED, SceneHome.GREY)
            stm_surface.blit(line_no_sur, (pos_x, text_y))
            # display text
            pos_x = SceneHome.ORIGIN_X + line_no_width
            text_sur = font.render(stm.get_text(), True, SceneHome.YELLOW)
            stm_surface.blit(text_sur, (pos_x, text_y))
            # blit stm_surface to root window
            pos_y = SceneHome.ORIGIN_Y + i*(stm_surface.get_rect().height)
            self.director.screen.blit(stm_surface, (SceneHome.ORIGIN_X , pos_y))
        self.visiable_start = start
        self.visiable_end = end

    def on_update(self):
        pass

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (not self.magnifier) and event.button == SceneHome.WHEEL_UP:
                self.display_text(max(0, self.visiable_start-1))
            elif (not self.magnifier) and event.button == SceneHome.WHEEL_DOWN:
                self.display_text(self.visiable_start+1)
            elif (not self.magnifier) and event.button == SceneHome.MOUSE_LEFT:
                pos = event.pos
                stm_sur = SceneHome.get_stm_surface()
                pos_index = min(pos[1]//stm_sur.get_rect().height, SceneHome.get_visible_stm_count()-1)
                stm_index = min(self.visiable_end, self.visiable_start + pos_index)
                stm = self.stms_list[stm_index]
                self.display_magnifier(stm, pos)
                self.magnifier = True
            elif self.magnifier and event.button == SceneHome.MOUSE_LEFT:
                self.magnifier = False
                self.display_text(self.visiable_start, True)

    def on_draw(self, screen):
        pass

    def display_magnifier(self, stm, pos):
        large_font = SceneHome.get_large_font()
        stripped_text = stm.get_text().strip()
        text_portions = SceneHome.split(stripped_text, large_font)
        portions = len(text_portions)
        pos_x = (SceneHome.MAGNIFIER_WIDTH - SceneHome.MAGNIFIER_TEXT_WIDTH)//2
        mag_x = SceneHome.ORIGIN_X
        height = portions*large_font.get_height()+0.5*large_font.get_linesize()
        mag_sur = pygame.Surface((SceneHome.MAGNIFIER_WIDTH, height))
        mag_sur.fill(SceneHome.GREY)
        for i, p in enumerate(text_portions):
            pos_y = 0.25*large_font.get_linesize() + i*large_font.get_height()
            text_sur = large_font.render(p, True, SceneHome.BLUE)
            mag_sur.blit(text_sur, (pos_x, pos_y))

        mag_y = pos[1]
        if mag_y + height > Director.HEIGHT:
            mag_y = Director.HEIGHT - height
        self.director.screen.blit(mag_sur, (mag_x, mag_y))
