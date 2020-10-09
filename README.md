A script which streamlines the grading process by combining individual pdfs across 300+ students into a single pdf for each question that they answer.

All you need is the most recent version of python, along with the 3 packages: glob, PyPDF2, and FPDF (all of which I think can be installed with "pip install NAME" from the windows command line, not sure about other OS).

You have to download the submission files from canvas by clicking the notorious "download all" button, then store this in "submissions/" in the same directory as the script.

Then "python make_pdfs.py i j k z" creates the pdfs for question i,j,k and z.
