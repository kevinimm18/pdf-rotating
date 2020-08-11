import PyPDF2

# mode read binary (rb) karena PDF only can read dalam format binary
with open('dummy.pdf', 'rb') as file:
# Kita baca file nya "dummy.pdf" pake method PdfFileReader
	reader = PyPDF2.PdfFileReader(file)
# Kita ambil halaman 1 dari pdf nya (ingat Python calculate start from 0)
	page = reader.getPage(0)
# Kita lakukan treatment (perlakuan) memutar file pdf nya 90 derajat counter clock
	page.rotateCounterClockwise(90)
#Kita tulis (write) file nya dengan isi pdf yang sudah di treatment
	writer = PyPDF2.PdfFileWriter()
# Buat halamannya
	writer.addPage(page)
# Buat nama file baru dengan nama 'tilt' dan format write binary (wb)
	with open('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)