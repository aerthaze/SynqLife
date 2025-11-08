import datetime
import locale
try:
    locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')
except:
    locale.setlocale(locale.LC_TIME, '')

def durasi_tidur(start_time, end_time):
    format = '%H:%M'
    start = datetime.datetime.strptime(start_time, format)
    end = datetime.datetime.strptime(end_time, format)
    if end < start:
        end += datetime.timedelta(days=1)

    durasi = end - start
    total_menit = durasi.seconds // 60
    jam = total_menit // 60
    menit = total_menit % 60
    return f"Anda tidur selama {jam} jam dan {menit} menit."