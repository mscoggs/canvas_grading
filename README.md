# canvas_grading
For a class with N students and Q questions, a grader will have to download and wait for an answer to open NQ times. This makes me sad. To avoid this, this script combines all of the students responses into Q pdfs, one per question.


## REQUIREMENTS
- python
- glob
- PyPDF2
- FPDF

## USAGE
You have to download the submission files from canvas by clicking the notorious "download all" button, then store this in "submissions/" in the same directory as the script. Hardcode each unique question ID into make_pdfs.py. Then:
 ```bash  
python make_pdfs.py i j k z
```
creates the pdfs for questions i,j,k.
