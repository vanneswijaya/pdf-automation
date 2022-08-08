from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display
from datetime import timedelta, date, datetime
import os


def Draw(bulanInp, tanggalInp, h1, h2, h3, filename_output):
    background = "kosong.png"
    white = "#FFFFFF"
    black = '#000000'
    font_type = "./bebasneue.ttf"

    # Set background
    with Image(filename=background) as img_background:
        with Drawing() as bulan:
            bulan.font = font_type
            bulan.fill_color = Color(black)
            bulan.font_size = 250
            bulan.font_weight = 700
            metrics = bulan.get_font_metrics(img_background,bulanInp,multiline = True)
            bulan.text(
                x = 500,
                y = 400,
                body = bulanInp
            )
            bulan(img_background)

        with Drawing() as tanggal1:
            # tanggal1.font = font_text
            tanggal1.font = font_type
            tanggal1.fill_color = Color(white)
            tanggal1.font_size = 70
            metrics = tanggal1.get_font_metrics(img_background,str(tanggalInp-2),multiline = True)
            tanggal1.text(
                x = 420,
                y = 570,
                body = str(tanggalInp-2)
            )
            tanggal1(img_background)

        with Drawing() as hari1:
            hari1.font = font_type
            hari1.fill_color = Color(white)
            hari1.font_size = 70
            hari1.font_weight = 700
            metrics = hari1.get_font_metrics(img_background,h1,multiline = True)
            hari1.text(
                x = 610,
                y = 570,
                body = h1
            )
            hari1(img_background)

        with Drawing() as tanggal2:
            # tanggal2.font = font_text
            tanggal2.font = font_type
            tanggal2.fill_color = Color(white)
            tanggal2.font_size = 70
            metrics = tanggal2.get_font_metrics(img_background,str(tanggalInp-1),multiline = True)
            tanggal2.text(
                x = 940,
                y = 1160,
                body = str(tanggalInp-1)
            )
            tanggal2(img_background)

        with Drawing() as hari2:
            hari2.font = font_type
            hari2.fill_color = Color(white)
            hari2.font_size = 70
            hari2.font_weight = 700
            metrics = hari2.get_font_metrics(img_background,h2,multiline = True)
            hari2.text(
                x = 1110,
                y = 1160,
                body = h2
            )
            hari2(img_background)

        with Drawing() as tanggal3:
            # tanggal3.font = font_text
            tanggal3.font = font_type
            tanggal3.fill_color = Color(white)
            tanggal3.font_size = 70
            metrics = tanggal3.get_font_metrics(img_background,str(tanggalInp),multiline = True)
            tanggal3.text(
                x = 430,
                y = 1760,
                body = str(tanggalInp)
            )
            tanggal3(img_background)

        with Drawing() as hari3:
            hari3.font = font_type
            hari3.fill_color = Color(white)
            hari3.font_size = 70
            hari3.font_weight = 700
            metrics = hari3.get_font_metrics(img_background,h3,multiline = True)
            hari3.text(
                x = 610,
                y = 1750,
                body = h3
            )
            hari3(img_background)

        img_background.format = "png"
        img_background.save(filename=filename_output)
    
    return filename_output

daydict = {
    'WEDNESDAY':'RABU',
    'THURSDAY':'KAMIS', 
    'FRIDAY':'JUMAT', 
    'SATURDAY':'SABTU', 
    'SUNDAY':'MINGGU', 
    'MONDAY':'SENIN', 
    'TUESDAY':'SELASA'
}
months = ['JANUARI', 'FEBUARI', 'MARET', 'APRIL', 'MEI', 'JUNI', 'JULI', 'AGUSTUS', 'SEPTEMBER', 'OKTOBER', 'NOVEMBER', 'DESEMBER']

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_year = int(input('Masukkan tahun start: '))
start_month = int(input('Masukkan bulan start: '))
start_day = int(input('Masukkan tanggal start : '))
end_year = int(input('Masukkan tahun finish: '))
end_month = int(input('Masukkan bulan finish: '))
end_day = int(input('Masukkan tanggal finish : '))
print('=============================')
folder_save = input('Masukkan nama folder untuk tempat save : ')

parentdir = '/Users/osissmakanisius/Documents/OSIS 20:21/JURNAL'
path = os.path.join(parentdir, folder_save)
os.mkdir(path)

start_date = date(start_year, start_month, start_day)
end_date = date(end_year, end_month, end_day)
counter = 1
datelist = []
for single_date in daterange(start_date, end_date):
    datelist.append(str(single_date.strftime("%A")).upper())
    if counter == 3:
        bulan_input = f'{months[single_date.month-1]} {single_date.year}'
        Draw(bulan_input, single_date.day, daydict[datelist[0]], daydict[datelist[1]], daydict[datelist[2]], f'{folder_save}/{folder_save}{single_date.day-2}.png')
        datelist.pop()
        datelist.pop()
        datelist.pop()
        counter = 1
        continue
    counter += 1


# for x in range(1,32,3):
#     Draw('JULI 2020', x, days[0], days[1], days[3], f'{x}.png')