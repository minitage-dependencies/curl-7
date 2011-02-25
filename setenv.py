import os
def h(options,buildout):
    """ Handle fedora explicit linker in fedora >= 13"""
    try:
        content = open('/etc/fedora-release').read().split()
        for i in content:
            try:
                value = int(i)
                if value >= 13:
                    print " -++++++++++++ Warning ++++++++++++++++++++++++-"
                    print "Enabling -lrt for fedora > 13 linker changes"
                    print " -++++++++++++ Warning ++++++++++++++++++++++++-"
                    if 'LDFLAGS' in os.environ:
                        os.environ['LDFLAGS'] += " -lrt"
                    else:
                        os.environ['LDFLAGS'] = "-lrt"
            except ValueError:
                pass
    except:
        pass

# vim:set ts=4 sts=4 et  :
