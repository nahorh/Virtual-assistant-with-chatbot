import webbrowser as wb
from datetime import datetime
import talk
# wb.open_new('www.youtube.com')


date1=datetime.now().time().strftime('%I%M%p')
print(date1)
talk.talk(date1)