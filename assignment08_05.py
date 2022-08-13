# Завдання: додати відсутні інструкції у наданому коді.
#           По завершенню програми повинно залишатись два файла
#           generated_sequence.txt з числовою, рандомно сгенерованою,
#           послідовністю (з переносами строк, у колонку)
#           та generated_matrix.txt у якому
#           таж сама послідовність представлена у виді двовимірной матриці
#           (також і візуально, з пробілами між елементами у рядку та переносами строк
#           між рядками, перший рядок файлу - розмірність матриці - n m).
#
# Підказки: використати toolset пакет з попередної домашки,
#           write, f-string/format, close
#
# Підказки:
#   * open(filename, options="r") - відкриває файл filename на читання та
#                                   повертає file_obj (файловий об'ект)
#                                   усі дії з файлом виконуються за допомогою
#                                   файлового об'єкта (основні дії: читання з/запис в)
#   * file_obj.read()/file_obj.readline() - зчитати увесь файл/одну строку з файла
#   * file_obj.write(data)/file_obj.writelines() - записати data (строка, умовно) /
#                                                 список строк
#   * file_obj.close() - закриває об'єект файлу (файл це ресурс, додаток має ліміт на
#                        кількість відкритих одночасно файлів - тому - закриваємо файл
#                        як тільки він нам не потрібний.
#   * with open(filenmae) as f:  # - спеціальна конструкція (у загальному значенні context manager)
#         lines = [line.strip() for line in f] # file_obj - iterable можемо використати у циклі
#                                              # with конструкція закриває f (викликає f.close() за
#                                              # розробника, по завершенню блока with, автоматично).
#   * f.write("\n")  напечатає перехід на новий рядок у файлі
#   * ', '.join(sequence) - надає можливість об'єднати елементи послідовності у строку розділені комами

import sequences

GENERATED_SEQ_FILE = "generated_sequence.txt"
GENERATED_MATRIX_FILE = "generated_matrix.txt"


def store_sequence(filename, seq):

    if not len(seq):
        return

    output_file = open(filename, "w")
    with open(filename, "w") as seq_file:
        for el in seq:
            seq_file.write(str(el))
            seq_file.write("\n")        # зберігаємо елемент у файл + в колонці
        return seq_file                 # повертаємо файл (ресурс) операційній системі


def store_matrix(filename, matrix):

    if not len(matrix) or not len(matrix[0]):
        raise RuntimeError("Strictly two-dimensional matrix is required")

    n, m = len(matrix), len(matrix[0])
    with open(filename, "w") as matrix_file:

        # зберігаємо спочатку розмірність - n m - у файл
        # новий рядок (у разі коли це не перша строка матриці)

        matrix_file.write(str(n) + ' x ' + (str(m)))
        matrix_file.write('\n')

        # зберігаємо кожний елемент у файл

        for row in matrix:
            for el in row:
                matrix_file.write(' '.join(map(str, row)))
                matrix_file.write("\n")
                break


def main():
    n, m = 5, 5
    seq = sequences.random_list(n*m, 0, n+m)
    store_sequence(GENERATED_SEQ_FILE, seq)
    matrix = [[seq[i*m+j] for j in range(m)] for i in range(n)]
    store_matrix(GENERATED_MATRIX_FILE, matrix)


if __name__ == "__main__":
    main()
