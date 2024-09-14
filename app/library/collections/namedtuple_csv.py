import csv
import collections

with open('library/collections/names.csv', 'w') as csvfile:
    fieldnames = ['first', 'last', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first': 'Mike', 'last': 'Jacson', 'address': 'A'})
    writer.writerow({'first': 'Jun', 'last': 'Sakai', 'address': 'B'})
    writer.writerow({'first': 'Nancy', 'last': 'Mask', 'address': 'C'})


with open('library/collections/names.csv', 'r') as f:
    csv_reader = csv.reader(f)
    # csv_readerはイテレーター
    # next(csv_reader) すると1回目は ['first', 'last', 'address']
    # headerを配列として渡すことでtupleの雛形をつくる
    Names = collections.namedtuple('Names', next(csv_reader))
    for row in csv_reader:
        # 作成した雛形にrowを入れる
        names = Names._make(row)
        print(names.first, names.last, names.address)
