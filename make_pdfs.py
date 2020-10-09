
import sys,os
import PyPDF2
import glob
from fpdf import FPDF

def make_names_pdf(full_name):
    try:
        name = full_name.replace("_", " ")
    except:
        name = full_name
    pdf = FPDF(unit="mm",format=[100,40])
    pdf.set_font("Arial", size = 15)

    pdf.add_page()
    pdf.cell(100,40, txt = name, align="t")
    pdf.output("name.pdf")

def pdf_cat(q_nums):

    pdfWriter = PyPDF2.PdfFileWriter()
    old_name, questions, counts = "", [[],[],[],[],[],[],[],[],[]],  [0,0,0,0,0,0,0,0,0]

    print("\n\n...Loading submissions...\n\n\n")
    for filename in sorted(glob.glob('submissions/*.pdf')):
        new_name = filename.split("_question")[0].split("\\")[1]
        if(old_name != new_name): q = 0
        questions[q].append(filename)
        counts[q] = counts[q] + 1
        old_name=new_name
        q+=1

    q=0
    for question in questions:
        file_count = 0
        q+=1
        print("\n\n")
        if(str(q) not in q_nums): continue
        for filename in question:

            print("\rCreating question_"+str(q)+".pdf, ", file_count,"/",counts[q], " submissions appended", end="")
            full_name =  filename.split("_question")[0].split("\\")[1]
            full_name = ''.join([i for i in full_name if not i.isdigit()])
            make_names_pdf(full_name)

            f = open("name.pdf", 'rb')
            pageObj = (PyPDF2.PdfFileReader(f)).getPage(1)
            pdfWriter.addPage(pageObj)

            try:
                pdfFileObj = open(filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)

            except:
                make_names_pdf("Error Reading File")
                pageObj = (PyPDF2.PdfFileReader(open("name.pdf", 'rb'))).getPage(1)
                pdfWriter.addPage(pageObj)


            pdfOutput = open('question_'+str(q)+'.pdf', 'wb')
            pdfWriter.write(pdfOutput)
            pdfOutput.close()
            file_count+=1
            f.close()




def main(q_nums):
    pdf_cat(q_nums)




if __name__ == "__main__":
   main(sys.argv[1:])
