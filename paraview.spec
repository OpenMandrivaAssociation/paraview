%define build_mpi	1
%{?_with_build_mpi: %{expand: %%global build_mpi 1}}
%{?_without_build_mpit: %{expand: %%global build_mpi 0}}

%define pv_maj 3
%define pv_min 2
%define pv_patch 3
%define pv_majmin %{pv_maj}.%{pv_min}

%define qt_dir 			%{_prefix}/lib/qt4
%define qt_designer_plugins_dir %{qt_dir}/plugins/%{_lib}/designer
%define python_include_path	%{_includedir}/python%{pyver}
%define python_library		%{_libdir}/python%{pyver}/config/libpython%{pyver}.a
%define python_site_package	%{_libdir}/python%{pyver}/site-packages

Name:           paraview
Version:        %{pv_majmin}.%{pv_patch}
Release:        %mkrel 1
Summary:        Parallel visualization application
Group:          Sciences/Other
License:        BSD
URL:            http://www.paraview.org/
Source0:        http://www.paraview.org/files/v%{pv_majmin}/paraview-%{version}.tar.lzma
Source2:        paraview.xml
Source3:	http://public.kitware.com/pub/paraview/logos/ParaView-logo-swirl-high-res.png
Patch0:         paraview-3.2.3-qt.patch
Patch1:         paraview-3.2.3-rpath.patch
Patch2:         paraview-3.2.3-install.patch
Patch3:         paraview-3.2.3-doc.patch
Patch4:         paraview-3.2.3-assistant-qt4.patch
Patch5:         paraview-3.2.3-make.patch
Patch6:		paraview-3.2.3-glxext_legacy.patch
Patch7:		paraview-3.2.3-dicomfile.patch
Patch8:		paraview-3.2.3-metautils.patch
Patch9:		paraview-3.2.3-OpenFOAM.patch
Patch10:	paraview-3.2.3-metacommand.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
%if %{mdkversion} >= 200810
BuildRequires:  cmake >= 2.5.0-0.20071024.3
%else
BuildRequires:  cmake
%endif
%if %{build_mpi}
BuildRequires:	openmpi
BuildRequires:  openmpi-devel
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gnuplot
BuildRequires:  expat-devel
BuildRequires:  freetype-devel
BuildRequires:  GL-devel
BuildRequires:	graphviz
BuildRequires:	hdf5-devel
BuildRequires:	ImageMagick
BuildRequires:  libtiff-devel
BuildRequires:  python-devel
BuildRequires:  qt4-devel
BuildRequires:  qt4-assistant
BuildRequires:  readline-devel
BuildRequires:  tk-devel
BuildRequires:  zlib-devel
Requires:       %{name}-data = %{version}-%{release}
Requires:       qt4-assistant
%ifarch %x86_64
Requires:	lib64hdf5_0
%endif
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

%description
ParaView is an application designed with the need to visualize large
data sets in mind. The goals of the ParaView project include the
following:

    * Develop an open-source, multi-platform visualization
      application.

    * Support distributed computation models to process large data
      sets.

    * Create an open, flexible, and intuitive user interface.

    * Develop an extensible architecture based on open standards.

ParaView runs on distributed and shared memory parallel as well as
single processor systems. Under the hood, ParaView uses the
Visualization Toolkit as the data processing and rendering engine and
has a user interface written using a unique blend of Tcl/Tk and C++.

NOTE: This version has NOT been compiled with MPI support.


%if %{build_mpi}
%package        mpi
Summary:        Parallel visualization application
Group:          Sciences/Other
Requires:       %{name}-data = %{version}-%{release}
Provides:       %{name}
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

%description    mpi
ParaView is an application designed with the need to visualize large
data sets in mind. The goals of the ParaView project include the
following:

    * Develop an open-source, multi-platform visualization
      application.

    * Support distributed computation models to process large data
      sets.

    * Create an open, flexible, and intuitive user interface.

    * Develop an extensible architecture based on open standards.

ParaView runs on distributed and shared memory parallel as well as
single processor systems. Under the hood, ParaView uses the
Visualization Toolkit as the data processing and rendering engine and
has a user interface written using a unique blend of Tcl/Tk and C++.

