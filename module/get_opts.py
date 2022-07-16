import sys


def get_opts(_opts):
    argv = sys.argv[1:]
    opts = dict()
    # print(sys.argv[1:])
    for i in range(0, len(argv)):
        opt = argv[i]
        if '=' not in opt and '--' in opt:  # pm2 args: "--interpreter python3 --host 127.0.0.1 --port 8001 ",
            name = opt.replace('-', '', 2)
            param = argv[i + 1]
            if ('--' not in param) and (_opts.count(name) != 0):
                opts[name] = param
        if '=' in opt and '--' in opt:  # --host=127.0.0.1 --port=8001
            [opt_name, param] = opt.split('=', 1)
            name = opt_name.replace('-', '', 2)
            if _opts.count(name) != 0:
                opts[name] = param
        else:
            continue
    return opts
