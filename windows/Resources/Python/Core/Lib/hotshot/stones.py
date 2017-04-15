# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: stones.py
import errno
import hotshot
import hotshot.stats
import sys
import test.pystone

def main(logfile):
    p = hotshot.Profile(logfile)
    benchtime, stones = p.runcall(test.pystone.pystones)
    p.close()
    print 'Pystone(%s) time for %d passes = %g' % (
     test.pystone.__version__, test.pystone.LOOPS, benchtime)
    print 'This machine benchmarks at %g pystones/second' % stones
    stats = hotshot.stats.load(logfile)
    stats.strip_dirs()
    stats.sort_stats('time', 'calls')
    try:
        stats.print_stats(20)
    except IOError as e:
        if e.errno != errno.EPIPE:
            raise


if __name__ == '__main__':
    if sys.argv[1:]:
        main(sys.argv[1])
    else:
        import tempfile
        main(tempfile.NamedTemporaryFile().name)