NOTE: This version has been compiled with OpenMPI support and requires
an operating OpenMPI runtime enviroment.
%endif

%package        data
Summary:        Data files for ParaView
Group:          Sciences/Other
Requires:       %{name} = %{version}-%{release}
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

%description    data
%{summary}.


%package        devel
Summary:        Development files for ParaView
Group:          Sciences/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
%{summary}.


%package        mpi-devel
Summary:        Development files for the mpi version of ParaView
Group:          Sciences/Other
Requires:       %{name}-mpi = %{version}-%{release}

%description    mpi-devel
%{summary}.


%prep
%setup -q -n ParaView%{version}
%patch0 -p1 -b .qt
%patch1 -p1 -b .rpath
%patch2 -p1 -b .install
%patch3 -p1 -b .doc
%patch4 -p1 -b .assistant-qt4
%patch5 -p0 -b .make
%patch6 -p1 -b .glxext
%patch7 -p1 -b .dicomfile
%patch8 -p1 -b .metautils
%patch9 -p1 -b .openfoam
%patch10 -p1 -b .metacommand

%build
rm -rf paraviewbuild paraviewbuild-mpi
mkdir paraviewbuild
pushd paraviewbuild
export CC='gcc'
export CXX='g++'
export MAKE='make'
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export QT_QMAKE_EXECUTABLE=%{qt_dir}/bin/qmake
cmake .. \
        -DPV_INSTALL_LIB_DIR:PATH=/%{_lib}/paraview \
        -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
        -DCMAKE_CXX_COMPILER:FILEPATH=$CXX \
        -DCMAKE_C_COMPILER:FILEPATH=$CC \
	-DCMAKE_CXX_FLAGS="%{optflags}" \
        -DTCL_LIBRARY:PATH=tcl \
        -DTK_LIBRARY:PATH=tk \
        -DPARAVIEW_ENABLE_PYTHON:BOOL=ON \
        -DPYTHON_INCLUDE_PATH:PATH=%{python_include_path} \
        -DPYTHON_LIBRARY:FILEPATH=%{python_library} \
        -DPARAVIEW_USE_SYSTEM_HDF5:BOOL=ON \
	-DQT_QMAKE_EXECUTABLE:FILEPATH=$QT_QMAKE_EXECUTABLE \
	-DQT_INCLUDE_DIR:FILEPATH=%{qt_dir}/include \
	-DQT_MOC_EXECUTABLE:FILEPATH=%{qt_dir}/bin/moc \
	-DQT_UIC_EXECUTABLE:FILEPATH=%{qt_dir}/bin/uic \
	-DVTK_INSTALL_QT_PLUGIN_DIR:STRING=%{qt_designer_plugins_dir} \
        -DVTK_OPENGL_HAS_OSMESA:BOOL=OFF \
        -DVTK_USE_INFOVIS:BOOL=OFF \
        -DVTK_USE_SYSTEM_EXPAT:BOOL=ON \
        -DVTK_USE_SYSTEM_FREETYPE:BOOL=ON \
        -DVTK_USE_SYSTEM_JPEG:BOOL=ON \
        -DVTK_USE_SYSTEM_PNG:BOOL=ON \
        -DVTK_USE_SYSTEM_TIFF:BOOL=ON \
        -DVTK_USE_SYSTEM_ZLIB:BOOL=ON \
        -DBUILD_DOCUMENTATION:BOOL=ON \
        -DBUILD_EXAMPLES:BOOL=ON \
	-DGLXEXT_LEGACY:BOOL=ON
cmake ..
%make VERBOSE=1
popd

