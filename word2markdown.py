from pydocx import PyDocX
html = PyDocX.to_html(r"C:\Users\jwx5319396\Desktop\docx2html.docx")
with open(r"C:\Users\jwx5319396\Desktop\docx2html.html", 'w',encoding='utf-8') as f:
    f.write(html)
