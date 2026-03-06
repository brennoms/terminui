#para testes

from terminui.terminui import Terminui
from terminui.core.content import Content

terminui = Terminui()

content = Content()
content.background_color = 'green'
content.width = 10
content.height = 5
content.pos_x = 10
content.pos_y = 5

terminui.addContent(content)

terminui.start()