%if %{build_mpi}
mkdir paraviewbuild-mpi
pushd paraviewbuild-mpi
export CC='gcc'
export CXX='mpic++'
export MAKE='make'
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
cmake .. \
        -DPV_INSTALL_LIB_DIR:PATH=/%{_lib}/paraview-mpi \
        -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
        -DCMAKE_CXX_COMPILER:FILEPATH=$CXX \
        -DCMAKE_C_COMPILER:FILEPATH=$CC \
	-DCMAKE_CXX_FLAGS="%{optflags}" \
        -DTCL_LIBRARY:PATH=tcl \
        -DTK_LIBRARY:PATH=tk \
        -DPARAVIEW_ENABLE_PYTHON:BOOL=ON \
        -DPYTHON_INCLUDE_PATH:PATH=%{python_include_path} \
        -DPYTHON_LIBRARY:FILEPATH=%{python_library} \
        -DPARAVIEW_USE_SYSTEM_HDF5:BOOL=ON \
	-DQT_QMAKE_EXECUTABLE:FILEPATH=$QT_QMAKE_EXECUTABLE \
	-DQT_INCLUDE_DIR:FILEPATH=%{qt_dir}/include \
	-DQT_MOC_EXECUTABLE:FILEPATH=%{qt_dir}/bin/moc \
	-DQT_UIC_EXECUTABLE:FILEPATH=%{qt_dir}/bin/uic \
	-DVTK_INSTALL_QT_PLUGIN_DIR:STRING=%{qt_designer_plugins_dir} \
        -DICET_BUILD_TESTING:BOOL=ON \
        -DVTK_USE_MPI:BOOL=ON \
        -DMPI_INCLUDE_PATH:PATH="%{_includedir}/openmpi" \
        -DMPI_LIBRARY:STRING="-L%{_libdir}/openmpi" \
        -DVTK_OPENGL_HAS_OSMESA:BOOL=OFF \
        -DVTK_USE_INFOVIS:BOOL=OFF \
        -DVTK_USE_SYSTEM_EXPAT:BOOL=ON \
        -DVTK_USE_SYSTEM_FREETYPE:BOOL=ON \
        -DVTK_USE_SYSTEM_JPEG:BOOL=ON \
        -DVTK_USE_SYSTEM_PNG:BOOL=ON \
        -DVTK_USE_SYSTEM_TIFF:BOOL=ON \
        -DVTK_USE_SYSTEM_ZLIB:BOOL=ON \
        -DBUILD_DOCUMENTATION:BOOL=ON \
        -DBUILD_EXAMPLES:BOOL=ON \
        -DGLXEXT_LEGACY:BOOL=ON
cmake ..
%make VERBOSE=1
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

# Fix permissions
find . \( -name \*.txt -o -name \*.xml -o -name '*.[ch]' -o -name '*.[ch][px][px]' \) -print0 | xargs -0 chmod -x

# Create some needed directories
install -d $RPM_BUILD_ROOT%{_datadir}/applications
install -d $RPM_BUILD_ROOT%{_datadir}/mime/packages
install -d $RPM_BUILD_ROOT%{_iconsdir}
install -d $RPM_BUILD_ROOT%{_miconsdir}
install -d $RPM_BUILD_ROOT%{_liconsdir}
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mime/packages
install -m644 %{SOURCE3} ./paraview-logo.png

# Build icons
convert paraview-logo.png -resize 48x48+0+0! -transparent white $RPM_BUILD_ROOT%{_liconsdir}/paraview.png
convert paraview-logo.png -resize 32x32+0+0! -transparent white $RPM_BUILD_ROOT%{_iconsdir}/paraview.png
convert paraview-logo.png -resize 16x16+0+0! -transparent white $RPM_BUILD_ROOT%{_miconsdir}/paraview.png


%if %{build_mpi}
# Install mpi version
pushd paraviewbuild-mpi
make install DESTDIR=$RPM_BUILD_ROOT

# ld.conf.d file
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/paraview-mpi > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/paraview-mpi-%{_arch}.conf

# Python Path
install -d $RPM_BUILD_ROOT%{python_site_package}
echo %{_libdir}/paraview-mpi > $RPM_BUILD_ROOT%{python_site_package}/paraview-mpi.pth

# Create desktop file
cat > %{name}-mpi.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=ParaView Viewer MPI
GenericName=ParaView Data Viewer
Comment=ParaView allows MPI enabled viewing of large data sets
Type=Application
Terminal=false
Icon=paraview
MimeType=application/x-paraview;
Categories=Graphics;Science;Math
Exec=mpirun C paraview-mpi
EOF

