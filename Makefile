# -*- Makefile -*-

-include $(buildTop)/share/dws/prefix.mk

srcDir        ?= .
installTop    ?= $(VIRTUAL_ENV)
binDir        ?= $(installTop)/bin

installBins   ?= /usr/bin/install -s -p -m 755
installDirs   ?= /usr/bin/install -d

CXXFLAGS      += -g

bins          := podofo-flatform

LDLIBS += -lpodofo -lfreetype -lfontconfig -ljpeg -lcrypto -lidn -lz
ifeq ($(filter Darwin,$(distHost)),)
LDLIBS +=  -lpthread
endif

libSearchPath ?= $(patsubst -L%,%,$(filter -L%, $(LDFLAGS)))


all:: podofo-flatform

install:: $(bins)
	$(if $^,$(installDirs) $(DESTDIR)$(binDir))
	$(if $^,$(installBins) $^ $(DESTDIR)$(binDir))

podofo-flatform: podofo-flatform.cc

vpath %.cc      $(srcDir)/src
