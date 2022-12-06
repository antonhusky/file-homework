text_dict = {}
for i in range(1, 4):
    file_name = f'{i}.txt'
    with open(file_name, 'rt', encoding='utf-8') as file:
        text_dict[file_name] = file.readlines()

with open('result.txt', 'wt', encoding='utf-8') as file:
    for key, value in sorted(text_dict.items(), key=lambda x: -len(x[1])):
        file.write(f'{key}\n')
        file.write(f'{str(len(value))}\n')
        file.write('\n'.join(value))
        file.write('\n')