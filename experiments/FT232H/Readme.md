## Stuff that looks interesting

intel's libraries for embedded computing. even includes SX1276 drivers:

http://iotdk.intel.com/docs/master/upm/modules.html
https://github.com/intel-iot-devkit/mraa


## Understanding WTF is going on with FT232H and Python

`libftdi1` is an open-source C driver for FTDI. It uses SWIG to auto-generate bindings to the C interface.

`pylibftdi` is a SEPARATE python library built on top of libftdi.

### Installing FT232H AdaFruit libraries

**TL;DR SKIP AHEAD TO THE BOTTOM OF THIS SECTIN TO SEE THE ANSWER:

There are many options, but we're building on top of `libftdi` (not pylibftdi)

Following https://learn.adafruit.com/downloads/pdf/adafruit-ft232h-breakout.pdf

**THIS DIDN'T WORK:**

	brew install cmake
	brew install libusb
	brew install swig
	brew install --build-from-source libftdi
	mkdir -p ~/Library/Python/2.7/lib/python/site-packages
	echo '/usr/local/lib/python2.7/site-packages' > ~/Library/Python/2.7/lib/python/site-packages/homebrew.pth


**SO TRY THIS:**

So, downloaded libfti myself: https://www.intra2net.com/en/developer/libftdi/download.php
and followed their installation instructions:

	mkdir build
	cd build

	cmake ../
	make
	make install

This worked fine.

Now, this installs `ftdi1.py` in the wrong place! UGH! I found it in:

	ls /usr/local/lib/python2.7/site-packages/

	-rwxr-xr-x 1 njoubert wheel 317K Feb 26 20:24 _ftdi1.so
	-rw-r--r-- 1 njoubert wheel  81K Feb 26 20:23 ftdi1.py

Now, fire up python and see where your site-packages are:

	python
	>>> import site; site.getsitepackages()

For me this is:

	['/Users/njoubert/Library/Enthought/Canopy_64bit/User/lib/python2.7/site-packages', '/Users/njoubert/Library/Enthought/Canopy_64bit/User/lib/site-python', '/Applications/Canopy.app/appdata/canopy-1.5.1.2730.macosx-x86_64/Canopy.app/Contents/lib/python2.7/site-packages', '/Applications/Canopy.app/appdata/canopy-1.5.1.2730.macosx-x86_64/Canopy.app/Contents/lib/site-python']

So, I'm gonna copy this over

	cp /usr/local/lib/python2.7/site-packages/* /Users/njoubert/Library/Enthought/Canopy_64bit/User/lib/python2.7/site-packages/

Try again:

	sudo python 
	>>> import ftdi1
		Fatal Python error: PyThreadState_Get: no current thread

Let's check what `_ftdi1.so` links against:

	cd ~/Library/Enthought/Canopy_64bit/User/lib/python2.7/site-packages
	otool -L _ftdi1.so

	_ftdi1.so:
		libftdi1.2.dylib (compatibility version 2.0.0, current version 2.2.0)
		/System/Library/Frameworks/Python.framework/Versions/2.7/Python (compatibility version 2.7.0, current version 2.7.6)
		/opt/local/lib/libusb-1.0.0.dylib (compatibility version 2.0.0, current version 2.0.0)
		/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1213.0.0)

Ah, it's linking against default python, and I'm using Canopy Python!

Add some lines to libftdi1-1.2/CMakeLists.txt from https://stackoverflow.com/questions/17686346/compiling-shared-library-for-python-to-distribute

	set (CMAKE_SHARED_LINKER_FLAGS "-L/Users/njoubert/Library/Enthought/Canopy_64bit/User/lib/ -ldl -framework CoreFoundation -lpython2.7 -u _PyMac_Error")

*DIDN'T WORK!*

**FINALLY HERE'S HOW TO DO IT:**

So, following this: https://cmake.org/pipermail/paraview/2013-September/029364.html
Run this from `libftdi1-1.2/build`

	cmake -DPYTHON_LIBRARY='/Applications/Canopy.app/appdata/canopy-1.5.1.2730.macosx-x86_64/Canopy.app/Contents/lib/libpython2.7.dylib' -DPYTHON_INCLUDE='/Applications/Canopy.app/appdata/canopy-1.5.1.2730.macosx-x86_64/Canopy.app/Contents/include/python2.7/' ..

then 

	cp /usr/local/lib/python2.7/site-packages/* /Users/njoubert/Library/Enthought/Canopy_64bit/User/lib/python2.7/site-packages/

Then we're up and running!


### pylibftdi is different from ftdi1:

OK, time to try pylibftdi

	pip install pylibftdi

Worked fine. Now load the right KEXT:

	sudo kextunload -bundle-id com.apple.driver.AppleUSBFTDI

(To reload later: sudo kextload -bundle-id com.apple.driver.AppleUSBFTDI) Check out if it worked:

	python -m pylibftdi.examples.info


	pylibftdi version     : 0.15.0
	libftdi version       : libftdi_version(major=1, minor=2, micro=0, version_str='1.2', snapshot_str='unknown')
	libftdi library name  : /usr/local/lib/libftdi1.dylib
	libusb version        : libusb_version(major=1, minor=0, micro=20, nano=11004, rc='', describe='http://libusb.info')
	libusb library name   : /usr/local/lib/libusb-1.0.dylib
	Python version        : 2.7.6
	OS platform           : Darwin-14.3.0-x86_64-i386-64bit

