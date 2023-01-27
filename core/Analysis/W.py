from wordcloud import ImageColorGenerator
from wordcloud import WordCloud as wc
from PIL import Image
import numpy as n

ff=open('core\MD\mdeditor\editormd\jquery-3.5.1.min.js').read() #导入文本文件并读取内容
bg=n.array(Image.open('core\Analysis\wallhaven-yj7o2l_1500x907.png')) #将图片以数组形式输出
 
 
#注意如果背景图片是png,那么模式必须是RGBA，因为png图片支持透明度设置,设置背景图片，背景颜色必须是白色
w=wc(font_path=r'assets\梦死醉生.ttf',mode='RGBA',mask=bg,repeat=True,background_color='#FFFFFF', random_state=8, scale=3)
wg=w.generate(ff) #嵌入文本
ig=ImageColorGenerator(bg) #图片颜色导入
wg.recolor(color_func=ig) #重新设置词云图颜色
wg.to_file('gf.png') #保存图片