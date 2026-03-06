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

content2 = Content()
content2.background_color = 'red'
content2.width = 10
content2.height = 5
content2.pos_x = 20
content2.pos_y = 10
terminui.addContent(content2)

content3 = Content()
content3.background_color = 'blue'
content3.width = 10
content3.height = 5
content3.pos_x = 20
content3.pos_y = 5
terminui.addContent(content3)

content4 = Content()
content4.background_color = 'blue'
content4.width = 10
content4.height = 5
content4.pos_x = 10
content4.pos_y = 10
terminui.addContent(content4)

terminui.start()
