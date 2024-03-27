# Staratedy Pettern : Dat Reporting Startegies
import webbrowser
from abc import ABC, abstractmethod
from turtle import pd


# inteface

class DataReportingStradegy(ABC):
    @abstractmethod
    def generate_report(self):
         pass


# concrete classes
 class TextReportStradegy(DataReportingStradegy):

     def generate_report(self, data):
         data_frame = pd.DataFrame(data)
       #  pd.set_option('display.max_columns', None)
         report = f"Text Report:\n{data_frame}"\n\nDescrobe Analys: \n{data_frame.describe()}"
         print(report)
         return  report

class CSVReportStradegy(DataReportingStradegy):

    def generate_report(self, data):
        #Assume data is a list of dictionaries
        header = ','.join(data[0].keys())
        rows = '\n'.join([','.join(map(str,row.values())) for row in data])
        report = f"CSV Report:\n{header}\n{rows}"
        with open("report.csv", "w") as csv_file:
            csv_file.write(f"{header}\n{rows}")

        print(report)
        return report

class ReturnReportStradegy(DataReportingStradegy):
    def generate_report(self,data):
        print(data)

class HTMLReportStradegy(DataReportingStradegy):
    def generate_report(self,data):
        data_frame = pd.DataFrame(data)
        report_html = f"<h1>Text Report:</h1>\n{data_frame.to_html()}\n\n<h1>Describe Analysis:</h1>\n{data_frame.describe().to_html()}

        #save the HTML report to a file

        with open("report.html", "w") as html_file:
            html_file.write(report_html)

        webbrowser.open("report.html")
        print("HTML Report generated successfully:")
        return  report_html

class DataReportingContext:
    def __init__(self):
        pass


