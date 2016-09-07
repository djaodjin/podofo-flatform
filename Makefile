# -*- Makefile -*-

-include $(buildTop)/share/dws/prefix.mk

srcDir        ?= .
installTop    ?= $(VIRTUAL_ENV)
binDir        ?= $(installTop)/bin

installBins   ?= /usr/bin/install -s -p -m 755
installDirs   ?= /usr/bin/install -d

CXXFLAGS      += -g

bins          := podofo-flatform

ifeq ($(filter Darwin,$(distHost)),)
LDLIBS +=  -lpthread
endif

all:: podofo-flatform

install:: $(bins)
	$(if $^,$(installDirs) $(DESTDIR)$(binDir))
	$(if $^,$(installBins) $^ $(DESTDIR)$(binDir))

podofo-flatform: podofo-flatform.cc \
    -lpodofo -lfreetype -lfontconfig -ljpeg -lcrypto -lidn -lz

vpath %.cc 		$(srcDir)/src
