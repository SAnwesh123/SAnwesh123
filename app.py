from operator import indexOf

def replace_file_content():
    path = r'C:\Users\Anwesh Saho\OneDrive\Desktop\Assignment FSDS_ML_Books\Python_Project\content.txt'
    with open(path, 'r+') as f:
        content = f.read()
        temp = content.split()
        idx= indexOf(temp,'placement')
        temp[idx]= 'screening'
        f.write('\n')
        f.write(' '.join(temp))



replace_file_content()
