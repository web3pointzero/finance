from django.shortcuts import render_to_response, get_object_or_404
import csv


def rsi(request):
	return render_to_response("rsi.html")

def csv2graph(request):
    days = 14
    #reader = csv.reader(open("/home/nedo/Projects/finance/static/csv/data.csv"), delimiter=',')
    #reader = csv.reader(open("/home/nedo/Projects/finance/static/csv/data2.csv"), delimiter=',')
    reader = csv.reader(open("/home/ahmet/code/finance/static/csv/data.csv"), delimiter=',')
    datalist = []

    for row in reader:
        if reader.line_num > 1:
            datalist.append([row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4])])

    for i in range(len(datalist)-days):
        upsum = downsum = 0
        for j in range(days):
            upsum += (datalist[i+j][4]-datalist[i+j+1][4])>0 and (datalist[i+j][4]-datalist[i+j+1][4]) or 0.0
        for j in range(days):
            downsum += (datalist[i+j][4]-datalist[i+j+1][4])<0 and abs(datalist[i+j][4]-datalist[i+j+1][4]) or 0.0
        datalist[i].append(100-(100/(1+upsum/downsum))) #rsi

    datalist = datalist[:len(datalist)-30]
    datalist.reverse()

    return render_to_response("csv.html", {'datalist': datalist})
