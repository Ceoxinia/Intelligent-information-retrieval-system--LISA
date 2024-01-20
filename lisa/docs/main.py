import os


if __name__ == '__main__':
    directory_path = './org_docs/'
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)

        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:

                file_contents = file.read()

                docs=file_contents.split('\n********************************************\n')
                for doc in docs:
                    if doc!=' ':
                        lines=doc.splitlines()
                        try:
                            first_line=lines[0]
                            first_line=first_line.split()
                            doc_id=first_line[1]
                            if doc_id!='APPLICATIONS':

                                new_doc='\n'.join(lines[1:])
                                out_file_path='./sep_docs/D'+str(doc_id)+'.txt'
                                with open(out_file_path,'w') as out_file:                                    out_file.write(new_doc)
                        except Exception as e:
                            pass