import csv

class WriteToCsv:
    fields = ['1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17']

    def CsvFile(self,L):
        self.L=L
        with open("DataInCsv.csv", 'w') as csvfile:

            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(WriteToCsv.fields)

            # writing the data rows
            csvwriter.writerows(self.L)

            csvfile.close()