#para testes

from terminui.terminui import Terminui
from terminui.core.content import Content

terminui = Terminui()
terminui.style.bg.color = 'cyan'

content = Content()
content.style.bg.color = 'green'
content.style.fg.color = 'black'
content.txtblock.text = 'green'
content.size.width = 10
content.size.height = 5
content.pos.x = 10
content.pos.y = 5
terminui.addContent(content)

content2 = Content()
content2.style.bg.color = 'red'
content2.style.fg.color = 'black'
content2.txtblock.text = 'red'
content2.size.width = 10
content2.size.height = 5
content2.pos.x = 20
content2.pos.y = 10
terminui.addContent(content2)

content3 = Content()
content3.style.bg.color = 'blue'
content3.style.fg.color = 'black'
content3.txtblock.text = 'blue'
content3.size.width = 10
content3.size.height = 5
content3.pos.x = 20
content3.pos.y = 5
terminui.addContent(content3)

content4 = Content()
content4.style.bg.color = 'white'
content4.style.fg.color = 'black'
content4.txtblock.text = 'white'
content4.size.width = 10
content4.size.height = 5
content4.pos.x = 10
content4.pos.y = 10
terminui.addContent(content4)

terminui.start()
