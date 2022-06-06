from docxtpl import DocxTemplate

with open(r'C:\Automation\Paper Processing\Input\variableContainerFile.csv', 'r') as csvf:
    op =csvf.readlines()

for i in op[0:]:

    CUSTOMER_NAME = i.split(",")[0]
    DAY_RATE = i.split(",")[1]

doc = DocxTemplate("C:\Automation\Paper Processing\Input\SOW Production Process Implementation.docx")
context = { 'CUSTOMER_NAME': CUSTOMER_NAME,
            'DAY_RATE': DAY_RATE }
doc.render(context)
doc.save(f"C:\Automation\Paper Processing\Output\{CUSTOMER_NAME}\{CUSTOMER_NAME}_SOW_PPI.docx")