desktop-file-install --vendor="" \
       --dir %{buildroot}%{_datadir}/applications/ \
       %{name}-mpi.desktop

popd

# Move the mpi binaries, includes, and man pages out of the way
pushd $RPM_BUILD_ROOT/%{_bindir}
for f in *
do
   mv $f ${f}-mpi
done
popd
mv $RPM_BUILD_ROOT/%{_includedir}/paraview-%{pv_majmin} \
	$RPM_BUILD_ROOT/%{_includedir}/paraview-%{pv_majmin}-mpi
rm -rf $RPM_BUILD_ROOT%{_mandir}

# Remove mpi copy of documentation
rm -rf $RPM_BUID_ROOT%{_datadir}/paraview/Documentation-mpi
rm -rf $RPM_BUID_ROOT%{_libdir}/paraview-mpi/doc
%endif

# Install the normal version
pushd paraviewbuild
make install DESTDIR=$RPM_BUILD_ROOT

# ld.conf.d file
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/paraview > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/paraview-%{_arch}.conf

# Python Path
install -d $RPM_BUILD_ROOT%{python_site_package}
echo %{_libdir}/paraview > $RPM_BUILD_ROOT%{python_site_package}/paraview.pth

# Create desktop file
cat > %{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=ParaView Viewer
GenericName=ParaView Data Viewer
Comment=ParaView allows viewing of large data sets
Type=Application
Terminal=false
Icon=paraview
MimeType=application/x-paraview;
Categories=Graphics;Science;Math;
Exec=paraview
EOF

desktop-file-install --vendor="" \
       --dir %{buildroot}%{_datadir}/applications/ \
       %{name}.desktop
popd


%clean
rm -rf $RPM_BUILD_ROOT


%post
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%update_desktop_database


%postun
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%clean_desktop_database

%if %{build_mpi}
%post   mpi
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%update_desktop_database

%postun mpi
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%clean_desktop_database
%endif


%post   data
%update_mime_database

%postun data
%clean_mime_database


%files
%defattr(-,root,root,-)
%doc License_v1.1.txt
%doc %{_datadir}/paraview/
%{_sysconfdir}/ld.so.conf.d/paraview-%{_arch}.conf
%{_bindir}/paraview
%{_bindir}/pvbatch
%{_bindir}/pvdataserver
%{_bindir}/pvpython
%{_bindir}/pvrenderserver
%{_bindir}/pvserver
%{_bindir}/pvTestDriver
%{_datadir}/applications/%{name}.desktop
%{_libdir}/paraview/
%{qt_dir}/plugins/%{_lib}/designer/*.so
%{python_site_package}/paraview.pth
%exclude %{_libdir}/paraview/doc/


%if %{build_mpi}
%files mpi
%defattr(-,root,root,-)
%doc License_v1.1.txt
%{_sysconfdir}/ld.so.conf.d/paraview-mpi-%{_arch}.conf
%{_bindir}/paraview-mpi
%{_bindir}/pvbatch-mpi
%{_bindir}/pvdataserver-mpi
%{_bindir}/pvpython-mpi
%{_bindir}/pvrenderserver-mpi
%{_bindir}/pvserver-mpi
%{_bindir}/pvTestDriver-mpi
%{_datadir}/applications/%{name}-mpi.desktop
%{_libdir}/paraview-mpi/
%{python_site_package}/paraview-mpi.pth
%endif


%files data
%defattr(-,root,root,-)
%attr(644,root,root) %{_iconsdir}/paraview.png
%attr(644,root,root) %{_liconsdir}/paraview.png
%attr(644,root,root) %{_miconsdir}/paraview.png
%{_datadir}/mime/packages/paraview.xml


%files devel
%defattr(-,root,root,-)
%{_includedir}/paraview-%{pv_majmin}/
%doc %{_libdir}/paraview/doc/


%files mpi-devel
%defattr(-,root,root,-)
%{_includedir}/paraview-%{pv_majmin}-mpi/


