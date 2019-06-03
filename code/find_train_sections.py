import csv
import sys


def get_sub_file_name(sub_file_counter):
    return str(sub_file_counter) + '.csv'


def split_train_data(in_train_file_name, out_summary_file_name):
    out_summary_file = open(out_summary_file_name, "w+", buffering=1)

    with open(in_train_file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # skip the header as we do not want to convert the header
        # title to float
        next(readCSV)

        row_number = 1
        sub_file_counter = 0

        sub_file_name = get_sub_file_name(sub_file_counter)
        sub_file = open(sub_file_name, "w+")

        last_time = -9999
        for row in readCSV:
            this_time = float(row[1])
            if this_time > last_time:
                output_text = 'last row_number: ' + str(row_number - 1) + \
                              ', last_time: ' + str(last_time)
                print(output_text)
                print(output_text, file=out_summary_file)
                output_text = 'this row_number: ' + str(row_number) + \
                              ', this_time: ' + str(this_time)
                print(output_text)
                print(output_text, file=out_summary_file)

                # close the sub_file
                sub_file.close()
                # update the sub_file counter
                sub_file_counter = sub_file_counter + 1
                # create a new sub_file
                sub_file_name = get_sub_file_name(sub_file_counter)
                # open the new sub_file
                sub_file = open(sub_file_name, "w+")

            # write the row in sub_file
            print(','.join(row), file=sub_file)

            last_time = this_time
            row_number = row_number + 1

            # show the progress, just for tracking
            if row_number % 1000000 == 0:
                output_text = str(row_number // 1000000) + 'm'
                print(output_text)
                # print(output_text, file=out_summary_file)

    out_summary_file.close()

if __name__ == "__main__":
    print(sys.argv[1], sys.argv[2])
    split_train_data(sys.argv[1], sys.argv[2])
    # split_train_data('/Users/roozbehdaneshvar/temp/temp-train.csv',
    #                  '/Users/roozbehdaneshvar/temp/temp-summary.txt')
