


def count(log_file):


        print(log_file)
        total = 0
        info = 0
        warning = 0
        performance = 0
        throwable = 0
        stacktrace = 0
        error = 0

        total_dict = {}
        info_dict = {}
        performance_dict = {}

        types = ('INFO', 'WARNING', 'PERFORMANCE', 'ERROR')

        with open(log_file, 'r') as f:
            for line in f:

                if line.startswith(types):
                    try:
                        splitcolon = line.split(':')
                        timestamp = splitcolon[1]
                        splittime = timestamp.split()
                        month = splittime[0]
                        day = splittime[1]
                        hour = splittime[2]
                        minute = splitcolon[2]

                        hourminute = '{}{}'.format(hour, minute)

                        if hourminute not in total_dict:
                            total_dict[hourminute] = 0
                        else:
                            total_dict[hourminute] += 1
                    except:
                        pass


                total += 1
                if line.startswith('INFO'):
                    info += 1
                elif line.startswith('WARNING'):
                    warning += 1
                elif line.startswith('PERFORMANCE'):
                    performance += 1
                elif line.startswith('THROWABLE'):
                    throwable += 1
                elif line.startswith('STACKTRACE'):
                    stacktrace += 1
                elif line.startswith('ERROR'):
                    error += 1
                










        print('TOTAL: {}'.format(total))
        print('INFO: {}'.format(info))
        print('WARNING: {}'.format(warning))
        print('PERFORMACE: {}'.format(performance))
        print('THROWABLE: {}'.format(throwable))
        print('STACKTRACE: {}'.format(stacktrace))
        print('ERROR: {}'.format(error))


        with open('output/{}{} - MineTracking - Total.csv'.format(month,day), 'w') as c:
            for key, value in total_dict.items():
                c.write('{},{}\n'.format(key, value))

