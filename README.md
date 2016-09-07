
Utility to construct a PDF from a template and key/value pairs

Compile podofo-0.9.4 on OSX

    $ mkdir -p ~/workspace/reps
    $ cd ~/workspace/reps
    $ wget http://downloads.sourceforge.net/podofo-0.9.4.tar.gz
    $ tar zxvf podofo-0.9.4.tar.gz
    $ mkdir -p podofo-0.9.4-build
    $ cd podofo-0.9.4-build
    $ cmake -G "Unix Makefiles" \
        -DWANT_FONTCONFIG:BOOL=TRUE \
        -DCMAKE_PREFIX_PATH=/opt/local \
        -DCMAKE_INCLUDE_PATH=/opt/local/include \
        -DCMAKE_LIBRARY_PATH=/opt/local/lib \
        -DCMAKE_FRAMEWORK_PATH=/opt/local/Library/Frameworks \
        -DCMAKE_FIND_FRAMEWORK=NEVER \
        -DCMAKE_INSTALL_PREFIX:PATH=$HOME/workspace \
        ../podofo-0.9.4
    $ make
    $ make install

Compile podofo-flatform

    $ cd ~/workspace/reps
    $ git clone https://github.com/djaodjin/podofo-flatform.git
    $ cd podofo-flatform
    $ make CPPFLAGS="-I$HOME/workspace/include" \
        LDFLAGS="-L$HOME/workspace/lib -L/opt/local/lib"

Example usage

    $ ./podofo-flatform --fill "First Name=Me" template.pdf output.pdf
