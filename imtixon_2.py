import pdfkit
import threading

b_url = 'https://tilshunos.com/paronims/?page='

path_wkh = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf=path_wkh)

def wkh_to_pdf(i):
    pdfkit.from_url(b_url +str(i),'tilshunoslik '+ str(i) + '.pdf', configuration = config)
    print(str(i)+'saved')

th = []

for i in range(1,5):
    t = threading.Thread(target=wkh_to_pdf, args=(i,))
    th.append(t)
    t.start()


for thr in th:
    thr.join()
