path = input()
file_with_extension = path.split('\\')[-1]
file, extension = file_with_extension.split('.')
print(f'File name: {file}')
print(f'File extension: {extension}')
