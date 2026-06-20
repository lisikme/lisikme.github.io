# import webview
# # webview.create_window('Привет, мир!', 'https://example.com')  # или html='<h1>Hello</h1>'
# webview.create_window('Привет, мир!', 'file:///C:/Users/LisikMe/Desktop/WinAPP/index.html')  # или html='<h1>Hello</h1>'
# webview.start()

import webview

title = 'KetaMeFM'
url = 'file:///C:/Users/LisikMe/Desktop/WinAPP/index.html'
width, height = 700, 500
webview.create_window(
    title = title,
    url = url,
    width = width,
    height = height
)
webview.start()